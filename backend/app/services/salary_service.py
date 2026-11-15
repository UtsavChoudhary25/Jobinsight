import os
import json
import joblib
import pandas as pd
from typing import Dict, Any

class SalaryPredictionService:
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        app_dir = os.path.dirname(current_dir)
        models_dir = os.path.join(app_dir, 'models')
        
        self.model_path = os.path.join(models_dir, 'salary_model.joblib')
        self.meta_path = os.path.join(models_dir, 'model_metadata.json')
        
        self.pipeline = None
        self.metadata = {}
        self.load_model()

    def load_model(self):
        try:
            if os.path.exists(self.model_path):
                self.pipeline = joblib.load(self.model_path)
            if os.path.exists(self.meta_path):
                with open(self.meta_path, 'r', encoding='utf-8') as f:
                    self.metadata = json.load(f)
        except Exception as e:
            print(f"Error loading salary model: {e}")
            self.pipeline = None

    def is_loaded(self) -> bool:
        return self.pipeline is not None

    def predict(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if not self.is_loaded():
            raise RuntimeError("Salary ML model is not loaded or missing.")

        # Ensure correct column naming and order matching training
        input_data = {
            'role_category': [str(data.get('role_category', 'Technology'))],
            'formatted_experience_level': [str(data.get('formatted_experience_level', 'Mid-Senior level'))],
            'formatted_work_type': [str(data.get('formatted_work_type', 'Full-time'))],
            'location_tier': [str(data.get('location_tier', 'Tier 1 (NYC, SF, Seattle, Boston)'))],
            'remote_allowed': [str(data.get('remote_allowed', '1'))]
        }
        
        df_input = pd.DataFrame(input_data)
        raw_pred = float(self.pipeline.predict(df_input)[0])
        predicted_salary = round(raw_pred, 2)

        # Compute empirical uncertainty range based on model MAE
        mae = float(self.metadata.get('metrics', {}).get('MAE', 30481.97))
        r2 = float(self.metadata.get('metrics', {}).get('R2', 0.3454))
        model_name = self.metadata.get('model_name', 'HistGradientBoosting')

        # 0.75 * MAE gives standard confidence interval for salary predictions
        margin = round(0.70 * mae, 2)
        expected_min = max(25000.0, round(predicted_salary - margin, 2))
        expected_max = round(predicted_salary + margin, 2)

        # Percentile rank against the ~35k real dataset observations
        # Empirical percentile estimation
        if predicted_salary <= 35000:
            percentile = max(5.0, round((predicted_salary / 35000) * 15, 1))
        elif predicted_salary <= 52000:
            percentile = round(15.0 + ((predicted_salary - 35000) / 17000) * 10, 1)
        elif predicted_salary <= 81500:
            percentile = round(25.0 + ((predicted_salary - 52000) / 29500) * 25, 1)
        elif predicted_salary <= 125000:
            percentile = round(50.0 + ((predicted_salary - 81500) / 43500) * 25, 1)
        elif predicted_salary <= 200000:
            percentile = round(75.0 + ((predicted_salary - 125000) / 75000) * 20, 1)
        else:
            percentile = min(99.0, round(95.0 + ((predicted_salary - 200000) / 100000) * 4, 1))

        return {
            "predicted_salary": predicted_salary,
            "expected_range_min": expected_min,
            "expected_range_max": expected_max,
            "percentile_rank": percentile,
            "currency": "USD",
            "pay_period": "YEARLY",
            "model_name": model_name,
            "model_r2_score": r2,
            "model_mae": mae,
            "features_used": {k: v[0] for k, v in input_data.items()}
        }

# Global singleton
salary_service = SalaryPredictionService()
