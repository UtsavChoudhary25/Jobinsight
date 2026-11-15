import os
import re
import subprocess
import shutil
import markdown

REPORT_MD_PATH = os.path.abspath("docs/JOBINSIGHT_TECHNICAL_REPORT.md")
HTML_OUTPUT_PATH = os.path.abspath("docs/JobInsight_Technical_Report.html")
PDF_OUTPUT_PATH = os.path.abspath("docs/JobInsight_Technical_Report.pdf")
ROOT_PDF_PATH = os.path.abspath("JobInsight_Technical_Report.pdf")
ARTIFACT_PDF_PATH = r"C:\Users\choud\.gemini\antigravity\brain\9f07df47-b440-4730-a84f-36f0189f7a4b\JobInsight_Technical_Report.pdf"

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(CHROME_PATH):
    CHROME_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

with open(REPORT_MD_PATH, "r", encoding="utf-8") as f:
    raw_md = f.read()

# Replace Mermaid Architecture Diagram with a clean, vector SVG flowchart
ARCH_SVG = """
<div class="diagram-box">
  <div class="diagram-title">System Architecture: Unified Serverless Full-Stack Flow</div>
  <svg viewBox="0 0 880 340" class="arch-svg" xmlns="http://www.w3.org/2000/svg">
    <!-- Definitions for gradients & markers -->
    <defs>
      <linearGradient id="gradClient" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#0f172a" />
        <stop offset="100%" stop-color="#1e293b" />
      </linearGradient>
      <linearGradient id="gradEdge" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#0369a1" />
        <stop offset="100%" stop-color="#0284c7" />
      </linearGradient>
      <linearGradient id="gradFastAPI" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#047857" />
        <stop offset="100%" stop-color="#059669" />
      </linearGradient>
      <linearGradient id="gradML" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%" stop-color="#4f46e5" />
        <stop offset="100%" stop-color="#6366f1" />
      </linearGradient>
      <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="#64748b" />
      </marker>
    </defs>

    <!-- Column 1: Client UI -->
    <rect x="20" y="20" width="180" height="300" rx="10" fill="url(#gradClient)" stroke="#334155" stroke-width="1.5" />
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

    <!-- Arrow 1 to 2 -->
    <path d="M 200 170 L 235 170" stroke="#64748b" stroke-width="2" marker-end="url(#arrow)" />

    <!-- Column 2: Serverless Router -->
    <rect x="240" y="20" width="180" height="300" rx="10" fill="url(#gradEdge)" stroke="#0284c7" stroke-width="1.5" />
    <text x="330" y="50" text-anchor="middle" fill="#ffffff" font-weight="700" font-size="13">2. VERCEL SERVERLESS</text>
    <rect x="255" y="80" width="150" height="65" rx="6" fill="#0f172a" stroke="#0369a1" />
    <text x="330" y="107" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="600">vercel.json Rewrites</text>
    <text x="330" y="125" text-anchor="middle" fill="#94a3b8" font-size="9">/api/* -&gt; api/index.py</text>
    <rect x="255" y="170" width="150" height="75" rx="6" fill="#0f172a" stroke="#0369a1" />
    <text x="330" y="198" text-anchor="middle" fill="#38bdf8" font-size="11" font-weight="600">api/index.py</text>
    <text x="330" y="216" text-anchor="middle" fill="#cbd5e1" font-size="9">Vercel Python Function</text>
    <text x="330" y="230" text-anchor="middle" fill="#94a3b8" font-size="9">Zero-CORS Same-Origin</text>

    <!-- Arrow 2 to 3 -->
    <path d="M 420 170 L 455 170" stroke="#64748b" stroke-width="2" marker-end="url(#arrow)" />

    <!-- Column 3: FastAPI Backend -->
    <rect x="460" y="20" width="190" height="300" rx="10" fill="url(#gradFastAPI)" stroke="#059669" stroke-width="1.5" />
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

    <!-- Arrow 3 to 4 -->
    <path d="M 650 170 L 685 170" stroke="#64748b" stroke-width="2" marker-end="url(#arrow)" />

    <!-- Column 4: ML & Artifacts -->
    <rect x="690" y="20" width="170" height="300" rx="10" fill="url(#gradML)" stroke="#6366f1" stroke-width="1.5" />
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

# Replace Benchmark Comparison Chart with clean SVG bar chart
BENCHMARK_SVG = """
<div class="diagram-box">
  <div class="diagram-title">Model Evaluation: Hold-Out Test MAE (USD) — Lower is Better</div>
  <svg viewBox="0 0 760 220" class="chart-svg" xmlns="http://www.w3.org/2000/svg">
    <!-- Grid lines -->
    <line x1="160" y1="30" x2="720" y2="30" stroke="#334155" stroke-dasharray="4" />
    <line x1="160" y1="75" x2="720" y2="75" stroke="#334155" stroke-dasharray="4" />
    <line x1="160" y1="120" x2="720" y2="120" stroke="#334155" stroke-dasharray="4" />
    <line x1="160" y1="165" x2="720" y2="165" stroke="#334155" stroke-dasharray="4" />

    <!-- Labels & Bars -->
    <!-- 1. HistGradientBoosting (Selected) -->
    <text x="150" y="47" text-anchor="end" fill="#38bdf8" font-weight="700" font-size="11">HistGradientBoosting (Best)</text>
    <rect x="160" y="32" width="480" height="25" rx="4" fill="#0284c7" />
    <text x="648" y="49" fill="#f8fafc" font-size="10" font-weight="700">$30,482 (R²: 0.3454) ★ Selected</text>

    <!-- 2. GradientBoosting -->
    <text x="150" y="92" text-anchor="end" fill="#94a3b8" font-size="11">GradientBoosting</text>
    <rect x="160" y="77" width="484" height="25" rx="4" fill="#334155" />
    <text x="652" y="94" fill="#cbd5e1" font-size="10">$30,508 (R²: 0.3446)</text>

    <!-- 3. RandomForest -->
    <text x="150" y="137" text-anchor="end" fill="#94a3b8" font-size="11">RandomForest</text>
    <rect x="160" y="122" width="491" height="25" rx="4" fill="#334155" />
    <text x="659" y="139" fill="#cbd5e1" font-size="10">$30,557 (R²: 0.3401)</text>

    <!-- 4. Ridge Regression -->
    <text x="150" y="182" text-anchor="end" fill="#94a3b8" font-size="11">Ridge (L2 Baseline)</text>
    <rect x="160" y="167" width="510" height="25" rx="4" fill="#475569" />
    <text x="678" y="184" fill="#cbd5e1" font-size="10">$31,411 (R²: 0.3202)</text>
  </svg>
