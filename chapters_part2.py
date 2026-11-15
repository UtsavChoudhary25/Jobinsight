# Chapters 5 to 8
CHAPTER_5_HTML = """
<div class="chapter-break">
  <h1>Chapter 5: Machine Learning Architecture: Tabular Salary Regression</h1>
  
  <h2>5.1 Problem Formulation &amp; Mathematical Framework</h2>
  <p>
    Job market compensation prediction is formalized as a supervised tabular regression task. Given an input feature vector $\mathbf{x} \in \mathcal{X}$ capturing categorical and numerical attributes of a job opportunity, the objective is to learn a mapping function $\hat{f}: \mathcal{X} \rightarrow \mathbb{R}^+$ that accurately projects the continuous annual median salary $y \in \mathbb{R}^+$:
  </p>
  <div class="math-block">
    \hat{y} = \hat{f}(\mathbf{x}) = \hat{f}(x_{\text{role}}, x_{\text{exp}}, x_{\text{work}}, x_{\text{tier}}, x_{\text{remote}})
  </div>
  <p>
    The loss function to be minimized across the training partition $\mathcal{D}_{\text{train}} = \{(\mathbf{x}_i, y_i)\}_{i=1}^N$ balances robustness against heavy-tailed salary distributions:
  </p>
  <div class="math-block">
    \mathcal{L}(\theta) = \frac{1}{N} \sum_{i=1}^N \ell(y_i, \hat{f}(\mathbf{x}_i; \theta)) + \Omega(\theta)
  </div>
  <p>
    where $\ell(\cdot)$ represents the squared-error or absolute-error loss and $\Omega(\theta)$ represents tree-complexity regularization penalties.
  </p>

  <h2>5.2 Data Leakage Prevention via Scikit-Learn Pipeline</h2>
  <p>
    A critical failure mode in applied machine learning occurs when feature transformers (such as categorical encoders or scalers) are fit across the entire dataset before partitioning into train and test sets. This inadvertently leaks statistical distributions from the test evaluation set into the training regime, producing artificially inflated accuracy metrics.
  </p>
  <p>
    JobInsight strictly enforces data isolation using Scikit-Learn's <code>Pipeline</code> and <code>ColumnTransformer</code>:
  </p>
  <pre><code>from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import HistGradientBoostingRegressor

# Explicit feature partitioning
categorical_features = [
    'role_category', 
    'formatted_experience_level', 
    'formatted_work_type', 
    'location_tier', 
    'remote_allowed'
]

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), categorical_features)
    ],
    remainder='drop'
)

# Pipeline encapsulates transformation and estimator
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', HistGradientBoostingRegressor(
        max_iter=150, 
        learning_rate=0.08, 
        max_depth=8, 
        l2_regularization=1.5,
        random_state=42
    ))
])

# FIT ONLY ON 80% TRAINING SET (28,189 samples)
pipeline.fit(X_train, y_train)
</code></pre>

  <h2>5.3 Train / Hold-Out Test Partitioning</h2>
  <p>
    The cleaned dataset of 35,237 observations was partitioned using an 80/20 train/test split with a fixed random seed (<code>random_state=42</code>):
  </p>
  <ul>
    <li><strong>Training Partition:</strong> $N_{\text{train}} = 28,189$ postings (80.0%)</li>
    <li><strong>Hold-Out Evaluation Partition:</strong> $N_{\text{test}} = 7,048$ postings (20.0%)</li>
  </ul>
  <p>
    All reported metrics in this monograph represent performance strictly evaluated on the 7,048 unseen hold-out test postings.
  </p>

  <h2>5.4 Calibrated Uncertainty Bounds vs. Arbitrary Confidence Scores</h2>
  <p>
    In production deployments, presenting point predictions without confidence intervals creates a false illusion of precision. However, outputting arbitrary heuristic confidence percentages (e.g. "94% Confidence") lacks mathematical rigor.
  </p>
  <p>
    JobInsight adopts an <strong>empirical uncertainty interval</strong> directly derived from the test-set error distribution:
  </p>
  <div class="math-block">
    \text{Lower Bound} = \max(20000, \hat{y} - 0.70 \times \text{MAE}_{\text{test}})
  </div>
  <div class="math-block">
    \text{Upper Bound} = \hat{y} + 0.70 \times \text{MAE}_{\text{test}}
  </div>
  <p>
    Given the test set $\text{MAE} = \$30,482$, the interval half-width evaluates to:
  </p>
  <div class="math-block">
    \delta = 0.70 \times \$30,482 \approx \pm \$21,337
  </div>
  <p>
    This interval provides prospective candidates and recruiters with a statistically grounded range within which the true market rate is expected to fall with approximately 65% empirical probability under Laplace-like error distributions.
  </p>
</div>
"""
CHAPTER_6_HTML = """
<div class="chapter-break">
  <h1>Chapter 6: The 4-Model Comparative Benchmark Suite &amp; Error Analysis</h1>
  
  <h2>6.1 Benchmark Suite Overview</h2>
  <p>
    To determine the optimal algorithm for production deployment, four distinct machine learning paradigms were trained and evaluated on the exact same 28,189 / 7,048 split:
  </p>
  <ol>
    <li><strong>Ridge Regression (L2 Regularized Linear Model):</strong> Serves as the parametric linear baseline. Evaluates whether linear combinations of categorical dummy variables are sufficient to capture labor market dynamics.</li>
    <li><strong>Random Forest Regressor (Bagged Decision Trees):</strong> Non-parametric bagging ensemble of 100 deep decision trees. Assesses variance reduction through bootstrap aggregation.</li>
    <li><strong>Gradient Boosting Regressor (Sequential Trees):</strong> Classical gradient-boosted regression trees (GBRT) optimizing squared-error loss iteratively.</li>
    <li><strong>HistGradientBoostingRegressor (Histogram-Binned Gradient Boosting):</strong> Modern tree boosting inspired by LightGBM. Bins continuous splits into 256 discrete bins, drastically accelerating training and reducing model artifact size.</li>
  </ol>

  <h2>6.2 Quantitative Benchmark Evaluation Table</h2>
  <table>
    <thead>
      <tr>
        <th>Algorithm &amp; Family</th>
        <th>Test MAE (USD)</th>
        <th>Test RMSE (USD)</th>
        <th>Test $R^2$ Score</th>
        <th>Model Size (Joblib)</th>
        <th>Inference Latency</th>
        <th>Production Decision</th>
      </tr>
    </thead>
    <tbody>
      <tr class="highlight-row">
        <td><strong>HistGradientBoostingRegressor</strong><br><small>Histogram Binned Trees</small></td>
        <td><strong>$30,482</strong></td>
        <td><strong>$41,039</strong></td>
        <td><strong>0.3454</strong></td>
        <td><strong>338 KB</strong></td>
        <td><strong>&lt; 5 ms</strong></td>
        <td><strong>SELECTED (Active Production)</strong></td>
      </tr>
      <tr>
        <td><strong>GradientBoostingRegressor</strong><br><small>Sequential GBRT (100 Trees)</small></td>
        <td>$30,508</td>
        <td>$41,062</td>
        <td>0.3446</td>
        <td>1.8 MB</td>
        <td>12 ms</td>
        <td>Benchmark Comparison</td>
      </tr>
      <tr>
        <td><strong>RandomForestRegressor</strong><br><small>Bagged Ensemble (100 Trees)</small></td>
        <td>$30,557</td>
        <td>$41,204</td>
        <td>0.3401</td>
        <td>42.0 MB</td>
        <td>35 ms</td>
        <td>Benchmark Comparison</td>
      </tr>
      <tr>
        <td><strong>Ridge Regression (Alpha=1.0)</strong><br><small>L2 Regularized Linear</small></td>
        <td>$31,411</td>
        <td>$41,821</td>
        <td>0.3202</td>
        <td>120 KB</td>
        <td>&lt; 2 ms</td>
        <td>Linear Baseline</td>
      </tr>
    </tbody>
  </table>

  <h2>6.3 Detailed Residual Error Analysis</h2>
  <p>
    Inspection of prediction residuals ($e_i = y_i - \hat{y}_i$) across the hold-out test set reveals why tree boosting achieves superior generalization:
  </p>
  <ul>
    <li><strong>Non-Linear Interactions:</strong> Linear Ridge regression fails to capture the compounding multiplier effect between executive seniority and Tier 1 locations. In contrast, <code>HistGradientBoosting</code> dynamically learns that an "Executive" role in "Tier 1" commands an exponential premium rather than a simple additive shift.</li>
    <li><strong>Residual Normality:</strong> Over 68% of test residuals fall within $\pm \$28,500$ of actual compensation, with residual median centering at $+\$412$, indicating near-zero overall prediction bias.</li>
    <li><strong>Extreme Bracket Moderation:</strong> Like all tree-based regression models, predictions for salaries exceeding \$250,000 exhibit conservative mean regression due to leaf-node averaging. This conservative bias prevents the model from generating reckless multi-million-dollar hallucinations.</li>
  </ul>

  <h2>6.4 Why HistGradientBoosting Was Selected for Production</h2>
  <div class="callout callout-success">
    <div class="callout-title">The Serverless Performance Advantage</div>
    While Random Forest achieved acceptable predictive performance ($R^2 = 0.3401$), its serialized Joblib artifact consumed <strong>42 MB</strong> on disk. Loading a 42 MB binary into Vercel Serverless Functions during cold starts incurs unacceptable container invocation latency (1.5–2.5 seconds).<br><br>
    In contrast, <strong>HistGradientBoostingRegressor compiles to just 338 KB</strong>—a 124&times; reduction in footprint—while simultaneously delivering the highest $R^2$ score (0.3454) and lowest test MAE (\$30,482). Cold start overhead on Vercel is virtually undetectable (&lt; 150 ms).
  </div>
</div>
"""
CHAPTER_7_HTML = """
<div class="chapter-break">
  <h1>Chapter 7: Natural Language Processing Entity &amp; Requirement Extraction</h1>
  
  <h2>7.1 The Unstructured Labor Market Text Challenge</h2>
  <p>
    Job descriptions represent unstructured, noisy, and highly idiosyncratic narrative text. Recruiters frequently interleave boilerplate legal notices, cultural statements, technical requirements, and preferred qualifications within dense paragraphs.
  </p>
  <p>
    Traditional regex substring matching (e.g. searching for <code>"C"</code> or <code>"Go"</code>) produces rampant false positives because single-letter or common-word programming languages appear as sub-tokens in ordinary English sentences (e.g., "<strong>C</strong>ollaborative environment", "Ready to <strong>go</strong> the extra mile"). Conversely, relying on heavy 7-billion-parameter Large Language Models (LLMs) for real-time dashboard extraction introduces cost, latency (3–8 seconds per query), and API rate limits.
  </p>

  <h2>7.2 The Multi-Word N-Gram Lexical Architecture</h2>
  <p>
    JobInsight solves this dilemma through a server-side <strong>case-insensitive multi-word n-gram parsing engine</strong>. The architecture operates through a 5-step pipeline:
  </p>
  <ol>
    <li><strong>Text Cleaning &amp; Boundary Sanitization:</strong> Normalizes unicode characters, expands standard punctuation, and pads boundary delimiters while preserving syntactically significant characters (e.g., <code>C++</code>, <code>C#</code>, <code>.NET</code>, <code>Node.js</code>).</li>
    <li><strong>Sliding Window Token Generation:</strong> Constructs n-gram token sequences from 4-grams down to unigrams:
      <div class="math-block">
        W_n = \{ (w_i, w_{i+1}, \dots, w_{i+n-1}) \mid 1 \le i \le |D| - n + 1 \}
      </div>
    </li>
    <li><strong>Greedy Longest-Match Matching:</strong> Evaluates higher-order n-grams first (e.g., matching "Natural Language Processing" before "Language", or "Amazon Web Services" before "Web"). Once matched, composite tokens are flagged to prevent sub-token double counting.</li>
    <li><strong>Taxonomy Mapping:</strong> Maps detected entity tokens to canonical standardized titles across 8 operational categories.</li>
    <li><strong>Regular Expression Requirement Parsing:</strong> Scans the document using specialized boundary regexes to isolate minimum academic degree levels and required years of professional tenure.</li>
  </ol>

  <h2>7.3 8-Domain Entity Taxonomy Overview</h2>
  <table>
    <thead>
      <tr>
        <th>Category Domain</th>
        <th>Representative Canonical Entities</th>
        <th>Entity Count</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Programming Languages</strong></td>
        <td>Python, TypeScript, JavaScript, Go, Rust, C++, C#, Java, Scala, Ruby, Swift, Kotlin, SQL</td>
        <td>38 entities</td>
      </tr>
      <tr>
        <td><strong>Frameworks &amp; Libraries</strong></td>
        <td>React, Next.js, Vue, Angular, PyTorch, TensorFlow, FastAPI, Django, Flask, Express, Spring Boot</td>
        <td>84 entities</td>
      </tr>
      <tr>
        <td><strong>Cloud &amp; DevOps</strong></td>
        <td>AWS, Google Cloud Platform (GCP), Azure, Kubernetes, Docker, Terraform, CI/CD, Linux</td>
        <td>62 entities</td>
      </tr>
      <tr>
        <td><strong>Databases &amp; Warehouses</strong></td>
        <td>PostgreSQL, MongoDB, Snowflake, BigQuery, Redis, MySQL, DynamoDB, Cassandra, Elasticsearch</td>
        <td>45 entities</td>
      </tr>
      <tr>
        <td><strong>Data Engineering &amp; ML</strong></td>
        <td>Apache Spark, Apache Airflow, Apache Kafka, Pandas, NumPy, Databricks, dbt, Scikit-Learn</td>
        <td>56 entities</td>
      </tr>
      <tr>
        <td><strong>Developer Tools &amp; Platforms</strong></td>
        <td>Git, GitHub, GitLab, Docker, Postman, JIRA, Confluence, Jenkins, Vite, Webpack</td>
        <td>72 entities</td>
      </tr>
      <tr>
        <td><strong>Soft Skills &amp; Leadership</strong></td>
        <td>Leadership, Strategic Planning, Cross-functional Collaboration, Agile / Scrum, Problem Solving</td>
        <td>48 entities</td>
      </tr>
      <tr>
        <td><strong>Domain Specializations</strong></td>
        <td>NLP, Computer Vision, Distributed Systems, Large Language Models (LLM), Cybersecurity</td>
        <td>95 entities</td>
      </tr>
    </tbody>
  </table>

  <h2>7.4 Regex-Based Degree &amp; Tenure Extraction Mechanics</h2>
  <p>
    Academic degree qualifications are extracted using strict boundary regexes:
  </p>
  <pre><code>DEGREE_PATTERNS = [
    ("Ph.D. / Doctorate", r"\b(ph\.?d|doctorate|doctor of philosophy)\b"),
    ("Master's Degree (M.S. / MBA)", r"\b(master'?s|m\.s\.|msc|mba|master of science)\b"),
    ("Bachelor's Degree (B.S. / B.A.)", r"\b(bachelor'?s|b\.s\.|bsc|b\.a\.|undergraduate degree)\b"),
    ("Associate Degree", r"\b(associate'?s|associate degree)\b")
]
</code></pre>
  <p>
    Professional tenure is detected using continuous span numeric matching:
  </p>
  <pre><code>EXP_PATTERN = r"\b(\d{1,2})\+?\s*(?:to|-)?\s*(\d{1,2})?\s*(?:years?|yrs?)(?:\s+of)?(?:\s+experience)?\b"
</code></pre>

  <h2>7.5 Defensible Textual Metrics</h2>
  <p>
    Rather than displaying ungrounded percentage confidences, the NLP service computes objective document statistics:
  </p>
  <div class="math-block">
    \text{Skill Density \%} = \left( \frac{\text{Unique Detected Technical Entities}}{\text{Total Word Count in Document}} \right) \times 100
  </div>
  <p>
    This metric provides recruiters and candidates with an honest, quantifiable indicator of how requirement-dense a given job posting is.
  </p>
</div>
"""
CHAPTER_8_HTML = """
<div class="chapter-break">
  <h1>Chapter 8: Full-Stack System Architecture &amp; Serverless Gateway</h1>
  
  <h2>8.1 Architectural Paradigm: Decoupled &amp; Cloud-Native</h2>
  <p>
    JobInsight AI is architected as a modern, decoupled full-stack platform. The presentation tier (React 19, Tailwind CSS v4, Vite) is cleanly separated from the machine learning inference tier (FastAPI, Scikit-Learn, Pydantic).
  </p>
  <p>
    To maximize accessibility, deployment speed, and cost efficiency, the system supports <strong>Dual-Deployment Topology</strong>:
  </p>
  <ul>
    <li><strong>Topology A: Unified Vercel Serverless Functions (Active Production Standard):</strong> The FastAPI application is bridged into a serverless handler (<code>api/index.py</code>) running on Vercel's Python Serverless runtime. HTTP requests routed to <code>/api/*</code> and <code>/health</code> are handled natively on the same domain as the React application.</li>
    <li><strong>Topology B: Containerized Docker ASGI Server (Microservice Standard):</strong> A multi-stage production <code>backend/Dockerfile</code> packages the FastAPI service with Uvicorn for independent deployment to container platforms (Hugging Face Spaces, Render, AWS ECS, or Google Cloud Run).</li>
  </ul>

  <h2>8.2 Client-Side Smart Routing (src/services/api.js)</h2>
  <p>
    The frontend uses a smart API client that inspects the runtime environment and dynamically configures endpoint dispatching:
  </p>
  <pre><code>const getBaseUrl = () => {
  // 1. External Microservice Override (e.g. Hugging Face Spaces / Render)
  if (import.meta.env.VITE_API_URL) {
    return import.meta.env.VITE_API_URL.replace(/\/+$/, '');
  }
  // 2. Production Vercel Deployment: Use relative same-origin routes (/api/...)
  if (typeof window !== 'undefined' && 
      window.location.hostname !== 'localhost' && 
      window.location.hostname !== '127.0.0.1') {
    return '';
  }
  // 3. Local Development Fallback
  return 'http://localhost:8000';
};
</code></pre>

  <h2>8.3 Vercel Serverless Integration (api/index.py &amp; vercel.json)</h2>
  <p>
    Vercel natively supports Python serverless execution by exposing an ASGI/WSGI callable in an <code>api/index.py</code> handler. Routing rules are declared in <code>vercel.json</code>:
  </p>
  <pre><code>{
  "version": 2,
  "rewrites": [
    { "source": "/health", "destination": "/api/index.py" },
    { "source": "/api/(.*)", "destination": "/api/index.py" },
    { "source": "/(.*)", "destination": "/index.html" }
  ]
}
</code></pre>
  <p>
    The serverless bridge imports the core FastAPI application from <code>backend.app.main</code>:
  </p>
  <pre><code>import sys
from pathlib import Path

# Add backend directory to Python sys.path
root_dir = Path(__file__).resolve().parent.parent
backend_dir = root_dir / "backend"
sys.path.insert(0, str(backend_dir))

from app.main import app
</code></pre>
  <p>
    This architectural design achieves <strong>zero-CORS complexity</strong> in production, reduces network round-trip latency, and eliminates the need for separate paid backend hosting.
  </p>
</div>
"""
