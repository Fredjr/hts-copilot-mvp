# Sprint 0: Foundation Setup Guide

## Overview
This guide covers the complete setup of the HTS Co-pilot infrastructure and deployment pipeline.

## Prerequisites
- GitHub account
- AWS account
- Vercel account
- Node.js 18+ installed
- Python 3.11+ installed

## Step 0.1: Cloud & Code Setup

### 1. Create GitHub Repository
```bash
# Repository should be private for security
# Name: hts-copilot
# Description: HTS Co-pilot - High Throughput Screening Analysis Platform
```

### 2. AWS Account Setup
1. Create AWS account if you don't have one
2. Create IAM user with programmatic access
3. Attach policies:
   - `AWSLambda_FullAccess`
   - `AmazonS3FullAccess`
   - `AmazonAPIGatewayAdministrator`
   - `CloudWatchLogsFullAccess`

### 3. Vercel Account Setup
1. Sign up at vercel.com
2. Connect your GitHub account
3. Create a new project (will be done in Step 0.3)

## Step 0.2: Project Scaffolding ✅

### Frontend (Next.js)
- ✅ Created with TypeScript, Tailwind CSS, ESLint
- ✅ App Router enabled
- ✅ Source directory structure
- ✅ Import aliases configured

### Backend (FastAPI)
- ✅ Basic FastAPI application
- ✅ Health check endpoints
- ✅ CORS configuration
- ✅ Requirements.txt with all dependencies

## Step 0.3: Deployment Pipeline Setup

### GitHub Secrets Required
Add these secrets to your GitHub repository:

#### AWS Secrets
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION`

#### Vercel Secrets
- `VERCEL_TOKEN`
- `VERCEL_ORG_ID`
- `VERCEL_PROJECT_ID`

### Environment Variables

#### Backend (.env)
```bash
# Copy env.example to .env and fill in your values
cp backend/env.example backend/.env
```

#### Frontend (.env.local)
```bash
# Create .env.local in frontend directory
NEXT_PUBLIC_API_URL=https://your-api-gateway-url.amazonaws.com
```

## Testing the Setup

### 1. Test Frontend Locally
```bash
cd frontend
npm install
npm run dev
# Should be available at http://localhost:3000
```

### 2. Test Backend Locally
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
# Should be available at http://localhost:8000
# API docs at http://localhost:8000/docs
```

### 3. Test Deployment Pipeline
1. Push to main branch
2. Check GitHub Actions tab
3. Verify frontend deploys to Vercel
4. Verify backend deploys to AWS Lambda

## Infrastructure Created

### AWS Resources
- Lambda function for API
- API Gateway for HTTP endpoints
- S3 buckets for file storage
- IAM roles and policies

### Vercel Resources
- Next.js application deployment
- Custom domain (if configured)
- Environment variables

## Next Steps
After completing Sprint 0:
1. Verify all deployments are working
2. Test the health check endpoints
3. Set up monitoring and logging
4. Proceed to Sprint 1: Core Features

## Troubleshooting

### Common Issues
1. **CORS errors**: Check CORS_ORIGINS in backend environment
2. **Lambda timeout**: Increase timeout in serverless.yml
3. **Build failures**: Check Node.js and Python versions in GitHub Actions
4. **Environment variables**: Ensure all secrets are set in GitHub

### Useful Commands
```bash
# Test backend locally
cd backend && uvicorn main:app --reload

# Test frontend locally
cd frontend && npm run dev

# Deploy backend manually
cd backend && serverless deploy

# Check Lambda logs
serverless logs -f api -t
``` 