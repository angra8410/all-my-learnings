# Data-AI-Course: AI-Powered Workflows, Prompt Tools & Automation Models

**16-Week Project-First Course**

A comprehensive, hands-on bootcamp that teaches how to build AI-powered workflows, prompt tools, and automation models for real business cases (finance, sports analytics, e-commerce, enterprise CRM).

## 🎯 Course Overview

This course emphasizes **pragmatic, production-ready skills** through:
- 🔨 80% hands-on practice, 20% theory (Pareto principle)
- 🚀 4 real-world capstone projects
- 💼 Business-focused use cases
- 🔒 Security and ethics-first approach
- 📊 Reproducible artifacts and templates

## 👥 Target Audience

Engineers, data scientists, and product managers who want to:
- Build and deploy LLM-powered applications
- Integrate AI into existing systems
- Create production-grade AI workflows
- Understand AI security and ethics

## 📋 Prerequisites

- **Python**: Intermediate level (functions, classes, imports)
- **ML/DS**: Basic concepts (models, training, evaluation)
- **APIs**: Familiarity with REST APIs
- **Git**: Version control basics
- **Docker**: Basic knowledge (recommended)
- **Cloud**: Basic familiarity (recommended)

## 🗓️ Course Structure (16 Weeks)

### Foundations (Weeks 0-4)
- **Week 00**: Setup & Tools — Environment, APIs, reproducibility
- **Week 01**: Prompt Engineering Fundamentals — Patterns, templates, debugging
- **Week 02**: Solving Natural Language Problems — RAG, semantic search, vector DBs
- **Week 03**: Building Generative AI Workflows — Chaining, streaming, multimodal
- **Week 04**: Python for AI — Async, batching, SDK patterns

### Advanced Techniques (Weeks 5-8)
- **Week 05**: Prompt Tools & Tooling — LangChain agents, tool design
- **Week 06**: Agentic AI Development — Agent patterns, memory, planning
- **Week 07**: Fine-Tuning & Instruction-Tuning — LoRA, PEFT, evaluation
- **Week 08**: Evaluating Generative AI Solutions — Metrics, hallucination detection

### Production & Operations (Weeks 9-13)
- **Week 09**: Testing & Monitoring — Unit tests, integration, data quality
- **Week 10**: Secure AI Development — Threat models, prompt injection, auditing
- **Week 11**: Ethical AI Practices — Fairness, bias, transparency, privacy
- **Week 12**: Automation Models for Business — Pipelines, idempotency
- **Week 13**: Orchestration & Production — Airflow, Kubernetes, CI/CD

### Real-World Projects (Weeks 14-16)
- **Week 14**: Case Study — FINANCE (Loan Default Prediction)
- **Week 15**: Case Study — SPORTS (NFL Draft Sentiment Analysis)
- **Week 16**: Case Studies — E-COMMERCE + ENTERPRISE + Capstone Delivery

## 🎓 Learning Outcomes

By completing this course, you will be able to:

1. ✅ Design and implement end-to-end generative AI workflows
2. ✅ Master prompt engineering patterns and debugging
3. ✅ Build, evaluate, and fine-tune LLMs for domain tasks
4. ✅ Integrate models into production orchestration
5. ✅ Apply ethical frameworks and security best practices
6. ✅ Produce reproducible artifacts (notebooks, CI, IaC)

## 🏗️ Capstone Projects

### 1. FINANCE: Loan Default Prediction
**Deliverables:**
- ETL pipeline for loan dataset ingestion
- Feature store design
- LLM/ML ensemble for risk narrative generation
- Deployable API endpoint
- Evaluation report with fairness audit

### 2. SPORTS: NFL Draft Sentiment Analysis
**Deliverables:**
- Social media scraper (Twitter/Reddit)
- Streaming or batch ingestion pipeline
- Sentiment analysis model
- Interactive dashboard
- Insights and evaluation report

### 3. E-COMMERCE: Order Management Chatbot
**Deliverables:**
- Conversational agent with tool integration
- RAG system for order policies
- Order lookup, cancel, and update functionality
- Comprehensive test suite
- Security review documentation

### 4. ENTERPRISE: Salesforce CRM Q&A Assistant
**Deliverables:**
- Dataset extraction from Salesforce
- RAG + LLM Q&A system
- Access control implementation
- Deployment guide for Salesforce integration
- Webhook/Connected App setup

