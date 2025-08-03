# HTS Co-pilot Technical Specification

## Core Workflow Architecture

### 1. Data Processing Pipeline
```
CSV Upload → S3 Storage → Python Analysis → AI Interpretation → Interactive Report
```

### 2. Python Backend (FastAPI) Responsibilities
- **CSV Processing**: Parse 384-well plate data
- **Statistical Analysis**: 
  - Z-score calculations
  - Hit identification (Z-score > 3)
  - Edge effect detection
  - Signal drop-off analysis
- **Data Normalization**: Handle various plate formats
- **Error Detection**: Flag common experimental artifacts

### 3. AI Core (LangChain + Claude) Responsibilities
- **Input**: Statistical analysis results from Python
- **Processing**: Structured prompts for expert interpretation
- **Output**: Human-readable experiment summaries
- **Role**: Expert computational biologist consultant

### 4. Frontend (Next.js) Responsibilities
- **File Upload**: Drag-and-drop CSV interface
- **Progress Tracking**: Real-time processing status
- **Report Display**: Interactive charts and summaries
- **User Management**: Authentication and experiment history

## Key Technical Components

### Backend API Endpoints (FastAPI)
```
POST /api/upload          # Upload CSV file
POST /api/analyze         # Trigger analysis pipeline
GET  /api/results/{id}    # Get analysis results
GET  /api/experiments     # List user experiments
```

### AI Integration Points
- **Analysis Results Format**: Structured JSON with statistical findings
- **Prompt Engineering**: Expert computational biologist persona
- **Response Format**: Markdown-formatted summaries with key insights

### Database Schema (PostgreSQL)
```sql
-- Users table (handled by Supabase)
users (id, email, created_at)

-- Experiments table
experiments (
  id, user_id, filename, 
  upload_date, analysis_date, 
  status, results_url
)

-- Analysis results
analysis_results (
  experiment_id, hits_count, 
  edge_effects_detected, 
  summary_text, raw_data_url
)
```

### File Storage (AWS S3)
- **Upload Bucket**: Secure CSV storage
- **Results Bucket**: Analysis outputs and reports
- **Access Control**: Signed URLs for secure access

## Performance Requirements
- **Upload Time**: < 30 seconds for typical CSV files
- **Analysis Time**: < 90 seconds total processing
- **Report Generation**: < 30 seconds for AI summary
- **Total Time**: < 2 minutes end-to-end

## Security Considerations
- **File Upload**: Virus scanning and format validation
- **Data Encryption**: At rest and in transit
- **User Authentication**: Supabase Auth integration
- **Access Control**: User-specific data isolation

## Scalability Design
- **Serverless Backend**: AWS Lambda auto-scaling
- **CDN**: Vercel edge caching for frontend
- **Database**: Managed PostgreSQL with connection pooling
- **File Storage**: S3 with lifecycle policies

## Monitoring & Observability
- **Application Metrics**: Response times, error rates
- **User Analytics**: Upload patterns, feature usage
- **AI Performance**: Claude API usage and response quality
- **Infrastructure**: Lambda cold starts, S3 access patterns 