# HTS Co-pilot MVP

## Mission Statement
The "HTS Co-pilot" is designed for computational biologists at London biotech startups who need to analyze 384-well plate experiments. Our product takes raw CSV data and delivers a secure, interactive report in under two minutes that identifies promising "hits," flags common errors like edge effects, and provides a concise, human-readable summary.

## Value Proposition
We save computational biologists a full day of tedious, error-prone work in Excel or custom Python scripts, allowing them to make immediate "go/no-go" decisions on their next steps.

## Technical Architecture

### Frontend: React (Next.js)
- Industry standard with large talent pool in London
- Fast, responsive user interfaces
- Component-based rapid development

### Backend: Python (FastAPI)
- Language of choice for data science and AI
- High performance with modern framework
- Essential libraries: Pandas, NumPy, SciPy

### AI Core: Claude Sonnet 4 API + LangChain
- Python handles raw math and statistical analysis
- LangChain orchestrates the AI workflow
- Claude Sonnet 4 provides expert interpretation and human-readable summaries

### Database & Storage
- **File Storage**: AWS S3 for secure CSV uploads
- **User Data**: PostgreSQL via Supabase/AWS RDS
- **Authentication**: Supabase handles user auth out of the box

### Deployment
- **Frontend**: Vercel (Next.js creators)
- **Backend**: AWS Lambda (serverless, cost-effective)

## Project Structure
```
hts-copilot/
├── frontend/          # React (Next.js) application
├── backend/           # Python (FastAPI) API
├── ai-core/          # LangChain + Claude integration
├── docs/             # Documentation
└── infrastructure/   # Deployment configurations
```

## MVP Features
1. CSV upload and secure storage
2. Statistical analysis (Z-scores, hit identification)
3. Error detection (edge effects, signal drop-offs)
4. AI-powered experiment summary
5. Interactive report generation
6. User authentication and data management 