</div>
"""

# Replace NLP Pipeline Diagram
NLP_SVG = """
<div class="diagram-box">
  <div class="diagram-title">NLP Entity & Requirement Processing Pipeline</div>
  <svg viewBox="0 0 760 140" class="arch-svg" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <marker id="arrow2" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
        <path d="M 0 1 L 10 5 L 0 9 z" fill="#64748b" />
      </marker>
    </defs>
    <!-- Step 1: Raw Text -->
    <rect x="10" y="30" width="130" height="75" rx="8" fill="#1e293b" stroke="#475569" />
    <text x="75" y="62" text-anchor="middle" fill="#f8fafc" font-size="11" font-weight="600">Raw Job Posting</text>
    <text x="75" y="80" text-anchor="middle" fill="#94a3b8" font-size="9">Arbitrary Unstructured Text</text>

    <path d="M 140 67 L 165 67" stroke="#64748b" stroke-width="2" marker-end="url(#arrow2)" />

    <!-- Step 2: Normalization -->
    <rect x="170" y="30" width="130" height="75" rx="8" fill="#1e293b" stroke="#475569" />
    <text x="235" y="62" text-anchor="middle" fill="#f8fafc" font-size="11" font-weight="600">Token Scanner</text>
    <text x="235" y="80" text-anchor="middle" fill="#94a3b8" font-size="9">1-gram to 4-gram Windows</text>

    <path d="M 300 67 L 325 67" stroke="#64748b" stroke-width="2" marker-end="url(#arrow2)" />

    <!-- Step 3: Dual Matching -->
    <rect x="330" y="20" width="180" height="45" rx="6" fill="#0369a1" fill-opacity="0.3" stroke="#0284c7" />
    <text x="420" y="47" text-anchor="middle" fill="#38bdf8" font-size="10" font-weight="600">500+ Entity Lexicon Match</text>

    <rect x="330" y="75" width="180" height="45" rx="6" fill="#047857" fill-opacity="0.3" stroke="#059669" />
    <text x="420" y="102" text-anchor="middle" fill="#34d399" font-size="10" font-weight="600">Regex Regex Degree &amp; Tenure</text>

    <path d="M 510 67 L 545 67" stroke="#64748b" stroke-width="2" marker-end="url(#arrow2)" />

    <!-- Step 4: Structured Output -->
    <rect x="550" y="30" width="190" height="75" rx="8" fill="#4f46e5" fill-opacity="0.25" stroke="#6366f1" />
    <text x="645" y="58" text-anchor="middle" fill="#a5b4fc" font-size="11" font-weight="700">Structured Response</text>
    <text x="645" y="74" text-anchor="middle" fill="#cbd5e1" font-size="9">Categorized Skills (8 Categories)</text>
    <text x="645" y="89" text-anchor="middle" fill="#94a3b8" font-size="9">Degree, Years &amp; Density Metric</text>
  </svg>
