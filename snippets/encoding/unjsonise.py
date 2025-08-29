import json
import base64

jsonfile = "data.json"
out_prepend = "new"

with open (jsonfile, "r") as f:
	data = json.load(f)

filename = f"{out_prepend}_{data['filename']}"
img = base64.standard_b64decode(data["image_png"].encode("utf-8"))

with open (filename, "wb") as pf:
	pf.write(img)
