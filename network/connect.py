import requests

def connect_in(query, data=None):
    json_string = requests.get(query, json=data)
    return json_string

def connect_out(query, data):
    requests.post(query, json=data)
    return 0

def decoder(query):
    newData = connect_in(query)
    if(newData == None):
        return None
    else:
        return newData.json()

if __name__ == '__main__':
    print(decoder('localhost:7010'))
    