import React, { useState, useEffect, useCallback } from 'react';
import { 
  Sparkles, 
  Cpu, 
  FileText, 
  TrendingUp, 
  CheckCircle, 
  Layers, 
  Zap,
  ArrowRight,
  AlertCircle,
  Loader2,
  RefreshCw,
  Server,
  Activity
} from 'lucide-react';
import { predictSalary, extractSkills, checkBackendHealth } from '../services/api';

export default function PredictiveLabTab() {
  // Backend Connectivity Status
  const [backendStatus, setBackendStatus] = useState('checking'); // 'online' | 'offline' | 'checking'
  const [apiError, setApiError] = useState(null);

  // Salary Predictor State
  const [roleCategory, setRoleCategory] = useState('Technology');
  const [experienceLevel, setExperienceLevel] = useState('Mid-Senior level');
  const [locationTier, setLocationTier] = useState('Tier 1 (NYC, SF, Seattle, Boston)');
  const [workArrangement, setWorkArrangement] = useState('1'); // '1' = Remote, '0' = On-site

  const [salaryResult, setSalaryResult] = useState(null);
  const [isPredicting, setIsPredicting] = useState(false);
  const [salaryError, setSalaryError] = useState(null);

  // Skill Extractor State
  const sampleDescriptions = [
    {
      label: "Senior Cloud & AI Engineer",
      text: "We are seeking a Senior Cloud Engineer with 5+ years of experience in distributed systems. Must have strong proficiency in Python, PyTorch, AWS (EC2, S3, ECS), Kubernetes, and Terraform. Experience with Large Language Models (LLMs), RAG architectures, and CI/CD pipelines is highly desirable. Excellent communication and agile collaboration skills required. Master's degree in Computer Science."
    },
    {
      label: "Marketing & Brand Strategist",
      text: "Looking for an experienced Marketing Coordinator to drive omnichannel digital campaigns. Candidate must excel at SEO, Google Analytics, content copywriting, and social media advertising. Familiarity with Hubspot CRM, Adobe Creative Suite, and A/B testing frameworks required. Bachelor's degree and 3+ years experience in B2B SaaS."
    },
    {
      label: "Clinical Healthcare Director",
      text: "Seeking a Director of Clinical Operations with a Master's degree in Nursing or Healthcare Administration. Minimum 8+ years leadership overseeing HIPAA compliance, clinical governance, multi-facility budgeting, patient safety protocols, and cross-functional medical staff management."
    }
  ];

  const [descriptionInput, setDescriptionInput] = useState(sampleDescriptions[0].text);
  const [extractedResults, setExtractedResults] = useState(null);
  const [isExtracting, setIsExtracting] = useState(false);
  const [nlpError, setNlpError] = useState(null);

  // Check backend health on mount
  const checkHealth = useCallback(async () => {
    setBackendStatus('checking');
    const health = await checkBackendHealth();
    if (health.status === 'healthy' && health.model_loaded) {
      setBackendStatus('online');
      setApiError(null);
    } else {
      setBackendStatus('offline');
      setApiError(health.error || "Backend model service is unreachable.");
    }
  }, []);

  useEffect(() => {
    checkHealth();
  }, [checkHealth]);

  // Execute Real Salary Prediction via FastAPI ML Pipeline
  const runSalaryPrediction = useCallback(async () => {
    setIsPredicting(true);
    setSalaryError(null);
    try {
      const payload = {
        role_category: roleCategory,
        formatted_experience_level: experienceLevel,
        formatted_work_type: "Full-time",
        location_tier: locationTier,
        remote_allowed: workArrangement
      };
      const data = await predictSalary(payload);
      setSalaryResult(data);
    } catch (err) {
      setSalaryError(err.message || "Failed to reach inference server");
    } finally {
      setIsPredicting(false);
    }
  }, [roleCategory, experienceLevel, locationTier, workArrangement]);

  // Automatically execute prediction when inputs change
  useEffect(() => {
    runSalaryPrediction();
  }, [runSalaryPrediction]);

  // Execute Real NLP Skill Extraction via FastAPI NLP Service
  const runNlpExtraction = async () => {
    if (!descriptionInput.trim()) return;
    setIsExtracting(true);
    setNlpError(null);
    try {
      const data = await extractSkills(descriptionInput);
      setExtractedResults(data);
    } catch (err) {
      setNlpError(err.message || "Failed to execute NLP extraction");
    } finally {
      setIsExtracting(false);
    }
  };

  return (
    <div className="space-y-6">
      
      {/* Header Banner */}
      <div className="rounded-2xl border border-stone-200 bg-white p-6 shadow-2xs dark:border-stone-800 dark:bg-stone-900">
        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
          <div>
            <div className="flex items-center gap-2 text-xs font-semibold uppercase tracking-wider text-indigo-600 dark:text-indigo-400">
              <Sparkles className="h-3.5 w-3.5" />
              <span>JobInsight Production ML Lab</span>
            </div>
            <h1 className="mt-1 text-2xl font-bold tracking-tight text-stone-900 dark:text-stone-100 sm:text-3xl">
              AI Predictive Lab &amp; NLP Modules
            </h1>
            <p className="mt-1 text-sm text-stone-600 dark:text-stone-400 max-w-3xl">
              Live inference service connected to the trained 
              <strong> HistGradientBoosting Regressor (R² = 0.345, 28k+ training records)</strong> and 
              the <strong>JobInsight NLP Skill &amp; Entity Extractor</strong>.
            </p>
          </div>

          {/* Backend Status Badge */}
          <div className="flex items-center gap-2">
            <div className={`inline-flex items-center gap-1.5 rounded-lg border px-3 py-1.5 text-xs font-mono font-medium ${
              backendStatus === 'online'
                ? 'bg-emerald-50 text-emerald-800 border-emerald-200 dark:bg-emerald-950/60 dark:text-emerald-300 dark:border-emerald-800'
                : backendStatus === 'checking'
                ? 'bg-amber-50 text-amber-800 border-amber-200 dark:bg-amber-950/60 dark:text-amber-300 dark:border-amber-800'
                : 'bg-rose-50 text-rose-800 border-rose-200 dark:bg-rose-950/60 dark:text-rose-300 dark:border-rose-800'
            }`}>
              <span className={`h-2 w-2 rounded-full ${
                backendStatus === 'online' ? 'bg-emerald-500 animate-pulse' : backendStatus === 'checking' ? 'bg-amber-500' : 'bg-rose-500'
              }`} />
              <span>{backendStatus === 'online' ? 'FastAPI ML Service Online' : backendStatus === 'checking' ? 'Connecting to Model...' : 'Model API Offline'}</span>
            </div>
            <button
              onClick={checkHealth}
              className="rounded-lg border border-stone-200 p-1.5 text-stone-500 hover:text-stone-900 hover:bg-stone-50 dark:border-stone-800 dark:text-stone-400"
              title="Refresh connection status"
            >
              <RefreshCw className="h-3.5 w-3.5" />
            </button>
          </div>
        </div>

        {/* Global API offline alert banner if disconnected */}
        {backendStatus === 'offline' && (
          <div className="mt-4 flex items-start gap-2.5 rounded-xl border border-amber-200 bg-amber-50/70 p-3.5 text-xs text-amber-900 dark:border-amber-900/60 dark:bg-amber-950/30 dark:text-amber-300">
            <AlertCircle className="h-4 w-4 shrink-0 text-amber-600 mt-0.5" />
            <div className="space-y-1">
              <span className="font-semibold block">FastAPI ML Backend Not Detected on Endpoint</span>
              <p className="text-[11px] text-amber-800/90 dark:text-amber-300/90">
                To connect predictions, start the local backend using <code className="font-mono bg-amber-100 px-1 py-0.5 rounded dark:bg-amber-900/60">uvicorn app.main:app --reload</code> inside <code className="font-mono bg-amber-100 px-1 py-0.5 rounded dark:bg-amber-900/60">backend/</code> or deploy to Hugging Face Spaces / Render and set <code className="font-mono bg-amber-100 px-1 py-0.5 rounded dark:bg-amber-900/60">VITE_API_URL</code>.
              </p>
            </div>
          </div>
        )}
      </div>

      {/* Grid: Tool 1 (Salary Estimator) & Tool 2 (Skill Extractor) */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        
        {/* Module 1: ML Salary Estimator */}
        <div className="rounded-2xl border border-stone-200 bg-white p-6 shadow-2xs dark:border-stone-800 dark:bg-stone-900 flex flex-col justify-between">
          <div>
            <div className="flex items-center justify-between pb-4 border-b border-stone-100 dark:border-stone-800">
              <div className="flex items-center gap-2">
                <Cpu className="h-4 w-4 text-emerald-600" />
                <h2 className="text-base font-semibold text-stone-900 dark:text-stone-100">
                  Trained ML Salary Regressor
                </h2>
              </div>
              <span className="rounded bg-emerald-50 px-2 py-0.5 text-[10px] font-mono font-semibold text-emerald-700 dark:bg-emerald-950 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-800">
                HistGradientBoosting
              </span>
            </div>

            <p className="mt-3 text-xs text-stone-500 dark:text-stone-400">
              Direct inference via Scikit-learn Pipeline trained on 28,189 verified LinkedIn postings with OneHotEncoding.
            </p>

            {/* Inputs Form */}
            <div className="mt-5 space-y-4 text-xs">
              
              {/* Role Family */}
              <div>
                <label className="font-medium text-stone-700 dark:text-stone-300 block mb-1">
                  Role Classification &amp; Industry
                </label>
                <select
                  value={roleCategory}
                  onChange={(e) => setRoleCategory(e.target.value)}
                  className="w-full rounded-lg border border-stone-200 bg-stone-50/70 p-2 text-stone-800 focus:outline-none dark:border-stone-800 dark:bg-stone-950 dark:text-stone-200"
                >
                  <option value="Technology">Technology &amp; Software Engineering</option>
                  <option value="Finance">Finance, Accounting &amp; Legal</option>
                  <option value="Management">Product &amp; Project Management</option>
                  <option value="Healthcare">Healthcare &amp; Clinical Operations</option>
                  <option value="Sales">Sales &amp; Account Management</option>
                  <option value="Operations">Customer Service &amp; Office Operations</option>
                  <option value="Retail">Retail &amp; Customer Support</option>
                  <option value="General Professional">General Professional</option>
                </select>
              </div>

              {/* Experience Tier */}
              <div>
                <label className="font-medium text-stone-700 dark:text-stone-300 block mb-1">
                  Experience Tier
                </label>
                <select
                  value={experienceLevel}
                  onChange={(e) => setExperienceLevel(e.target.value)}
                  className="w-full rounded-lg border border-stone-200 bg-stone-50/70 p-2 text-stone-800 focus:outline-none dark:border-stone-800 dark:bg-stone-950 dark:text-stone-200"
                >
                  <option value="Internship">Internship (0 years)</option>
                  <option value="Entry level">Entry level (0 - 2 years)</option>
                  <option value="Associate">Associate (2 - 5 years)</option>
                  <option value="Mid-Senior level">Mid-Senior level (5 - 8 years)</option>
                  <option value="Director">Director (8 - 12 years)</option>
                  <option value="Executive">Executive / VP (12+ years)</option>
                  <option value="Not Specified">Not Specified</option>
                </select>
              </div>

              {/* Geography Tier */}
              <div>
                <label className="font-medium text-stone-700 dark:text-stone-300 block mb-1">
                  Location Cost Tier
                </label>
                <select
                  value={locationTier}
                  onChange={(e) => setLocationTier(e.target.value)}
                  className="w-full rounded-lg border border-stone-200 bg-stone-50/70 p-2 text-stone-800 focus:outline-none dark:border-stone-800 dark:bg-stone-950 dark:text-stone-200"
                >
                  <option value="Tier 1 (NYC, SF, Seattle, Boston)">Tier 1 Metro (New York, SF Bay Area, Seattle, Boston)</option>
                  <option value="Tier 2 (Austin, Chicago, Denver, Atlanta)">Tier 2 Metro (Austin, Chicago, Dallas, Atlanta, Denver)</option>
                  <option value="Tier 3 (Regional / Secondary)">Tier 3 / Regional Markets</option>
                </select>
              </div>

              {/* Remote Arrangement */}
              <div>
                <label className="font-medium text-stone-700 dark:text-stone-300 block mb-1">
                  Work Arrangement
                </label>
                <div className="grid grid-cols-2 gap-2">
                  <button
                    type="button"
                    onClick={() => setWorkArrangement('1')}
                    className={`rounded-lg border py-1.5 text-center transition-all ${
                      workArrangement === '1'
                        ? 'border-emerald-600 bg-emerald-50 text-emerald-800 font-medium dark:bg-emerald-950 dark:text-emerald-200 dark:border-emerald-700'
                        : 'border-stone-200 bg-stone-50 text-stone-600 dark:border-stone-800 dark:bg-stone-950 dark:text-stone-400'
                    }`}
                  >
                    Remote Eligible
                  </button>
                  <button
                    type="button"
                    onClick={() => setWorkArrangement('0')}
                    className={`rounded-lg border py-1.5 text-center transition-all ${
                      workArrangement === '0'
                        ? 'border-emerald-600 bg-emerald-50 text-emerald-800 font-medium dark:bg-emerald-950 dark:text-emerald-200 dark:border-emerald-700'
                        : 'border-stone-200 bg-stone-50 text-stone-600 dark:border-stone-800 dark:bg-stone-950 dark:text-stone-400'
                    }`}
                  >
                    On-Site / Location Bound
                  </button>
                </div>
              </div>

            </div>
          </div>

          {/* Model Output Card */}
          <div className="mt-6 rounded-xl border border-stone-200 bg-stone-50/80 p-4 dark:border-stone-800 dark:bg-stone-800/40">
            {isPredicting ? (
              <div className="flex items-center justify-center py-6 gap-2 text-xs text-stone-500">
                <Loader2 className="h-4 w-4 animate-spin text-emerald-600" />
                <span>Running Scikit-learn inference pipeline...</span>
              </div>
            ) : salaryError ? (
              <div className="text-xs text-rose-600 dark:text-rose-400 space-y-1">
                <div className="flex items-center gap-1.5 font-semibold">
                  <AlertCircle className="h-4 w-4" />
                  <span>Prediction Service Offline</span>
                </div>
                <p className="text-[11px] text-stone-500">
                  {salaryError}
                </p>
                <button
                  onClick={runSalaryPrediction}
                  className="mt-2 text-xs underline font-medium hover:text-rose-700"
                >
                  Retry Prediction
                </button>
              </div>
            ) : salaryResult ? (
              <div>
                <div className="flex items-center justify-between text-xs text-stone-500">
                  <span>ML Predicted Compensation</span>
                  <span className="font-mono text-emerald-600 dark:text-emerald-400 font-medium">
                    {salaryResult.model_name} (R² = {salaryResult.model_r2_score})
                  </span>
                </div>
                
                <div className="mt-2 font-mono text-2xl font-bold text-stone-900 dark:text-stone-100">
                  ${salaryResult.predicted_salary?.toLocaleString()}
                  <span className="text-xs font-normal text-stone-500 ml-1">/ year</span>
                </div>
                
                <div className="text-[11px] text-stone-500 mt-0.5">
                  Expected Empirical Range: <strong className="text-stone-800 dark:text-stone-200 font-mono">
                    ${salaryResult.expected_range_min?.toLocaleString()} – ${salaryResult.expected_range_max?.toLocaleString()}
                  </strong> (±0.70 MAE)
                </div>

                {/* Percentile bar */}
                <div className="mt-4 pt-3 border-t border-stone-200/60 dark:border-stone-700/60">
                  <div className="flex items-center justify-between text-[11px] mb-1 text-stone-600 dark:text-stone-400">
                    <span>Market Percentile Ranking</span>
                    <span className="font-mono font-bold text-stone-800 dark:text-stone-200">
                      {salaryResult.percentile_rank}th Percentile
                    </span>
                  </div>
                  <div className="h-2 w-full rounded-full bg-stone-200 dark:bg-stone-700 overflow-hidden">
                    <div 
                      className="h-full rounded-full bg-emerald-600 transition-all duration-300"
                      style={{ width: `${salaryResult.percentile_rank}%` }}
                    />
                  </div>
                </div>
              </div>
            ) : (
              <div className="text-center py-4 text-xs text-stone-400">
                Adjust parameters above to generate predictions.
              </div>
            )}
          </div>
        </div>

        {/* Module 2: Real NLP Skill Extractor */}
        <div className="rounded-2xl border border-stone-200 bg-white p-6 shadow-2xs dark:border-stone-800 dark:bg-stone-900 flex flex-col justify-between">
          <div>
            <div className="flex items-center justify-between pb-4 border-b border-stone-100 dark:border-stone-800">
              <div className="flex items-center gap-2">
                <FileText className="h-4 w-4 text-indigo-600" />
                <h2 className="text-base font-semibold text-stone-900 dark:text-stone-100">
                  NLP Description &amp; Entity Extractor
                </h2>
              </div>
              <span className="rounded bg-indigo-50 px-2 py-0.5 text-[10px] font-mono font-semibold text-indigo-700 dark:bg-indigo-950 dark:text-indigo-300 border border-indigo-200 dark:border-indigo-800">
                FastAPI Tokenizer
              </span>
            </div>

            <p className="mt-3 text-xs text-stone-500 dark:text-stone-400">
              Processes raw descriptions through phrase-level n-gram matching, credential regex extraction, and token metrics.
            </p>

            {/* Presets */}
            <div className="mt-4 flex flex-wrap items-center gap-1.5 text-xs">
              <span className="text-[11px] text-stone-400">Sample Job Profiles:</span>
              {sampleDescriptions.map((preset) => (
                <button
                  key={preset.label}
                  onClick={() => {
                    setDescriptionInput(preset.text);
                    setExtractedResults(null);
                  }}
                  className="rounded-md border border-stone-200 bg-stone-50 px-2 py-0.5 text-[11px] text-stone-600 hover:bg-stone-100 dark:border-stone-800 dark:bg-stone-950 dark:text-stone-400"
                >
                  {preset.label}
                </button>
              ))}
            </div>

            {/* Textarea */}
            <div className="mt-3">
              <textarea
                rows={4}
                value={descriptionInput}
                onChange={(e) => setDescriptionInput(e.target.value)}
                placeholder="Paste any job description to extract skills..."
                className="w-full rounded-xl border border-stone-200 bg-stone-50/70 p-3 text-xs text-stone-800 placeholder-stone-400 focus:border-stone-400 focus:bg-white focus:outline-none dark:border-stone-800 dark:bg-stone-950 dark:text-stone-200 leading-relaxed font-mono"
              />
            </div>

            {/* Action button */}
            <button
              onClick={runNlpExtraction}
              disabled={isExtracting || !descriptionInput.trim()}
              className="mt-2 inline-flex items-center gap-1.5 rounded-lg bg-indigo-600 px-3.5 py-2 text-xs font-medium text-white shadow-sm hover:bg-indigo-700 transition-colors disabled:opacity-50"
            >
              {isExtracting ? (
                <>
                  <Loader2 className="h-3.5 w-3.5 animate-spin" />
                  <span>Processing NLP Pipeline...</span>
                </>
              ) : (
                <>
                  <Zap className="h-3.5 w-3.5" />
                  <span>Run NLP Entity Extraction</span>
                </>
              )}
            </button>
          </div>

          {/* Results Container */}
          <div className="mt-5 rounded-xl border border-stone-200 bg-stone-50/80 p-4 dark:border-stone-800 dark:bg-stone-800/40">
            {nlpError ? (
              <div className="text-xs text-rose-600 dark:text-rose-400 flex items-center gap-2">
                <AlertCircle className="h-4 w-4 shrink-0" />
                <span>{nlpError}</span>
              </div>
            ) : extractedResults ? (
              <div className="space-y-3 text-xs">
                <div className="flex items-center justify-between border-b border-stone-200/60 pb-2 dark:border-stone-700/60">
                  <span className="font-semibold text-stone-800 dark:text-stone-200">
                    Inferred Domain: {extractedResults.inferred_category}
                  </span>
                  <span className="font-mono text-indigo-600 dark:text-indigo-400 font-bold">
                    {extractedResults.total_detected} Entities Found
                  </span>
                </div>

                {/* Technical Skills */}
                <div>
                  <span className="text-[11px] text-stone-500 block mb-1">
                    Technical &amp; Computational Skills ({extractedResults.technical_skills?.length || 0}):
                  </span>
                  <div className="flex flex-wrap gap-1.5">
                    {extractedResults.technical_skills?.length > 0 ? (
                      extractedResults.technical_skills.map(s => (
                        <span key={s} className="rounded-md bg-indigo-50 border border-indigo-200 px-2 py-0.5 text-[10px] font-mono font-medium text-indigo-700 dark:bg-indigo-950 dark:border-indigo-800 dark:text-indigo-300">
                          {s}
                        </span>
                      ))
                    ) : (
                      <span className="text-stone-400 text-[11px]">No technical competencies identified</span>
                    )}
                  </div>
                </div>

                {/* Soft & Leadership Skills */}
                {extractedResults.soft_skills?.length > 0 && (
                  <div>
                    <span className="text-[11px] text-stone-500 block mb-1">
                      Soft &amp; Leadership Skills:
                    </span>
                    <div className="flex flex-wrap gap-1.5">
                      {extractedResults.soft_skills.map(s => (
                        <span key={s} className="rounded-md bg-emerald-50 border border-emerald-200 px-2 py-0.5 text-[10px] font-medium text-emerald-800 dark:bg-emerald-950 dark:border-emerald-800 dark:text-emerald-300">
                          {s}
                        </span>
                      ))}
                    </div>
                  </div>
                )}

                {/* Experience & Education */}
                <div className="grid grid-cols-2 gap-2 pt-2 border-t border-stone-200/60 dark:border-stone-700/60 text-[11px]">
                  <div>
                    <span className="text-stone-500 block">Experience Duration:</span>
                    <strong className="text-stone-800 dark:text-stone-200">{extractedResults.experience_required}</strong>
                  </div>
                  <div>
                    <span className="text-stone-500 block">Educational Qualification:</span>
                    <strong className="text-stone-800 dark:text-stone-200">{extractedResults.degree_required}</strong>
                  </div>
                </div>

                {/* Real Token Statistics */}
                <div className="pt-2 border-t border-stone-200/60 dark:border-stone-700/60 flex items-center justify-between text-[10px] text-stone-400 font-mono">
                  <span>Tokens: {extractedResults.token_statistics?.word_count} words</span>
                  <span>Unique: {extractedResults.token_statistics?.unique_words}</span>
                  <span>Density: {extractedResults.token_statistics?.skill_density_pct}%</span>
                </div>
              </div>
            ) : (
              <div className="py-4 text-center text-xs text-stone-400">
                Click <strong>"Run NLP Entity Extraction"</strong> to send this job description to the FastAPI NLP processor.
              </div>
            )}
          </div>
        </div>

      </div>

    </div>
  );
}
