from fastapi import APIRouter

router = APIRouter(
	prefix="/clients",
    tags=["clients"]
)

@router.get("/end_user_client_process")
def end_user_client_process():
    print("end_user_client_process")
    return {"end_user_client_process"}

