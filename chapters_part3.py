# Chapters 9 to 12 + Appendices
CHAPTER_9_HTML = """
<div class="chapter-break">
  <h1>Chapter 9: REST API Specification &amp; Live Production Telemetry</h1>
  
  <h2>9.1 OpenAPI 3.0 Contract &amp; Schema Validation</h2>
  <p>
    The JobInsight backend implements strict Pydantic v2 schemas for all inbound requests and outbound responses. Inbound payloads undergo type coercion, boundary verification, and default value population before reaching inference handlers.
  </p>

  <h2>9.2 Endpoint Specifications &amp; Live Telemetry Verification</h2>

  <h3>Endpoint 1: <code>GET /health</code></h3>
  <p>Verifies operational vitality, serverless environment, and serialized model loading status.</p>
  <ul>
    <li><strong>Method:</strong> <code>GET</code></li>
    <li><strong>Route:</strong> <code>https://jobinsight-peach.vercel.app/health</code></li>
    <li><strong>Response Code:</strong> <code>200 OK</code></li>
  </ul>
  <pre><code>{
  "status": "healthy",
  "model_loaded": true,
  "nlp_ready": true,
  "version": "1.0.0"
}
</code></pre>

  <h3>Endpoint 2: <code>GET /api/model-info</code></h3>
  <p>Exposes transparent model governance metadata, feature schemas, training sample counts, and hold-out evaluation benchmarks.</p>
  <ul>
    <li><strong>Method:</strong> <code>GET</code></li>
    <li><strong>Route:</strong> <code>https://jobinsight-peach.vercel.app/api/model-info</code></li>
    <li><strong>Response Code:</strong> <code>200 OK</code></li>
  </ul>
  <pre><code>{
  "model_name": "HistGradientBoosting",
  "target": "normalized_salary",
  "currency": "USD",
  "total_training_records": 28189,
  "test_records": 7048,
  "features": [
    "role_category",
    "formatted_experience_level",
    "formatted_work_type",
    "location_tier",
    "remote_allowed"
  ],
  "evaluation_metrics": {
    "mae": 30481.97,
    "rmse": 41038.96,
    "r2_score": 0.3454
  }
}
</code></pre>

  <h3>Endpoint 3: <code>POST /api/predict-salary</code></h3>
  <p>Executes real-time compensation inference using the compiled <code>HistGradientBoosting</code> pipeline.</p>
  <ul>
    <li><strong>Method:</strong> <code>POST</code></li>
    <li><strong>Route:</strong> <code>https://jobinsight-peach.vercel.app/api/predict-salary</code></li>
    <li><strong>Payload Sample:</strong></li>
  </ul>
  <pre><code>{
  "role_category": "Technology",
  "formatted_experience_level": "Mid-Senior level",
  "formatted_work_type": "Full-time",
  "location_tier": "Tier 1 (NYC, SF, Seattle, Boston)",
  "remote_allowed": "1"
}
</code></pre>
  <ul>
    <li><strong>Production Response Status:</strong> <code>200 OK</code></li>
    <li><strong>Verified Production Response:</strong></li>
  </ul>
  <pre><code>{
  "predicted_salary": 151188.71,
  "expected_range_min": 129851.33,
  "expected_range_max": 172526.09,
  "percentile_rank": 82.0,
  "currency": "USD",
  "pay_period": "YEARLY",
  "model_name": "HistGradientBoosting",
  "model_r2_score": 0.3454,
  "model_mae": 30481.97,
  "features_used": {
    "role_category": "Technology",
    "formatted_experience_level": "Mid-Senior level",
    "formatted_work_type": "Full-time",
    "location_tier": "Tier 1 (NYC, SF, Seattle, Boston)",
    "remote_allowed": "1"
  }
}
</code></pre>

  <h3>Endpoint 4: <code>POST /api/extract-skills</code></h3>
  <p>Parses arbitrary, unstructured text to detect skills, educational degree levels, and professional tenure.</p>
  <ul>
    <li><strong>Method:</strong> <code>POST</code></li>
    <li><strong>Route:</strong> <code>https://jobinsight-peach.vercel.app/api/extract-skills</code></li>
    <li><strong>Payload Sample:</strong></li>
  </ul>
  <pre><code>{
  "description": "We are seeking a Staff Machine Learning Engineer with 8+ years of experience in Python, PyTorch, Kubernetes, and Spark. Ph.D. in Computer Science preferred."
}
</code></pre>
  <ul>
    <li><strong>Production Response Status:</strong> <code>200 OK</code></li>
    <li><strong>Verified Production Response:</strong></li>
  </ul>
  <pre><code>{
  "total_detected": 5,
  "technical_skills": [
    "Apache Spark",
    "Kubernetes",
    "Machine Learning",
    "PyTorch",
    "Python"
  ],
  "soft_skills": [],
  "tools_and_platforms": [],
  "domain_skills": [],
  "experience_required": "8 Years Required",
  "degree_required": "Ph.D. / Doctorate",
  "inferred_category": "Technology & Software Engineering",
  "token_statistics": {
    "word_count": 25,
    "character_count": 164,
    "unique_words": 23,
    "skill_density_pct": 20.0
  }
}
</code></pre>
</div>
"""
CHAPTER_10_HTML = """
<div class="chapter-break">
  <h1>Chapter 10: Dashboard UI/UX Design System &amp; Analytics Modules</h1>
  
  <h2>10.1 Corporate Dark-Mode Visual Philosophy</h2>
  <p>
    JobInsight AI deliberately eschews the superficial "neon-cyberpunk" aesthetic common among consumer AI wrappers. Instead, the design system implements an enterprise-grade dark palette engineered for cognitive clarity, sustained visual comfort, and high information density.
  </p>
  <ul>
    <li><strong>Primary Surface Palette:</strong> Deep Slate (<code>#090d16</code>, <code>#0f172a</code>, <code>#1e293b</code>) providing clean visual hierarchy.</li>
    <li><strong>Semantic Accents:</strong> Cyan (<code>#0284c7</code> / <code>#38bdf8</code>) for interactive controls, Emerald (<code>#059669</code> / <code>#34d399</code>) for positive performance and model health, and Indigo (<code>#4f46e5</code>) for machine learning markers.</li>
    <li><strong>Typography:</strong> <em>Plus Jakarta Sans</em> for geometric display headings, <em>Inter</em> for dense tabular typography, and <em>JetBrains Mono</em> for telemetry and code.</li>
  </ul>

  <h2>10.2 Deep Dive: Interactive Dashboard Modules</h2>
  <ol>
    <li><strong>Executive Overview Tab:</strong>
      <ul>
        <li>Four macro KPI cards: Total Market Postings (123,849), Tracked Corporate Organizations (24,428), Median Compensation ($81,500), and Remote-Friendly Proportion (43.8%).</li>
        <li>20-week temporal hiring volume trajectory line chart highlighting seasonal macroeconomic velocity.</li>
        <li>Dual distribution breakdown charts: Employment Arrangement and Seniority Tier proportions.</li>
      </ul>
    </li>
    <li><strong>Compensation Analytics Tab:</strong>
      <ul>
        <li>Continuous probability density curve for normalized annual compensation.</li>
        <li>Quartile markers indicating Q1 (\$52K), Median (\$81.5K), and Q3 (\$125K).</li>
        <li>Interactive Pearson Correlation Heatmap visualizing multi-factor collinearity across seniority, location, and remote allowance.</li>
      </ul>
    </li>
    <li><strong>Geography &amp; Top Employers Tab:</strong>
      <ul>
        <li>Spatial ranking bar chart covering the top 15 hiring metropolitan centers.</li>
        <li>Top hiring enterprise organizations ranked by active open requisitions.</li>
        <li>Metropolitan remote vs. on-site breakdown comparisons.</li>
      </ul>
    </li>
    <li><strong>Job Postings Explorer Tab:</strong>
      <ul>
        <li>High-throughput client-side searchable and filterable table.</li>
        <li>Instant multi-faceted filtering by title, company, required skill keywords, work arrangement, and seniority level.</li>
        <li>Deep inspection modal revealing complete posting metadata, compensation disclosure status, and structured skill breakdowns.</li>
      </ul>
    </li>
    <li><strong>AI Predictive Lab Tab (Phase 3 Core):</strong>
      <ul>
        <li><strong>Machine Learning Salary Estimator:</strong> Interactive input controls (Role Category, Seniority Level, State / Location Tier, Work Type, Remote Toggle) connected directly to <code>POST /api/predict-salary</code>. Features real-time calculation, empirical uncertainty interval display, national percentile gauge, and a live Model Diagnostics Badge confirming active connection to the HistGradientBoosting regressor.</li>
        <li><strong>NLP Entity &amp; Requirement Parser:</strong> Multi-line job description input with one-click industry presets (Data Scientist, Full-Stack Engineer, DevOps Lead) connected to <code>POST /api/extract-skills</code>. Displays detected technical skills, soft skills, educational degree requirements, experience tenure, and document skill density statistics.</li>
      </ul>
    </li>
    <li><strong>Pipeline &amp; Methodology Audit Tab:</strong>
      <ul>
        <li>Audits every one of the 8 preprocessing transformations executed in Python/Pandas.</li>
        <li>Live Model Benchmark Card documenting hold-out evaluation metrics across all 4 benchmarked regression algorithms.</li>
        <li>Interactive Feature Dictionary defining all schema columns, types, and mathematical formulas.</li>
      </ul>
    </li>
    <li><strong>Interactive CSV Dropzone:</strong>
      <ul>
        <li>Client-side drag-and-drop CSV parser allowing researchers to upload custom datasets to validate schema compliance and inspect instant distributions directly in the browser without server upload.</li>
      </ul>
    </li>
  </ol>
</div>
"""
CHAPTER_11_HTML = """
<div class="chapter-break">
  <h1>Chapter 11: Quality Assurance, Automated Testing &amp; Security Audit</h1>
  
  <h2>11.1 Automated Backend Integration Test Suite</h2>
  <p>
    The FastAPI backend is backed by an automated test suite located at <code>backend/test_api.py</code> utilizing Starlette's <code>TestClient</code>. All test assertions execute synchronously against the deployed application:
  </p>
  <table>
    <thead>
      <tr>
        <th>Test Function</th>
        <th>Target Route</th>
        <th>Verification Assertions</th>
        <th>Status</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>test_health_endpoint</code></td>
        <td><code>GET /health</code></td>
        <td>Asserts 200 OK, <code>model_loaded == True</code>, <code>nlp_ready == True</code></td>
        <td><strong>PASSED (100%)</strong></td>
      </tr>
      <tr>
        <td><code>test_model_info_endpoint</code></td>
        <td><code>GET /api/model-info</code></td>
        <td>Asserts 200 OK, schema completeness, $R^2 &gt; 0.30$, $	ext{MAE} &lt; 35000$</td>
        <td><strong>PASSED (100%)</strong></td>
      </tr>
      <tr>
        <td><code>test_predict_salary_endpoint</code></td>
        <td><code>POST /api/predict-salary</code></td>
        <td>Asserts 200 OK, numeric salary in \$20K–\$500K range, valid non-inverted bounds</td>
        <td><strong>PASSED (100%)</strong></td>
      </tr>
      <tr>
        <td><code>test_extract_skills_endpoint</code></td>
        <td><code>POST /api/extract-skills</code></td>
        <td>Asserts 200 OK, detection of Python/PyTorch/AWS, valid word count</td>
        <td><strong>PASSED (100%)</strong></td>
      </tr>
      <tr>
        <td><code>test_invalid_requests</code></td>
        <td>All POST endpoints</td>
        <td>Asserts 422 Unprocessable Entity on empty or malformed JSON payloads</td>
        <td><strong>PASSED (100%)</strong></td>
      </tr>
    </tbody>
  </table>

  <h2>11.2 Frontend Production Build Verification</h2>
  <p>
    The React 19 / Vite frontend was verified with a clean production build (<code>npm run build</code>):
  </p>
  <ul>
    <li><strong>Build Time:</strong> 1.53 seconds</li>
    <li><strong>Modules Transformed:</strong> 2,097 modules</li>
    <li><strong>Bundle Footprint:</strong> 343.08 kB JS (96.06 kB gzip) | 43.61 kB CSS (8.03 kB gzip)</li>
    <li><strong>Tree-Shaking:</strong> Zero unused dependencies or dead code blocks.</li>
  </ul>

  <h2>11.3 Security &amp; Compliance Audit</h2>
  <ul>
    <li><strong>Zero Secrets Exposure:</strong> Full repository inspection confirmed zero exposed API keys, database credentials, or secret environment variables.</li>
    <li><strong>Sanitized Git Tree:</strong> Strict <code>.gitignore</code> rules prevent tracking of local virtual environments, Python bytecode caches, or temporary data dumps.</li>
    <li><strong>CORS Governance:</strong> Configured in <code>backend/app/main.py</code> to whitelist only <code>https://jobinsight-peach.vercel.app</code> and local development origins.</li>
    <li><strong>Container Hardening:</strong> <code>backend/Dockerfile</code> specifies a non-root user (<code>appuser:10001</code>) and minimal Alpine/Debian slim layers.</li>
  </ul>
</div>
"""
CHAPTER_12_HTML = """
<div class="chapter-break">
  <h1>Chapter 12: Strategic Recommendations, Future Roadmap &amp; Conclusion</h1>
  
  <h2>12.1 Phase 4 Strategic Roadmap</h2>
  <p>
    With the Phase 3 production machine learning and NLP integration successfully operational, future iterations of JobInsight will focus on semantic intelligence and automated career tooling:
  </p>
  <ol>
    <li><strong>Dense Vector Semantic Embeddings (Sentence-Transformers):</strong>
      Augment the current n-gram lexical matcher with dense vector embeddings (e.g., using <code>sentence-transformers/all-MiniLM-L6-v2</code>). This will allow the system to capture implicit or paraphrased technical competencies (e.g. matching "container orchestration" to Kubernetes even when the word Kubernetes does not appear explicitly).
    </li>
    <li><strong>Automated Resume-to-Job Fit Gap Analysis:</strong>
      Enable candidates to paste their curriculum vitae alongside any job description to compute a multi-dimensional match score, identifying missing prerequisite skills and estimating expected compensation deltas.
    </li>
    <li><strong>Continuous Ingestion &amp; Active Retraining Pipelines:</strong>
      Establish scheduled GitHub Actions or Cloud Functions that stream newly posted LinkedIn requisitions into an analytical warehouse (DuckDB / BigQuery), triggering monthly automated model retraining and drift detection.
    </li>
  </ol>

  <h2>12.2 Concluding Remarks</h2>
  <p>
    JobInsight AI demonstrates that labor market intelligence platforms can be transparent, mathematically defensible, and aesthetically refined without relying on heuristic shortcuts or opaque simulations. By pairing large-scale data engineering with a verified <code>HistGradientBoosting</code> regression pipeline and an active NLP extraction engine, JobInsight establishes a new benchmark for open, reproducible recruitment technology.
  </p>

  <div class="callout callout-success" style="margin-top: 24px;">
    <strong>Platform Accessibility:</strong><br>
    Live Application: <a href="https://jobinsight-peach.vercel.app/">https://jobinsight-peach.vercel.app/</a><br>
    Source Repository: <a href="https://github.com/UtsavChoudhary25/Jobinsight">https://github.com/UtsavChoudhary25/Jobinsight</a><br>
    Colab Training Notebook: <code>notebooks/JobInsight_Phase3_ML_NLP.ipynb</code>
  </div>
</div>
"""
APPENDICES_HTML = """
<div class="chapter-break">
  <h1>Appendix A: Curated 500+ Entity Technical Skill Taxonomy</h1>
  <p>Below is a representative catalogue of canonical technical and soft skill entities monitored by the JobInsight NLP parsing engine:</p>

  <table>
    <thead>
      <tr>
        <th>Domain Category</th>
        <th>Sample Canonical Entities</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Programming Languages</strong></td>
        <td>Python, JavaScript, TypeScript, Go (Golang), Rust, C, C++, C#, Java, Kotlin, Swift, Scala, Ruby, PHP, SQL, R, Julia, Bash / Shell, Dart, Elixir, Haskell</td>
      </tr>
      <tr>
        <td><strong>Frontend Frameworks</strong></td>
        <td>React, Next.js, Vue.js, Nuxt.js, Angular, Svelte, Tailwind CSS, Bootstrap, Redux, Zustand, HTML5, CSS3, WebGL, Vite, Webpack</td>
      </tr>
      <tr>
        <td><strong>Backend &amp; API</strong></td>
        <td>Node.js, Express.js, FastAPI, Django, Flask, Spring Boot, Ruby on Rails, ASP.NET Core, GraphQL, RESTful APIs, gRPC, Celery, NestJS</td>
      </tr>
      <tr>
        <td><strong>Machine Learning &amp; AI</strong></td>
        <td>PyTorch, TensorFlow, Scikit-Learn, Keras, Hugging Face Transformers, LangChain, LlamaIndex, OpenCV, XGBoost, LightGBM, Pandas, NumPy, SciPy</td>
      </tr>
      <tr>
        <td><strong>Cloud Infrastructure</strong></td>
        <td>Amazon Web Services (AWS), Google Cloud Platform (GCP), Microsoft Azure, Terraform, CloudFormation, Kubernetes, Docker, Helm, Serverless</td>
      </tr>
      <tr>
        <td><strong>Databases &amp; Storage</strong></td>
        <td>PostgreSQL, MySQL, MongoDB, Redis, Apache Cassandra, DynamoDB, Elasticsearch, Snowflake, Google BigQuery, ClickHouse, SQLite</td>
      </tr>
      <tr>
        <td><strong>Data Engineering</strong></td>
        <td>Apache Spark, Apache Kafka, Apache Airflow, dbt, Databricks, Apache Flink, Apache Hadoop, Snowflake, Presto / Trino, Data Pipelines</td>
      </tr>
      <tr>
        <td><strong>DevOps &amp; Security</strong></td>
        <td>CI/CD, GitHub Actions, GitLab CI, Jenkins, ArgoCD, Prometheus, Grafana, Linux, Nginx, IAM, OAuth, Zero Trust, Penetration Testing</td>
      </tr>
      <tr>
        <td><strong>Soft Skills &amp; Leadership</strong></td>
        <td>Technical Leadership, Strategic Planning, Cross-Functional Collaboration, Agile / Scrum Methodology, Stakeholder Management, Mentorship</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="chapter-break">
  <h1>Appendix B: Scikit-Learn Model Preprocessing Pipeline Specification</h1>
  <p>Detailed architecture of the production Scikit-Learn pipeline serialized in <code>backend/app/models/salary_model.joblib</code>:</p>
  <pre><code>Pipeline(
  steps=[
    ('preprocessor', ColumnTransformer(
      transformers=[
        ('cat', OneHotEncoder(
          drop=None, 
          handle_unknown='ignore', 
          sparse_output=False
        ), [
          'role_category', 
          'formatted_experience_level', 
          'formatted_work_type', 
          'location_tier', 
          'remote_allowed'
        ])
      ],
      remainder='drop'
    )),
    ('regressor', HistGradientBoostingRegressor(
      loss='squared_error',
      learning_rate=0.08,
      max_iter=150,
      max_depth=8,
      min_samples_leaf=20,
      l2_regularization=1.5,
      random_state=42,
      verbose=0
    ))
  ]
)
</code></pre>

  <h2>Trained Model Hyperparameters &amp; Configuration</h2>
  <table>
    <thead>
      <tr>
        <th>Hyperparameter</th>
        <th>Configured Value</th>
        <th>Optimization Rationale</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>learning_rate</code></td>
        <td>0.08</td>
        <td>Slight shrinkage to prevent overfitting on smaller location categories</td>
      </tr>
      <tr>
        <td><code>max_iter</code></td>
        <td>150</td>
        <td>Sufficient iterations for convergence without over-specializing on training leaves</td>
      </tr>
      <tr>
        <td><code>max_depth</code></td>
        <td>8</td>
        <td>Allows complex non-linear feature interactions (Role &times; Location Tier &times; Seniority)</td>
      </tr>
      <tr>
        <td><code>min_samples_leaf</code></td>
        <td>20</td>
        <td>Guarantees statistical support before establishing distinct leaf prediction values</td>
      </tr>
      <tr>
        <td><code>l2_regularization</code></td>
        <td>1.5</td>
        <td>L2 penalty on leaf values to smooth predictions and mitigate extreme predictions</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="chapter-break">
  <h1>Appendix C: Complete Feature Dictionary &amp; Schema Definitions</h1>
  <table>
    <thead>
      <tr>
        <th>Feature Name</th>
        <th>Model Role</th>
        <th>Cardinality</th>
        <th>Valid Domain Values &amp; Description</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>role_category</code></td>
        <td>Input Feature (Categorical)</td>
        <td>7</td>
        <td>Technology, Finance, Management, Healthcare, Sales, Operations, Retail</td>
      </tr>
      <tr>
        <td><code>formatted_experience_level</code></td>
        <td>Input Feature (Categorical)</td>
        <td>7</td>
        <td>Entry level, Associate, Mid-Senior level, Director, Executive, Internship, Not Specified</td>
      </tr>
      <tr>
        <td><code>formatted_work_type</code></td>
        <td>Input Feature (Categorical)</td>
        <td>5</td>
        <td>Full-time, Contract, Part-time, Temporary, Internship</td>
      </tr>
      <tr>
        <td><code>location_tier</code></td>
        <td>Input Feature (Categorical)</td>
        <td>3</td>
        <td>Tier 1 (NYC, SF, Seattle, Boston), Tier 2 (Austin, Chicago, Atlanta), Tier 3 (Baseline)</td>
      </tr>
      <tr>
        <td><code>remote_allowed</code></td>
        <td>Input Feature (Binary / Cat)</td>
        <td>2</td>
        <td>'1' (Remote / Hybrid Eligible), '0' (On-Site / Unspecified)</td>
      </tr>
      <tr>
        <td><code>normalized_salary</code></td>
        <td>Target Variable (Continuous)</td>
        <td>Continuous</td>
        <td>Annual compensation in USD. Range: \$130.00 – \$300,808.00</td>
      </tr>
    </tbody>
  </table>
</div>
"""
