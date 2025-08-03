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
- **File Storage**: Google Cloud Storage for secure CSV uploads
- **User Data**: PostgreSQL via Supabase/Google Cloud SQL
- **Authentication**: Supabase handles user auth out of the box

### Deployment
- **Frontend**: Vercel (Next.js creators)
- **Backend**: Google Cloud Functions (serverless, cost-effective)

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

## Deployment Status

### ✅ Sprint 0: Foundation Complete
- [x] GitHub repository setup
- [x] Next.js frontend scaffolded
- [x] FastAPI backend scaffolded
- [x] GitHub Actions CI/CD pipeline
- [x] Google Cloud Functions configuration
- [x] Vercel deployment setup
- [x] **Frontend deployed to Vercel** ✅
- [x] **GitHub Actions workflow configured** ✅

### 🔄 Current Status
- [x] Vercel deployment successful
- [x] Frontend accessible at Vercel URL
- [ ] Backend deployment to Google Cloud Functions
- [ ] Connect frontend to backend API
- [ ] Sprint 1: Core Features

### 🚀 Live Application
- **Frontend**: Deployed on Vercel (URL available in Vercel dashboard)
- **Backend**: Ready for Google Cloud Functions deployment
- **CI/CD**: GitHub Actions workflow active

## Why Google Cloud Functions?

### Advantages over AWS Lambda:
- **Simpler pricing**: Pay only for actual compute time
- **Better cold start performance**: Generally faster than Lambda
- **Native Python support**: Excellent for your FastAPI backend
- **Easy integration**: Works seamlessly with other Google services
- **Free tier**: 2 million invocations per month free
- **Better documentation**: More straightforward setup process

## Next Steps
1. ✅ **Frontend Deployment** - Complete
2. 🔄 **Backend Deployment** - Set up Google Cloud Functions
3. 🔄 **API Integration** - Connect frontend to backend
4. 📋 **Sprint 1** - Build core features (CSV upload, analysis, AI integration)

## Setup Guides
- [Vercel Setup Guide](VERCEL_SETUP_GUIDE.md) - Frontend deployment
- [Google Cloud Setup Guide](GOOGLE_CLOUD_SETUP.md) - Backend deployment 