import httpx

# 비동기 클라이언트 생성
async def B2_client(): # TODO: you need to change when setting server sample script
    async with httpx.AsyncClient() as client:
        isNull = False
        with open("../B_public/example.txt", "r") as file: # TODO: you need to change when setting server sample script
            lines = file.readlines()
            if lines == []:
                isNull = True
        if isNull == False:
            data = {"number": int(lines[0])+2} # TODO: you need to change when setting server sample script
            response = await client.post("http://localhost:8001/", json=data) # TODO: you need to change when setting server sample script
            with open("../B_public/example.txt", "w") as file: # TODO: you need to change when setting server sample script
                file.writelines(lines[1:])
            print("POST 요청 응답:", response.json())

def B2_run(): # TODO: you need to change when setting server sample script
    import asyncio
    while True:
        asyncio.run(B2_client()) # TODO: you need to change when setting server sample script


if __name__ == "__main__":
    B2_run() # TODO: you need to change when setting server sample script