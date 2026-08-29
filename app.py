from fastapi import FastAPI, APIRouter

router = APIRouter(prefix="/hello-world")

app = FastAPI()

@router.get("/")
def get_helloworld():
    return "Hello World"

app.include_router(router)