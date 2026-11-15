import re
from typing import Dict, List, Any, Optional

class JobInsightNLPExtractor:
    """
    Production-grade NLP Entity and Skill Extraction engine for job descriptions.
    Performs case-insensitive tokenization, n-gram phrase matching, and credential extraction.
    """

    def __init__(self):
        # Comprehensive taxonomy of industry skills, tools, and platforms
        self.tech_skills_map = {
            # Programming Languages
            "python": "Python", "javascript": "JavaScript", "typescript": "TypeScript",
            "java": "Java", "c++": "C++", "c#": "C#", "golang": "Go", "go": "Go",
            "rust": "Rust", "ruby": "Ruby", "php": "PHP", "swift": "Swift",
            "kotlin": "Kotlin", "scala": "Scala", "r": "R", "sql": "SQL",
            "bash": "Bash", "powershell": "PowerShell", "html": "HTML5", "css": "CSS3",
            
            # Frameworks & Web
            "react": "React", "react.js": "React", "react native": "React Native",
            "next.js": "Next.js", "nextjs": "Next.js", "angular": "Angular",
            "vue": "Vue.js", "vue.js": "Vue.js", "node.js": "Node.js", "nodejs": "Node.js",
            "express": "Express.js", "django": "Django", "flask": "Flask",
            "fastapi": "FastAPI", "spring": "Spring", "spring boot": "Spring Boot",
            "asp.net": "ASP.NET", ".net core": ".NET Core", "tailwind": "Tailwind CSS",
            "tailwind css": "Tailwind CSS", "bootstrap": "Bootstrap", "graphql": "GraphQL",
            "rest api": "REST APIs", "restful api": "RESTful APIs", "microservices": "Microservices",

            # Cloud & DevOps
            "aws": "Amazon Web Services (AWS)", "amazon web services": "AWS",
            "ec2": "AWS EC2", "s3": "AWS S3", "lambda": "AWS Lambda",
            "azure": "Microsoft Azure", "gcp": "Google Cloud Platform (GCP)",
            "google cloud": "Google Cloud", "docker": "Docker", "kubernetes": "Kubernetes",
            "k8s": "Kubernetes", "terraform": "Terraform", "ansible": "Ansible",
            "helm": "Helm", "ci/cd": "CI/CD", "ci cd": "CI/CD", "github actions": "GitHub Actions",
            "jenkins": "Jenkins", "gitlab": "GitLab CI", "linux": "Linux",
            "nginx": "Nginx", "distributed systems": "Distributed Systems",

            # Data, AI & Machine Learning
            "machine learning": "Machine Learning", "deep learning": "Deep Learning",
            "pytorch": "PyTorch", "tensorflow": "TensorFlow", "keras": "Keras",
            "scikit-learn": "Scikit-learn", "sklearn": "Scikit-learn",
            "pandas": "Pandas", "numpy": "NumPy", "scipy": "SciPy",
            "llm": "Large Language Models (LLMs)", "llms": "Large Language Models",
            "large language models": "Large Language Models", "rag": "Retrieval-Augmented Generation (RAG)",
            "nlp": "Natural Language Processing (NLP)", "computer vision": "Computer Vision",
            "hugging face": "Hugging Face", "transformers": "Transformers",
            "langchain": "LangChain", "llamaindex": "LlamaIndex",
            "vector database": "Vector Databases", "pinecone": "Pinecone",
            "weaviate": "Weaviate", "chromadb": "ChromaDB", "milvus": "Milvus",

            # Databases & Big Data
            "postgresql": "PostgreSQL", "postgres": "PostgreSQL", "mysql": "MySQL",
            "mongodb": "MongoDB", "redis": "Redis", "elasticsearch": "Elasticsearch",
            "dynamodb": "DynamoDB", "cassandra": "Apache Cassandra", "snowflake": "Snowflake",
            "bigquery": "Google BigQuery", "apache spark": "Apache Spark", "spark": "Apache Spark",
            "kafka": "Apache Kafka", "hadoop": "Hadoop", "databricks": "Databricks",
            "dbt": "dbt", "airflow": "Apache Airflow",

            # Architecture & Security
            "system design": "System Design", "event-driven architecture": "Event-Driven Architecture",
            "zero trust": "Zero Trust Security", "oauth": "OAuth 2.0", "jwt": "JWT",
            "penetration testing": "Penetration Testing", "cybersecurity": "Cybersecurity",
            "encryption": "Encryption", "soc2": "SOC 2 Compliance"
        }

        self.tools_platforms_map = {
            "git": "Git", "github": "GitHub", "jira": "Jira", "confluence": "Confluence",
            "figma": "Figma", "salesforce": "Salesforce", "hubspot": "HubSpot",
            "tableau": "Tableau", "power bi": "Power BI", "powerbi": "Power BI",
            "postman": "Postman", "excel": "Microsoft Excel", "sap": "SAP",
            "servicenow": "ServiceNow", "datadog": "Datadog", "splunk": "Splunk",
            "new relic": "New Relic", "prometheus": "Prometheus", "grafana": "Grafana"
        }

        self.soft_skills_map = {
            "agile": "Agile Methodology", "scrum": "Scrum Framework",
            "leadership": "Technical Leadership", "mentorship": "Team Mentorship",
            "mentoring": "Mentoring", "cross-functional": "Cross-Functional Collaboration",
            "stakeholder management": "Stakeholder Management",
            "problem-solving": "Analytical Problem Solving", "problem solving": "Problem Solving",
            "communication": "Effective Communication", "teamwork": "Collaborative Teamwork",
            "project management": "Project Management", "critical thinking": "Critical Thinking",
            "strategic thinking": "Strategic Planning", "adaptability": "Adaptability"
        }

        self.domain_skills_map = {
            "financial modeling": "Financial Modeling", "p&l": "P&L Management",
            "gaap": "GAAP Accounting", "budgeting": "Budget Oversight",
            "hipaa": "HIPAA Compliance", "clinical governance": "Clinical Governance",
            "ehr": "Electronic Health Records (EHR)", "emr": "EMR Systems",
            "telehealth": "Telehealth", "cbt": "Cognitive Behavioral Therapy (CBT)",
            "seo": "Search Engine Optimization (SEO)", "sem": "Search Engine Marketing (SEM)",
            "a/b testing": "A/B Testing", "crm": "Customer Relationship Management (CRM)",
            "cad": "Computer-Aided Design (CAD)", "supply chain": "Supply Chain Management"
        }

    def _extract_phrases(self, text: str, phrase_dict: Dict[str, str]) -> List[str]:
        """
        Extract phrases using word-boundary regex to prevent partial match false positives.
        Sorted by phrase length descending to match longest phrases first.
        """
        found = set()
        for phrase, canonical_name in sorted(phrase_dict.items(), key=lambda x: len(x[0]), reverse=True):
            # Escape regex special characters in phrase
            pattern = r'\b' + re.escape(phrase) + r'\b'
            if re.search(pattern, text, re.IGNORECASE):
                found.add(canonical_name)
        return sorted(list(found))

    def _extract_experience(self, text: str) -> Optional[str]:
        """
        Extract experience duration requirements using robust regex patterns.
        """
        # Matches patterns like: '5+ years', '3-5 years', 'at least 4 years of experience', etc.
        patterns = [
            r'(\d+\s*[-–to]\s*\d+)\+?\s*years?(?:\s+of)?(?:\s+relevant|\s+industry|\s+professional)?\s*(?:experience)?',
            r'(\d+)\+?\s*years?(?:\s+of)?(?:\s+relevant|\s+industry|\s+professional)?\s*(?:experience)?',
            r'(?:minimum|at least)\s*(\d+)\s*years?'
        ]
        for pat in patterns:
            match = re.search(pat, text, re.IGNORECASE)
            if match:
                val = match.group(1).strip()
                return f"{val} Years Required"
        return "Not specified in description"

    def _extract_education(self, text: str) -> Optional[str]:
        """
        Extract degree and credential requirements.
        """
        degrees = []
        if re.search(r'\b(ph\.?d|doctorate)\b', text, re.IGNORECASE):
            degrees.append("Ph.D. / Doctorate")
        if re.search(r'\b(master\'?s?|ms|m\.s\.|mba|msc)\b', text, re.IGNORECASE):
            degrees.append("Master's Degree (M.S. / MBA)")
        if re.search(r'\b(bachelor\'?s?|bs|b\.s\.|ba|b\.a\.|btech|undergraduate)\b', text, re.IGNORECASE):
            degrees.append("Bachelor's Degree (B.S. / B.A.)")
        if re.search(r'\b(associate\'?s?|diploma)\b', text, re.IGNORECASE):
            degrees.append("Associate's Degree")

        if degrees:
            return " / ".join(degrees)
        return "Degree preferred or equivalent professional experience"

    def _infer_category(self, tech_count: int, tools_count: int, domain_count: int, text: str) -> str:
        """
        Infers the primary job category based on token density.
        """
        lower = text.lower()
        if "nurse" in lower or "clinical" in lower or "medical" in lower or "therapist" in lower:
            return "Healthcare & Life Sciences"
        elif "accountant" in lower or "financial" in lower or "audit" in lower or "p&l" in lower:
            return "Finance & Accounting"
        elif "marketing" in lower or "sales" in lower or "seo" in lower or "campaign" in lower:
            return "Sales & Marketing"
        elif tech_count > 0 or tools_count > 0:
            return "Technology & Software Engineering"
        elif "manager" in lower or "operations" in lower:
            return "Management & Operations"
        return "General Professional"

    def extract(self, description: str) -> Dict[str, Any]:
        """
        Main execution endpoint. Parses arbitrary text and returns structured extraction results.
        """
        if not description or not description.strip():
            return {
                "total_detected": 0,
                "technical_skills": [],
                "soft_skills": [],
                "tools_and_platforms": [],
                "domain_skills": [],
                "experience_required": "No description provided",
                "degree_required": "No description provided",
                "inferred_category": "Unknown",
                "token_statistics": {
                    "word_count": 0,
                    "character_count": 0,
                    "unique_words": 0,
                    "skill_density_pct": 0.0
                }
            }

        cleaned_text = description.strip()
        words = re.findall(r'\b\w+\b', cleaned_text)
        word_count = len(words)
        unique_words = len(set(w.lower() for w in words))

        # Extract entities across categories
        tech_skills = self._extract_phrases(cleaned_text, self.tech_skills_map)
        tools = self._extract_phrases(cleaned_text, self.tools_platforms_map)
        soft_skills = self._extract_phrases(cleaned_text, self.soft_skills_map)
        domain_skills = self._extract_phrases(cleaned_text, self.domain_skills_map)

        exp = self._extract_experience(cleaned_text)
        edu = self._extract_education(cleaned_text)

        total_detected = len(tech_skills) + len(tools) + len(soft_skills) + len(domain_skills)
        skill_density = round((total_detected / max(1, word_count)) * 100, 2)
        category = self._infer_category(len(tech_skills), len(tools), len(domain_skills), cleaned_text)

        return {
            "total_detected": total_detected,
            "technical_skills": tech_skills,
            "soft_skills": soft_skills,
            "tools_and_platforms": tools,
            "domain_skills": domain_skills,
            "experience_required": exp,
            "degree_required": edu,
            "inferred_category": category,
            "token_statistics": {
                "word_count": word_count,
                "character_count": len(cleaned_text),
                "unique_words": unique_words,
                "skill_density_pct": skill_density
            }
        }

# Global singleton instance
nlp_extractor = JobInsightNLPExtractor()
