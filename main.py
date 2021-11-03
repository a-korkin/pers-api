import uvicorn
from fastapi import FastAPI
from routers import persons

def create_app() -> FastAPI:
    app = FastAPI(
        docs_url=None,
        redoc_url=None,
        openapi_url=None
    )

    app.include_router(persons.router, prefix="/api")
    return app

app = create_app()    

def main() -> None:
    uvicorn.run(app="main:app", port=5000, reload=True)    

if __name__ == "__main__":
    main()
