from fastapi import APIRouter

router = APIRouter(
	prefix="/servers",
    tags=["servers"]
)

@router.get("/decoder_server_process")
def decoder_server_process():
    print("end_user_client_process")
    return {"end_user_client_process"}

