# Vercel Web Analytics Configuration

This document describes the Vercel Web Analytics integration for the SnickyLink FastAPI application.

## Overview

Vercel Web Analytics has been integrated into this FastAPI project to track web traffic and user interactions when the application is deployed on Vercel.

## What Was Installed

1. **Package**: `@vercel/analytics` (v1.4.1)
   - Installed via npm in `package.json`
   - Provides the Vercel Analytics tracking script

2. **Integration Method**: Vanilla HTML/JavaScript
   - Since this is a FastAPI (Python) backend, we use the HTML/JS integration approach
   - The analytics script is embedded directly in the HTML served by FastAPI

## Implementation Details

### Files Modified/Created

1. **`package.json`** - Added to manage the `@vercel/analytics` npm package
2. **`app/main.py`** - FastAPI application with:
   - Root endpoint (`/`) serving HTML with Vercel Analytics
   - Analytics script embedded in the HTML response
   - Health check endpoint at `/health`
3. **`app/__init__.py`** - Python package initialization
4. **`vercel.json`** - Vercel deployment configuration with analytics enabled

### How It Works

The Vercel Analytics integration uses the following approach:

```html
<!-- Vercel Web Analytics -->
<script>
    window.va = window.va || function () { 
        (window.vaq = window.vaq || []).push(arguments); 
    };
</script>
<script defer src="/_vercel/insights/script.js"></script>
```

This code:
1. Initializes the `window.va` function queue
2. Loads the Vercel analytics script from `/_vercel/insights/script.js`
3. Automatically tracks page views when users visit the site

## Deployment

### Deploying to Vercel

1. **Connect your repository to Vercel**:
   ```bash
   vercel
   ```

2. **Enable Web Analytics**:
   - Go to your project settings in the Vercel dashboard
   - Navigate to the "Analytics" tab
   - Click "Enable Web Analytics"

3. **Deploy**:
   ```bash
   vercel --prod
   ```

### Environment Variables

Make sure to set the required environment variables in your Vercel project settings:
- `DATABASE_URL`
- `SECRET_KEY`
- `REDIS_HOST`
- And other variables from `.env.example`

## Verification

After deployment, verify the analytics are working:

1. Visit your deployed site
2. Open browser DevTools (F12) → Network tab
3. Look for requests to `/_vercel/insights/view`
4. Check the Vercel dashboard Analytics section for tracked data

## Analytics Data Collected

When deployed on Vercel, the following data is tracked:
- **Page Views**: Each time a user visits a page
- **Unique Visitors**: Distinct users (anonymized)
- **Referrers**: Where traffic comes from
- **Geolocation**: Country/region data
- **Device Information**: Browser, OS, device type

All data is collected in compliance with privacy regulations and is anonymized.

## For Local Development

The analytics script will not track data in local development. The `/_vercel/insights/script.js` endpoint only exists on Vercel's platform.

To test locally:
```bash
# Install Python dependencies
pip install -r requirements.txt

# Run the FastAPI app
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Visit http://localhost:8000
```

## Additional Resources

- [Vercel Analytics Documentation](https://vercel.com/docs/analytics)
- [Vercel Analytics Quickstart](https://vercel.com/docs/analytics/quickstart)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

## Notes for FastAPI Backend

Since this is primarily a backend API (not a traditional web frontend), the analytics will mainly track:
- Visits to the root page (`/`)
- API documentation pages (`/docs`, `/redoc`)
- Any other HTML pages you add to the application

For comprehensive API monitoring, consider also using:
- Vercel's Function Logs
- FastAPI's built-in logging
- Third-party APM tools (New Relic, DataDog, etc.)
