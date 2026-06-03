from fastapi import FastAPI

app = FastAPI(title="OJT API")


@app.get("/health")
def health_check():
    return {"status": "healthy"}