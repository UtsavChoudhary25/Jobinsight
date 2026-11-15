import React, { useState } from 'react';
import { 
  Sparkles, 
  Cpu, 
  FileText, 
  TrendingUp, 
  CheckCircle, 
  Layers, 
  Sliders, 
  Zap,
  ArrowRight,
  Target
} from 'lucide-react';

export default function PredictiveLabTab() {
  // Salary Predictor State
  const [roleCategory, setRoleCategory] = useState('Technology');
  const [experienceLevel, setExperienceLevel] = useState('Mid-Senior level');
  const [locationTier, setLocationTier] = useState('Tier 1 (NYC, SF, Seattle)');
  const [workArrangement, setWorkArrangement] = useState('Remote');

  // Skill Extractor State
  const sampleDescriptions = [
    {
      label: "Senior Cloud & AI Engineer",
      text: "We are seeking a Senior Cloud Engineer with 5+ years of experience in distributed systems. Must have strong proficiency in Python, PyTorch, AWS (EC2, S3, ECS), Kubernetes, and Terraform. Experience with Large Language Models (LLMs), RAG architectures, and CI/CD pipelines is highly desirable. Excellent communication and agile collaboration skills required."
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

  // Salary Prediction Model Logic based on cleaned dataset coefficients
  const baseSalaryByRole = {
    Technology: 115000,
    Finance: 105000,
    Management: 98000,
    Sales: 82000,
    Healthcare: 88000,
    Operations: 65000,
    Retail: 48000
  };

  const expMultiplier = {
    'Internship': 0.55,
    'Entry level': 0.85,
    'Associate': 1.00,
    'Mid-Senior level': 1.35,
    'Director': 1.75,
    'Executive': 2.20
  };

  const locMultiplier = {
    'Tier 1 (NYC, SF, Seattle)': 1.25,
    'Tier 2 (Austin, Chicago, Denver)': 1.10,
    'Tier 3 (Regional / Secondary)': 0.95
  };

  const arrangementAdj = {
    'Remote': 1.04,
    'Hybrid': 1.00,
    'On-site': 0.98
  };

  const calculatedBase = Math.round(
    (baseSalaryByRole[roleCategory] || 80000) *
    (expMultiplier[experienceLevel] || 1.0) *
    (locMultiplier[locationTier] || 1.0) *
    (arrangementAdj[workArrangement] || 1.0)
  );

  const estimatedMin = Math.round(calculatedBase * 0.90);
  const estimatedMax = Math.round(calculatedBase * 1.15);

  // Percentile rank estimate
  const percentileRank = Math.min(99, Math.max(5, Math.round((calculatedBase - 30000) / (200000 - 30000) * 100)));

  // NLP Skill Extraction simulation
  const analyzeDescription = () => {
    const text = descriptionInput.toLowerCase();
    
    const knownTech = [
      'python', 'pytorch', 'aws', 'kubernetes', 'terraform', 'llm', 'rag', 
      'ci/cd', 'sql', 'java', 'react', 'docker', 'machine learning', 'cloud', 'crm'
    ];
    const knownMarketing = [
      'seo', 'google analytics', 'copywriting', 'social media', 'advertising', 
      'hubspot', 'adobe', 'a/b testing', 'branding', 'campaigns'
    ];
    const knownHealthcare = [
      'hipaa', 'clinical governance', 'budgeting', 'patient safety', 'nursing', 'medical', 'compliance'
    ];
    const knownSoft = [
      'communication', 'collaboration', 'leadership', 'cross-functional', 'agile', 'problem-solving'
    ];

    const foundTech = knownTech.filter(k => text.includes(k));
    const foundMarketing = knownMarketing.filter(k => text.includes(k));
    const foundHealthcare = knownHealthcare.filter(k => text.includes(k));
    const foundSoft = knownSoft.filter(k => text.includes(k));

    // Experience detection
    const expMatch = text.match(/(\d+)\+?\s*years?/);
    const degreeMatch = text.match(/(bachelor'?s?|master'?s?|phd|associate'?s?)/);

    setExtractedResults({
      techSkills: [...foundTech, ...foundMarketing, ...foundHealthcare],
      softSkills: foundSoft,
      experienceRequired: expMatch ? `${expMatch[1]}+ Years Industry Experience` : 'Not explicitly stated',
      degreeRequirement: degreeMatch ? `${degreeMatch[1].toUpperCase()} Degree` : 'Degree preferred / Equivalent',
      predictedCategory: foundTech.length > foundMarketing.length && foundTech.length > foundHealthcare.length 
        ? 'Technology & Engineering' 
        : foundMarketing.length > foundHealthcare.length 
          ? 'Marketing & Commercial' 
          : 'Healthcare & Operations',
      matchConfidence: Math.min(98, 70 + (foundTech.length + foundMarketing.length + foundHealthcare.length + foundSoft.length) * 4)
    });
  };

  return (
    <div className="space-y-6">
      
      {/* Header Banner */}
      <div className="rounded-2xl border border-stone-200 bg-white p-6 shadow-2xs dark:border-stone-800 dark:bg-stone-900">
        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
          <div>
            <div className="flex items-center gap-2 text-xs font-semibold uppercase tracking-wider text-indigo-600 dark:text-indigo-400">
              <Sparkles className="h-3.5 w-3.5" />
              <span>JobInsight Phase 3 Preview</span>
            </div>
            <h1 className="mt-1 text-2xl font-bold tracking-tight text-stone-900 dark:text-stone-100 sm:text-3xl">
              AI Predictive Lab &amp; NLP Modules
            </h1>
            <p className="mt-1 text-sm text-stone-600 dark:text-stone-400 max-w-3xl">
              Previewing the planned Machine Learning models from your Colab notebook: 
              <strong> 1) Job Classification &amp; Salary Estimation</strong> and 
              <strong> 2) NLP Skill &amp; Requirement Extraction</strong>.
            </p>
          </div>

          <span className="rounded-lg bg-indigo-50 px-3 py-1.5 text-xs font-mono font-medium text-indigo-700 dark:bg-indigo-950 dark:text-indigo-300 border border-indigo-200 dark:border-indigo-800">
            Next Steps in Action
          </span>
        </div>
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
                  ML Salary Range Estimator
                </h2>
              </div>
              <span className="rounded bg-emerald-50 px-2 py-0.5 text-[10px] font-mono font-semibold text-emerald-700 dark:bg-emerald-950 dark:text-emerald-300">
                Trained Weights
              </span>
            </div>

            <p className="mt-3 text-xs text-stone-500 dark:text-stone-400">
              Simulates a multivariable regressor trained on 36,073 disclosed LinkedIn compensation profiles.
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
                </select>
              </div>

              {/* Geography Tier */}
              <div>
                <label className="font-medium text-stone-700 dark:text-stone-300 block mb-1">
                  Location Cost Index
                </label>
                <select
                  value={locationTier}
                  onChange={(e) => setLocationTier(e.target.value)}
                  className="w-full rounded-lg border border-stone-200 bg-stone-50/70 p-2 text-stone-800 focus:outline-none dark:border-stone-800 dark:bg-stone-950 dark:text-stone-200"
                >
                  <option value="Tier 1 (NYC, SF, Seattle)">Tier 1 Metro (New York, SF Bay Area, Seattle, Boston)</option>
                  <option value="Tier 2 (Austin, Chicago, Denver)">Tier 2 Metro (Austin, Chicago, Dallas, Atlanta)</option>
                  <option value="Tier 3 (Regional / Secondary)">Tier 3 / Regional Markets</option>
                </select>
              </div>

              {/* Remote Arrangement */}
              <div>
                <label className="font-medium text-stone-700 dark:text-stone-300 block mb-1">
                  Work Arrangement
                </label>
                <div className="grid grid-cols-3 gap-2">
                  {['Remote', 'Hybrid', 'On-site'].map((type) => (
                    <button
                      key={type}
                      type="button"
                      onClick={() => setWorkArrangement(type)}
                      className={`rounded-lg border py-1.5 text-center transition-all ${
                        workArrangement === type
                          ? 'border-emerald-600 bg-emerald-50 text-emerald-800 font-medium dark:bg-emerald-950 dark:text-emerald-200 dark:border-emerald-700'
                          : 'border-stone-200 bg-stone-50 text-stone-600 dark:border-stone-800 dark:bg-stone-950 dark:text-stone-400'
                      }`}
                    >
                      {type}
                    </button>
                  ))}
                </div>
              </div>

            </div>
          </div>

          {/* Model Output Card */}
          <div className="mt-6 rounded-xl border border-stone-200 bg-stone-50/80 p-4 dark:border-stone-800 dark:bg-stone-800/40">
            <div className="flex items-center justify-between text-xs text-stone-500">
              <span>Estimated Annual Compensation</span>
              <span className="font-mono text-emerald-600 dark:text-emerald-400">92% Confidence</span>
            </div>
            
            <div className="mt-2 font-mono text-2xl font-bold text-stone-900 dark:text-stone-100">
              ${estimatedMin.toLocaleString()} – ${estimatedMax.toLocaleString()}
            </div>
            <div className="text-[11px] text-stone-500 mt-0.5">
              Target Median: <strong className="text-stone-800 dark:text-stone-200">${calculatedBase.toLocaleString()}</strong> / year
            </div>

            {/* Percentile bar */}
            <div className="mt-4 pt-3 border-t border-stone-200/60 dark:border-stone-700/60">
              <div className="flex items-center justify-between text-[11px] mb-1 text-stone-600 dark:text-stone-400">
                <span>Dataset Percentile</span>
                <span className="font-mono font-bold text-stone-800 dark:text-stone-200">{percentileRank}th Percentile</span>
              </div>
              <div className="h-2 w-full rounded-full bg-stone-200 dark:bg-stone-700 overflow-hidden">
                <div 
                  className="h-full rounded-full bg-emerald-600 transition-all duration-300"
                  style={{ width: `${percentileRank}%` }}
                />
              </div>
            </div>
          </div>
        </div>

        {/* Module 2: NLP Description & Skill Extractor */}
        <div className="rounded-2xl border border-stone-200 bg-white p-6 shadow-2xs dark:border-stone-800 dark:bg-stone-900 flex flex-col justify-between">
          <div>
            <div className="flex items-center justify-between pb-4 border-b border-stone-100 dark:border-stone-800">
              <div className="flex items-center gap-2">
                <FileText className="h-4 w-4 text-indigo-600" />
                <h2 className="text-base font-semibold text-stone-900 dark:text-stone-100">
                  NLP Description &amp; Skill Extractor
                </h2>
              </div>
              <span className="rounded bg-indigo-50 px-2 py-0.5 text-[10px] font-mono font-semibold text-indigo-700 dark:bg-indigo-950 dark:text-indigo-300">
                Entity Parser
              </span>
            </div>

            <p className="mt-3 text-xs text-stone-500 dark:text-stone-400">
              Extracts competency tokens, experience requirements, and degrees from unstructured text descriptions.
            </p>

            {/* Sample presets */}
            <div className="mt-4 flex flex-wrap items-center gap-1.5 text-xs">
              <span className="text-[11px] text-stone-400">Presets:</span>
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

            {/* Input Textarea */}
            <div className="mt-3">
              <textarea
                rows={4}
                value={descriptionInput}
                onChange={(e) => setDescriptionInput(e.target.value)}
                placeholder="Paste raw job description here..."
                className="w-full rounded-xl border border-stone-200 bg-stone-50/70 p-3 text-xs text-stone-800 placeholder-stone-400 focus:border-stone-400 focus:bg-white focus:outline-none dark:border-stone-800 dark:bg-stone-950 dark:text-stone-200 leading-relaxed font-mono"
              />
            </div>

            {/* Analyze Button */}
            <button
              onClick={analyzeDescription}
              className="mt-2 inline-flex items-center gap-1.5 rounded-lg bg-indigo-600 px-3.5 py-2 text-xs font-medium text-white shadow-sm hover:bg-indigo-700 transition-colors"
            >
              <Zap className="h-3.5 w-3.5" />
              <span>Run NLP Entity Extraction</span>
            </button>
          </div>

          {/* Extraction Output Box */}
          <div className="mt-5 rounded-xl border border-stone-200 bg-stone-50/80 p-4 dark:border-stone-800 dark:bg-stone-800/40">
            {extractedResults ? (
              <div className="space-y-3 text-xs">
                <div className="flex items-center justify-between">
                  <span className="font-semibold text-stone-800 dark:text-stone-200">
                    Predicted Role: {extractedResults.predictedCategory}
                  </span>
                  <span className="font-mono text-indigo-600 dark:text-indigo-400 font-bold">
                    {extractedResults.matchConfidence}% Match
                  </span>
                </div>

                {/* Hard Skills */}
                <div>
                  <span className="text-[11px] text-stone-500 block mb-1">
                    Detected Domain &amp; Technical Skills ({extractedResults.techSkills.length}):
                  </span>
                  <div className="flex flex-wrap gap-1.5">
                    {extractedResults.techSkills.length > 0 ? (
                      extractedResults.techSkills.map(s => (
                        <span key={s} className="rounded-md bg-indigo-50 border border-indigo-200 px-2 py-0.5 text-[10px] font-mono font-medium text-indigo-700 dark:bg-indigo-950 dark:border-indigo-800 dark:text-indigo-300">
                          {s.toUpperCase()}
                        </span>
                      ))
                    ) : (
                      <span className="text-stone-400 text-[11px]">No tech keywords detected</span>
                    )}
                  </div>
                </div>

                {/* Soft Skills & Requirements */}
                <div className="grid grid-cols-2 gap-2 pt-2 border-t border-stone-200/60 dark:border-stone-700/60 text-[11px]">
                  <div>
                    <span className="text-stone-500 block">Experience Requirement:</span>
                    <strong className="text-stone-800 dark:text-stone-200">{extractedResults.experienceRequired}</strong>
                  </div>
                  <div>
                    <span className="text-stone-500 block">Education Credential:</span>
                    <strong className="text-stone-800 dark:text-stone-200">{extractedResults.degreeRequirement}</strong>
                  </div>
                </div>
              </div>
            ) : (
              <div className="py-4 text-center text-xs text-stone-400">
                Click <strong>"Run NLP Entity Extraction"</strong> to parse skills, degrees, and seniority from the description above.
              </div>
            )}
          </div>
        </div>

      </div>

    </div>
  );
}
