import httpx
import json

# # 비동기 클라이언트 생성
# async def B2_client(): # TODO: you need to change when setting server sample script
#     async with httpx.AsyncClient() as client:
#         isNull = False
#         with open("../B_public/example.txt", "r") as file: # TODO: you need to change when setting server sample script
#             lines = file.readlines()
#             if lines == []:
#                 isNull = True
#         if isNull == False:
#             lines[0] = lines[0].replace("\n", "")
#             if(lines[0] != ""):
#                 data = {"data": int(lines[0])+2, "isnull": False} # TODO: you need to change when setting server sample script
                
#             else:
#                 data = {"data":1, "isnull": True}
#             with open("../B_public/example.txt", "w") as file: # TODO: you need to change when setting server sample script
#                 file.writelines(lines[1:])

#             response = await client.post("http://localhost:8001/", json=data) # TODO: you need to change when setting server sample script
#             print("POST 요청 응답:", response.json())

async def B2_client():
    with open("../B_public/data.json", "r") as json_file:
        json_data = json.load(json_file)
    data_list = json_data["data"]
    if not len(data_list) == 0:
        i = data_list.pop(0)


        print(i) #TODO :여기에 db insert 로직 작성 예정


        json_data["data"] = data_list
        with open("../B_public/data.json", "w") as file:
            json.dump(json_data, file, default=str)


def B2_run():
    import asyncio
    while True:
        asyncio.run(B2_client())


if __name__ == "__main__":
    B2_run()