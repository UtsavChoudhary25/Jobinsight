import React, { useState, useMemo } from 'react';
import { sampleJobPostings } from '../data/jobInsightData';
import { 
  Search, 
  Filter, 
  MapPin, 
  Building, 
  Briefcase, 
  DollarSign, 
  Globe, 
  ChevronLeft, 
  ChevronRight,
  Eye,
  SlidersHorizontal
} from 'lucide-react';

export default function ExplorerTab({ searchQuery, setSearchQuery, onSelectJob }) {
  const [workTypeFilter, setWorkTypeFilter] = useState('All');
  const [experienceFilter, setExperienceFilter] = useState('All');
  const [remoteOnly, setRemoteOnly] = useState(false);
  const [currentPage, setCurrentPage] = useState(1);
  const pageSize = 8;

  // Filter logic
  const filteredJobs = useMemo(() => {
    return sampleJobPostings.filter((job) => {
      const matchesSearch = 
        !searchQuery ||
        job.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
        job.company.toLowerCase().includes(searchQuery.toLowerCase()) ||
        job.location.toLowerCase().includes(searchQuery.toLowerCase()) ||
        job.skills.some(s => s.toLowerCase().includes(searchQuery.toLowerCase()));

      const matchesWorkType = 
        workTypeFilter === 'All' || job.workType.toLowerCase() === workTypeFilter.toLowerCase();

      const matchesExperience = 
        experienceFilter === 'All' || job.experience.toLowerCase() === experienceFilter.toLowerCase();

      const matchesRemote = !remoteOnly || job.remote === true;

      return matchesSearch && matchesWorkType && matchesExperience && matchesRemote;
    });
  }, [searchQuery, workTypeFilter, experienceFilter, remoteOnly]);

  const totalPages = Math.ceil(filteredJobs.length / pageSize) || 1;
  const paginatedJobs = filteredJobs.slice((currentPage - 1) * pageSize, currentPage * pageSize);

  return (
    <div className="space-y-6">
      
      {/* Title & Filter Bar */}
      <div className="rounded-2xl border border-stone-200 bg-white p-6 shadow-2xs dark:border-stone-800 dark:bg-stone-900">
        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
          <div>
            <div className="flex items-center gap-2 text-xs font-semibold uppercase tracking-wider text-stone-600 dark:text-stone-300">
              <Briefcase className="h-3.5 w-3.5 text-indigo-600" />
              <span>Job Postings Explorer</span>
            </div>
            <h1 className="mt-1 text-2xl font-bold tracking-tight text-stone-900 dark:text-stone-100 sm:text-3xl">
              Inspect Real Cleaned Listings
            </h1>
            <p className="mt-1 text-sm text-stone-600 dark:text-stone-400">
              Filter and explore normalized job listings with full skills breakdown, salary rates, and attributes.
            </p>
          </div>

          <div className="flex items-center gap-2 text-xs font-mono text-stone-500">
            <span>Showing {filteredJobs.length} matching of {sampleJobPostings.length} indexed records</span>
          </div>
        </div>

        {/* Filter Controls Row */}
        <div className="mt-6 flex flex-wrap items-center gap-3 pt-4 border-t border-stone-100 dark:border-stone-800">
          
          {/* Search Box */}
          <div className="relative flex-1 min-w-[200px]">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 h-3.5 w-3.5 text-stone-400" />
            <input
              type="text"
              placeholder="Filter by title, company, or skill..."
              value={searchQuery}
              onChange={(e) => {
                setSearchQuery(e.target.value);
                setCurrentPage(1);
              }}
              className="w-full rounded-lg border border-stone-200 bg-stone-50/70 py-1.5 pl-8 pr-3 text-xs text-stone-800 placeholder-stone-400 focus:border-stone-400 focus:bg-white focus:outline-none dark:border-stone-800 dark:bg-stone-950 dark:text-stone-200"
            />
          </div>

          {/* Work Type Filter */}
          <select
            value={workTypeFilter}
            onChange={(e) => {
              setWorkTypeFilter(e.target.value);
              setCurrentPage(1);
            }}
            className="rounded-lg border border-stone-200 bg-stone-50/70 py-1.5 px-3 text-xs text-stone-700 focus:outline-none dark:border-stone-800 dark:bg-stone-950 dark:text-stone-300"
          >
            <option value="All">All Work Types</option>
            <option value="Full-time">Full-time</option>
            <option value="Part-time">Part-time</option>
            <option value="Contract">Contract</option>
          </select>

          {/* Experience Filter */}
          <select
            value={experienceFilter}
            onChange={(e) => {
              setExperienceFilter(e.target.value);
              setCurrentPage(1);
            }}
            className="rounded-lg border border-stone-200 bg-stone-50/70 py-1.5 px-3 text-xs text-stone-700 focus:outline-none dark:border-stone-800 dark:bg-stone-950 dark:text-stone-300"
          >
            <option value="All">All Experience Levels</option>
            <option value="Entry level">Entry level</option>
            <option value="Associate">Associate</option>
            <option value="Mid-Senior level">Mid-Senior level</option>
            <option value="Director">Director</option>
          </select>

          {/* Remote Toggle */}
          <button
            onClick={() => {
              setRemoteOnly(!remoteOnly);
              setCurrentPage(1);
            }}
            className={`inline-flex items-center gap-1.5 rounded-lg border py-1.5 px-3 text-xs font-medium transition-all ${
              remoteOnly
                ? 'border-indigo-600 bg-indigo-50 text-indigo-700 dark:bg-indigo-950 dark:text-indigo-300 dark:border-indigo-700'
                : 'border-stone-200 bg-stone-50/70 text-stone-600 dark:border-stone-800 dark:bg-stone-950 dark:text-stone-400'
            }`}
          >
            <Globe className="h-3.5 w-3.5" />
            <span>Remote Only</span>
          </button>

          {/* Reset Filters */}
          {(searchQuery || workTypeFilter !== 'All' || experienceFilter !== 'All' || remoteOnly) && (
            <button
              onClick={() => {
                setSearchQuery('');
                setWorkTypeFilter('All');
                setExperienceFilter('All');
                setRemoteOnly(false);
                setCurrentPage(1);
              }}
              className="text-xs text-stone-400 hover:text-stone-700 dark:hover:text-stone-200 transition-colors ml-auto"
            >
              Reset Filters
            </button>
          )}

        </div>
      </div>

      {/* Table Container */}
      <div className="rounded-2xl border border-stone-200 bg-white overflow-hidden shadow-2xs dark:border-stone-800 dark:bg-stone-900">
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs">
            <thead className="border-b border-stone-100 bg-stone-50/70 text-stone-500 dark:border-stone-800 dark:bg-stone-800/40 dark:text-stone-400">
              <tr>
                <th className="py-3 px-4 font-semibold">Role &amp; Company</th>
                <th className="py-3 px-4 font-semibold">Location</th>
                <th className="py-3 px-4 font-semibold">Arrangement</th>
                <th className="py-3 px-4 font-semibold">Experience</th>
                <th className="py-3 px-4 font-semibold">Compensation</th>
                <th className="py-3 px-4 font-semibold">Skills Extracted</th>
                <th className="py-3 px-4 text-right font-semibold">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-stone-100 dark:divide-stone-800">
              {paginatedJobs.length === 0 ? (
                <tr>
                  <td colSpan="7" className="py-12 text-center text-stone-400">
                    No job postings found matching your current filters.
                  </td>
                </tr>
              ) : (
                paginatedJobs.map((job) => (
                  <tr 
                    key={job.id}
                    onClick={() => onSelectJob(job)}
                    className="hover:bg-stone-50/80 dark:hover:bg-stone-800/50 cursor-pointer transition-colors"
                  >
                    {/* Role & Company */}
                    <td className="py-3.5 px-4">
                      <div className="font-semibold text-stone-900 dark:text-stone-100">
                        {job.title}
                      </div>
                      <div className="text-[11px] text-stone-500 flex items-center gap-1 mt-0.5">
                        <Building className="h-3 w-3" />
                        <span>{job.company}</span>
                      </div>
                    </td>

                    {/* Location */}
                    <td className="py-3.5 px-4 text-stone-600 dark:text-stone-300 whitespace-nowrap">
                      <div className="flex items-center gap-1">
                        <MapPin className="h-3 w-3 text-stone-400 shrink-0" />
                        <span>{job.location}</span>
                      </div>
                    </td>

                    {/* Work Type & Remote badge */}
                    <td className="py-3.5 px-4 whitespace-nowrap">
                      <div className="flex items-center gap-1.5">
                        <span className="rounded bg-stone-100 px-2 py-0.5 text-[10px] font-medium text-stone-700 dark:bg-stone-800 dark:text-stone-300">
                          {job.workType}
                        </span>
                        {job.remote && (
                          <span className="rounded bg-indigo-50 px-1.5 py-0.5 text-[10px] font-medium text-indigo-700 dark:bg-indigo-950 dark:text-indigo-300">
                            Remote
                          </span>
                        )}
                      </div>
                    </td>

                    {/* Experience Level */}
                    <td className="py-3.5 px-4 text-stone-600 dark:text-stone-400 whitespace-nowrap">
                      {job.experience}
                    </td>

                    {/* Compensation */}
                    <td className="py-3.5 px-4 whitespace-nowrap">
                      <div className="font-mono font-medium text-stone-900 dark:text-stone-100">
                        {job.salaryDisplay}
                      </div>
                      <div className="text-[10px] text-stone-400">
                        {job.payPeriod}
                      </div>
                    </td>

                    {/* Skills pills */}
                    <td className="py-3.5 px-4">
                      <div className="flex flex-wrap gap-1 max-w-[200px]">
                        {job.skills.slice(0, 2).map((s) => (
                          <span 
                            key={s} 
                            className="rounded-full bg-stone-100 px-2 py-0.2 text-[9px] text-stone-600 dark:bg-stone-800 dark:text-stone-400"
                          >
                            {s}
                          </span>
                        ))}
                        {job.skills.length > 2 && (
                          <span className="text-[9px] text-stone-400 self-center">
                            +{job.skills.length - 2}
                          </span>
                        )}
                      </div>
                    </td>

                    {/* Action */}
                    <td className="py-3.5 px-4 text-right">
                      <button 
                        onClick={(e) => {
                          e.stopPropagation();
                          onSelectJob(job);
                        }}
                        className="rounded-md border border-stone-200 bg-white p-1.5 text-stone-500 hover:text-stone-900 hover:bg-stone-50 dark:border-stone-700 dark:bg-stone-800 dark:text-stone-300 transition-colors"
                        title="View Full Posting Details"
                      >
                        <Eye className="h-3.5 w-3.5" />
                      </button>
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>

        {/* Pagination Footer */}
        <div className="flex items-center justify-between border-t border-stone-100 px-4 py-3 text-xs text-stone-500 dark:border-stone-800">
          <div>
            Page <span className="font-mono font-semibold text-stone-800 dark:text-stone-200">{currentPage}</span> of <span className="font-mono">{totalPages}</span>
          </div>

          <div className="flex items-center gap-1">
            <button
              onClick={() => setCurrentPage(p => Math.max(1, p - 1))}
              disabled={currentPage === 1}
              className="inline-flex items-center gap-1 rounded-md border border-stone-200 px-2.5 py-1 text-xs text-stone-600 hover:bg-stone-50 disabled:opacity-40 disabled:pointer-events-none dark:border-stone-700 dark:text-stone-300"
            >
              <ChevronLeft className="h-3.5 w-3.5" />
              <span>Previous</span>
            </button>
            <button
              onClick={() => setCurrentPage(p => Math.min(totalPages, p + 1))}
              disabled={currentPage === totalPages}
              className="inline-flex items-center gap-1 rounded-md border border-stone-200 px-2.5 py-1 text-xs text-stone-600 hover:bg-stone-50 disabled:opacity-40 disabled:pointer-events-none dark:border-stone-700 dark:text-stone-300"
            >
              <span>Next</span>
              <ChevronRight className="h-3.5 w-3.5" />
            </button>
          </div>
        </div>
      </div>

    </div>
  );
}
