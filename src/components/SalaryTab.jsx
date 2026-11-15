import React, { useState } from 'react';
import { 
  overviewStats, 
  salaryDistributionBins, 
  correlationMatrix 
} from '../data/jobInsightData';
import { 
  DollarSign, 
  TrendingUp, 
  Scale, 
  PieChart, 
  AlertCircle, 
  Info,
  Layers,
  ArrowRight
} from 'lucide-react';

export default function SalaryTab() {
  const [selectedCell, setSelectedCell] = useState(null);

  const { salaryMetrics } = overviewStats;

  // SVG dimensions for Salary Distribution curve
  const svgWidth = 760;
  const svgHeight = 220;
  const padding = { top: 20, right: 30, bottom: 40, left: 50 };

  const maxBinCount = Math.max(...salaryDistributionBins.map(b => b.count));
  const binWidth = (svgWidth - padding.left - padding.right) / salaryDistributionBins.length;

  return (
    <div className="space-y-6">
      
      {/* Title & Context */}
      <div className="rounded-2xl border border-stone-200 bg-white p-6 shadow-2xs dark:border-stone-800 dark:bg-stone-900">
        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
          <div>
            <div className="flex items-center gap-2 text-xs font-semibold uppercase tracking-wider text-stone-600 dark:text-stone-300">
              <DollarSign className="h-3.5 w-3.5 text-emerald-600" />
              <span>Compensation Analytics</span>
            </div>
            <h1 className="mt-1 text-2xl font-bold tracking-tight text-stone-900 dark:text-stone-100 sm:text-3xl">
              Normalized Annual Salary Intelligence
            </h1>
            <p className="mt-1 text-sm text-stone-600 dark:text-stone-400 max-w-2xl">
              Analyzed from 36,073 salary-disclosing job records. Hourly rates have been harmonized to 
              2,080 annual work hours to allow direct macroeconomic comparison.
            </p>
          </div>

          <div className="flex items-center gap-2">
            <span className="rounded-lg bg-emerald-50 px-3 py-1.5 text-xs font-medium text-emerald-800 dark:bg-emerald-950/60 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-800">
              Disclosed in 29.1% of Postings
            </span>
          </div>
        </div>
      </div>

      {/* 4 Quartile / Metric Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        
        {/* Q1: 25th Percentile */}
        <div className="rounded-xl border border-stone-200 bg-white p-5 shadow-2xs dark:border-stone-800 dark:bg-stone-900">
          <span className="text-xs font-medium uppercase tracking-wider text-stone-500 dark:text-stone-400">
            25th Percentile (Q1)
          </span>
          <div className="mt-2 font-mono text-2xl font-bold text-stone-900 dark:text-stone-100">
            ${salaryMetrics.q1.toLocaleString()}
          </div>
          <p className="mt-1 text-xs text-stone-500 dark:text-stone-400">
            Lower quartile threshold for baseline entry roles
          </p>
        </div>

        {/* Median Salary */}
        <div className="rounded-xl border border-emerald-300/80 bg-emerald-50/30 p-5 shadow-2xs dark:border-emerald-900/60 dark:bg-emerald-950/20">
          <div className="flex items-center justify-between">
            <span className="text-xs font-medium uppercase tracking-wider text-emerald-800 dark:text-emerald-300">
              Median Salary (50th)
            </span>
            <span className="rounded bg-emerald-600 px-1.5 py-0.5 text-[10px] font-semibold text-white">
              Benchmark
            </span>
          </div>
          <div className="mt-2 font-mono text-3xl font-bold text-emerald-950 dark:text-emerald-200">
            ${salaryMetrics.median.toLocaleString()}
          </div>
          <p className="mt-1 text-xs text-emerald-800/80 dark:text-emerald-300/80">
            True central compensation across all job sectors
          </p>
        </div>

        {/* Q3: 75th Percentile */}
        <div className="rounded-xl border border-stone-200 bg-white p-5 shadow-2xs dark:border-stone-800 dark:bg-stone-900">
          <span className="text-xs font-medium uppercase tracking-wider text-stone-500 dark:text-stone-400">
            75th Percentile (Q3)
          </span>
          <div className="mt-2 font-mono text-2xl font-bold text-stone-900 dark:text-stone-100">
            ${salaryMetrics.q3.toLocaleString()}
          </div>
          <p className="mt-1 text-xs text-stone-500 dark:text-stone-400">
            Upper quartile for senior, specialized, and engineering roles
          </p>
        </div>

        {/* 99th Percentile Cutoff */}
        <div className="rounded-xl border border-stone-200 bg-white p-5 shadow-2xs dark:border-stone-800 dark:bg-stone-900">
          <span className="text-xs font-medium uppercase tracking-wider text-stone-500 dark:text-stone-400">
            99% Truncation Cap
          </span>
          <div className="mt-2 font-mono text-2xl font-bold text-stone-900 dark:text-stone-100">
            ${salaryMetrics.p99Cutoff.toLocaleString()}
          </div>
          <p className="mt-1 text-xs text-stone-500 dark:text-stone-400">
            Outlier-clipped envelope for robust modeling
          </p>
        </div>

      </div>

      {/* Salary Distribution Histogram Chart */}
      <div className="rounded-2xl border border-stone-200 bg-white p-6 shadow-2xs dark:border-stone-800 dark:bg-stone-900">
        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between pb-4 border-b border-stone-100 dark:border-stone-800 gap-2">
          <div>
            <h2 className="text-base font-semibold text-stone-900 dark:text-stone-100">
              Distribution of Normalized Annual Salaries
            </h2>
            <p className="text-xs text-stone-500 dark:text-stone-400">
              Binned across 36,073 reported salaries with kernel density profile
            </p>
          </div>
          <div className="flex items-center gap-4 text-xs font-mono text-stone-600 dark:text-stone-400">
            <span className="flex items-center gap-1.5">
              <span className="h-2.5 w-2.5 rounded-sm bg-indigo-600"></span>
              Salary Brackets
            </span>
            <span className="flex items-center gap-1.5">
              <span className="h-0.5 w-4 bg-emerald-500"></span>
              Median ($81.5k)
            </span>
          </div>
        </div>

        {/* SVG Histogram */}
        <div className="relative mt-6 w-full overflow-x-auto">
          <svg 
            viewBox={`0 0 ${svgWidth} ${svgHeight}`} 
            className="w-full h-auto min-w-[650px] select-none"
          >
            {/* Grid lines */}
            {[0, 0.25, 0.5, 0.75, 1].map((ratio) => {
              const y = svgHeight - padding.bottom - ratio * (svgHeight - padding.top - padding.bottom);
              const val = Math.round(ratio * maxBinCount);
              return (
                <g key={ratio}>
                  <line 
                    x1={padding.left} 
                    y1={y} 
                    x2={svgWidth - padding.right} 
                    y2={y} 
                    stroke="currentColor" 
                    className="text-stone-100 dark:text-stone-800" 
                    strokeDasharray="3 3"
                  />
                  <text 
                    x={padding.left - 8} 
                    y={y + 4} 
                    textAnchor="end" 
                    className="text-[10px] fill-stone-400 font-mono"
                  >
                    {val >= 1000 ? `${(val/1000).toFixed(1)}k` : val}
                  </text>
                </g>
              );
            })}

            {/* Binned Bars */}
            {salaryDistributionBins.map((bin, i) => {
              const barHeight = (bin.count / maxBinCount) * (svgHeight - padding.top - padding.bottom);
              const x = padding.left + i * binWidth + 4;
              const y = svgHeight - padding.bottom - barHeight;
              const actualWidth = binWidth - 8;

              return (
                <g key={bin.bracket} className="group cursor-pointer">
                  <rect 
                    x={x} 
                    y={y} 
                    width={actualWidth} 
                    height={barHeight} 
                    rx="3"
                    className="fill-indigo-600/85 hover:fill-indigo-700 dark:fill-indigo-500/80 dark:hover:fill-indigo-400 transition-colors"
                  />
                  {/* Count on top of bar */}
                  <text 
                    x={x + actualWidth / 2} 
                    y={y - 6} 
                    textAnchor="middle" 
                    className="text-[9px] font-mono fill-stone-500 dark:fill-stone-400"
                  >
                    {bin.count.toLocaleString()}
                  </text>
                  {/* X Axis Label */}
                  <text 
                    x={x + actualWidth / 2} 
                    y={svgHeight - 16} 
                    textAnchor="middle" 
                    className="text-[10px] fill-stone-500 dark:fill-stone-400 font-mono"
                  >
                    {bin.bracket}
                  </text>
                </g>
              );
            })}

            {/* Median Marker Line ($81.5k falls in the 4th bucket: $70k - $90k) */}
            {(() => {
              const medianX = padding.left + 3.5 * binWidth;
              return (
                <g>
                  <line 
                    x1={medianX} 
                    y1={padding.top} 
                    x2={medianX} 
                    y2={svgHeight - padding.bottom} 
                    stroke="#10b981" 
                    strokeWidth="2" 
                    strokeDasharray="4 2"
                  />
                  <rect 
                    x={medianX - 35} 
                    y={padding.top} 
                    width="70" 
                    height="18" 
                    rx="4" 
                    className="fill-emerald-600"
                  />
                  <text 
                    x={medianX} 
                    y={padding.top + 12} 
                    textAnchor="middle" 
                    className="text-[9px] font-bold fill-white font-mono"
                  >
                    MEDIAN $81.5K
                  </text>
                </g>
              );
            })()}
          </svg>
        </div>

        {/* Insight note */}
        <div className="mt-4 flex items-start gap-2.5 rounded-lg bg-stone-50 p-3.5 text-xs text-stone-600 dark:bg-stone-800/40 dark:text-stone-300">
          <Info className="h-4 w-4 text-stone-500 shrink-0 mt-0.5" />
          <p className="leading-relaxed">
            <strong>Right-skewed Distribution:</strong> The densest concentration occurs between 
            <strong> $50,000 and $90,000</strong> (accounting for 43.3% of all disclosed compensation). 
            Extreme positive outliers up to $535M represent unvalidated scraping anomalies that were filtered in Phase 2 via 99th percentile capping.
          </p>
        </div>
      </div>

      {/* Two-Column Grid: Correlation Heatmap & Pay Period Breakdown */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        
        {/* Correlation Heatmap */}
        <div className="rounded-2xl border border-stone-200 bg-white p-6 shadow-2xs dark:border-stone-800 dark:bg-stone-900">
          <div className="flex items-center justify-between pb-4 border-b border-stone-100 dark:border-stone-800">
            <div>
              <h2 className="text-base font-semibold text-stone-900 dark:text-stone-100">
                Numerical Variable Correlation Matrix
              </h2>
              <p className="text-xs text-stone-500 dark:text-stone-400">
                Pearson correlation coefficients from cleaned dataset
              </p>
            </div>
            <span className="font-mono text-xs text-stone-500">
              5 Variables
            </span>
          </div>

          <div className="mt-6 overflow-x-auto">
            <table className="w-full border-collapse text-xs">
              <thead>
                <tr>
                  <th className="p-2 text-left font-medium text-stone-400 text-[11px]">Feature</th>
                  <th className="p-2 text-center font-medium text-stone-600 dark:text-stone-300">Views</th>
                  <th className="p-2 text-center font-medium text-stone-600 dark:text-stone-300">Applies</th>
                  <th className="p-2 text-center font-medium text-stone-600 dark:text-stone-300">Max Sal</th>
                  <th className="p-2 text-center font-medium text-stone-600 dark:text-stone-300">Min Sal</th>
                  <th className="p-2 text-center font-medium text-stone-600 dark:text-stone-300">Norm Sal</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-stone-100 dark:divide-stone-800">
                {correlationMatrix.map((row) => (
                  <tr key={row.variable}>
                    <td className="p-2.5 font-medium text-stone-800 dark:text-stone-200 whitespace-nowrap">
                      {row.variable}
                    </td>
                    {[row.views, row.applies, row.maxSalary, row.minSalary, row.normalizedSalary].map((val, idx) => {
                      // Heatmap color logic
                      let bgClass = "bg-stone-50 dark:bg-stone-800/40 text-stone-600 dark:text-stone-400";
                      if (val === 1.0) bgClass = "bg-red-500 text-white font-bold";
                      else if (val >= 0.45) bgClass = "bg-red-200 text-red-900 font-semibold dark:bg-red-950 dark:text-red-200";
                      else if (val >= 0.1) bgClass = "bg-blue-100 text-blue-900 font-medium dark:bg-blue-950 dark:text-blue-200";
                      else if (val <= -0.01) bgClass = "bg-indigo-100 text-indigo-900 dark:bg-indigo-950 dark:text-indigo-200";

                      return (
                        <td 
                          key={idx}
                          onMouseEnter={() => setSelectedCell({ var: row.variable, val })}
                          onMouseLeave={() => setSelectedCell(null)}
                          className={`p-2.5 text-center font-mono rounded transition-all cursor-default ${bgClass}`}
                        >
                          {val.toFixed(2)}
                        </td>
                      );
                    })}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          <div className="mt-4 pt-3 border-t border-stone-100 dark:border-stone-800 text-xs text-stone-500">
            <strong>Key Correlation: </strong> 
            Job Views and Applications demonstrate a significant positive correlation of <code className="font-mono text-stone-800 dark:text-stone-200 font-semibold">+0.49</code>. 
            Compensation shows negligible correlation with applicant traffic (-0.01).
          </div>
        </div>

        {/* Pay Period & Compensation Structure */}
        <div className="rounded-2xl border border-stone-200 bg-white p-6 shadow-2xs dark:border-stone-800 dark:bg-stone-900">
          <div className="flex items-center justify-between pb-4 border-b border-stone-100 dark:border-stone-800">
            <div>
              <h2 className="text-base font-semibold text-stone-900 dark:text-stone-100">
                Compensation Frequency Breakdown
              </h2>
              <p className="text-xs text-stone-500 dark:text-stone-400">
                Structure of compensation disclosure models
              </p>
            </div>
            <span className="font-mono text-xs text-stone-500">
              36,073 Disclosed
            </span>
          </div>

          <div className="mt-6 space-y-4">
            
            {/* Yearly */}
            <div className="rounded-xl border border-stone-200 p-4 dark:border-stone-800 bg-stone-50/50 dark:bg-stone-800/30">
              <div className="flex items-center justify-between">
                <span className="font-medium text-xs text-stone-800 dark:text-stone-200">
                  Yearly Salaried (Standard)
                </span>
                <span className="font-mono text-xs font-bold text-stone-900 dark:text-stone-100">
                  ~68.2%
                </span>
              </div>
              <div className="mt-2 h-2 w-full rounded-full bg-stone-200 dark:bg-stone-700 overflow-hidden">
                <div className="h-full rounded-full bg-indigo-600" style={{ width: '68.2%' }}></div>
              </div>
              <p className="mt-2 text-[11px] text-stone-500 dark:text-stone-400">
                Primary pay structure for tech, legal, medical, and corporate managerial roles.
              </p>
            </div>

            {/* Hourly */}
            <div className="rounded-xl border border-stone-200 p-4 dark:border-stone-800 bg-stone-50/50 dark:bg-stone-800/30">
              <div className="flex items-center justify-between">
                <span className="font-medium text-xs text-stone-800 dark:text-stone-200">
                  Hourly Rate (Contract / Healthcare)
                </span>
                <span className="font-mono text-xs font-bold text-stone-900 dark:text-stone-100">
                  ~30.4%
                </span>
              </div>
              <div className="mt-2 h-2 w-full rounded-full bg-stone-200 dark:bg-stone-700 overflow-hidden">
                <div className="h-full rounded-full bg-emerald-600" style={{ width: '30.4%' }}></div>
              </div>
              <p className="mt-2 text-[11px] text-stone-500 dark:text-stone-400">
                Common in healthcare, allied therapy, skilled trades, and IT staff augmentation.
              </p>
            </div>

            {/* Other: Monthly / Weekly / Commission */}
            <div className="rounded-xl border border-stone-200 p-4 dark:border-stone-800 bg-stone-50/50 dark:bg-stone-800/30">
              <div className="flex items-center justify-between">
                <span className="font-medium text-xs text-stone-800 dark:text-stone-200">
                  Monthly / Weekly / Commission
                </span>
                <span className="font-mono text-xs font-bold text-stone-900 dark:text-stone-100">
                  ~1.4%
                </span>
              </div>
              <div className="mt-2 h-2 w-full rounded-full bg-stone-200 dark:bg-stone-700 overflow-hidden">
                <div className="h-full rounded-full bg-amber-600" style={{ width: '1.4%' }}></div>
              </div>
              <p className="mt-2 text-[11px] text-stone-500 dark:text-stone-400">
                Representing seasonal roles, performance commission bases, and international postings.
              </p>
            </div>

          </div>
        </div>

      </div>

    </div>
  );
}
