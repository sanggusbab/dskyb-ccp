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

def parse(request):
    requests = request.split(",")
    #DB나 다른데서 모션코드 찾아서 변환해줘야함.


async def B2_client(subgroup_code):
    with open("../B_public/data.json", "r") as json_file:
        json_data = json.load(json_file)
    data_list = json_data["data"]
    if not len(data_list) == 0:
        data = data_list.pop(0)
        subgroup_code += 1
        motion_codes = parse(data.request)
        for i, code in motion_codes:
            """subgroup_detail_data : task_subgroup_code = 1, location_x = data.location_x, location_y = data.location_y, motion_code = code, sequence = i+1, requested_start_time = data.start_time"""
        print(data)
        """
        subgroup_info_data : task_id  = data.task_id, task_group = data.task_group, task_subgroup_code = subgroup_code, user_id = data.user_id
        """
        json_data["data"] = data_list
        with open("../B_public/data.json", "w") as file:
            json.dump(json_data, file, default=str)
    return subgroup_code


def B2_run():
    subgroup_code = 0
    import asyncio
    while True:
        asyncio.run(subgroup_code = B2_client(subgroup_code))


if __name__ == "__main__":
    B2_run()