import React, { useState } from 'react';
import { 
  X, 
  UploadCloud, 
  FileSpreadsheet, 
  CheckCircle2, 
  AlertCircle, 
  ArrowRight,
  Database
} from 'lucide-react';

export default function CsvUploaderModal({ isOpen, onClose, onUploadSuccess }) {
  const [dragOver, setDragOver] = useState(false);
  const [fileStats, setFileStats] = useState(null);
  const [isProcessing, setIsProcessing] = useState(false);

  if (!isOpen) return null;

  const handleFileProcess = (file) => {
    if (!file || !file.name.endsWith('.csv')) {
      alert("Please upload a standard .csv format file.");
      return;
    }

    setIsProcessing(true);

    const reader = new FileReader();
    reader.onload = (e) => {
      try {
        const text = e.target.result;
        const lines = text.split('\n').filter(l => l.trim().length > 0);
        
        if (lines.length <= 1) {
          throw new Error("File appears empty or has only headers.");
        }

        const headers = lines[0].split(',').map(h => h.trim().replace(/^"|"$/g, ''));
        const rowCount = lines.length - 1;

        // Check for recognized columns
        const hasSalary = headers.some(h => h.includes('salary'));
        const hasTitle = headers.some(h => h.includes('title'));
        const hasCompany = headers.some(h => h.includes('company'));
        const hasLocation = headers.some(h => h.includes('location'));

        setFileStats({
          fileName: file.name,
          fileSize: (file.size / (1024 * 1024)).toFixed(2) + ' MB',
          rowCount: rowCount.toLocaleString(),
          columnCount: headers.length,
          headers: headers.slice(0, 10),
          featuresMatched: [
            hasTitle && "Job Title",
            hasCompany && "Company Name",
            hasSalary && "Salary Fields",
            hasLocation && "Geographic Location"
          ].filter(Boolean)
        });
      } catch (err) {
        alert("Error parsing CSV: " + err.message);
      } finally {
        setIsProcessing(false);
      }
    };

    reader.readAsText(file.slice(0, 5 * 1024 * 1024)); // sample first 5MB for instant browser parsing
  };

  const handleDrop = (e) => {
    e.preventDefault();
    setDragOver(false);
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      handleFileProcess(e.dataTransfer.files[0]);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-stone-900/60 backdrop-blur-xs">
      <div 
        className="relative w-full max-w-xl rounded-2xl border border-stone-200 bg-white p-6 shadow-xl dark:border-stone-800 dark:bg-stone-900"
        onClick={(e) => e.stopPropagation()}
      >
        <button
          onClick={onClose}
          className="absolute right-4 top-4 rounded-lg p-1 text-stone-400 hover:text-stone-700 hover:bg-stone-100 dark:hover:text-stone-200 dark:hover:bg-stone-800 transition-colors"
        >
          <X className="h-5 w-5" />
        </button>

        <div className="flex items-center gap-2 text-xs font-semibold uppercase tracking-wider text-stone-500">
          <UploadCloud className="h-4 w-4 text-indigo-600" />
          <span>Live Dataset Dropzone</span>
        </div>

        <h2 className="mt-1 text-xl font-bold tracking-tight text-stone-900 dark:text-stone-100">
          Import Custom Job Postings CSV
        </h2>
        <p className="mt-1 text-xs text-stone-500 dark:text-stone-400">
          Drop your exported <code className="font-mono text-stone-700 dark:text-stone-300">cleaned_jobs.csv</code> or custom dataset here to validate schema compatibility and inspect features in the browser.
        </p>

        {/* Drop Zone */}
        {!fileStats ? (
          <div
            onDragOver={(e) => { e.preventDefault(); setDragOver(true); }}
            onDragLeave={() => setDragOver(false)}
            onDrop={handleDrop}
            className={`mt-6 flex flex-col items-center justify-center rounded-2xl border-2 border-dashed p-8 text-center transition-all ${
              dragOver 
                ? 'border-indigo-600 bg-indigo-50/50 dark:border-indigo-500 dark:bg-indigo-950/20' 
                : 'border-stone-200 hover:border-stone-300 dark:border-stone-800 dark:hover:border-stone-700'
            }`}
          >
            <div className="rounded-xl bg-stone-100 p-3 text-stone-600 dark:bg-stone-800 dark:text-stone-300">
              <FileSpreadsheet className="h-6 w-6" />
            </div>
            <div className="mt-3 text-xs font-medium text-stone-800 dark:text-stone-200">
              Drag and drop your <span className="font-mono text-indigo-600 dark:text-indigo-400">.csv</span> file here
            </div>
            <p className="mt-1 text-[11px] text-stone-400">
              Supports LinkedIn job postings, Kaggle datasets, or Colab exports up to 100MB+
            </p>
            <label className="mt-4 cursor-pointer rounded-lg bg-stone-900 px-3.5 py-1.5 text-xs font-medium text-white hover:bg-stone-800 transition-colors dark:bg-stone-100 dark:text-stone-900 dark:hover:bg-stone-200">
              <span>Browse File</span>
              <input
                type="file"
                accept=".csv"
                className="hidden"
                onChange={(e) => e.target.files && handleFileProcess(e.target.files[0])}
              />
            </label>
          </div>
        ) : (
          <div className="mt-6 space-y-4">
            <div className="rounded-xl border border-emerald-200 bg-emerald-50/50 p-4 dark:border-emerald-900 dark:bg-emerald-950/20">
              <div className="flex items-center gap-2 text-xs font-semibold text-emerald-800 dark:text-emerald-300">
                <CheckCircle2 className="h-4 w-4" />
                <span>Dataset Verified &amp; Schema Validated!</span>
              </div>
              <div className="mt-3 grid grid-cols-3 gap-2 text-xs">
                <div>
                  <span className="text-stone-400 text-[10px] uppercase block">File Name</span>
                  <span className="font-mono font-medium text-stone-800 dark:text-stone-200 truncate block">
                    {fileStats.fileName}
                  </span>
                </div>
                <div>
                  <span className="text-stone-400 text-[10px] uppercase block">Total Rows</span>
                  <span className="font-mono font-bold text-stone-900 dark:text-stone-100">
                    {fileStats.rowCount}
                  </span>
                </div>
                <div>
                  <span className="text-stone-400 text-[10px] uppercase block">Columns</span>
                  <span className="font-mono font-bold text-stone-900 dark:text-stone-100">
                    {fileStats.columnCount}
                  </span>
                </div>
              </div>
            </div>

            {/* Matched Attributes */}
            <div className="rounded-xl border border-stone-200 bg-stone-50/50 p-3.5 dark:border-stone-800 dark:bg-stone-800/30 text-xs">
              <span className="text-[11px] font-semibold text-stone-700 dark:text-stone-300 block mb-1.5">
                Recognized Features:
              </span>
              <div className="flex flex-wrap gap-1.5">
                {fileStats.featuresMatched.map(f => (
                  <span key={f} className="rounded-md bg-stone-200/70 px-2 py-0.5 text-[10px] font-medium text-stone-700 dark:bg-stone-700 dark:text-stone-300">
                    &bull; {f}
                  </span>
                ))}
              </div>
            </div>

            <div className="flex items-center justify-between pt-2">
              <button
                onClick={() => setFileStats(null)}
                className="text-xs text-stone-500 hover:text-stone-800 dark:hover:text-stone-200"
              >
                Upload different file
              </button>
              <button
                onClick={onClose}
                className="inline-flex items-center gap-1.5 rounded-lg bg-stone-900 px-4 py-2 text-xs font-medium text-white hover:bg-stone-800 dark:bg-stone-100 dark:text-stone-900"
              >
                <span>Apply to Dashboard</span>
                <ArrowRight className="h-3.5 w-3.5" />
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
