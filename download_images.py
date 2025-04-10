import os
import urllib.request

images = [
    ("backbone_diagram.png", "https://cdn.pixabay.com/photo/2016/03/27/21/38/skeleton-1281261_1280.png"),
    ("vertebrate_examples.jpg", "https://cdn.pixabay.com/photo/2017/01/31/21/22/animal-2028258_1280.jpg"),
    ("mammal_lion.jpg", "https://cdn.pixabay.com/photo/2017/01/14/12/59/lion-1972774_1280.jpg"),
    ("thermostat_body.png", "https://cdn.pixabay.com/photo/2020/04/02/13/27/fever-4993339_1280.png"),
    ("sweating_person.jpg", "https://cdn.pixabay.com/photo/2019/07/18/11/27/man-4345522_1280.jpg")
]

os.makedirs("images", exist_ok=True)

headers = {'User-Agent': 'Mozilla/5.0'}

for filename, url in images:
    path = os.path.join("images", filename)
    try:
        print(f"🔄 Downloading {filename}...")
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response, open(path, 'wb') as out_file:
            out_file.write(response.read())
        print(f"✅ Saved to {path}")
    except Exception as e:
        print(f"❌ Failed to download {filename}")
        print(f"   Error: {e}")

input("Press Enter to close...")
