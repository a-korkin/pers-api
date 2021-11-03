from logging import debug
import uvicorn
from fastapi import FastAPI
from routers import persons
from config import settings

def create_app() -> FastAPI:
    app = FastAPI(
        docs_url=None,
        redoc_url=None,
        openapi_url=None
    )

    app.include_router(persons.router, prefix=settings.API_V1)
    return app

app = create_app()    

def main() -> None:
    uvicorn.run(app="main:app", port=5000, reload=True)    

if __name__ == "__main__":
    main()
