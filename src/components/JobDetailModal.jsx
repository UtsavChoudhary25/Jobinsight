import React from 'react';
import { 
  X, 
  Building, 
  MapPin, 
  DollarSign, 
  Briefcase, 
  Globe, 
  Eye, 
  Users, 
  Tag, 
  ExternalLink,
  Calendar,
  Share2
} from 'lucide-react';

export default function JobDetailModal({ job, onClose }) {
  if (!job) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-stone-900/60 backdrop-blur-xs">
      <div 
        className="relative w-full max-w-2xl rounded-2xl border border-stone-200 bg-white p-6 shadow-xl dark:border-stone-800 dark:bg-stone-900 max-h-[90vh] overflow-y-auto"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Close Button */}
        <button
          onClick={onClose}
          className="absolute right-4 top-4 rounded-lg p-1 text-stone-400 hover:text-stone-700 hover:bg-stone-100 dark:hover:text-stone-200 dark:hover:bg-stone-800 transition-colors"
        >
          <X className="h-5 w-5" />
        </button>

        {/* Top Badges */}
        <div className="flex flex-wrap items-center gap-2">
          <span className="rounded bg-indigo-50 px-2 py-0.5 text-xs font-semibold text-indigo-700 dark:bg-indigo-950 dark:text-indigo-300">
            {job.workType}
          </span>
          {job.remote && (
            <span className="rounded bg-emerald-50 px-2 py-0.5 text-xs font-semibold text-emerald-700 dark:bg-emerald-950 dark:text-emerald-300">
              Remote Eligible
            </span>
          )}
          <span className="rounded bg-stone-100 px-2 py-0.5 text-xs text-stone-600 dark:bg-stone-800 dark:text-stone-400">
            ID: #{job.id}
          </span>
        </div>

        {/* Title & Company */}
        <div className="mt-3">
          <h2 className="text-xl font-bold tracking-tight text-stone-900 dark:text-stone-100">
            {job.title}
          </h2>
          <div className="mt-1 flex flex-wrap items-center gap-3 text-xs text-stone-600 dark:text-stone-400">
            <span className="flex items-center gap-1 font-medium text-stone-800 dark:text-stone-200">
              <Building className="h-3.5 w-3.5 text-stone-400" />
              {job.company}
            </span>
            <span className="flex items-center gap-1">
              <MapPin className="h-3.5 w-3.5 text-stone-400" />
              {job.location}
            </span>
            <span className="flex items-center gap-1">
              <Briefcase className="h-3.5 w-3.5 text-stone-400" />
              {job.experience}
            </span>
          </div>
        </div>

        {/* Key Metrics Strip */}
        <div className="mt-5 grid grid-cols-3 gap-3 rounded-xl border border-stone-100 bg-stone-50/70 p-3.5 dark:border-stone-800 dark:bg-stone-800/40 text-xs">
          <div>
            <span className="text-stone-400 text-[10px] uppercase font-medium block">Compensation</span>
            <span className="font-mono font-bold text-stone-900 dark:text-stone-100 text-sm">
              {job.salaryDisplay}
            </span>
          </div>
          <div>
            <span className="text-stone-400 text-[10px] uppercase font-medium block">Candidate Views</span>
            <span className="font-mono font-semibold text-stone-700 dark:text-stone-300">
              {job.views || 'N/A'} views
            </span>
          </div>
          <div>
            <span className="text-stone-400 text-[10px] uppercase font-medium block">Applications</span>
            <span className="font-mono font-semibold text-stone-700 dark:text-stone-300">
              {job.applies || 'N/A'} applies
            </span>
          </div>
        </div>

        {/* Extracted Skills */}
        <div className="mt-5">
          <h3 className="text-xs font-semibold uppercase tracking-wider text-stone-500 mb-2">
            Required &amp; Extracted Competencies
          </h3>
          <div className="flex flex-wrap gap-1.5">
            {job.skills.map((skill) => (
              <span
                key={skill}
                className="rounded-lg border border-stone-200 bg-stone-50 px-2.5 py-1 text-xs font-medium text-stone-700 dark:border-stone-700 dark:bg-stone-800 dark:text-stone-300"
              >
                {skill}
              </span>
            ))}
          </div>
        </div>

        {/* Job Description */}
        <div className="mt-5">
          <h3 className="text-xs font-semibold uppercase tracking-wider text-stone-500 mb-2">
            Job Description &amp; Scope
          </h3>
          <div className="rounded-xl border border-stone-100 bg-stone-50/40 p-4 text-xs leading-relaxed text-stone-700 dark:border-stone-800 dark:bg-stone-800/20 dark:text-stone-300">
            {job.description}
          </div>
        </div>

        {/* Footer actions */}
        <div className="mt-6 flex items-center justify-between border-t border-stone-100 pt-4 dark:border-stone-800">
          <span className="text-xs text-stone-400">
            Source: LinkedIn dataset <code className="font-mono text-[10px]">cleaned_jobs.csv</code>
          </span>
          <button
            onClick={onClose}
            className="rounded-lg bg-stone-900 px-4 py-2 text-xs font-medium text-white hover:bg-stone-800 transition-colors dark:bg-stone-100 dark:text-stone-900 dark:hover:bg-stone-200"
          >
            Done
          </button>
        </div>
      </div>
    </div>
  );
}