## 🚀 Getting Started

### 1. Clone Repository
```bash
git clone <repository-url>
cd Data-AI-Course
```

### 2. Set Up Environment
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure API Keys
```bash
# Copy template
cp .env.example .env

# Edit .env and add your API keys:
# - OPENAI_API_KEY
# - ANTHROPIC_API_KEY
# - Other required keys
```

### 4. Verify Setup
```bash
cd week-00-setup-tools/examples
python test_setup.py
```

### 5. Start Learning!
Begin with **Week 00: Setup & Tools** and progress sequentially.

## 📂 Repository Structure

```
Data-AI-Course/
├── week-00-setup-tools/
│   ├── README.md
│   ├── actividad-interactiva.md
│   ├── project-steps.md
│   ├── progreso.md
│   ├── retroalimentacion.md
│   ├── resources.md
│   └── examples/
├── week-01-prompt-engineering/
│   └── ...
├── week-02-natural-language-problems/
│   └── ...
├── ...
├── week-16-ecommerce-enterprise-capstone/
│   └── ...
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

### Each Week Contains:
- **README.md** — Learning objectives, theory, concepts
- **actividad-interactiva.md** — 4-8 hands-on exercises with verification
- **project-steps.md** — Incremental capstone project tasks
- **progreso.md** — Personal progress tracking
- **retroalimentacion.md** — Evaluation rubric
- **resources.md** — Curated links, libraries, configs
- **examples/** — Runnable code examples

## 🎯 Grading & Evaluation

### Weekly Deliverables (60%)
- **Correctness**: 60%
- **Reproducibility**: 20%
- **Documentation**: 20%

### Capstone Project (40%)
- **Functionality & Reproducibility**: 40%
- **Modeling & Prompt Quality**: 25%
- **Testing & Monitoring**: 15%
- **Ethics & Security**: 10%
- **Documentation & Demo**: 10%

**Minimum Passing Score**: 70%

## 🔒 Security & Ethics Guidelines

### Mandatory Practices:
- ❌ **Never** commit real credentials to Git
- ✅ **Always** use placeholders: `<API_KEY>`, `<DB_CONN>`, `<TENANT_ID>`
- ✅ **Implement** input sanitization for prompts
- ✅ **Apply** principle of least privilege
- ✅ **Include** bias and privacy checks in all projects
- ✅ **Document** security considerations

## 📚 Recommended Resources

### Books
- "Designing Machine Learning Systems" by Chip Huyen
- "Building LLM Applications" by Valentina Alto
- "Prompt Engineering Guide" (promptingguide.ai)

### Online Courses
- DeepLearning.AI - ChatGPT Prompt Engineering
- Full Stack Deep Learning
- Fast.ai Practical Deep Learning

### Communities
- r/MachineLearning
- LangChain Discord
- OpenAI Community Forum

## 💡 Study Tips

1. **Pareto Principle**: Focus on 20% of concepts that deliver 80% of value
2. **Hands-On First**: Build before optimizing
3. **Incremental Progress**: Complete one week before moving to the next
4. **Document Everything**: Keep notes and code examples
5. **Join Communities**: Learn from others, share your work
6. **Security First**: Never compromise on security practices

## 🤝 Contributing

This course is designed to be:
- **Reproducible** — All examples should run with minimal setup
- **Practical** — Focus on real-world applications
- **Secure** — Never include real credentials
- **Ethical** — Consider bias, fairness, and privacy

## 📞 Getting Help

- **Review Materials** — Check README and resources for each week
- **Run Examples** — All code should work out of the box
- **Check Troubleshooting** — Common issues documented in each week
- **Community Forums** — Ask in relevant communities

## 📄 License

This course content is provided for educational purposes.

## 🎓 Course Completion

Upon completing all 16 weeks and capstone projects, you will have:
- ✅ Portfolio of 4 production-ready AI applications
- ✅ Comprehensive understanding of LLM workflows
- ✅ Skills to build and deploy AI systems
- ✅ Knowledge of AI security and ethics
- ✅ Experience with modern AI tools and frameworks

---

**Ready to start?** Head to [Week 00: Setup & Tools](week-00-setup-tools/) to begin your AI journey! 🚀

**Questions?** Check the resources or reach out to the community.

**Good luck!** 🎯
