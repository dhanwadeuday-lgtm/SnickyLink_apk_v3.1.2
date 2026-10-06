"""
SnickyLink FastAPI Application
Main application entry point with Vercel Web Analytics integration
"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import os

app = FastAPI(
    title="SnickyLink API",
    description="SnickyLink cross-platform relationship app API",
    version="3.1.2"
)

# Mount static files directory for serving web assets
static_dir = os.path.join(os.path.dirname(__file__), "static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/", response_class=HTMLResponse)
async def root():
    """
    Root endpoint serving HTML page with Vercel Web Analytics
    """
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SnickyLink API</title>
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 2rem;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                color: #333;
            }
            .container {
                background: white;
                border-radius: 12px;
                padding: 2rem;
                box-shadow: 0 10px 40px rgba(0,0,0,0.1);
            }
            h1 {
                color: #667eea;
                margin-bottom: 0.5rem;
            }
            .version {
                color: #888;
                font-size: 0.9rem;
                margin-bottom: 2rem;
            }
            .feature {
                background: #f7f7f7;
                padding: 1rem;
                border-radius: 8px;
                margin-bottom: 1rem;
            }
            .feature h3 {
                margin-top: 0;
                color: #764ba2;
            }
            a {
                color: #667eea;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
            .status {
                display: inline-block;
                padding: 0.25rem 0.75rem;
                background: #10b981;
                color: white;
                border-radius: 20px;
                font-size: 0.875rem;
                font-weight: 600;
            }
        </style>
        
        <!-- Vercel Web Analytics -->
        <script>
            window.va = window.va || function () { 
                (window.vaq = window.vaq || []).push(arguments); 
            };
        </script>
        <script defer src="/_vercel/insights/script.js"></script>
    </head>
    <body>
        <div class="container">
            <h1>🔗 SnickyLink API</h1>
            <p class="version">Version 3.1.2 | <span class="status">Active</span></p>
            
            <p>Welcome to the SnickyLink API. This is a FastAPI-based backend service for the SnickyLink cross-platform relationship application.</p>
            
            <div class="feature">
                <h3>📊 Vercel Web Analytics Enabled</h3>
                <p>This page is now tracking analytics using Vercel Web Analytics. Page views and visitor data will be collected when deployed on Vercel.</p>
            </div>
            
            <div class="feature">
                <h3>📖 API Documentation</h3>
                <p>Access the interactive API documentation:</p>
                <ul>
                    <li><a href="/docs">Swagger UI Documentation</a></li>
                    <li><a href="/redoc">ReDoc Documentation</a></li>
                </ul>
            </div>
            
            <div class="feature">
                <h3>🔧 Technology Stack</h3>
                <ul>
                    <li>FastAPI - High-performance Python web framework</li>
                    <li>PostgreSQL - Primary database</li>
                    <li>Redis - Caching and session storage</li>
                    <li>Flutter - Mobile client (Android & iOS)</li>
                </ul>
            </div>
            
            <div class="feature">
                <h3>📱 Mobile App</h3>
                <p>This API powers the SnickyLink mobile application available for Android and iOS.</p>
            </div>
        </div>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "snickylink-api", "version": "3.1.2"}

# Additional API routes would be added here
# For example:
# from app.routers import auth, users, calendar, chat, community
# app.include_router(auth.router)
# app.include_router(users.router)
# etc.
