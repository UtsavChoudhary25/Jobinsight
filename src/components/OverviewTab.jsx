import React, { useState } from 'react';
import { 
  overviewStats, 
  employmentTypes, 
  experienceLevels, 
  weeklyPostingTimeline,
  monthlyTrends
} from '../data/jobInsightData';
import { 
  TrendingUp, 
  Briefcase, 
  Building, 
  DollarSign, 
  Globe, 
  Calendar, 
  ArrowUpRight, 
  CheckCircle2, 
  Layers,
  ChevronRight
} from 'lucide-react';

export default function OverviewTab({ setActiveTab }) {
  const [hoveredWeek, setHoveredWeek] = useState(null);

  // SVG dimensions for weekly posting graph
  const svgWidth = 800;
  const svgHeight = 220;
  const padding = { top: 20, right: 30, bottom: 40, left: 60 };

  const maxPostings = Math.max(...weeklyPostingTimeline.map(d => d.postings));
  const points = weeklyPostingTimeline.map((d, i) => {
    const x = padding.left + (i / (weeklyPostingTimeline.length - 1)) * (svgWidth - padding.left - padding.right);
    const y = svgHeight - padding.bottom - (d.postings / maxPostings) * (svgHeight - padding.top - padding.bottom);
    return { ...d, x, y };
  });

  const pathD = points.reduce((acc, curr, idx) => {
    return idx === 0 ? `M ${curr.x} ${curr.y}` : `${acc} L ${curr.x} ${curr.y}`;
  }, '');

  const areaD = `${pathD} L ${points[points.length - 1].x} ${svgHeight - padding.bottom} L ${points[0].x} ${svgHeight - padding.bottom} Z`;

  return (
    <div className="space-y-6">
      
      {/* Editorial Header Banner */}
      <div className="rounded-2xl border border-stone-200/90 bg-white p-6 shadow-2xs dark:border-stone-800 dark:bg-stone-900">
        <div className="flex flex-col lg:flex-row lg:items-center lg:justify-between gap-4">
          <div>
            <div className="flex items-center gap-2 text-xs font-semibold uppercase tracking-wider text-stone-600 dark:text-stone-300">
              <span>Executive Briefing</span>
              <span>&bull;</span>
              <span>Phase 1 &amp; Phase 2 Completed</span>
            </div>
            <h1 className="mt-1 text-2xl font-bold tracking-tight text-stone-900 dark:text-stone-100 sm:text-3xl">
              Job Market Intelligence Report
            </h1>
            <p className="mt-2 text-sm text-stone-600 dark:text-stone-400 max-w-3xl leading-relaxed">
              Comprehensive exploratory data analysis and feature engineering performed on 
              <strong className="font-semibold text-stone-900 dark:text-stone-200"> 123,849 LinkedIn job listings</strong>. 
              Examining macroeconomic hiring trajectories, compensation distributions, and organizational workforce requirements.
            </p>
          </div>

          <div className="flex flex-wrap items-center gap-2 pt-2 lg:pt-0">
            <button
              onClick={() => setActiveTab('salary')}
              className="inline-flex items-center gap-1.5 rounded-lg bg-stone-900 px-3.5 py-2 text-xs font-medium text-white shadow-sm hover:bg-stone-800 transition-colors dark:bg-stone-100 dark:text-stone-900 dark:hover:bg-stone-200"
            >
              <span>Explore Salary Data</span>
              <ArrowUpRight className="h-3.5 w-3.5" />
            </button>
            <button
              onClick={() => setActiveTab('explorer')}
              className="inline-flex items-center gap-1.5 rounded-lg border border-stone-200 bg-white px-3.5 py-2 text-xs font-medium text-stone-700 hover:bg-stone-50 transition-colors dark:border-stone-800 dark:bg-stone-900 dark:text-stone-300 dark:hover:bg-stone-800"
            >
              <span>Browse Job Postings</span>
              <ChevronRight className="h-3.5 w-3.5 text-stone-400" />
            </button>
          </div>
        </div>
      </div>

      {/* KPI Cards Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        
        {/* KPI 1: Total Postings */}
        <div className="rounded-xl border border-stone-200 bg-white p-5 shadow-2xs dark:border-stone-800 dark:bg-stone-900">
          <div className="flex items-center justify-between text-stone-500 dark:text-stone-400">
            <span className="text-xs font-medium uppercase tracking-wider">Total Postings</span>
            <div className="rounded-lg bg-stone-100 p-2 text-stone-700 dark:bg-stone-800 dark:text-stone-300">
              <Briefcase className="h-4 w-4" />
            </div>
          </div>
          <div className="mt-3 flex items-baseline gap-2">
            <span className="font-mono text-3xl font-bold tracking-tight text-stone-900 dark:text-stone-100">
              123,849
            </span>
          </div>
          <p className="mt-2 text-xs text-stone-500 dark:text-stone-400 flex items-center gap-1">
            <span className="inline-block h-1.5 w-1.5 rounded-full bg-emerald-500"></span>
            100% deduplicated by unique job_id
          </p>
        </div>

        {/* KPI 2: Active Companies */}
        <div className="rounded-xl border border-stone-200 bg-white p-5 shadow-2xs dark:border-stone-800 dark:bg-stone-900">
          <div className="flex items-center justify-between text-stone-500 dark:text-stone-400">
            <span className="text-xs font-medium uppercase tracking-wider">Unique Employers</span>
            <div className="rounded-lg bg-stone-100 p-2 text-stone-700 dark:bg-stone-800 dark:text-stone-300">
              <Building className="h-4 w-4" />
            </div>
          </div>
          <div className="mt-3 flex items-baseline gap-2">
            <span className="font-mono text-3xl font-bold tracking-tight text-stone-900 dark:text-stone-100">
              24,428
            </span>
          </div>
          <p className="mt-2 text-xs text-stone-500 dark:text-stone-400">
            Across 8,526 distinct geographic locations
          </p>
        </div>

        {/* KPI 3: Median Annual Salary */}
        <div className="rounded-xl border border-stone-200 bg-white p-5 shadow-2xs dark:border-stone-800 dark:bg-stone-900">
          <div className="flex items-center justify-between text-stone-500 dark:text-stone-400">
            <span className="text-xs font-medium uppercase tracking-wider">Median Salary</span>
            <div className="rounded-lg bg-stone-100 p-2 text-stone-700 dark:bg-stone-800 dark:text-stone-300">
              <DollarSign className="h-4 w-4" />
            </div>
          </div>
          <div className="mt-3 flex items-baseline gap-2">
            <span className="font-mono text-3xl font-bold tracking-tight text-stone-900 dark:text-stone-100">
              $81,500
            </span>
            <span className="text-xs text-stone-500">/ yr</span>
          </div>
          <p className="mt-2 text-xs text-stone-500 dark:text-stone-400">
            IQR: $52,000 (25th) – $125,000 (75th)
          </p>
        </div>

        {/* KPI 4: Remote Work Share */}
        <div className="rounded-xl border border-stone-200 bg-white p-5 shadow-2xs dark:border-stone-800 dark:bg-stone-900">
          <div className="flex items-center justify-between text-stone-500 dark:text-stone-400">
            <span className="text-xs font-medium uppercase tracking-wider">Remote Positions</span>
            <div className="rounded-lg bg-stone-100 p-2 text-stone-700 dark:bg-stone-800 dark:text-stone-300">
              <Globe className="h-4 w-4" />
            </div>
          </div>
          <div className="mt-3 flex items-baseline gap-2">
            <span className="font-mono text-3xl font-bold tracking-tight text-stone-900 dark:text-stone-100">
              15,246
            </span>
            <span className="text-xs font-semibold text-emerald-600 dark:text-emerald-400">
              12.3%
            </span>
          </div>
          <p className="mt-2 text-xs text-stone-500 dark:text-stone-400">
            108.6k On-site / Unspecified listings
          </p>
        </div>

      </div>

      {/* Main Section: 20-Week Timeline */}
      <div className="rounded-2xl border border-stone-200 bg-white p-6 shadow-2xs dark:border-stone-800 dark:bg-stone-900">
        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between pb-4 border-b border-stone-100 dark:border-stone-800 gap-2">
          <div>
            <div className="flex items-center gap-2">
              <h2 className="text-base font-semibold text-stone-900 dark:text-stone-100">
                Weekly Job Posting Trends
              </h2>
              <span className="rounded bg-stone-100 px-2 py-0.5 font-mono text-[11px] text-stone-600 dark:bg-stone-800 dark:text-stone-300">
                20 Weekly Observations
              </span>
            </div>
            <p className="text-xs text-stone-500 dark:text-stone-400 mt-0.5">
              Time-series resampled from Dec 05, 2023 to Apr 20, 2024 (UTC)
            </p>
          </div>

          <div className="flex items-center gap-4 text-xs">
            <div className="flex items-center gap-1.5 text-stone-500">
              <div className="h-2 w-2 rounded-full bg-indigo-600"></div>
              <span>Postings Volume</span>
            </div>
            <span className="font-mono text-stone-700 dark:text-stone-300 text-xs">
              Peak: 84.9k (Week 20)
            </span>
          </div>
        </div>

        {/* SVG Interactive Line Chart */}
        <div className="relative mt-6 w-full overflow-x-auto">
          <svg 
            viewBox={`0 0 ${svgWidth} ${svgHeight}`} 
            className="w-full h-auto min-w-[600px] select-none"
          >
            <defs>
              <linearGradient id="postingGradient" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0%" stopColor="#4f46e5" stopOpacity="0.22" />
                <stop offset="100%" stopColor="#4f46e5" stopOpacity="0.0" />
              </linearGradient>
            </defs>

            {/* Horizontal Grid lines */}
            {[0, 0.25, 0.5, 0.75, 1].map((ratio) => {
              const y = svgHeight - padding.bottom - ratio * (svgHeight - padding.top - padding.bottom);
              const val = Math.round(ratio * maxPostings);
              return (
                <g key={ratio}>
                  <line 
                    x1={padding.left} 
                    y1={y} 
                    x2={svgWidth - padding.right} 
                    y2={y} 
                    stroke="currentColor" 
                    className="text-stone-100 dark:text-stone-800" 
                    strokeDasharray="4 4"
                  />
                  <text 
                    x={padding.left - 10} 
                    y={y + 4} 
                    textAnchor="end" 
                    className="text-[10px] fill-stone-400 font-mono"
                  >
                    {val >= 1000 ? `${(val / 1000).toFixed(0)}k` : val}
                  </text>
                </g>
              );
            })}

            {/* Area fill */}
            <path d={areaD} fill="url(#postingGradient)" />

            {/* Line path */}
            <path 
              d={pathD} 
              fill="none" 
              stroke="#4f46e5" 
              strokeWidth="2.5" 
              strokeLinecap="round" 
              strokeLinejoin="round" 
            />

            {/* Data points */}
            {points.map((pt, idx) => {
              const isHovered = hoveredWeek === idx;
              return (
                <g 
                  key={idx}
                  onMouseEnter={() => setHoveredWeek(idx)}
                  onMouseLeave={() => setHoveredWeek(null)}
                  className="cursor-pointer"
                >
                  <circle 
                    cx={pt.x} 
                    cy={pt.y} 
                    r={isHovered ? 6 : (idx === points.length - 1 ? 5 : 3.5)} 
                    className={`transition-all ${
                      isHovered 
                        ? 'fill-white stroke-indigo-600 stroke-3' 
                        : 'fill-indigo-600 stroke-white dark:stroke-stone-900 stroke-1.5'
                    }`}
                  />
                  {/* X Axis Labels for key points */}
                  {(idx % 4 === 0 || idx === points.length - 1) && (
                    <text 
                      x={pt.x} 
                      y={svgHeight - 12} 
                      textAnchor="middle" 
                      className="text-[10px] fill-stone-400 font-mono"
                    >
                      {pt.week.split(' ')[0]}
                    </text>
                  )}
                </g>
              );
            })}
          </svg>

          {/* Hover Tooltip display */}
          {hoveredWeek !== null && (
            <div className="mt-2 flex items-center justify-center gap-3 rounded-lg border border-stone-200 bg-stone-50 py-1.5 px-3 text-xs text-stone-700 dark:border-stone-800 dark:bg-stone-800/80 dark:text-stone-300">
              <Calendar className="h-3.5 w-3.5 text-indigo-500" />
              <span className="font-medium">{points[hoveredWeek].week}</span>
              <span className="font-mono font-bold text-stone-900 dark:text-stone-100">
                {points[hoveredWeek].postings.toLocaleString()} postings
              </span>
            </div>
          )}
        </div>

        {/* Temporal Observation Takeaways */}
        <div className="mt-6 grid grid-cols-1 md:grid-cols-3 gap-4 pt-4 border-t border-stone-100 dark:border-stone-800 text-xs">
          <div className="rounded-lg bg-stone-50/70 p-3 dark:bg-stone-800/40">
            <span className="font-semibold text-stone-800 dark:text-stone-200 block mb-1">
              Q1 Initial Ramp (Dec - Feb)
            </span>
            <p className="text-stone-500 dark:text-stone-400 text-[11px] leading-relaxed">
              Baseline sampling collected 19 postings over 12 weeks, capturing initial LinkedIn index crawling.
            </p>
          </div>
          <div className="rounded-lg bg-stone-50/70 p-3 dark:bg-stone-800/40">
            <span className="font-semibold text-stone-800 dark:text-stone-200 block mb-1">
              March Surge (1.8K Postings)
            </span>
            <p className="text-stone-500 dark:text-stone-400 text-[11px] leading-relaxed">
              Postings accelerated to 1,815 listings as automated pipeline ingestion scaled up across North American metros.
            </p>
          </div>
          <div className="rounded-lg bg-stone-50/70 p-3 dark:bg-stone-800/40">
            <span className="font-semibold text-stone-800 dark:text-stone-200 block mb-1">
              April Ingestion (122.0K Postings)
            </span>
            <p className="text-stone-500 dark:text-stone-400 text-[11px] leading-relaxed">
              Mass bulk crawl completed in mid-April 2024, providing a dense cross-sectional census of live hiring demand.
            </p>
          </div>
        </div>
      </div>

      {/* Two Column Breakdown: Employment Types & Experience Levels */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        
        {/* Employment Types Card */}
        <div className="rounded-2xl border border-stone-200 bg-white p-6 shadow-2xs dark:border-stone-800 dark:bg-stone-900">
          <div className="flex items-center justify-between pb-4 border-b border-stone-100 dark:border-stone-800">
            <div>
              <h2 className="text-base font-semibold text-stone-900 dark:text-stone-100">
                Employment Types Breakdown
              </h2>
              <p className="text-xs text-stone-500 dark:text-stone-400">
                Classified by <code className="font-mono text-[11px]">formatted_work_type</code>
              </p>
            </div>
            <span className="text-xs font-mono font-medium text-stone-600 dark:text-stone-300">
              123,849 Total
            </span>
          </div>

          <div className="mt-5 space-y-3.5">
            {employmentTypes.map((item) => (
              <div key={item.type} className="group">
                <div className="flex items-center justify-between text-xs mb-1">
                  <span className="font-medium text-stone-700 dark:text-stone-300">
                    {item.type}
                  </span>
                  <div className="flex items-center gap-2">
                    <span className="font-mono text-stone-500 dark:text-stone-400">
                      {item.count.toLocaleString()}
                    </span>
                    <span className="font-mono font-semibold text-stone-900 dark:text-stone-100 w-12 text-right">
                      {item.percentage}%
                    </span>
                  </div>
                </div>
                {/* Clean Bar */}
                <div className="h-2 w-full rounded-full bg-stone-100 dark:bg-stone-800 overflow-hidden">
                  <div 
                    className="h-full rounded-full transition-all duration-500" 
                    style={{ 
                      width: `${item.percentage}%`,
                      backgroundColor: item.color 
                    }}
                  />
                </div>
              </div>
            ))}
          </div>

          <div className="mt-6 rounded-lg bg-stone-50 p-3 text-xs text-stone-600 dark:bg-stone-800/40 dark:text-stone-400">
            <span className="font-semibold text-stone-800 dark:text-stone-200">Key Finding: </span>
            Full-time employment accounts for <strong className="text-stone-900 dark:text-stone-100">79.79%</strong> of all opportunities, followed by Contract (9.78%) and Part-time (7.83%).
          </div>
        </div>

        {/* Experience Level Hierarchy Card */}
        <div className="rounded-2xl border border-stone-200 bg-white p-6 shadow-2xs dark:border-stone-800 dark:bg-stone-900">
          <div className="flex items-center justify-between pb-4 border-b border-stone-100 dark:border-stone-800">
            <div>
              <h2 className="text-base font-semibold text-stone-900 dark:text-stone-100">
                Experience Level Distribution
              </h2>
              <p className="text-xs text-stone-500 dark:text-stone-400">
                Classified by <code className="font-mono text-[11px]">formatted_experience_level</code>
              </p>
            </div>
            <span className="text-xs font-mono font-medium text-stone-600 dark:text-stone-300">
              7 Tiers
            </span>
          </div>

          <div className="mt-5 space-y-3.5">
            {experienceLevels.map((item) => (
              <div key={item.level} className="group">
                <div className="flex items-center justify-between text-xs mb-1">
                  <span className="font-medium text-stone-700 dark:text-stone-300">
                    {item.level}
                  </span>
                  <div className="flex items-center gap-2">
                    <span className="font-mono text-stone-500 dark:text-stone-400">
                      {item.count.toLocaleString()}
                    </span>
                    <span className="font-mono font-semibold text-stone-900 dark:text-stone-100 w-12 text-right">
                      {item.percentage}%
                    </span>
                  </div>
                </div>
                {/* Clean Bar */}
                <div className="h-2 w-full rounded-full bg-stone-100 dark:bg-stone-800 overflow-hidden">
                  <div 
                    className="h-full rounded-full transition-all duration-500" 
                    style={{ 
                      width: `${item.percentage}%`,
                      backgroundColor: item.color 
                    }}
                  />
                </div>
              </div>
            ))}
          </div>

          <div className="mt-6 rounded-lg bg-stone-50 p-3 text-xs text-stone-600 dark:bg-stone-800/40 dark:text-stone-400">
            <span className="font-semibold text-stone-800 dark:text-stone-200">Key Finding: </span>
            <strong className="text-stone-900 dark:text-stone-100">Mid-Senior level (33.5%)</strong> and <strong className="text-stone-900 dark:text-stone-100">Entry level (29.6%)</strong> form the backbone of market demand.
          </div>
        </div>

      </div>

    </div>
  );
}
