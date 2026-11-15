import React from 'react';
import { 
  Sparkles, 
  Sun, 
  Moon, 
  UploadCloud, 
  ExternalLink, 
  Search, 
  Database,
  Layers
} from 'lucide-react';

export default function Header({ 
  darkMode, 
  setDarkMode, 
  onOpenUpload, 
  searchQuery, 
  setSearchQuery,
  activeTab,
  setActiveTab 
}) {
  return (
    <header className="sticky top-0 z-30 border-b border-stone-200 bg-white/80 backdrop-blur-md dark:border-stone-800 dark:bg-stone-900/80">
      <div className="flex h-16 items-center justify-between px-4 sm:px-6 lg:px-8">
        
        {/* Left: Branding & Status */}
        <div className="flex items-center gap-3">
          <div className="flex h-9 w-9 items-center justify-center rounded-lg bg-stone-900 text-stone-100 shadow-sm dark:bg-stone-100 dark:text-stone-900">
            <Layers className="h-5 w-5" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <span className="font-semibold text-stone-900 tracking-tight dark:text-stone-100 text-base">
                JobInsight
              </span>
              <span className="hidden sm:inline-flex items-center rounded-md bg-stone-100 px-2 py-0.5 text-xs font-medium text-stone-600 dark:bg-stone-800 dark:text-stone-300 border border-stone-200 dark:border-stone-700">
                123.8k Postings
              </span>
              <span className="inline-flex items-center rounded-full bg-emerald-50 px-1.5 py-0.5 text-[10px] font-medium text-emerald-700 dark:bg-emerald-950/50 dark:text-emerald-400 border border-emerald-200 dark:border-emerald-800">
                Cleaned &amp; Validated
              </span>
            </div>
            <p className="text-xs text-stone-500 dark:text-stone-400 hidden md:block">
              LinkedIn Market Intelligence &bull; Dec 2023 – Apr 2024
            </p>
          </div>
        </div>

        {/* Center: Quick Search */}
        <div className="relative hidden md:block w-72 lg:w-96">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-4 w-4 text-stone-400" />
          <input
            type="text"
            placeholder="Search roles, companies, or skills..."
            value={searchQuery}
            onChange={(e) => {
              setSearchQuery(e.target.value);
              if (activeTab !== 'explorer' && e.target.value.trim().length > 0) {
                setActiveTab('explorer');
              }
            }}
            className="w-full rounded-lg border border-stone-200 bg-stone-50/70 py-1.5 pl-9 pr-8 text-xs text-stone-800 placeholder-stone-400 transition-colors focus:border-stone-400 focus:bg-white focus:outline-none dark:border-stone-800 dark:bg-stone-950/60 dark:text-stone-200 dark:focus:border-stone-600"
          />
          {searchQuery && (
            <button 
              onClick={() => setSearchQuery('')}
              className="absolute right-2.5 top-1/2 -translate-y-1/2 text-xs text-stone-400 hover:text-stone-600 dark:hover:text-stone-200"
            >
              &times;
            </button>
          )}
        </div>

        {/* Right: Actions & Theme Toggle */}
        <div className="flex items-center gap-2">
          
          {/* Upload Custom CSV button */}
          <button
            onClick={onOpenUpload}
            className="inline-flex items-center gap-1.5 rounded-lg border border-stone-200 bg-white px-3 py-1.5 text-xs font-medium text-stone-700 shadow-2xs hover:bg-stone-50 transition-all dark:border-stone-800 dark:bg-stone-900 dark:text-stone-300 dark:hover:bg-stone-800"
            title="Upload custom dataset CSV"
          >
            <UploadCloud className="h-3.5 w-3.5 text-stone-500" />
            <span className="hidden sm:inline">Upload CSV</span>
          </button>

          {/* Colab Notebook Source Link */}
          <a
            href="https://colab.research.google.com/drive/12gZ5TJsW5yFXXYcQWN8XYurIssWK6J7y?usp=sharing"
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-1.5 rounded-lg border border-stone-200 bg-white px-3 py-1.5 text-xs font-medium text-stone-700 shadow-2xs hover:bg-stone-50 transition-all dark:border-stone-800 dark:bg-stone-900 dark:text-stone-300 dark:hover:bg-stone-800"
            title="Open original Google Colab Notebook"
          >
            <ExternalLink className="h-3.5 w-3.5 text-stone-500" />
            <span className="hidden sm:inline">Google Colab</span>
          </a>

          {/* Dark / Light Mode Toggle */}
          <button
            onClick={() => setDarkMode(!darkMode)}
            className="flex h-8 w-8 items-center justify-center rounded-lg border border-stone-200 text-stone-600 hover:bg-stone-100 transition-colors dark:border-stone-800 dark:text-stone-300 dark:hover:bg-stone-800"
            aria-label="Toggle theme"
          >
            {darkMode ? <Sun className="h-4 w-4 text-amber-400" /> : <Moon className="h-4 w-4 text-stone-600" />}
          </button>

        </div>

      </div>
    </header>
  );
}
