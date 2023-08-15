from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

# CORS 설정 추가
origins = [
    "http://localhost:3000",  # 프론트엔드 앱의 주소
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/message")
def get_message():
    return {"message": "Hello, juju World!"}

if __name__ == "__main__":
    print('server started')
    uvicorn.run(app, host="0.0.0.0", port=8000)
