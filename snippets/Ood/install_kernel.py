#!/usr/bin/env python3

def fix_json(path):
	import os
	import json

	LD_LIBRARY_PATH = os.environ["LD_LIBRARY_PATH"]

	kernelspec = {}
	with open(path) as kernelspec_json:
		kernelspec = json.load(kernelspec_json)
		kernelspec_json.close()

	env = {"LD_LIBRARY_PATH" : LD_LIBRARY_PATH}
	kernelspec["env"] = env

	with open(path, "w", encoding="utf-8") as kernelspec_json:
		json.dump(kernelspec, kernelspec_json, indent=4, sort_keys=True)
		kernelspec_json.close()

def main():
	import sys

	if len(sys.argv) > 0:
		fix_json(sys.argv[1])
	else:
		print("Call with json file as first argument.")

if __name__ == "__main__":
	main()

