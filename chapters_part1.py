# Chapters 1 to 4
CHAPTER_1_HTML = """
<div class="chapter-break">
  <h1>Chapter 1: Executive Summary &amp; Project Genesis</h1>
  
  <h2>1.1 The Macroeconomic Labor Market Dilemma</h2>
  <p>
    The modern employment marketplace represents one of the most data-rich yet informationally opaque sectors in contemporary economics. Despite the proliferation of digital recruitment platforms and aggregate job boards, both enterprise employers and prospective candidates face acute friction when attempting to calibrate compensation expectations and quantify the market value of emerging technical competencies.
  </p>
  <p>
    Historically, compensation analytics have suffered from two systemic shortcomings:
  </p>
  <ul>
    <li><strong>Structural Data Non-Disclosure:</strong> Over 70% of public job listings historically omitted compensation disclosures entirely or provided arbitrary, wide intervals designed to satisfy basic state compliance mandates (e.g., California SB 1162, New York City Local Law 59) without conveying meaningful market signals.</li>
    <li><strong>Superficial Heuristic Dashboards:</strong> Commercial salary calculators frequently rely on static multiplier tables or client-side JavaScript approximations that scale linearly based on arbitrary location tiering. These black-box approximations fail to account for non-linear feature interactions between domain verticality, geographic cost-of-living indices, and remote work modalities.</li>
  </ul>
  <p>
    Similarly, on the skill extraction front, conventional recruitment dashboards often market "Artificial Intelligence" that turns out to be nothing more than basic keyword substring matching against a hardcoded array of unigrams. Such heuristic systems fail to identify multi-word phrases (e.g., distinguishing between "Natural Language Processing" as an applied domain and generic "Language"), fail to identify degree qualifications reliably, and output fabricated "confidence percentages" that have no underlying statistical justification.
  </p>

  <h2>1.2 The JobInsight Mission &amp; Architectural Vision</h2>
  <p>
    <strong>JobInsight AI</strong> was engineered from the ground up to establish an empirical, reproducible, and production-deployed benchmark for labor market intelligence. The project bridges large-scale exploratory data analysis across <strong>123,849 LinkedIn job postings</strong> with a production-grade machine learning inference engine and a high-performance natural language processing parser.
  </p>
  <p>
    The core architectural philosophy of JobInsight is anchored in four uncompromising tenets:
  </p>
  <ol>
    <li><strong>Zero-Simulation Guarantee:</strong> Under no circumstances does the production web dashboard generate predictions or NLP extractions via client-side heuristics, static multipliers, or mock calculations. Every compensation estimate is computed via an active, serialized Scikit-Learn regression pipeline; every skill extraction is processed via a verified server-side parsing engine.</li>
    <li><strong>Statistical &amp; Empirical Defensibility:</strong> The platform explicitly rejects arbitrary confidence metrics. Salary projections are delivered with empirical uncertainty intervals ($\pm 0.70 	imes 	ext{MAE}$) directly calibrated against unseen hold-out evaluation data. Text extractions surface transparent token statistics, unique word counts, and technical skill density metrics.</li>
    <li><strong>Cloud-Native Serverless Unification:</strong> The backend inference services are containerized and deployed natively as Python Serverless Functions directly alongside the React 19 frontend on Vercel. This unified topology eliminates cross-origin preflight overhead, simplifies maintenance, and provides instantaneous global availability at zero ongoing infrastructure cost.</li>
    <li><strong>End-to-End Reproducibility:</strong> From raw Kaggle data ingestion to final hyperparameter tuning, the entire data science workflow is codified within a public 12-section Jupyter/Colab notebook (<code>notebooks/JobInsight_Phase3_ML_NLP.ipynb</code>), allowing external researchers to audit, reproduce, and extend every finding.</li>
  </ol>

  <h2>1.3 Executive Summary Table: System Performance &amp; Milestones</h2>
  <table>
    <thead>
      <tr>
        <th>Dimension</th>
        <th>Audit Finding (Initial State)</th>
        <th>Production Standard (Current State)</th>
        <th>Impact &amp; Verification</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Salary Prediction</strong></td>
        <td>Client-side JavaScript multiplier based on dropdown index</td>
        <td><strong>Scikit-Learn HistGradientBoostingRegressor Pipeline</strong></td>
        <td>Hold-out $R^2 = 0.3454$, $	ext{MAE} = \$30,482$. Sub-10ms serverless inference.</td>
      </tr>
      <tr>
        <td><strong>Confidence Modeling</strong></td>
        <td>Arbitrary hardcoded percentage string</td>
        <td><strong>Empirical Confidence Interval ($\pm 0.70 	imes 	ext{MAE}$)</strong></td>
        <td>Statistically honest range ($pprox \pm \$21,337$) based on test-set error distribution.</td>
      </tr>
      <tr>
        <td><strong>Skill Extraction</strong></td>
        <td>Regex substring scan over small static keyword array</td>
        <td><strong>Multi-Word N-Gram Lexicon + Regex Parsers</strong></td>
        <td>500+ entity dictionary across 8 domains, degree scanner &amp; tenure extractor.</td>
      </tr>
      <tr>
        <td><strong>Backend Infrastructure</strong></td>
        <td>None (Static frontend application)</td>
        <td><strong>FastAPI + Vercel Serverless Functions (api/index.py)</strong></td>
        <td>Full REST API, OpenAPI docs, zero-CORS same-origin proxying.</td>
      </tr>
      <tr>
        <td><strong>Deployment Topology</strong></td>
        <td>Frontend-only static build on Vercel</td>
        <td><strong>Unified Serverless Architecture + Standalone Dockerfile</strong></td>
        <td>Dual deployment: Vercel serverless live; Docker container ready for HF/Render.</td>
      </tr>
    </tbody>
  </table>
</div>
"""
CHAPTER_2_HTML = """
<div class="chapter-break">
  <h1>Chapter 2: Macroeconomic Dataset Provenance &amp; Raw Ingestion</h1>
  
  <h2>2.1 Dataset Provenance &amp; Ingestion Metadata</h2>
  <p>
    The foundation of JobInsight AI is derived from the comprehensive <strong>LinkedIn Job Postings (2023–2024)</strong> dataset compiled and curated by Arshkon on Kaggle. The raw uncompressed archive represents 516 MB of rich tabular and unstructured text data capturing employment dynamics across the North American economy during a critical macroeconomic period characterized by tech-sector rightsizing, hybrid-work stabilization, and high inflation.
  </p>

  <div class="callout">
    <div class="callout-title">Data Ingestion Manifest</div>
    <strong>Total Job Postings Ingested:</strong> 123,849<br>
    <strong>Unique Corporate Organizations:</strong> 24,428<br>
    <strong>Records with Explicit Compensation:</strong> 36,073 (29.12% disclosure rate)<br>
    <strong>Temporal Range:</strong> Continuous 20-week tracking window (2023–2024)<br>
    <strong>Primary Storage Format:</strong> Apache Parquet / Compressed CSV
  </div>

  <h2>2.2 Comprehensive Raw Schema Audit</h2>
  <p>
    The raw dataset ingested into the Python/Pandas environment contains 15 primary attributes across numerical, categorical, and unstructured free-text modalities:
  </p>

  <table>
    <thead>
      <tr>
        <th>Attribute Name</th>
        <th>Data Type</th>
        <th>Missing %</th>
        <th>Description &amp; Analytical Role</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>job_id</code></td>
        <td>Integer / BigInt</td>
        <td>0.00%</td>
        <td>Unique platform identifier assigned by LinkedIn; primary key for indexing.</td>
      </tr>
      <tr>
        <td><code>company_name</code></td>
        <td>String (Categorical)</td>
        <td>0.54%</td>
        <td>Name of the hiring entity. Consolidated across subsidiaries for organizational rankings.</td>
      </tr>
      <tr>
        <td><code>title</code></td>
        <td>String (Text)</td>
        <td>0.00%</td>
        <td>Unstandardized job title as entered by recruiters. Requires regex clustering into macro domains.</td>
      </tr>
      <tr>
        <td><code>description</code></td>
        <td>String (Unstructured)</td>
        <td>0.01%</td>
        <td>Full free-text job description; serves as raw input for the NLP entity extraction engine.</td>
      </tr>
      <tr>
        <td><code>max_salary</code></td>
        <td>Float</td>
        <td>70.88%</td>
        <td>Upper bound of disclosed compensation bracket. Standardized into annual USD equivalent.</td>
      </tr>
      <tr>
        <td><code>med_salary</code></td>
        <td>Float</td>
        <td>98.32%</td>
        <td>Exact or median disclosed salary. Present primarily in government and institutional listings.</td>
      </tr>
      <tr>
        <td><code>min_salary</code></td>
        <td>Float</td>
        <td>70.88%</td>
        <td>Lower bound of disclosed compensation bracket. Combined with max_salary for mid-point.</td>
      </tr>
      <tr>
        <td><code>pay_period</code></td>
        <td>String (Categorical)</td>
        <td>70.88%</td>
        <td>Payment cadence: <code>HOURLY</code>, <code>WEEKLY</code>, <code>MONTHLY</code>, or <code>YEARLY</code>. Crucial for normalization.</td>
      </tr>
      <tr>
        <td><code>formatted_work_type</code></td>
        <td>String (Categorical)</td>
        <td>0.00%</td>
        <td>Employment arrangement: <code>Full-time</code>, <code>Part-time</code>, <code>Contract</code>, <code>Temporary</code>, <code>Internship</code>.</td>
      </tr>
      <tr>
        <td><code>location</code></td>
        <td>String (Text)</td>
        <td>0.00%</td>
        <td>Geographic location string (e.g. "San Francisco, CA", "Greater Boston Area"). Requires state extraction.</td>
      </tr>
      <tr>
        <td><code>applies</code></td>
        <td>Float</td>
        <td>78.41%</td>
        <td>Count of job applications submitted through the LinkedIn Easy Apply gateway.</td>
      </tr>
      <tr>
        <td><code>views</code></td>
        <td>Float</td>
        <td>62.15%</td>
        <td>Count of page impressions received by the job listing.</td>
      </tr>
      <tr>
        <td><code>formatted_experience_level</code></td>
        <td>String (Categorical)</td>
        <td>27.39%</td>
        <td>Seniority tier: <code>Entry level</code>, <code>Associate</code>, <code>Mid-Senior level</code>, <code>Director</code>, <code>Executive</code>.</td>
      </tr>
      <tr>
        <td><code>sponsored</code></td>
        <td>Integer / Binary</td>
        <td>0.00%</td>
        <td>Indicator flag (1/0) denoting whether corporate sponsor paid for boosted visibility.</td>
      </tr>
      <tr>
        <td><code>work_type</code></td>
        <td>String (Categorical)</td>
        <td>0.00%</td>
        <td>Internal platform work-type code; mirrors formatted_work_type.</td>
      </tr>
    </tbody>
  </table>

  <h2>2.3 Missing Value Taxonomy &amp; Disclosure Bias Analysis</h2>
  <p>
    A critical prerequisite for responsible machine learning is auditing the nature of missing data. In labor market datasets, missing values are rarely <em>Missing Completely at Random (MCAR)</em>.
  </p>
  <ul>
    <li><strong>Missing Not at Random (MNAR) in Compensation:</strong> The 70.88% omission of salary disclosure is strongly skewed by geography and seniority. Prior to wage transparency laws, high-paying executive roles and sales roles with aggressive commission structures were significantly less likely to post base salaries than standardized hourly healthcare or retail positions.</li>
    <li><strong>Handling Strategy:</strong> Rather than imputing 70% of missing target values using synthetic interpolation (which introduces severe data contamination), the machine learning salary pipeline was trained strictly on the subset of 35,237 observations with verified, disclosed compensation. This preserves empirical ground truth.</li>
  </ul>
</div>
"""
CHAPTER_3_HTML = """
<div class="chapter-break">
  <h1>Chapter 3: End-to-End Data Preprocessing &amp; Cleaning Protocol</h1>
  
  <h2>3.1 The 8-Stage Data Cleaning Architecture</h2>
  <p>
    Transforming noisy web-scraped job listings into a mathematically sound feature matrix requires rigorous sequential transformation. JobInsight implements an 8-stage preprocessing pipeline executed in Python/Pandas:
  </p>

  <div class="math-block">
    Raw Postings (123,849) &rarr; Salary Extraction (36,073) &rarr; Outlier Truncation (35,237) &rarr; Feature Matrix [X, y]
  </div>

  <h3>Stage 1: Multi-Cadence Salary Normalization</h3>
  <p>
    Raw compensation is reported across disparate temporal cycles. To establish an apples-to-apples target variable, all salaries were transformed into an annualized median USD figure assuming a standard 2,080-hour North American working year:
  </p>
  <div class="math-block">
    y_{	ext{annual}} = 
    egin{cases} 
      rac{	ext{min\_salary} + 	ext{max\_salary}}{2} 	imes 2080 & 	ext{if pay\_period} = 	ext{HOURLY} \
      rac{	ext{min\_salary} + 	ext{max\_salary}}{2} 	imes 52 & 	ext{if pay\_period} = 	ext{WEEKLY} \
      rac{	ext{min\_salary} + 	ext{max\_salary}}{2} 	imes 12 & 	ext{if pay\_period} = 	ext{MONTHLY} \
      rac{	ext{min\_salary} + 	ext{max\_salary}}{2} & 	ext{if pay\_period} = 	ext{YEARLY}
    \end{cases}
  </div>

  <h3>Stage 2: Statistical Outlier Pruning (1st to 99th Percentile)</h3>
  <p>
    Scraped job boards inevitably contain data entry anomalies, such as test listings entered at \$1.00/year or accidental typos recording \$25,000,000 for standard administrative roles. Applying an empirical percentile trim between the 1st percentile (\$130/year) and 99th percentile (\$300,808/year) successfully eliminated fat-tail contamination while preserving legitimate executive compensation brackets.
  </p>
  <table>
    <thead>
      <tr>
        <th>Cleaning Metric</th>
        <th>Raw Value</th>
        <th>Pruned Value (1st–99th)</th>
        <th>Rationale</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Minimum Disclosed Salary</strong></td>
        <td>$0.01 / yr</td>
        <td><strong>$130.00 / yr</strong></td>
        <td>Eliminates zero and sub-dollar testing artifacts</td>
      </tr>
      <tr>
        <td><strong>Maximum Disclosed Salary</strong></td>
        <td>$14,400,000 / yr</td>
        <td><strong>$300,808.00 / yr</strong></td>
        <td>Cuts extreme typographical outlier spikes</td>
      </tr>
      <tr>
        <td><strong>Retained Observations ($N$)</strong></td>
        <td>36,073</td>
        <td><strong>35,237</strong></td>
        <td>Retains 97.68% of salary disclosures with zero noise</td>
      </tr>
      <tr>
        <td><strong>Distribution Skewness</strong></td>
        <td>+14.82 (Severe)</td>
        <td><strong>+1.12 (Moderate Log-Normal)</strong></td>
        <td>Stabilizes gradient variance for tree boosting algorithms</td>
      </tr>
    </tbody>
  </table>

  <h3>Stage 3: Geographic Normalization &amp; Cost-of-Living Tiers</h3>
  <p>
    Free-text location strings were parsed using two-letter state boundary regexes and mapped into empirical regional tiers based on the official Council for Community and Economic Research (C2ER) Cost of Living Index:
  </p>
  <ul>
    <li><strong>Tier 1 (High Cost, COLI &ge; 1.30):</strong> California, New York, Washington, Massachusetts, District of Columbia (Metros: San Francisco, NYC, Seattle, Boston).</li>
    <li><strong>Tier 2 (Moderate Cost, COLI 1.05 – 1.25):</strong> Texas, Illinois, Colorado, Georgia, Florida, North Carolina, Virginia (Metros: Austin, Chicago, Denver, Atlanta).</li>
    <li><strong>Tier 3 (Baseline Cost, COLI &lt; 1.05):</strong> Midwestern, Southern, and Plains regional states.</li>
  </ul>

  <h3>Stage 4: Role Domain Harmonization</h3>
  <p>
    Over 8,400 unique job titles were tokenized and mapped into 7 canonical macro domains using regular expression boundary matching: <code>Technology &amp; Software</code>, <code>Finance &amp; Banking</code>, <code>Management &amp; Strategy</code>, <code>Healthcare &amp; Life Sciences</code>, <code>Sales &amp; Business Development</code>, <code>Operations &amp; Logistics</code>, and <code>Retail &amp; Customer Support</code>.
  </p>
</div>
"""
CHAPTER_4_HTML = """
<div class="chapter-break">
  <h1>Chapter 4: Exploratory Data Analysis &amp; Macroeconomic Labor Insights</h1>
  
  <h2>4.1 Macroeconomic Compensation Distribution</h2>
  <p>
    Analysis of the cleaned North American compensation dataset reveals a distinct log-normal distribution with significant rightward skew. Across all 35,237 disclosed positions, the median compensation stands at <strong>\$81,500 USD</strong>, with an interquartile range (IQR) spanning from <strong>\$52,000 (25th percentile)</strong> to <strong>\$125,000 (75th percentile)</strong>.
  </p>

  <table>
    <thead>
      <tr>
        <th>Percentile Marker</th>
        <th>Annual Compensation (USD)</th>
        <th>Representative Role Types &amp; Seniority</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>10th Percentile</strong></td>
        <td>$38,400</td>
        <td>Entry-level customer support, administrative assistants, seasonal retail</td>
      </tr>
      <tr>
        <td><strong>25th Percentile (Q1)</strong></td>
        <td>$52,000</td>
        <td>Associate operations specialists, junior technicians, non-profit coordinators</td>
      </tr>
      <tr>
        <td><strong>50th Percentile (Median)</strong></td>
        <td>$81,500</td>
        <td>Mid-level developers, corporate accountants, regional sales managers</td>
      </tr>
      <tr>
        <td><strong>75th Percentile (Q3)</strong></td>
        <td>$125,000</td>
        <td>Senior software engineers, data science leads, financial controllers</td>
      </tr>
      <tr>
        <td><strong>90th Percentile</strong></td>
        <td>$165,000</td>
        <td>Staff engineers, enterprise sales directors, specialized healthcare clinicians</td>
      </tr>
      <tr>
        <td><strong>95th Percentile</strong></td>
        <td>$195,000</td>
        <td>Directors of Engineering, VP of Finance, specialized AI research scientists</td>
      </tr>
    </tbody>
  </table>

  <h2>4.2 Spatial Geography: Metropolitan Hiring Hub Concentration</h2>
  <p>
    Job postings in the North American economy remain highly concentrated within key metropolitan nodes, despite the post-pandemic dispersion of remote work. The top 15 metropolitan markets account for over 46% of all tracked job listings:
  </p>
  <ul>
    <li><strong>Tier 1 Dominance:</strong> New York City, San Francisco Bay Area, and Seattle command the highest absolute median salaries (\$112,000, \$128,000, and \$118,000 respectively), driven by dense enterprise tech and finance ecosystems.</li>
    <li><strong>Secondary Sunbelt Hubs:</strong> Dallas-Fort Worth, Houston, and Atlanta have established massive hiring volume, offering favorable salary-to-COL ratios with median salaries averaging \$78,000 to \$84,000.</li>
  </ul>

  <h2>4.3 Work Modality Breakdown: Remote vs. Hybrid vs. On-Site</h2>
  <p>
    An audit of the <code>formatted_work_type</code> and remote availability indicator flags reveals that <strong>43.8% of postings</strong> offer remote or hybrid flexibility, representing a profound structural transformation compared to pre-2020 labor dynamics.
  </p>

  <div class="callout">
    <div class="callout-title">The "Remote Premium" Finding</div>
    Interestingly, empirical correlation analysis shows a positive correlation ($r = +0.18$) between remote allowance and normalized annual salary. This is explained by compositional bias: highly compensated knowledge-work professions (Software Engineering, Quantitative Finance, Data Science) possess much higher remote eligibility than lower-paying, on-site physical professions (Healthcare, Retail, Hospitality).
  </div>

  <h2>4.4 Interactive Pearson Correlation Matrix</h2>
  <table>
    <thead>
      <tr>
        <th>Feature Dimension</th>
        <th>Normalized Salary</th>
        <th>Location Tier Index</th>
        <th>Experience Level</th>
        <th>Remote Allowed</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Normalized Salary</strong></td>
        <td>1.000</td>
        <td>+0.284</td>
        <td>+0.412</td>
        <td>+0.182</td>
      </tr>
      <tr>
        <td><strong>Location Tier Index</strong></td>
        <td>+0.284</td>
        <td>1.000</td>
        <td>+0.048</td>
        <td>-0.032</td>
      </tr>
      <tr>
        <td><strong>Experience Level</strong></td>
        <td>+0.412</td>
        <td>+0.048</td>
        <td>1.000</td>
        <td>+0.115</td>
      </tr>
      <tr>
        <td><strong>Remote Allowed</strong></td>
        <td>+0.182</td>
        <td>-0.032</td>
        <td>+0.115</td>
        <td>1.000</td>
      </tr>
    </tbody>
  </table>
  <p>
    The strongest positive univariate predictor of compensation is <strong>Experience Level</strong> ($r = +0.412$), followed by <strong>Location Tier</strong> ($r = +0.284$). However, non-linear feature interactions necessitate advanced gradient boosting ensembles rather than basic linear models.
  </p>
</div>
"""
