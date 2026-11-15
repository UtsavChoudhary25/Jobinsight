import os
import re
import subprocess
import shutil

OUTPUT_HTML = os.path.abspath("docs/JobInsight_Extended_Monograph.html")
OUTPUT_PDF = os.path.abspath("docs/JobInsight_Extended_Monograph.pdf")
ROOT_PDF = os.path.abspath("JobInsight_Technical_Report_30Pages.pdf")
ARTIFACT_PDF = r"C:\Users\choud\.gemini\antigravity\brain\9f07df47-b440-4730-a84f-36f0189f7a4b\JobInsight_Technical_Report_30Pages.pdf"

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(CHROME_PATH):
    CHROME_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

HTML_HEAD = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>JobInsight AI — Comprehensive Technical Monograph</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

    @page {
      size: A4 portrait;
      margin: 22mm 18mm 22mm 18mm;
      @top-right {
        content: "JobInsight AI — Production Technical Monograph";
        font-size: 7.5pt;
        color: #64748b;
        font-family: 'Plus Jakarta Sans', sans-serif;
        text-transform: uppercase;
        letter-spacing: 0.5px;
      }
      @bottom-right {
        content: "Page " counter(page);
        font-size: 8pt;
        color: #64748b;
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-weight: 600;
      }
      @bottom-left {
        content: "https://jobinsight-peach.vercel.app/ | github.com/UtsavChoudhary25/Jobinsight";
        font-size: 7pt;
        color: #94a3b8;
        font-family: 'JetBrains Mono', monospace;
      }
    }

    *, *:before, *:after {
      box-sizing: border-box;
    }

    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      color: #0f172a;
      background-color: #ffffff;
      line-height: 1.68;
      font-size: 9.6pt;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
    }

    /* Force page breaks between major chapters */
    .chapter-break {
      page-break-before: always;
      padding-top: 15px;
    }

    .no-break {
      page-break-inside: avoid;
    }

    /* Cover Page */
    .cover-page {
      height: 100%;
      min-height: 980px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 40px 30px;
      background: linear-gradient(145deg, #090d16 0%, #0f172a 50%, #1e293b 100%);
      color: #ffffff;
      border-radius: 12px;
      border: 1px solid #334155;
      page-break-after: always;
      margin-bottom: 20px;
    }

    .cover-top {
      border-bottom: 1px solid rgba(255, 255, 255, 0.15);
      padding-bottom: 25px;
    }

    .cover-badge {
      display: inline-block;
      font-size: 8.5pt;
      font-weight: 700;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: #38bdf8;
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.35);
      padding: 5px 14px;
      border-radius: 6px;
      margin-bottom: 24px;
    }

    .cover-title {
      font-size: 27pt;
      font-weight: 800;
      line-height: 1.15;
      letter-spacing: -0.8px;
      color: #f8fafc;
      margin: 0 0 14px 0;
    }

    .cover-subtitle {
      font-size: 12.5pt;
      color: #94a3b8;
      font-weight: 400;
      line-height: 1.5;
      margin: 0 0 25px 0;
      max-width: 680px;
    }

    .cover-abstract {
      background: rgba(255, 255, 255, 0.04);
      border-left: 3px solid #38bdf8;
      padding: 18px 20px;
      border-radius: 0 8px 8px 0;
      font-size: 9.5pt;
      color: #cbd5e1;
      line-height: 1.6;
      margin: 25px 0;
    }

    .cover-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
      margin-top: 30px;
    }

    .cover-card {
      background: rgba(15, 23, 42, 0.6);
      border: 1px solid rgba(255, 255, 255, 0.1);
      padding: 14px 16px;
      border-radius: 8px;
    }

    .cover-card-label {
      font-size: 7.5pt;
      color: #94a3b8;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      font-weight: 600;
      margin-bottom: 4px;
    }

    .cover-card-value {
      font-size: 11pt;
      font-weight: 700;
      color: #f8fafc;
    }

    .cover-footer {
      border-top: 1px solid rgba(255, 255, 255, 0.15);
      padding-top: 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 8.5pt;
      color: #94a3b8;
    }

    /* Headings */
    h1 {
      font-size: 17pt;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.4px;
      margin-top: 0;
      margin-bottom: 14px;
      padding-bottom: 8px;
      border-bottom: 2.5px solid #0f172a;
      page-break-after: avoid;
    }

    h2 {
      font-size: 12.5pt;
      font-weight: 700;
      color: #0f172a;
      letter-spacing: -0.2px;
      margin-top: 24px;
      margin-bottom: 10px;
      padding-bottom: 4px;
      border-bottom: 1px solid #cbd5e1;
      page-break-after: avoid;
    }

    h3 {
      font-size: 10.5pt;
      font-weight: 700;
      color: #1e293b;
      margin-top: 18px;
      margin-bottom: 6px;
      page-break-after: avoid;
    }

    p {
      margin: 0 0 10px 0;
      color: #334155;
      text-align: justify;
    }

    strong {
      color: #0f172a;
      font-weight: 600;
    }

    a {
      color: #0284c7;
      text-decoration: none;
    }

    ul, ol {
      margin: 0 0 12px 0;
      padding-left: 22px;
      color: #334155;
    }

    li {
      margin-bottom: 5px;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      margin: 12px 0 16px 0;
      font-size: 8.5pt;
      page-break-inside: avoid;
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      overflow: hidden;
    }

    th, td {
      padding: 7px 10px;
      text-align: left;
      border-bottom: 1px solid #e2e8f0;
      vertical-align: top;
    }

    th {
      background-color: #0f172a;
      color: #f8fafc;
      font-weight: 700;
      text-transform: uppercase;
      font-size: 7.2pt;
      letter-spacing: 0.6px;
    }

    tr:nth-child(even) {
      background-color: #f8fafc;
    }

    .highlight-row {
      background-color: #f0fdf4 !important;
      font-weight: 600;
      border-left: 3px solid #10b981;
    }

    pre {
      background-color: #090d16;
      color: #f1f5f9;
      padding: 12px 14px;
      border-radius: 8px;
      font-family: 'JetBrains Mono', Consolas, monospace;
      font-size: 7.8pt;
      line-height: 1.45;
      overflow-x: auto;
      margin: 10px 0 14px 0;
      border: 1px solid #334155;
      page-break-inside: avoid;
    }

    code {
      font-family: 'JetBrains Mono', Consolas, monospace;
      font-size: 8.2pt;
      background-color: #f1f5f9;
      color: #0369a1;
      padding: 2px 5px;
      border-radius: 4px;
      border: 1px solid #e2e8f0;
    }

    pre code {
      background-color: transparent;
      color: inherit;
      padding: 0;
      border: none;
      font-size: 7.8pt;
    }

    .callout {
      background-color: #f8fafc;
      border-left: 4px solid #0284c7;
      padding: 12px 16px;
      border-radius: 0 8px 8px 0;
      margin: 14px 0 18px 0;
      font-size: 9pt;
      color: #1e293b;
      page-break-inside: avoid;
      border-top: 1px solid #e2e8f0;
      border-right: 1px solid #e2e8f0;
      border-bottom: 1px solid #e2e8f0;
    }

    .callout-success {
      border-left-color: #10b981;
      background-color: #f0fdf4;
      color: #064e3b;
    }

    .callout-title {
      font-weight: 700;
      font-size: 9pt;
      margin-bottom: 3px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    .math-block {
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 10px 16px;
      margin: 12px 0 14px 0;
      text-align: center;
      font-family: 'JetBrains Mono', monospace;
      font-size: 8.8pt;
      color: #0f172a;
      page-break-inside: avoid;
    }

    .diagram-container {
      background: #090d16;
      border: 1px solid #334155;
      border-radius: 10px;
      padding: 16px;
      margin: 16px 0 20px 0;
      page-break-inside: avoid;
    }

    .diagram-title {
      font-size: 8.5pt;
      font-weight: 700;
      color: #38bdf8;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      margin-bottom: 12px;
      text-align: center;
    }

    svg {
      width: 100%;
      height: auto;
      display: block;
    }

    .toc-item {
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      padding: 6px 0;
      border-bottom: 1px dotted #cbd5e1;
      font-size: 9.5pt;
    }
    .toc-title {
      font-weight: 600;
      color: #0f172a;
    }
    .toc-dots {
      flex: 1;
      border-bottom: 1px dotted #94a3b8;
      margin: 0 8px;
    }
    .toc-page {
      font-family: 'JetBrains Mono', monospace;
      font-weight: 600;
      color: #0284c7;
    }
  </style>
</head>
<body>
"""

from chapters_data import COVER_HTML, TOC_HTML
from chapters_part1 import CHAPTER_1_HTML, CHAPTER_2_HTML, CHAPTER_3_HTML, CHAPTER_4_HTML
from chapters_part2 import CHAPTER_5_HTML, CHAPTER_6_HTML, CHAPTER_7_HTML, CHAPTER_8_HTML
from chapters_part3 import CHAPTER_9_HTML, CHAPTER_10_HTML, CHAPTER_11_HTML, CHAPTER_12_HTML, APPENDICES_HTML

ARCH_SVG = """
<div class="diagram-container">
  <div class="diagram-title">System Architecture: Unified Serverless Full-Stack Flow</div>
  <svg viewBox="0 0 880 340" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <linearGradient id="gC" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#0f172a" />
        <stop offset="100%" stop-color="#1e293b" />
      </linearGradient>
      <linearGradient id="gE" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#0369a1" />
        <stop offset="100%" stop-color="#0284c7" />
      </linearGradient>
      <linearGradient id="gF" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#047857" />
        <stop offset="100%" stop-color="#059669" />
      </linearGradient>
      <linearGradient id="gM" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#4f46e5" />
        <stop offset="100%" stop-color="#6366f1" />
      </linearGradient>
      <marker id="arr" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="#64748b" />
      </marker>
    </defs>
    <!-- Col 1 -->
    <rect x="20" y="20" width="180" height="300" rx="10" fill="url(#gC)" stroke="#334155" stroke-width="1.5" />
    <text x="110" y="50" text-anchor="middle" fill="#38bdf8" font-weight="700" font-size="13">1. CLIENT LAYER</text>
    <rect x="35" y="70" width="150" height="42" rx="6" fill="#1e293b" stroke="#475569" />
    <text x="110" y="96" text-anchor="middle" fill="#f8fafc" font-size="11">Vite + React 19 UI</text>
    <rect x="35" y="125" width="150" height="50" rx="6" fill="#1e293b" stroke="#475569" />
    <text x="110" y="147" text-anchor="middle" fill="#f8fafc" font-size="11">Exploratory Dashboard</text>
    <text x="110" y="162" text-anchor="middle" fill="#94a3b8" font-size="9">(123K Postings Analytics)</text>
    <rect x="35" y="188" width="150" height="50" rx="6" fill="#1e293b" stroke="#475569" />
    <text x="110" y="210" text-anchor="middle" fill="#f8fafc" font-size="11">AI Predictive Lab</text>
    <text x="110" y="225" text-anchor="middle" fill="#94a3b8" font-size="9">(Salary Form + NLP Box)</text>
    <rect x="35" y="252" width="150" height="42" rx="6" fill="#0369a1" fill-opacity="0.3" stroke="#0284c7" />
    <text x="110" y="278" text-anchor="middle" fill="#38bdf8" font-size="11">Smart API Client</text>
    <path d="M 200 170 L 235 170" stroke="#64748b" stroke-width="2" marker-end="url(#arr)" />
    <!-- Col 2 -->
    <rect x="240" y="20" width="180" height="300" rx="10" fill="url(#gE)" stroke="#0284c7" stroke-width="1.5" />
    <text x="330" y="50" text-anchor="middle" fill="#ffffff" font-weight="700" font-size="13">2. VERCEL SERVERLESS</text>
    <rect x="255" y="80" width="150" height="65" rx="6" fill="#0f172a" stroke="#0369a1" />
    <text x="330" y="107" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="600">vercel.json Rewrites</text>
    <text x="330" y="125" text-anchor="middle" fill="#94a3b8" font-size="9">/api/* -&gt; api/index.py</text>
    <rect x="255" y="170" width="150" height="75" rx="6" fill="#0f172a" stroke="#0369a1" />
    <text x="330" y="198" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="600">api/index.py</text>
    <text x="330" y="216" text-anchor="middle" fill="#cbd5e1" font-size="9">Vercel Python Function</text>
    <text x="330" y="230" text-anchor="middle" fill="#94a3b8" font-size="9">Zero-CORS Same-Origin</text>
    <path d="M 420 170 L 455 170" stroke="#64748b" stroke-width="2" marker-end="url(#arr)" />
    <!-- Col 3 -->
    <rect x="460" y="20" width="190" height="300" rx="10" fill="url(#gF)" stroke="#059669" stroke-width="1.5" />
    <text x="555" y="50" text-anchor="middle" fill="#ffffff" font-weight="700" font-size="13">3. FASTAPI BACKEND</text>
    <rect x="475" y="75" width="160" height="45" rx="6" fill="#0f172a" stroke="#059669" />
    <text x="555" y="97" text-anchor="middle" fill="#34d399" font-size="11" font-weight="600">FastAPI App (main.py)</text>
    <text x="555" y="111" text-anchor="middle" fill="#94a3b8" font-size="9">Pydantic v2 Validation</text>
    <rect x="475" y="135" width="160" height="65" rx="6" fill="#0f172a" stroke="#059669" />
    <text x="555" y="157" text-anchor="middle" fill="#34d399" font-size="10" font-weight="600">POST /api/predict-salary</text>
    <text x="555" y="173" text-anchor="middle" fill="#cbd5e1" font-size="9">Salary Inference Service</text>
    <text x="555" y="188" text-anchor="middle" fill="#94a3b8" font-size="8">Empirical Confidence Interval</text>
    <rect x="475" y="215" width="160" height="65" rx="6" fill="#0f172a" stroke="#059669" />
    <text x="555" y="237" text-anchor="middle" fill="#34d399" font-size="10" font-weight="600">POST /api/extract-skills</text>
    <text x="555" y="253" text-anchor="middle" fill="#cbd5e1" font-size="9">NLP Token Scanner</text>
    <text x="555" y="268" text-anchor="middle" fill="#94a3b8" font-size="8">Degree &amp; Experience Regex</text>
    <path d="M 650 170 L 685 170" stroke="#64748b" stroke-width="2" marker-end="url(#arr)" />
    <!-- Col 4 -->
    <rect x="690" y="20" width="170" height="300" rx="10" fill="url(#gM)" stroke="#6366f1" stroke-width="1.5" />
    <text x="775" y="50" text-anchor="middle" fill="#ffffff" font-weight="700" font-size="13">4. ML &amp; LEXICON</text>
    <rect x="705" y="75" width="140" height="80" rx="6" fill="#0f172a" stroke="#6366f1" />
    <text x="775" y="98" text-anchor="middle" fill="#a5b4fc" font-size="11" font-weight="700">HistGradientBoosting</text>
    <text x="775" y="115" text-anchor="middle" fill="#34d399" font-size="10">R² = 0.3454 | MAE: $30.4K</text>
    <text x="775" y="131" text-anchor="middle" fill="#cbd5e1" font-size="9">salary_model.joblib</text>
    <text x="775" y="145" text-anchor="middle" fill="#94a3b8" font-size="8">Size: 338 KB (Serverless Opt)</text>
    <rect x="705" y="175" width="140" height="70" rx="6" fill="#0f172a" stroke="#6366f1" />
    <text x="775" y="198" text-anchor="middle" fill="#a5b4fc" font-size="11" font-weight="700">NLP Entity Lexicon</text>
    <text x="775" y="215" text-anchor="middle" fill="#cbd5e1" font-size="9">500+ Curated Entities</text>
    <text x="775" y="230" text-anchor="middle" fill="#94a3b8" font-size="8">8 Distinct Skill Categories</text>
  </svg>
</div>
"""

BENCHMARK_SVG = """
<div class="diagram-container">
  <div class="diagram-title">Hold-Out Test Error (MAE in USD) Across Evaluated Models — Lower is Better</div>
  <svg viewBox="0 0 760 210" xmlns="http://www.w3.org/2000/svg">
    <line x1="160" y1="30" x2="720" y2="30" stroke="#334155" stroke-dasharray="4" />
    <line x1="160" y1="75" x2="720" y2="75" stroke="#334155" stroke-dasharray="4" />
    <line x1="160" y1="120" x2="720" y2="120" stroke="#334155" stroke-dasharray="4" />
    <line x1="160" y1="165" x2="720" y2="165" stroke="#334155" stroke-dasharray="4" />
    <!-- 1 -->
    <text x="150" y="47" text-anchor="end" fill="#38bdf8" font-weight="700" font-size="11">HistGradientBoosting</text>
    <rect x="160" y="32" width="480" height="25" rx="4" fill="#0284c7" />
    <text x="648" y="49" fill="#f8fafc" font-size="10" font-weight="700">$30,482 (R²: 0.3454) ★ Selected</text>
    <!-- 2 -->
    <text x="150" y="92" text-anchor="end" fill="#94a3b8" font-size="11">GradientBoosting</text>
    <rect x="160" y="77" width="484" height="25" rx="4" fill="#334155" />
    <text x="652" y="94" fill="#cbd5e1" font-size="10">$30,508 (R²: 0.3446)</text>
    <!-- 3 -->
    <text x="150" y="137" text-anchor="end" fill="#94a3b8" font-size="11">RandomForest</text>
    <rect x="160" y="122" width="491" height="25" rx="4" fill="#334155" />
    <text x="659" y="139" fill="#cbd5e1" font-size="10">$30,557 (R²: 0.3401)</text>
    <!-- 4 -->
    <text x="150" y="182" text-anchor="end" fill="#94a3b8" font-size="11">Ridge (L2 Baseline)</text>
    <rect x="160" y="167" width="510" height="25" rx="4" fill="#475569" />
    <text x="678" y="184" fill="#cbd5e1" font-size="10">$31,411 (R²: 0.3202)</text>
  </svg>
</div>
"""

NLP_SVG = """
<div class="diagram-container">
  <div class="diagram-title">Dynamic N-Gram NLP Information Extraction Engine</div>
  <svg viewBox="0 0 760 140" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <marker id="arr2" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="#64748b" />
      </marker>
    </defs>
    <rect x="10" y="30" width="130" height="75" rx="8" fill="#1e293b" stroke="#475569" />
    <text x="75" y="62" text-anchor="middle" fill="#f8fafc" font-size="11" font-weight="600">Raw Job Posting</text>
    <text x="75" y="80" text-anchor="middle" fill="#94a3b8" font-size="9">Arbitrary Narrative Text</text>
    <path d="M 140 67 L 165 67" stroke="#64748b" stroke-width="2" marker-end="url(#arr2)" />
    <rect x="170" y="30" width="130" height="75" rx="8" fill="#1e293b" stroke="#475569" />
    <text x="235" y="62" text-anchor="middle" fill="#f8fafc" font-size="11" font-weight="600">Token Scanner</text>
    <text x="235" y="80" text-anchor="middle" fill="#94a3b8" font-size="9">1-gram to 4-gram Window</text>
    <path d="M 300 67 L 325 67" stroke="#64748b" stroke-width="2" marker-end="url(#arr2)" />
    <rect x="330" y="20" width="180" height="45" rx="6" fill="#0369a1" fill-opacity="0.3" stroke="#0284c7" />
    <text x="420" y="47" text-anchor="middle" fill="#38bdf8" font-size="10" font-weight="600">500+ Entity Lexicon Match</text>
    <rect x="330" y="75" width="180" height="45" rx="6" fill="#047857" fill-opacity="0.3" stroke="#059669" />
    <text x="420" y="102" text-anchor="middle" fill="#34d399" font-size="10" font-weight="600">Regex Regex Degree &amp; Tenure</text>
    <path d="M 510 67 L 545 67" stroke="#64748b" stroke-width="2" marker-end="url(#arr2)" />
    <rect x="550" y="30" width="190" height="75" rx="8" fill="#4f46e5" fill-opacity="0.25" stroke="#6366f1" />
    <text x="645" y="58" text-anchor="middle" fill="#a5b4fc" font-size="11" font-weight="700">Structured Response</text>
    <text x="645" y="74" text-anchor="middle" fill="#cbd5e1" font-size="9">Categorized Skills (8 Groups)</text>
    <text x="645" y="89" text-anchor="middle" fill="#94a3b8" font-size="9">Degree, Years &amp; Density Metric</text>
  </svg>
</div>
"""

# Inject diagrams into chapters
c6_with_svg = CHAPTER_6_HTML.replace("<h2>6.2 Quantitative Benchmark Evaluation Table</h2>", BENCHMARK_SVG + "<h2>6.2 Quantitative Benchmark Evaluation Table</h2>")
c7_with_svg = CHAPTER_7_HTML.replace("<h2>7.3 8-Domain Entity Taxonomy Overview</h2>", NLP_SVG + "<h2>7.3 8-Domain Entity Taxonomy Overview</h2>")
c8_with_svg = CHAPTER_8_HTML.replace("<h2>8.2 Client-Side Smart Routing (src/services/api.js)</h2>", ARCH_SVG + "<h2>8.2 Client-Side Smart Routing (src/services/api.js)</h2>")

full_monograph_html = (
    HTML_HEAD
    + COVER_HTML
    + TOC_HTML
    + CHAPTER_1_HTML
    + CHAPTER_2_HTML
    + CHAPTER_3_HTML
    + CHAPTER_4_HTML
    + CHAPTER_5_HTML
    + c6_with_svg
    + c7_with_svg
    + c8_with_svg
    + CHAPTER_9_HTML
    + CHAPTER_10_HTML
    + CHAPTER_11_HTML
    + CHAPTER_12_HTML
    + APPENDICES_HTML
    + "\n</body>\n</html>"
)

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(full_monograph_html)

print(f"Generated extended monograph HTML at: {OUTPUT_HTML} ({len(full_monograph_html)} characters)")

# Compile to PDF using Headless Chrome
chrome_cmd = [
    CHROME_PATH,
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    "--run-all-compositor-stages-before-draw",
    f"--print-to-pdf={OUTPUT_PDF}",
    OUTPUT_HTML
]

print(f"Compiling PDF via: {' '.join(chrome_cmd)}")
res = subprocess.run(chrome_cmd, capture_output=True, text=True)

if os.path.exists(OUTPUT_PDF) and os.path.getsize(OUTPUT_PDF) > 0:
    pdf_size = os.path.getsize(OUTPUT_PDF)
    print(f"SUCCESS: Generated PDF at {OUTPUT_PDF} ({pdf_size} bytes)")
    
    with open(OUTPUT_PDF, "rb") as f:
        pdf_data = f.read()
    pages = len(re.findall(rb'/Type\s*/Page\b', pdf_data))
    print(f"Total Page Count: {pages} Pages!")
    
    # Copy to project root
    shutil.copyfile(OUTPUT_PDF, ROOT_PDF)
    print(f"Copied to root: {ROOT_PDF}")
    
    # Copy to artifact directory
    shutil.copyfile(OUTPUT_PDF, ARTIFACT_PDF)
    print(f"Copied to artifact dir: {ARTIFACT_PDF}")
else:
    print(f"ERROR: {res.stderr}")
