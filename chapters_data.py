# chapters_data.py
# Contains the extensive text, tables, formulas, and SVG definitions for the 30-page JobInsight Monograph.

COVER_HTML = """
<div class="cover-page">
  <div class="cover-top">
    <div class="cover-badge">ENTERPRISE TECHNICAL SPECIFICATION &bull; PRODUCTION MONOGRAPH</div>
    <div class="cover-title">JobInsight AI: Architectural Blueprint &amp; Technical Monograph</div>
    <div class="cover-subtitle">
      A Production-Grade Macroeconomic Intelligence Platform, Tabular Gradient Boosting Compensation Regressor, and Dynamic N-Gram NLP Information Extraction Engine Built on 123,849 LinkedIn Job Postings.
    </div>

    <div class="cover-abstract">
      <strong>Monograph Abstract:</strong> This technical monograph details the end-to-end design, mathematical formulation, empirical benchmarking, and cloud-native deployment of <strong>JobInsight AI</strong>. Addressing pervasive opacity in labor market compensation and superficial heuristic estimations, JobInsight couples macroeconomic data engineering on 123,849 North American job postings with a verified Scikit-Learn <code>HistGradientBoostingRegressor</code> inference pipeline (35,237 disclosed salary records, hold-out $R^2 = 0.3454$, $\text{MAE} = \$30,482$) and a 500+ entity multi-word n-gram natural language processing parser. The system is deployed as a unified full-stack architecture leveraging Vite, React 19, Tailwind CSS v4, FastAPI, and Vercel Serverless Functions, providing high-concurrency, zero-CORS inference with zero external cloud dependencies.
    </div>
  </div>

  <div>
    <div class="cover-grid">
      <div class="cover-card">
        <div class="cover-card-label">Production Web Application</div>
        <div class="cover-card-value"><a href="https://jobinsight-peach.vercel.app/" style="color:#38bdf8;">jobinsight-peach.vercel.app</a></div>
      </div>
      <div class="cover-card">
        <div class="cover-card-label">Source Code Repository</div>
        <div class="cover-card-value"><a href="https://github.com/UtsavChoudhary25/Jobinsight" style="color:#38bdf8;">github.com/.../Jobinsight</a></div>
      </div>
      <div class="cover-card">
        <div class="cover-card-label">Primary Raw Dataset</div>
        <div class="cover-card-value">123,849 Postings (24,428 Orgs)</div>
      </div>
      <div class="cover-card">
        <div class="cover-card-label">Selected ML Algorithm</div>
        <div class="cover-card-value">HistGradientBoosting (338 KB)</div>
      </div>
      <div class="cover-card">
        <div class="cover-card-label">Test Evaluation Metrics</div>
        <div class="cover-card-value">MAE: $30,482 | R²: 0.3454</div>
      </div>
      <div class="cover-card">
        <div class="cover-card-label">NLP Entity Taxonomy</div>
        <div class="cover-card-value">500+ Entities (8 Categories)</div>
      </div>
    </div>
  </div>

  <div class="cover-footer">
    <div><strong>Author / Lead Architect:</strong> Utsav Choudhary &bull; Machine Learning &amp; Full-Stack Engineering</div>
    <div><strong>Document Edition:</strong> 2.0 (Production Verified) &bull; A4 Technical Monograph</div>
  </div>
</div>
"""

TOC_HTML = """
<div class="chapter-break">
  <h1>Table of Contents &amp; Document Guide</h1>
  <p>This monograph serves as the authoritative technical reference for the JobInsight AI platform, encompassing data preprocessing, statistical benchmarking, natural language processing, frontend systems engineering, and serverless cloud deployment.</p>

  <div style="margin-top: 24px;">
    <div class="toc-item"><span class="toc-title">1. Executive Summary &amp; Project Genesis</span><span class="toc-dots"></span><span class="toc-page">Chapter 1</span></div>
    <div class="toc-item"><span class="toc-title">2. Macroeconomic Dataset Provenance &amp; Raw Ingestion</span><span class="toc-dots"></span><span class="toc-page">Chapter 2</span></div>
    <div class="toc-item"><span class="toc-title">3. End-to-End Data Preprocessing &amp; Cleaning Protocol</span><span class="toc-dots"></span><span class="toc-page">Chapter 3</span></div>
    <div class="toc-item"><span class="toc-title">4. Exploratory Data Analysis &amp; Macroeconomic Labor Insights</span><span class="toc-dots"></span><span class="toc-page">Chapter 4</span></div>
    <div class="toc-item"><span class="toc-title">5. Machine Learning Architecture: Tabular Salary Regression</span><span class="toc-dots"></span><span class="toc-page">Chapter 5</span></div>
    <div class="toc-item"><span class="toc-title">6. The 4-Model Comparative Benchmark Suite &amp; Error Analysis</span><span class="toc-dots"></span><span class="toc-page">Chapter 6</span></div>
    <div class="toc-item"><span class="toc-title">7. Natural Language Processing Entity &amp; Requirement Extraction</span><span class="toc-dots"></span><span class="toc-page">Chapter 7</span></div>
    <div class="toc-item"><span class="toc-title">8. Full-Stack System Architecture &amp; Serverless Gateway</span><span class="toc-dots"></span><span class="toc-page">Chapter 8</span></div>
    <div class="toc-item"><span class="toc-title">9. REST API Specification &amp; Live Production Telemetry</span><span class="toc-dots"></span><span class="toc-page">Chapter 9</span></div>
    <div class="toc-item"><span class="toc-title">10. Dashboard UI/UX Design System &amp; Analytics Modules</span><span class="toc-dots"></span><span class="toc-page">Chapter 10</span></div>
    <div class="toc-item"><span class="toc-title">11. Quality Assurance, Automated Testing &amp; Security Audit</span><span class="toc-dots"></span><span class="toc-page">Chapter 11</span></div>
    <div class="toc-item"><span class="toc-title">12. Strategic Recommendations, Future Roadmap &amp; Conclusion</span><span class="toc-dots"></span><span class="toc-page">Chapter 12</span></div>
    <div class="toc-item"><span class="toc-title">Appendix A: Curated 500+ Entity Technical Skill Taxonomy</span><span class="toc-dots"></span><span class="toc-page">Appendix A</span></div>
    <div class="toc-item"><span class="toc-title">Appendix B: Scikit-Learn Model Preprocessing Pipeline Specification</span><span class="toc-dots"></span><span class="toc-page">Appendix B</span></div>
    <div class="toc-item"><span class="toc-title">Appendix C: Complete Feature Dictionary &amp; Schema Definitions</span><span class="toc-dots"></span><span class="toc-page">Appendix C</span></div>
  </div>

  <div class="callout" style="margin-top: 30px;">
    <div class="callout-title">Methodological Standard of Reproducibility</div>
    All statistical benchmarks, mathematical equations, and operational procedures detailed in this monograph are derived from real execution runs against the primary LinkedIn job postings dataset. All software components are operational on the public production website at <code>https://jobinsight-peach.vercel.app/</code>.
  </div>
</div>
"""
