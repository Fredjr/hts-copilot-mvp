# Vercel Setup & Deployment Testing Guide

## Step 1: Vercel Account Setup

### 1.1 Create Vercel Account
1. Go to [vercel.com](https://vercel.com)
2. Sign up with your GitHub account
3. Authorize Vercel to access your repositories

### 1.2 Import Your Project
1. In Vercel dashboard, click "New Project"
2. Import your GitHub repository: `Fredjr/hts-copilot-mvp`
3. Configure the project:
   - **Framework Preset**: Next.js
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `.next`
   - **Install Command**: `npm install`

### 1.3 Environment Variables
Add these environment variables in Vercel:
- `NEXT_PUBLIC_API_URL`: `https://your-api-gateway-url.amazonaws.com` (we'll get this after AWS setup)

## Step 2: Get Vercel Credentials

### 2.1 Get Vercel Token
1. Go to [vercel.com/account/tokens](https://vercel.com/account/tokens)
2. Create a new token with name "HTS Co-pilot Deployment"
3. Copy the token

### 2.2 Get Project & Org IDs
1. In your Vercel project dashboard
2. Go to Settings → General
3. Copy:
   - **Project ID** (e.g., `prj_abc123...`)
   - **Team ID** (same as Org ID)

## Step 3: Configure GitHub Secrets

Go to your GitHub repository → Settings → Secrets and variables → Actions

### Add these secrets:

**Vercel Secrets:**
- `VERCEL_TOKEN`: Your Vercel token
- `VERCEL_ORG_ID`: Your team/org ID
- `VERCEL_PROJECT_ID`: Your project ID

**AWS Secrets (for backend):**
- `AWS_ACCESS_KEY_ID`: Your AWS access key
- `AWS_SECRET_ACCESS_KEY`: Your AWS secret key
- `AWS_REGION`: Your AWS region (e.g., `us-east-1`)

## Step 4: Test Deployment

### 4.1 Manual Vercel Deploy (Test First)
```bash
# In the frontend directory
vercel --prod
```

### 4.2 Test GitHub Actions Deployment
```bash
# Merge test branch to main
git checkout master
git merge test-deployment
git push origin master
```

## Step 5: Verify Deployment

### 5.1 Check Vercel Dashboard
- Go to your Vercel project
- Check deployment status
- Visit the live URL

### 5.2 Check GitHub Actions
- Go to your GitHub repository
- Click "Actions" tab
- Verify the deployment workflow runs successfully

## Expected Results

### ✅ Success Indicators
- Vercel deployment shows "Ready" status
- GitHub Actions workflow completes without errors
- Frontend is accessible at your Vercel URL
- Backend health check endpoint responds

### 🔧 Troubleshooting

**If Vercel deployment fails:**
1. Check build logs in Vercel dashboard
2. Verify `package.json` has correct scripts
3. Ensure all dependencies are in `package.json`

**If GitHub Actions fails:**
1. Check secrets are correctly set
2. Verify Vercel project ID and token
3. Check workflow logs for specific errors

## Next Steps

After successful deployment:
1. ✅ Test frontend at Vercel URL
2. ✅ Set up AWS Lambda for backend
3. ✅ Connect frontend to backend API
4. 🚀 Proceed to Sprint 1: Core Features

## Quick Commands

```bash
# Test frontend locally
cd frontend && npm run dev

# Deploy to Vercel manually
cd frontend && vercel --prod

# Check deployment status
vercel ls
``` 