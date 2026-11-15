import React, { useState } from 'react';
import { 
  topLocations, 
  topCompanies, 
  topJobTitles,
  overviewStats 
} from '../data/jobInsightData';
import { 
  MapPin, 
  Building2, 
  Globe, 
  Briefcase, 
  TrendingUp, 
  Compass, 
  Filter,
  Check
} from 'lucide-react';

export default function GeographyTab() {
  const [activeCategory, setActiveCategory] = useState('all');

  const maxLocationCount = Math.max(...topLocations.map(l => l.count));
  const maxCompanyCount = Math.max(...topCompanies.map(c => c.count));
  const maxTitleCount = Math.max(...topJobTitles.map(t => t.count));

  const filteredTitles = activeCategory === 'all' 
    ? topJobTitles 
    : topJobTitles.filter(t => t.category.toLowerCase() === activeCategory.toLowerCase());

  return (
    <div className="space-y-6">
      
      {/* Header Banner */}
      <div className="rounded-2xl border border-stone-200 bg-white p-6 shadow-2xs dark:border-stone-800 dark:bg-stone-900">
        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
          <div>
            <div className="flex items-center gap-2 text-xs font-semibold uppercase tracking-wider text-stone-600 dark:text-stone-300">
              <Compass className="h-3.5 w-3.5 text-indigo-600" />
              <span>Spatial &amp; Organizational Census</span>
            </div>
            <h1 className="mt-1 text-2xl font-bold tracking-tight text-stone-900 dark:text-stone-100 sm:text-3xl">
              Geography, Employers &amp; Dominant Roles
            </h1>
            <p className="mt-1 text-sm text-stone-600 dark:text-stone-400 max-w-2xl">
              Aggregated across 8,526 distinct geographical centers and 24,428 organizations. 
              Visualizing the top market concentrations across North America.
            </p>
          </div>

          <div className="flex items-center gap-2">
            <span className="rounded-lg bg-stone-100 px-3 py-1.5 text-xs font-mono font-medium text-stone-700 dark:bg-stone-800 dark:text-stone-300 border border-stone-200 dark:border-stone-700">
              8,526 Total Hubs
            </span>
          </div>
        </div>
      </div>

      {/* Remote vs Non-Remote Callout Banner */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        
        {/* Remote */}
        <div className="rounded-xl border border-stone-200 bg-white p-5 shadow-2xs dark:border-stone-800 dark:bg-stone-900">
          <div className="flex items-center justify-between text-stone-500">
            <span className="text-xs font-medium uppercase tracking-wider">Remote Designated</span>
            <Globe className="h-4 w-4 text-indigo-600 dark:text-indigo-400" />
          </div>
          <div className="mt-2 flex items-baseline gap-2">
            <span className="font-mono text-3xl font-bold text-stone-900 dark:text-stone-100">
              {overviewStats.remoteBreakdown.remote.toLocaleString()}
            </span>
            <span className="font-mono text-xs font-semibold text-indigo-600 dark:text-indigo-400">
              12.31%
            </span>
          </div>
          <p className="mt-1 text-xs text-stone-500">Explicitly flagged as work-from-anywhere</p>
        </div>

        {/* On-Site / Unspecified */}
        <div className="rounded-xl border border-stone-200 bg-white p-5 shadow-2xs dark:border-stone-800 dark:bg-stone-900">
          <div className="flex items-center justify-between text-stone-500">
            <span className="text-xs font-medium uppercase tracking-wider">On-Site / Location Bound</span>
            <MapPin className="h-4 w-4 text-amber-600 dark:text-amber-400" />
          </div>
          <div className="mt-2 flex items-baseline gap-2">
            <span className="font-mono text-3xl font-bold text-stone-900 dark:text-stone-100">
              {overviewStats.remoteBreakdown.nonRemoteSpecified.toLocaleString()}
            </span>
            <span className="font-mono text-xs font-semibold text-amber-600 dark:text-amber-400">
              87.69%
            </span>
          </div>
          <p className="mt-1 text-xs text-stone-500">Physical attendance at regional corporate office</p>
        </div>

        {/* Remote Ratio Bar */}
        <div className="rounded-xl border border-stone-200 bg-white p-5 shadow-2xs dark:border-stone-800 dark:bg-stone-900 flex flex-col justify-between">
          <span className="text-xs font-medium uppercase tracking-wider text-stone-500">
            Market Arrangement Share
          </span>
          <div className="mt-2">
            <div className="h-3 w-full rounded-full bg-amber-100 dark:bg-amber-950 overflow-hidden flex">
              <div className="h-full bg-indigo-600 transition-all" style={{ width: '12.31%' }} title="Remote: 12.31%"></div>
              <div className="h-full bg-stone-300 dark:bg-stone-700 transition-all" style={{ width: '87.69%' }} title="Onsite: 87.69%"></div>
            </div>
            <div className="mt-2 flex items-center justify-between text-[11px] text-stone-500">
              <span className="flex items-center gap-1">
                <span className="h-2 w-2 rounded-full bg-indigo-600"></span> Remote (12.3%)
              </span>
              <span className="flex items-center gap-1">
                <span className="h-2 w-2 rounded-full bg-stone-400"></span> On-site (87.7%)
              </span>
            </div>
          </div>
          <p className="text-[11px] text-stone-400">Sampled from 123,849 total records</p>
        </div>

      </div>

      {/* Two Column Grid: Top Locations & Top Companies */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        
        {/* Top 15 Locations */}
        <div className="rounded-2xl border border-stone-200 bg-white p-6 shadow-2xs dark:border-stone-800 dark:bg-stone-900">
          <div className="flex items-center justify-between pb-4 border-b border-stone-100 dark:border-stone-800">
            <div>
              <h2 className="text-base font-semibold text-stone-900 dark:text-stone-100">
                Top 15 Job Posting Locations
              </h2>
              <p className="text-xs text-stone-500 dark:text-stone-400">
                Major metropolitan hubs and nationwide distribution
              </p>
            </div>
            <span className="font-mono text-xs text-stone-500">
              Top 15
            </span>
          </div>

          <div className="mt-5 space-y-2.5">
            {topLocations.map((loc, i) => {
              const pct = (loc.count / maxLocationCount) * 100;
              return (
                <div key={loc.location} className="group">
                  <div className="flex items-center justify-between text-xs mb-1">
                    <div className="flex items-center gap-2">
                      <span className="font-mono text-[10px] text-stone-400 w-4">
                        {i + 1}.
                      </span>
                      <span className="font-medium text-stone-800 dark:text-stone-200">
                        {loc.location}
                      </span>
                    </div>
                    <span className="font-mono font-semibold text-stone-900 dark:text-stone-100">
                      {loc.count.toLocaleString()}
                    </span>
                  </div>
                  <div className="h-2 w-full rounded-full bg-stone-100 dark:bg-stone-800 overflow-hidden">
                    <div 
                      className="h-full rounded-full bg-stone-700 dark:bg-stone-300 transition-all duration-500" 
                      style={{ width: `${pct}%` }}
                    />
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Top 15 Companies */}
        <div className="rounded-2xl border border-stone-200 bg-white p-6 shadow-2xs dark:border-stone-800 dark:bg-stone-900">
          <div className="flex items-center justify-between pb-4 border-b border-stone-100 dark:border-stone-800">
            <div>
              <h2 className="text-base font-semibold text-stone-900 dark:text-stone-100">
                Top 15 Hiring Organizations
              </h2>
              <p className="text-xs text-stone-500 dark:text-stone-400">
                Organizations with highest active recruitment volume
              </p>
            </div>
            <span className="font-mono text-xs text-stone-500">
              Top 15
            </span>
          </div>

          <div className="mt-5 space-y-2.5">
            {topCompanies.map((comp, i) => {
              const pct = (comp.count / maxCompanyCount) * 100;
              return (
                <div key={comp.company} className="group">
                  <div className="flex items-center justify-between text-xs mb-1">
                    <div className="flex items-center gap-2">
                      <span className="font-mono text-[10px] text-stone-400 w-4">
                        {i + 1}.
                      </span>
                      <span className="font-medium text-stone-800 dark:text-stone-200 truncate max-w-[220px]">
                        {comp.company}
                      </span>
                      <span className="rounded bg-stone-100 px-1.5 py-0.2 text-[10px] text-stone-500 dark:bg-stone-800 dark:text-stone-400 hidden sm:inline">
                        {comp.industry}
                      </span>
                    </div>
                    <span className="font-mono font-semibold text-stone-900 dark:text-stone-100">
                      {comp.count.toLocaleString()}
                    </span>
                  </div>
                  <div className="h-2 w-full rounded-full bg-stone-100 dark:bg-stone-800 overflow-hidden">
                    <div 
                      className="h-full rounded-full bg-indigo-600 dark:bg-indigo-400 transition-all duration-500" 
                      style={{ width: `${pct}%` }}
                    />
                  </div>
                </div>
              );
            })}
          </div>
        </div>

      </div>

      {/* Top Job Titles Section */}
      <div className="rounded-2xl border border-stone-200 bg-white p-6 shadow-2xs dark:border-stone-800 dark:bg-stone-900">
        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between pb-4 border-b border-stone-100 dark:border-stone-800 gap-3">
          <div>
            <h2 className="text-base font-semibold text-stone-900 dark:text-stone-100">
              Top 15 Most Common Job Titles
            </h2>
            <p className="text-xs text-stone-500 dark:text-stone-400">
              Most frequently listed roles in the LinkedIn snapshot
            </p>
          </div>

          {/* Category Filter Pills */}
          <div className="flex flex-wrap items-center gap-1.5">
            {['all', 'Sales', 'Operations', 'Finance', 'Management', 'Healthcare', 'Technology'].map((cat) => (
              <button
                key={cat}
                onClick={() => setActiveCategory(cat)}
                className={`rounded-md px-2.5 py-1 text-xs font-medium transition-all ${
                  activeCategory.toLowerCase() === cat.toLowerCase()
                    ? 'bg-stone-900 text-white dark:bg-stone-100 dark:text-stone-900'
                    : 'bg-stone-100 text-stone-600 hover:bg-stone-200 dark:bg-stone-800 dark:text-stone-400 dark:hover:bg-stone-700'
                }`}
              >
                {cat.charAt(0).toUpperCase() + cat.slice(1)}
              </button>
            ))}
          </div>
        </div>

        {/* Titles Grid */}
        <div className="mt-6 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3">
          {filteredTitles.map((t, idx) => (
            <div 
              key={t.title}
              className="flex items-center justify-between rounded-xl border border-stone-200/90 bg-stone-50/50 p-3.5 hover:border-stone-300 transition-all dark:border-stone-800 dark:bg-stone-800/30 dark:hover:border-stone-700"
            >
              <div>
                <span className="text-xs font-medium text-stone-800 dark:text-stone-200 block">
                  {t.title}
                </span>
                <span className="text-[10px] text-stone-500 dark:text-stone-400">
                  {t.category}
                </span>
              </div>
              <div className="text-right">
                <span className="font-mono text-sm font-bold text-stone-900 dark:text-stone-100 block">
                  {t.count}
                </span>
                <span className="text-[10px] text-stone-400">postings</span>
              </div>
            </div>
          ))}
        </div>
      </div>

    </div>
  );
}
