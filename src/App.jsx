import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import OverviewTab from './components/OverviewTab';
import SalaryTab from './components/SalaryTab';
import GeographyTab from './components/GeographyTab';
import ExplorerTab from './components/ExplorerTab';
import PredictiveLabTab from './components/PredictiveLabTab';
import PipelineTab from './components/PipelineTab';
import JobDetailModal from './components/JobDetailModal';
import CsvUploaderModal from './components/CsvUploaderModal';

export default function App() {
  const [darkMode, setDarkMode] = useState(false);
  const [activeTab, setActiveTab] = useState('overview');
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedJob, setSelectedJob] = useState(null);
  const [isUploadOpen, setIsUploadOpen] = useState(false);

  // Sync dark mode with <html> class
  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [darkMode]);

  // Global keyboard shortcuts
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'Escape') {
        setSelectedJob(null);
        setIsUploadOpen(false);
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  return (
    <div className="min-h-screen bg-stone-50 font-sans text-stone-900 transition-colors dark:bg-stone-950 dark:text-stone-100 flex flex-col">
      
      {/* Top Navigation Bar */}
      <Header
        darkMode={darkMode}
        setDarkMode={setDarkMode}
        onOpenUpload={() => setIsUploadOpen(true)}
        searchQuery={searchQuery}
        setSearchQuery={setSearchQuery}
        activeTab={activeTab}
        setActiveTab={setActiveTab}
      />

      {/* Main Content Layout */}
      <div className="flex-1 flex flex-col md:flex-row max-w-[1600px] w-full mx-auto">
        
        {/* Left Sticky Sidebar */}
        <Sidebar 
          activeTab={activeTab} 
          setActiveTab={setActiveTab} 
        />

        {/* Dynamic Analytics View */}
        <main className="flex-1 p-4 sm:p-6 lg:p-8 min-w-0">
          {activeTab === 'overview' && (
            <OverviewTab setActiveTab={setActiveTab} />
          )}

          {activeTab === 'salary' && (
            <SalaryTab />
          )}

          {activeTab === 'geography' && (
            <GeographyTab />
          )}

          {activeTab === 'explorer' && (
            <ExplorerTab 
              searchQuery={searchQuery} 
              setSearchQuery={setSearchQuery}
              onSelectJob={(job) => setSelectedJob(job)}
            />
          )}

          {activeTab === 'predictive' && (
            <PredictiveLabTab />
          )}

          {activeTab === 'pipeline' && (
            <PipelineTab />
          )}

          {/* Footer */}
          <footer className="mt-12 pt-6 border-t border-stone-200 text-xs text-stone-500 dark:border-stone-800 dark:text-stone-400 flex flex-col sm:flex-row items-center justify-between gap-3">
            <div>
              <strong>JobInsight</strong> &bull; LinkedIn Job Market Intelligence Platform
            </div>
            <div className="flex items-center gap-4 text-stone-400">
              <span>Google Colab Integration</span>
              <span>&bull;</span>
              <span>123,849 Observations</span>
              <span>&bull;</span>
              <a 
                href="https://colab.research.google.com/drive/12gZ5TJsW5yFXXYcQWN8XYurIssWK6J7y?usp=sharing"
                target="_blank"
                rel="noreferrer"
                className="underline hover:text-stone-600 dark:hover:text-stone-200"
              >
                Colab Notebook
              </a>
            </div>
          </footer>
        </main>

      </div>

      {/* Modals */}
      <JobDetailModal 
        job={selectedJob} 
        onClose={() => setSelectedJob(null)} 
      />

      <CsvUploaderModal 
        isOpen={isUploadOpen} 
        onClose={() => setIsUploadOpen(false)} 
        onUploadSuccess={() => setIsUploadOpen(false)}
      />

    </div>
  );
}
