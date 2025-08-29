import json
import base64

inputfile = "testpng.png"
outputfile = "data.json"

data = {}

with open(inputfile, "rb") as f:
	img = f.read()

data["filename"] = inputfile
data["image_png"] = base64.standard_b64encode(img).decode("utf-8")

with open(outputfile, "w") as jf:
	json.dump(data, jf, indent=4)
