#!/usr/bin/env python3
import os
import json
import sys

def fix_json(path):
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

def generate_path(kernel_name):
	userid = os.getlogin()

	return f"/home/{userid}/.local/share/jupyter/kernels/{kernel_name}/kernel.json"
 
def main():

	if len(sys.argv) > 0:
		fix_json(generate_path(sys.argv[1]))
	else:
		print("Call with kernel name as first argument.")

if __name__ == "__main__":
	main()

