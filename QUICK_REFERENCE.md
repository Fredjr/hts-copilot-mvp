# HTS Co-pilot Quick Reference

## 🎯 Mission
Transform 384-well plate experiment analysis from a day-long Excel process into a 2-minute automated report with AI-powered insights.

## 🏗️ Tech Stack
- **Frontend**: React + Next.js (Vercel deployment)
- **Backend**: Python + FastAPI (AWS Lambda)
- **AI**: Claude Sonnet 4 + LangChain
- **Database**: PostgreSQL (Supabase)
- **Storage**: AWS S3
- **Auth**: Supabase Auth

## 🔄 Core Workflow
1. User uploads CSV → S3 storage
2. Python analyzes data (Z-scores, hits, errors)
3. Results sent to Claude via LangChain
4. AI generates expert summary
5. Interactive report delivered

## 📊 Key Features
- CSV upload & secure storage
- Statistical analysis (Z-scores, hit identification)
- Error detection (edge effects, signal drop-offs)
- AI-powered experiment summaries
- Interactive report generation
- User authentication & experiment history

## ⚡ Performance Target
**< 2 minutes end-to-end processing**

## 🎯 Target User
Computational biologist at London biotech startup

## 💡 Value Proposition
Save a full day of Excel/Python work → immediate "go/no-go" decisions

## 📁 Project Structure
```
hts-copilot/
├── frontend/          # Next.js app
├── backend/           # FastAPI API
├── ai-core/          # LangChain + Claude
├── docs/             # Documentation
└── infrastructure/   # Deployment configs
```

## 🔑 Key Technical Decision
**Python handles math, AI provides interpretation** - Ensures reliability and speed

## 📈 Success Metrics
- Technical: < 2 minute processing
- User: Intuitive interface
- Business: Clear decision support
- Quality: Reliable hit identification 