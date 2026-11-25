from fastapi import FastAPI

app = FastAPI(
    title="SkillBridge API",
    description="Starter API for the SkillBridge career development platform.",
    version="0.1.0",
)


@app.get("/api/health", tags=["health"])
def health_check() -> dict[str, str]:
    return {"status": "ok"}
