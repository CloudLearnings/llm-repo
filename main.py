# import json
# import requests
# API_URL = "https://api-inference.huggingface.co/models/gpt3"
# headers = {"Authorization": "Bearer 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"}
# def query(payload):
#     data = json.dumps(payload)
#     response = requests.request("POST", API_URL, headers=headers, data=data)
#     return json.loads(response.content.decode("utf-8"))
# data = query("Who won the cricket world cup 2011")
# print(data)

import requests

API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query("Image.jpg")
print(output[0]["generated_text"])