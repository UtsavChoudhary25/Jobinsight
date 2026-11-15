import React, { useState } from 'react';
import { dataCleaningStats } from '../data/jobInsightData';
import { 
  Database, 
  CheckCircle2, 
  Terminal, 
  Layers, 
  Clock, 
  FileCheck, 
  Copy, 
  Check,
  ShieldCheck,
  Code2
} from 'lucide-react';

export default function PipelineTab() {
  const [copiedSnippet, setCopiedSnippet] = useState(null);

  const colabCodeSnippet = `# 6. HANDLE MISSING VALUES
jobs['description'] = jobs['description'].fillna('')
jobs['company_name'] = jobs['company_name'].fillna('Unknown')
jobs['formatted_experience_level'] = (
    jobs['formatted_experience_level'].fillna('Not Specified')
)
jobs['skills_desc'] = jobs['skills_desc'].fillna('')
jobs['formatted_work_type'] = jobs['formatted_work_type'].fillna('Unknown')

# 8. CONVERT UNIX TIMESTAMPS TO DATETIME
jobs['posted_date'] = pd.to_datetime(
    jobs['original_listed_time'], unit='ms', errors='coerce', utc=True
)

# 9. EXTRACT CALENDAR FEATURES
jobs['posting_year'] = jobs['posted_date'].dt.year
jobs['posting_month'] = jobs['posted_date'].dt.month
jobs['posting_day'] = jobs['posted_date'].dt.day
jobs['posting_weekday'] = jobs['posted_date'].dt.day_name()`;

  const copyCode = () => {
    navigator.clipboard.writeText(colabCodeSnippet);
    setCopiedSnippet(true);
    setTimeout(() => setCopiedSnippet(false), 2000);
  };

  const featureSchema = [
    { name: "job_id", type: "int64", role: "Primary Key", desc: "Unique LinkedIn job posting identifier" },
    { name: "company_name", type: "object", role: "Categorical", desc: "Hiring entity; imputed to 'Unknown' when null" },
    { name: "title", type: "object", role: "Categorical", desc: "Designation title, trimmed and sanitized" },
    { name: "normalized_salary", type: "float64", role: "Target Variable", desc: "Standardized annual rate across hourly & yearly disclosures" },
    { name: "formatted_work_type", type: "object", role: "Categorical", desc: "Full-time, Contract, Part-time, Temporary" },
    { name: "formatted_experience_level", type: "object", role: "Categorical", desc: "Entry level, Mid-Senior, Associate, Director" },
    { name: "remote_allowed", type: "float64", role: "Binary Flag", desc: "1.0 if remote, 0.0 or null for on-site requirements" },
    { name: "posted_date", type: "datetime64[ns, UTC]", role: "Temporal Index", desc: "Converted from original_listed_time millisecond epoch" },
    { name: "posting_weekday", type: "object", role: "Engineered Feature", desc: "Day of week (Monday–Sunday) extracted from UTC timestamp" },
  ];

  return (
    <div className="space-y-6">
      
      {/* Header Banner */}
      <div className="rounded-2xl border border-stone-200 bg-white p-6 shadow-2xs dark:border-stone-800 dark:bg-stone-900">
        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
          <div>
            <div className="flex items-center gap-2 text-xs font-semibold uppercase tracking-wider text-stone-600 dark:text-stone-300">
              <Database className="h-3.5 w-3.5 text-indigo-600" />
              <span>Data Engineering &amp; ETL Audit</span>
            </div>
            <h1 className="mt-1 text-2xl font-bold tracking-tight text-stone-900 dark:text-stone-100 sm:text-3xl">
              Preprocessing &amp; Transformation Pipeline
            </h1>
            <p className="mt-1 text-sm text-stone-600 dark:text-stone-400 max-w-2xl">
              Verification of all data cleaning, schema validation, and feature engineering steps 
              executed in Phase 1 &amp; Phase 2 inside Google Colab.
            </p>
          </div>

          <div className="flex items-center gap-2 text-xs font-mono">
            <span className="rounded-lg bg-emerald-50 px-3 py-1.5 font-medium text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-800 flex items-center gap-1.5">
              <CheckCircle2 className="h-3.5 w-3.5" />
              <span>Phase 1 &amp; 2 Verified</span>
            </span>
          </div>
        </div>
      </div>

      {/* Audit Stages Progress Cards */}
      <div className="rounded-2xl border border-stone-200 bg-white p-6 shadow-2xs dark:border-stone-800 dark:bg-stone-900">
        <div className="flex items-center justify-between pb-4 border-b border-stone-100 dark:border-stone-800">
          <h2 className="text-base font-semibold text-stone-900 dark:text-stone-100">
            Pipeline Execution Checklist
          </h2>
          <span className="font-mono text-xs text-stone-500">
            8 Sequential Steps
          </span>
        </div>

        <div className="mt-6 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          {dataCleaningStats.map((item, idx) => (
            <div 
              key={item.stage}
              className="rounded-xl border border-stone-200/90 bg-stone-50/50 p-4 dark:border-stone-800 dark:bg-stone-800/30 flex flex-col justify-between"
            >
              <div>
                <div className="flex items-center justify-between text-xs mb-2">
                  <span className="font-mono text-[10px] text-stone-400">Step 0{idx + 1}</span>
                  <CheckCircle2 className="h-4 w-4 text-emerald-600 dark:text-emerald-400" />
                </div>
                <h3 className="font-semibold text-xs text-stone-900 dark:text-stone-100">
                  {item.stage}
                </h3>
                <div className="mt-1 font-mono text-sm font-bold text-indigo-600 dark:text-indigo-400">
                  {item.count}
                </div>
              </div>
              <p className="mt-3 text-[11px] text-stone-500 dark:text-stone-400 border-t border-stone-200/60 pt-2 dark:border-stone-700/60">
                {item.note}
              </p>
            </div>
          ))}
        </div>
      </div>

      {/* Code Snippet & Feature Dictionary Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        
        {/* Feature Schema Table */}
        <div className="rounded-2xl border border-stone-200 bg-white p-6 shadow-2xs dark:border-stone-800 dark:bg-stone-900">
          <div className="flex items-center justify-between pb-4 border-b border-stone-100 dark:border-stone-800">
            <div>
              <h2 className="text-base font-semibold text-stone-900 dark:text-stone-100">
                Cleaned Data Dictionary
              </h2>
              <p className="text-xs text-stone-500 dark:text-stone-400">
                Key features exported to <code className="font-mono text-[10px]">cleaned_jobs.csv</code>
              </p>
            </div>
            <span className="font-mono text-xs text-stone-500">
              38 Total Columns
            </span>
          </div>

          <div className="mt-4 overflow-x-auto">
            <table className="w-full text-left text-xs">
              <thead className="text-[11px] text-stone-400 border-b border-stone-100 dark:border-stone-800">
                <tr>
                  <th className="py-2 pr-3 font-medium">Feature</th>
                  <th className="py-2 px-3 font-medium">Type</th>
                  <th className="py-2 px-3 font-medium">Role</th>
                  <th className="py-2 pl-3 font-medium">Notes</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-stone-100 dark:divide-stone-800 font-mono text-[11px]">
                {featureSchema.map((f) => (
                  <tr key={f.name}>
                    <td className="py-2.5 pr-3 font-bold text-stone-800 dark:text-stone-200">
                      {f.name}
                    </td>
                    <td className="py-2.5 px-3 text-stone-500">
                      {f.type}
                    </td>
                    <td className="py-2.5 px-3">
                      <span className="rounded bg-stone-100 px-1.5 py-0.5 text-[10px] text-stone-700 dark:bg-stone-800 dark:text-stone-300">
                        {f.role}
                      </span>
                    </td>
                    <td className="py-2.5 pl-3 font-sans text-stone-500 dark:text-stone-400 text-[11px]">
                      {f.desc}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>

        {/* Python Code Card */}
        <div className="rounded-2xl border border-stone-200 bg-white p-6 shadow-2xs dark:border-stone-800 dark:bg-stone-900 flex flex-col justify-between">
          <div>
            <div className="flex items-center justify-between pb-4 border-b border-stone-100 dark:border-stone-800">
              <div className="flex items-center gap-2">
                <Code2 className="h-4 w-4 text-stone-600 dark:text-stone-300" />
                <h2 className="text-base font-semibold text-stone-900 dark:text-stone-100">
                  Colab Preprocessing Pipeline Script
                </h2>
              </div>
              <button
                onClick={copyCode}
                className="inline-flex items-center gap-1.5 rounded-md border border-stone-200 bg-stone-50 px-2.5 py-1 text-xs text-stone-600 hover:bg-stone-100 dark:border-stone-700 dark:bg-stone-800 dark:text-stone-300"
              >
                {copiedSnippet ? <Check className="h-3 w-3 text-emerald-600" /> : <Copy className="h-3 w-3" />}
                <span>{copiedSnippet ? 'Copied' : 'Copy Python'}</span>
              </button>
            </div>

            <p className="mt-3 text-xs text-stone-500 dark:text-stone-400">
              Exact cleaning logic implemented in Python and executed on Google Colab hardware.
            </p>

            <div className="mt-4 rounded-xl bg-stone-900 p-4 text-[11px] font-mono text-stone-200 overflow-x-auto leading-relaxed dark:bg-stone-950 border border-stone-800">
              <pre>{colabCodeSnippet}</pre>
            </div>
          </div>

          <div className="mt-4 pt-3 border-t border-stone-100 dark:border-stone-800 flex items-center justify-between text-xs text-stone-500">
            <span>Cleaned output saved:</span>
            <code className="font-mono text-stone-800 dark:text-stone-200">/content/cleaned_jobs.csv</code>
          </div>
        </div>

      </div>

    </div>
  );
}
