from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routes.product import router as product_router
from routes.upload import router as upload_router
app = FastAPI()

app.include_router(product_router)
app.include_router(upload_router)

app.mount("/static", StaticFiles(directory="static"), name="static")