from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from starlette.middleware.sessions import SessionMiddleware

from app.routers.google_auth import router

app = FastAPI()

app.add_middleware(
    SessionMiddleware,
    secret_key="super-secret-key"
)

app.include_router(router)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return HTMLResponse(
        """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>Login with Google</title>
            <style>
                body {
                    margin: 0;
                    padding: 0;
                    font-family: Arial, sans-serif;
                    background: linear-gradient(135deg, #4285f4 0%, #34a853 100%);
                    color: #ffffff;
                    min-height: 100vh;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }
                .card {
                    background: rgba(255, 255, 255, 0.12);
                    border: 1px solid rgba(255, 255, 255, 0.25);
                    border-radius: 24px;
                    box-shadow: 0 18px 40px rgba(0, 0, 0, 0.2);
                    padding: 40px 36px;
                    max-width: 420px;
                    width: 100%;
                    text-align: center;
                    backdrop-filter: blur(14px);
                }
                h1 {
                    margin: 0 0 12px;
                    font-size: 2.2rem;
                }
                p {
                    margin: 0 0 28px;
                    color: rgba(255, 255, 255, 0.85);
                    line-height: 1.6;
                }
                .google-btn {
                    display: inline-flex;
                    align-items: center;
                    justify-content: center;
                    width: 100%;
                    max-width: 320px;
                    padding: 14px 20px;
                    border: none;
                    border-radius: 999px;
                    background: #ffffff;
                    color: #3c4043;
                    text-decoration: none;
                    font-weight: 600;
                    font-size: 0.95rem;
                    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.12);
                    transition: transform 0.2s ease, box-shadow 0.2s ease;
                }
                .google-btn:hover {
                    transform: translateY(-2px);
                    box-shadow: 0 14px 26px rgba(0, 0, 0, 0.18);
                }
                .google-icon {
                    width: 20px;
                    margin-right: 12px;
                }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>FastAPI Google OAuth</h1>
                <p>Sign in with Google to continue to your application.</p>
                <a class="google-btn" href="/login/google">
                    <img class="google-icon" src="https://www.gstatic.com/firebasejs/ui/2.0.0/images/auth/google.svg" alt="Google logo" />
                    Login with Google
                </a>
            </div>
        </body>
        </html>
        """
    )