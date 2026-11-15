import React from 'react';
import { 
  LayoutDashboard, 
  DollarSign, 
  MapPin, 
  Briefcase, 
  Sparkles, 
  Database,
  Building2,
  TrendingUp,
  Award
} from 'lucide-react';

export default function Sidebar({ activeTab, setActiveTab }) {
  const navItems = [
    {
      id: 'overview',
      label: 'Executive Overview',
      subtitle: 'Market summary & KPIs',
      icon: LayoutDashboard,
    },
    {
      id: 'salary',
      label: 'Compensation Analytics',
      subtitle: 'Salaries, percentiles & bands',
      icon: DollarSign,
    },
    {
      id: 'geography',
      label: 'Geography & Employers',
      subtitle: 'Top hubs & company ranking',
      icon: MapPin,
    },
    {
      id: 'explorer',
      label: 'Postings Explorer',
      subtitle: 'Search & filter raw listings',
      icon: Briefcase,
    },
    {
      id: 'predictive',
      label: 'AI Predictive Lab',
      subtitle: 'Salary estimator & skill parser',
      icon: Sparkles,
      badge: 'ML Prototype'
    },
    {
      id: 'pipeline',
      label: 'Pipeline & Methodology',
      subtitle: 'Data cleaning & audit stats',
      icon: Database,
    },
  ];

  return (
    <aside className="w-full md:w-64 shrink-0 border-r border-stone-200 bg-stone-50/50 p-4 dark:border-stone-800 dark:bg-stone-900/30">
      <div className="space-y-1">
        <div className="px-3 py-2 text-[11px] font-semibold uppercase tracking-wider text-stone-600 dark:text-stone-300">
          Analytics Views
        </div>

        {navItems.map((item) => {
          const Icon = item.icon;
          const isActive = activeTab === item.id;

          return (
            <button
              key={item.id}
              onClick={() => setActiveTab(item.id)}
              className={`group flex w-full items-start gap-3 rounded-lg px-3 py-2.5 text-left text-xs transition-all ${
                isActive
                  ? 'bg-white text-stone-900 shadow-2xs font-medium dark:bg-stone-800 dark:text-stone-100 border border-stone-200/80 dark:border-stone-700'
                  : 'text-stone-600 hover:bg-stone-100 hover:text-stone-900 dark:text-stone-400 dark:hover:bg-stone-800/60 dark:hover:text-stone-200'
              }`}
            >
              <Icon className={`mt-0.5 h-4 w-4 shrink-0 transition-colors ${
                isActive ? 'text-indigo-600 dark:text-indigo-400' : 'text-stone-400 group-hover:text-stone-600 dark:text-stone-500'
              }`} />
              <div className="flex-1 min-w-0">
                <div className="flex items-center justify-between">
                  <span className="truncate">{item.label}</span>
                  {item.badge && (
                    <span className="rounded-sm bg-indigo-50 px-1 py-0.2 text-[9px] font-medium text-indigo-700 dark:bg-indigo-950/70 dark:text-indigo-300">
                      {item.badge}
                    </span>
                  )}
                </div>
                <div className="truncate text-[11px] text-stone-400 dark:text-stone-500">
                  {item.subtitle}
                </div>
              </div>
            </button>
          );
        })}
      </div>

      {/* Dataset quick callout box */}
      <div className="mt-8 rounded-xl border border-stone-200 bg-white p-3.5 shadow-2xs dark:border-stone-800 dark:bg-stone-900">
        <div className="flex items-center gap-2 text-xs font-semibold text-stone-800 dark:text-stone-200">
          <Award className="h-3.5 w-3.5 text-amber-500" />
          <span>Research Snapshot</span>
        </div>
        <p className="mt-1.5 text-[11px] leading-relaxed text-stone-500 dark:text-stone-400">
          Evaluated from 123,849 job listings across North America. Cleaned, normalized, and timestamp-indexed.
        </p>
        <div className="mt-3 pt-2.5 border-t border-stone-100 dark:border-stone-800 flex items-center justify-between text-[10px] text-stone-400">
          <span>Python 3.10 / Pandas</span>
          <span className="font-mono">100% Unique ID</span>
        </div>
      </div>
    </aside>
  );
}
