# JobInsight — AI-Powered Job Market Intelligence Platform

JobInsight is a modern data science web dashboard analyzing **123,849 LinkedIn job postings** across North America. Built with React, Vite, Tailwind CSS, and Lucide icons, it presents macroeconomic hiring trajectories, compensation distributions, spatial employer rankings, and machine learning prototypes.

Derived from the Google Colab Data Preprocessing and Exploratory Data Analysis project ([Colab Notebook](https://colab.research.google.com/drive/12gZ5TJsW5yFXXYcQWN8XYurIssWK6J7y?usp=sharing)).

---

## Key Features

- **Executive Overview**: High-level KPIs (123,849 postings, 24,428 organizations, $81.5K median salary), 20-week temporal hiring volume trajectory, and work-type/experience tier distributions.
- **Compensation & Salary Analytics**: Normalized annual compensation distribution with 25th ($52k), 50th ($81.5k), and 75th ($125k) quartile markers, plus an interactive Pearson correlation matrix.
- **Geography & Top Employers**: Top 15 hiring hubs (New York, Chicago, Houston, Dallas, Atlanta, etc.), top 15 hiring organizations, and remote arrangement breakdown.
- **Job Postings Explorer**: Searchable and filterable data table (by title, company, skills, work type, experience level, remote-only) with pagination and deep inspection modals.
- **AI Predictive Lab (Phase 3 Preview)**:
  - *ML Salary Estimator*: Real-time compensation projection by role category, experience level, location cost index, and work arrangement.
  - *NLP Skill & Requirement Parser*: Extracts in-demand technical competencies, soft skills, and degree requirements from raw job descriptions.
- **Pipeline & Methodology**: Audits all 8 preprocessing steps executed in Python/Pandas with an interactive feature dictionary.
- **Live CSV Dropzone**: Drag and drop any custom `cleaned_jobs.csv` directly in the browser to validate schema and rows.

---

## Tech Stack

- **Frontend**: React 19, Vite 8, Tailwind CSS v4
- **Icons**: Lucide React
- **Typography**: Plus Jakarta Sans, Inter, JetBrains Mono
- **Data Engineering**: Python, Pandas, Seaborn, Matplotlib (Google Colab)

---

## Getting Started

### Prerequisites
- Node.js (v18+)
- npm

### Installation
```bash
# Clone the repository
git clone https://github.com/UtsavChoudhary25/Jobinsight.git
cd Jobinsight

# Install dependencies
npm install

# Start development server
npm run dev
```

### Production Build
```bash
npm run build
npm run preview
```
