import httpx

# 비동기 클라이언트 생성
async def F2_client(): # TODO: you need to change when setting server sample script
    async with httpx.AsyncClient() as client:
        isNull = False
        with open("../F_public/example.txt", "r") as file: # TODO: you need to change when setting server sample script
            lines = file.readlines()
            if lines == []:
                isNull = True
        if isNull == False:
            data = {"number": int(lines[0])+20000} # TODO: you need to change when setting server sample script
            response = await client.post("http://localhost:8005/", json=data) # TODO: you need to change when setting server sample script
            with open("../F_public/example.txt", "w") as file: # TODO: you need to change when setting server sample script
                file.writelines(lines[1:])
            print("POST 요청 응답:", response.json())

def F2_run(): # TODO: you need to change when setting server sample script
    import asyncio
    while True:
        asyncio.run(F2_client()) # TODO: you need to change when setting server sample script


if __name__ == "__main__":
    F2_run() # TODO: you need to change when setting server sample script