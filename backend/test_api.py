import sys
import os

# Add backend directory to sys.path
backend_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, backend_dir)

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

print("=" * 60)
print("TESTING JOBINSIGHT FASTAPI BACKEND & ML PIPELINES")
print("=" * 60)

# Test 1: Root endpoint
res_root = client.get("/")
print("1. Root Endpoint Status:", res_root.status_code)
assert res_root.status_code == 200
print("   Response:", res_root.json())

# Test 2: Health Check
res_health = client.get("/health")
print("\n2. Health Check Status:", res_health.status_code)
assert res_health.status_code == 200
data_health = res_health.json()
print("   Response:", data_health)
assert data_health["model_loaded"] is True
assert data_health["nlp_ready"] is True

# Test 3: Model Info
res_info = client.get("/api/model-info")
print("\n3. Model Info Status:", res_info.status_code)
assert res_info.status_code == 200
data_info = res_info.json()
print(f"   Model Name: {data_info['model_name']}")
print(f"   Trained Records: {data_info['total_training_records']:,}")
print(f"   Test Set R²: {data_info['metrics']['R2']}")
print(f"   Test Set MAE: ${data_info['metrics']['MAE']:,.2f}")

# Test 4: Real Salary Prediction
salary_payload = {
    "role_category": "Technology",
    "formatted_experience_level": "Mid-Senior level",
    "formatted_work_type": "Full-time",
    "location_tier": "Tier 1 (NYC, SF, Seattle, Boston)",
    "remote_allowed": "1"
}
res_salary = client.post("/api/predict-salary", json=salary_payload)
print("\n4. Salary Prediction Status:", res_salary.status_code)
assert res_salary.status_code == 200
data_salary = res_salary.json()
print("   Payload:", salary_payload)
print(f"   Predicted Median: ${data_salary['predicted_salary']:,.2f}")
print(f"   Expected Range: ${data_salary['expected_range_min']:,.2f} – ${data_salary['expected_range_max']:,.2f}")
print(f"   Percentile Rank: {data_salary['percentile_rank']}th percentile")
print(f"   Model: {data_salary['model_name']} (R² = {data_salary['model_r2_score']})")

# Test 5: Real NLP Skill Extraction
nlp_payload = {
    "description": (
        "We are looking for a Senior Distributed Systems Engineer. "
        "Must have 5+ years of experience in Python, PyTorch, Go, Docker, and Kubernetes. "
        "Familiarity with AWS (S3, EC2, Lambda), Terraform, CI/CD pipelines, and Kafka is essential. "
        "Master's Degree in Computer Science or equivalent. Strong leadership and agile communication skills."
    )
}
res_nlp = client.post("/api/extract-skills", json=nlp_payload)
print("\n5. NLP Skill Extraction Status:", res_nlp.status_code)
assert res_nlp.status_code == 200
data_nlp = res_nlp.json()
print(f"   Inferred Category: {data_nlp['inferred_category']}")
print(f"   Total Entities Detected: {data_nlp['total_detected']}")
print(f"   Technical Skills ({len(data_nlp['technical_skills'])}): {data_nlp['technical_skills']}")
print(f"   Tools & Platforms ({len(data_nlp['tools_and_platforms'])}): {data_nlp['tools_and_platforms']}")
print(f"   Soft Skills ({len(data_nlp['soft_skills'])}): {data_nlp['soft_skills']}")
print(f"   Experience Detected: {data_nlp['experience_required']}")
print(f"   Degree Detected: {data_nlp['degree_required']}")
print(f"   Word Count: {data_nlp['token_statistics']['word_count']}, Skill Density: {data_nlp['token_statistics']['skill_density_pct']}%")

print("\n" + "=" * 60)
print("ALL 5 BACKEND API & ML PIPELINE TESTS PASSED SUCCESSFULLY!")
print("=" * 60)
