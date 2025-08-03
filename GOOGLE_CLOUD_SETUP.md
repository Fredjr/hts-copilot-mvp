# Google Cloud Setup Guide

## Why Google Cloud Functions?

### Advantages over AWS Lambda:
- **Simpler pricing**: Pay only for actual compute time
- **Better cold start performance**: Generally faster than Lambda
- **Native Python support**: Excellent for your FastAPI backend
- **Easy integration**: Works seamlessly with other Google services
- **Free tier**: 2 million invocations per month free
- **Better documentation**: More straightforward setup process

## Step 1: Google Cloud Account Setup

### 1.1 Create Google Cloud Account
1. Go to [cloud.google.com](https://cloud.google.com)
2. Sign up with your Google account
3. Enable billing (required for Cloud Functions)

### 1.2 Enable Required APIs
Run these commands in Google Cloud Console or gcloud CLI:

```bash
# Enable Cloud Functions API
gcloud services enable cloudfunctions.googleapis.com

# Enable Cloud Storage API
gcloud services enable storage.googleapis.com

# Enable Secret Manager API
gcloud services enable secretmanager.googleapis.com
```

## Step 2: Create Google Cloud Storage Buckets

### 2.1 Create Storage Buckets
```bash
# Create bucket for file uploads
gsutil mb gs://hts-copilot-uploads

# Create bucket for analysis results
gsutil mb gs://hts-copilot-results

# Set bucket permissions (public read for results)
gsutil iam ch allUsers:objectViewer gs://hts-copilot-results
```

### 2.2 Configure CORS for Storage
Create a CORS configuration file `cors.json`:
```json
[
  {
    "origin": ["*"],
    "method": ["GET", "POST", "PUT", "DELETE"],
    "responseHeader": ["Content-Type"],
    "maxAgeSeconds": 3600
  }
]
```

Apply CORS to buckets:
```bash
gsutil cors set cors.json gs://hts-copilot-uploads
gsutil cors set cors.json gs://hts-copilot-results
```

## Step 3: Create Service Account

### 3.1 Create Service Account
```bash
# Create service account
gcloud iam service-accounts create hts-copilot-sa \
  --display-name="HTS Co-pilot Service Account"

# Get the service account email
SA_EMAIL=$(gcloud iam service-accounts list \
  --filter="displayName:HTS Co-pilot Service Account" \
  --format="value(email)")
```

### 3.2 Assign Permissions
```bash
# Grant Cloud Functions invoker role
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SA_EMAIL" \
  --role="roles/cloudfunctions.invoker"

# Grant Storage admin role
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SA_EMAIL" \
  --role="roles/storage.admin"

# Grant Secret Manager access
gcloud projects add-iam-policy-binding $PROJECT_ID \
  --member="serviceAccount:$SA_EMAIL" \
  --role="roles/secretmanager.secretAccessor"
```

### 3.3 Create and Download Key
```bash
# Create service account key
gcloud iam service-accounts keys create key.json \
  --iam-account=$SA_EMAIL

# The key.json file contains your service account credentials
```

## Step 4: Store Secrets

### 4.1 Store API Keys in Secret Manager
```bash
# Store Anthropic API key
echo -n "your-anthropic-api-key" | \
gcloud secrets create anthropic-api-key --data-file=-

# Store database URL
echo -n "your-database-url" | \
gcloud secrets create database-url --data-file=-
```

## Step 5: Configure GitHub Secrets

Go to your GitHub repository → Settings → Secrets and variables → Actions

### Add these secrets:

**Google Cloud Secrets:**
- `GCP_SA_KEY`: The entire content of your `key.json` file
- `GCP_PROJECT_ID`: Your Google Cloud project ID
- `GCP_REGION`: Your preferred region (e.g., `us-central1`)
- `GCS_BUCKET_NAME`: `hts-copilot-uploads`

**Vercel Secrets (unchanged):**
- `VERCEL_TOKEN`: Your Vercel token
- `VERCEL_ORG_ID`: Your team/org ID
- `VERCEL_PROJECT_ID`: Your project ID

## Step 6: Deploy Cloud Function

### 6.1 Manual Deployment (Test First)
```bash
# Navigate to backend directory
cd backend

# Deploy the function
gcloud functions deploy hts-copilot-api \
  --gen2 \
  --runtime=python311 \
  --region=us-central1 \
  --source=. \
  --entry-point=hts_copilot_api \
  --trigger=http \
  --allow-unauthenticated \
  --memory=512MB \
  --timeout=540s \
  --set-env-vars=GCS_BUCKET_NAME=hts-copilot-uploads
```

### 6.2 Test the Function
```bash
# Get the function URL
FUNCTION_URL=$(gcloud functions describe hts-copilot-api \
  --region=us-central1 \
  --format="value(serviceConfig.uri)")

# Test the health endpoint
curl $FUNCTION_URL/health
```

## Step 7: Update Frontend Configuration

### 7.1 Update Environment Variables
In your Vercel project, add:
- `NEXT_PUBLIC_API_URL`: Your Cloud Function URL

### 7.2 Test Frontend-Backend Connection
The frontend will now call your Google Cloud Function instead of AWS Lambda.

## Expected Results

### ✅ Success Indicators
- Cloud Function deploys successfully
- Health endpoint responds: `{"status": "healthy", "platform": "Google Cloud Functions"}`
- Storage test endpoint works
- Frontend can connect to backend
- GitHub Actions deploys automatically

### 🔧 Troubleshooting

**If Cloud Function deployment fails:**
1. Check service account permissions
2. Verify APIs are enabled
3. Check function logs: `gcloud functions logs read hts-copilot-api --region=us-central1`

**If storage connection fails:**
1. Verify bucket exists: `gsutil ls`
2. Check service account has storage permissions
3. Verify CORS configuration

## Cost Comparison

### Google Cloud Functions Pricing:
- **Free tier**: 2 million invocations/month
- **After free tier**: $0.40 per million invocations
- **Compute time**: $0.0000025 per GB-second

### Estimated Monthly Cost for MVP:
- **1000 invocations/day**: ~$0.12/month
- **Storage**: ~$0.02/GB/month
- **Total**: < $5/month for typical usage

## Next Steps

After successful Google Cloud setup:
1. ✅ Test Cloud Function deployment
2. ✅ Connect frontend to backend
3. ✅ Test file upload to Google Cloud Storage
4. 🚀 Proceed to Sprint 1: Core Features

## Quick Commands

```bash
# Deploy function
gcloud functions deploy hts-copilot-api --gen2 --runtime=python311 --region=us-central1 --source=. --entry-point=hts_copilot_api --trigger=http --allow-unauthenticated

# View logs
gcloud functions logs read hts-copilot-api --region=us-central1

# Test function
curl https://us-central1-YOUR_PROJECT.cloudfunctions.net/hts-copilot-api/health
``` 