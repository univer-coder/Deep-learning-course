import requests

response = requests.post(
    f"https://api.stability.ai/v2beta/stable-image/generate/sd3",
    headers={
        "authorization": f"Bearer sk-BNBLo0ldnboc3h5qTddJwlQ197yqGSBH5Exn6n0RAJbi69e9",
        "accept": "image/*"
    },
    files={"none": ''},
    data={
        "prompt": "Lighthouse on a cliff overlooking the ocean, the spectacle of modern life, essence of modernity, the sensation produced by a landscape, effects of changing light",
        "output_format": "jpeg",
    },
)

if response.status_code == 200:
    with open("./lighthouse.jpeg", 'wb') as file:
        file.write(response.content)
else:
    raise Exception(str(response.json()))