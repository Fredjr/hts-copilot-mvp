# HTS Co-pilot Project Context

## MVP Mission: The "HTS Co-pilot"

### Job-to-be-Done
For a computational biologist at a London biotech startup who has just finished a 384-well plate experiment, our product will take their raw CSV data and, in under two minutes, deliver a secure, interactive report that identifies the most promising "hits," flags common errors like edge effects, and provides a concise, human-readable summary of the experiment's outcome.

### Value Proposition
We save them a full day of tedious, error-prone work in Excel or custom Python scripts, allowing them to make a "go/no-go" decision on their next steps immediately. This is our Minimum Wowable Product (MWP).

## Technical Architecture: A Simple Blueprint

### 1. The Frontend: The "Show Home"
**Technology Choice**: React (using the Next.js framework)

**Why This Choice**:
- It's the Industry Standard: React is the most popular choice for building modern web applications
- Speed & Performance: Next.js helps build incredibly fast and responsive user interfaces
- Rapid Development: Component-based like Lego bricks, building reusable pieces dramatically speeds up development

### 2. The Backend: The "Engine Room"
**Technology Choice**: Python (using the FastAPI framework)

**Why This Choice**:
- The Language of Science: Python is the undisputed king for data science and AI
- High Performance: FastAPI is modern, fast, and efficient
- Essential Libraries: Pandas for data manipulation, NumPy for numerical operations, SciPy for statistics

### 3. The AI Core: Our "Expert Consultant"
**LLM Choice**: Anthropic's Claude Sonnet 4 API
**Orchestration Framework**: LangChain

**How We'll Use Them (Critical Approach)**:
1. **Step 1 (Python does the math)**: Python backend uses Pandas and SciPy to ingest CSV, normalize data, calculate Z-scores, and identify statistical "hits" and errors
2. **Step 2 (The Agent provides the insight)**: LangChain orchestrates the expert interpretation
3. **Step 3 (Claude Sonnet 4 writes the summary)**: Claude acts as expert computational biologist to write concise, human-readable summaries

### 4. Database & Storage: The "Secure Vault"
- **For File Storage**: AWS S3 (Simple Storage Service) - gold standard for file storage
- **For User Data**: PostgreSQL (via managed service like Supabase or AWS RDS)
- **Authentication**: Supabase handles user authentication out of the box

### 5. Cloud & Deployment: Our "Foundation & Construction Crew"
- **Frontend Deployment**: Vercel (made by Next.js creators)
- **Backend Deployment**: AWS Lambda (serverless, cost-effective)

## Summary of MVP Tech Stack
- **Frontend**: React (Next.js)
- **Backend**: Python (FastAPI)
- **AI Core**: Claude Sonnet 4 API + LangChain
- **Database**: PostgreSQL (via Supabase/AWS)
- **Storage**: AWS S3
- **Deployment**: Vercel + AWS Lambda

## Key Technical Decisions
1. **Python handles raw math, AI provides interpretation** - This is the core architectural decision that ensures reliability and speed
2. **Serverless deployment** - Cost-effective for MVP with automatic scaling
3. **Managed services** - Focus energy on unique features rather than infrastructure
4. **Modern, robust, scalable stack** - Designed for small, focused team to build and launch quickly

## Target User Profile
- **Role**: Computational biologist
- **Company**: London biotech startup
- **Pain Point**: Manual Excel/Python analysis of 384-well plate experiments
- **Goal**: Quick, reliable analysis with immediate decision-making capability 