</div>
"""

# Replace mermaid blocks in raw markdown with SVG diagrams
processed_md = re.sub(r"```mermaid\s*flowchart TD[\s\S]*?```", ARCH_SVG, raw_md)
processed_md = re.sub(r"```mermaid\s*xychart-beta[\s\S]*?```", BENCHMARK_SVG, processed_md)
processed_md = re.sub(r"```mermaid\s*flowchart LR[\s\S]*?```", NLP_SVG, processed_md)
processed_md = re.sub(r"```mermaid\s*timeline[\s\S]*?```", "", processed_md)

# Convert Markdown to HTML
content_html = markdown.markdown(processed_md, extensions=['tables', 'fenced_code', 'toc'])

# Complete Executive Document HTML Template with CSS Print Styling
FULL_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>JobInsight AI — Technical & Executive Report</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

    @page {{
      size: A4 portrait;
      margin: 18mm 16mm 18mm 16mm;
      @bottom-right {{
        content: "Page " counter(page);
        font-size: 8pt;
        color: #64748b;
        font-family: 'Plus Jakarta Sans', sans-serif;
      }}
      @bottom-left {{
        content: "JobInsight AI — Technical & Executive Report";
        font-size: 8pt;
        color: #64748b;
        font-family: 'Plus Jakarta Sans', sans-serif;
      }}
    }}

    *, *:before, *:after {{
      box-sizing: border-box;
    }}

    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      color: #0f172a;
      background-color: #ffffff;
      line-height: 1.6;
      font-size: 9.8pt;
      margin: 0;
      padding: 0;
      -webkit-font-smoothing: antialiased;
    }}

    /* Cover / Header Banner */
    .report-header {{
      background: linear-gradient(135deg, #090d16 0%, #0f172a 60%, #1e293b 100%);
      color: #ffffff;
      padding: 32px 28px;
      border-radius: 12px;
      margin-bottom: 28px;
      border: 1px solid #334155;
      page-break-after: avoid;
    }}

    .report-brand {{
      display: inline-block;
      font-size: 9pt;
      font-weight: 700;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      color: #38bdf8;
      background: rgba(56, 189, 248, 0.12);
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 4px 10px;
      border-radius: 4px;
      margin-bottom: 12px;
    }}

    .report-title {{
      font-size: 22pt;
      font-weight: 800;
      line-height: 1.25;
      margin: 0 0 8px 0;
      letter-spacing: -0.5px;
      color: #f8fafc;
    }}

    .report-subtitle {{
      font-size: 11pt;
      color: #94a3b8;
      margin: 0 0 20px 0;
      font-weight: 400;
    }}

    .meta-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
      padding-top: 18px;
      border-top: 1px solid rgba(255, 255, 255, 0.12);
    }}

    .meta-item {{
      background: rgba(255, 255, 255, 0.04);
      padding: 8px 12px;
      border-radius: 6px;
      border: 1px solid rgba(255, 255, 255, 0.08);
    }}

    .meta-label {{
      font-size: 7.5pt;
      color: #94a3b8;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      font-weight: 600;
      margin-bottom: 2px;
    }}

    .meta-value {{
      font-size: 9pt;
      font-weight: 700;
      color: #f1f5f9;
    }}

    .meta-value a {{
      color: #38bdf8;
      text-decoration: none;
    }}

    /* Typography */
    h1, h2, h3, h4 {{
      color: #0f172a;
      font-weight: 700;
      letter-spacing: -0.3px;
      page-break-after: avoid;
    }}

    h2 {{
      font-size: 14pt;
      margin-top: 26px;
      margin-bottom: 12px;
      padding-bottom: 6px;
      border-bottom: 2px solid #e2e8f0;
      color: #0f172a;
      display: flex;
      align-items: center;
    }}

    h3 {{
      font-size: 11.5pt;
      margin-top: 18px;
      margin-bottom: 8px;
      color: #1e293b;
    }}

    p {{
      margin: 0 0 10px 0;
      color: #334155;
      text-align: justify;
    }}

    strong {{
      color: #0f172a;
      font-weight: 600;
    }}

    a {{
      color: #0284c7;
      text-decoration: none;
    }}

    /* Lists */
    ul, ol {{
      margin: 0 0 12px 0;
      padding-left: 20px;
      color: #334155;
    }}

    li {{
      margin-bottom: 5px;
    }}

    /* Tables */
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 14px 0 18px 0;
      font-size: 8.8pt;
      page-break-inside: avoid;
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      overflow: hidden;
    }}

    th, td {{
      padding: 7px 10px;
      text-align: left;
      border-bottom: 1px solid #e2e8f0;
    }}

    th {{
      background-color: #0f172a;
      color: #f8fafc;
      font-weight: 600;
      text-transform: uppercase;
      font-size: 7.5pt;
      letter-spacing: 0.5px;
    }}

    tr:nth-child(even) {{
      background-color: #f8fafc;
    }}

    tr:hover {{
      background-color: #f1f5f9;
    }}

    /* Highlight the selected model in the table */
    tr:has(td strong:contains("HistGradientBoosting")) {{
      background-color: #f0fdf4 !important;
      font-weight: 600;
    }}

    /* Code & JSON Blocks */
    pre {{
      background-color: #0f172a;
      color: #f1f5f9;
      padding: 12px 14px;
      border-radius: 8px;
      font-family: 'JetBrains Mono', Consolas, 'Courier New', monospace;
      font-size: 8pt;
      line-height: 1.45;
      overflow-x: auto;
      margin: 10px 0 14px 0;
      border: 1px solid #334155;
      page-break-inside: avoid;
    }}

    code {{
      font-family: 'JetBrains Mono', Consolas, 'Courier New', monospace;
      font-size: 8.5pt;
      background-color: #f1f5f9;
      color: #0369a1;
      padding: 2px 5px;
      border-radius: 4px;
      border: 1px solid #e2e8f0;
    }}

    pre code {{
      background-color: transparent;
      color: inherit;
      padding: 0;
      border: none;
      font-size: 8pt;
    }}

    /* Diagram Containers */
    .diagram-box {{
      background: #090d16;
      border: 1px solid #334155;
      border-radius: 10px;
      padding: 14px 16px;
      margin: 16px 0 20px 0;
      page-break-inside: avoid;
    }}

    .diagram-title {{
      font-size: 9pt;
      font-weight: 700;
      color: #38bdf8;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      margin-bottom: 10px;
      text-align: center;
    }}

    svg.arch-svg, svg.chart-svg {{
      width: 100%;
      height: auto;
      display: block;
      margin: 0 auto;
    }}

    /* Callout Badges & Highlights */
    .callout {{
      background-color: #f0fdf4;
      border-left: 4px solid #10b981;
      padding: 10px 14px;
      border-radius: 0 6px 6px 0;
      margin: 12px 0 16px 0;
      font-size: 9pt;
      color: #064e3b;
      page-break-inside: avoid;
    }}

    .callout-title {{
      font-weight: 700;
      margin-bottom: 2px;
      color: #047857;
    }}

    hr {{
      border: none;
      border-top: 1px solid #e2e8f0;
      margin: 24px 0;
    }}

    .page-break {{
      page-break-after: always;
    }}
  </style>
</head>
<body>

  <!-- Cover Header -->
  <div class="report-header">
    <div class="report-brand">Official Engineering &amp; ML Architecture Report</div>
    <div class="report-title">JobInsight AI — Technical &amp; Executive Report</div>
    <div class="report-subtitle">Production Machine Learning Compensation Regressor, Dynamic NLP Requirement Extractor, and Macroeconomic Analytics Platform</div>
    
    <div class="meta-grid">
      <div class="meta-item">
        <div class="meta-label">Live Platform</div>
        <div class="meta-value"><a href="https://jobinsight-peach.vercel.app/">jobinsight-peach.vercel.app</a></div>
      </div>
      <div class="meta-item">
        <div class="meta-label">Source Repository</div>
        <div class="meta-value"><a href="https://github.com/UtsavChoudhary25/Jobinsight">github.com/UtsavChoudhary25/Jobinsight</a></div>
      </div>
      <div class="meta-item">
        <div class="meta-label">Dataset Provenance</div>
        <div class="meta-value">LinkedIn Postings (123,849 Records)</div>
      </div>
      <div class="meta-item">
        <div class="meta-label">Production Model</div>
        <div class="meta-value">HistGradientBoosting (R² = 0.3454)</div>
      </div>
    </div>
  </div>

  <!-- Main Report Body -->
  {content_html}

</body>
</html>
"""

# Write HTML file
with open(HTML_OUTPUT_PATH, "w", encoding="utf-8") as f:
    f.write(FULL_HTML)

print(f"Generated HTML report at: {HTML_OUTPUT_PATH}")

# Convert HTML to PDF using Chrome Headless
chrome_cmd = [
    CHROME_PATH,
    "--headless=new",
    "--disable-gpu",
    "--no-pdf-header-footer",
    "--run-all-compositor-stages-before-draw",
    f"--print-to-pdf={PDF_OUTPUT_PATH}",
    HTML_OUTPUT_PATH
]

print(f"Executing: {' '.join(chrome_cmd)}")
res = subprocess.run(chrome_cmd, capture_output=True, text=True)

if os.path.exists(PDF_OUTPUT_PATH) and os.path.getsize(PDF_OUTPUT_PATH) > 0:
    pdf_size = os.path.getsize(PDF_OUTPUT_PATH)
    print(f"SUCCESS: Generated PDF at: {PDF_OUTPUT_PATH} ({pdf_size} bytes)")
    
    # Copy to project root
    shutil.copyfile(PDF_OUTPUT_PATH, ROOT_PDF_PATH)
    print(f"Copied to root: {ROOT_PDF_PATH}")
    
    # Copy to artifacts directory
    shutil.copyfile(PDF_OUTPUT_PATH, ARTIFACT_PDF_PATH)
    print(f"Copied to artifact dir: {ARTIFACT_PDF_PATH}")
else:
    print(f"ERROR generating PDF: {res.stderr}")
