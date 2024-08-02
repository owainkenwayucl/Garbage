import json
import os

settings_file = f"{os.path.expanduser('~')}/.rancher/cli2.json"

print(f"Updating Settings file {settings_file}")

data = ""

with open(settings_file) as f_handle:
    data = json.load(f_handle)

kube_confs = list(data['Servers']['rancherDefault']['kubeConfigs'].keys())

for a in kube_confs:
    clusters = list(data['Servers']['rancherDefault']['kubeConfigs'][a]['clusters'].keys())
    for b in clusters:
        print(f"Updating {a}/{b}")
        temp = data['Servers']['rancherDefault']['kubeConfigs'][a]['clusters'][b].pop('certificate-authority-data', None)
        if temp == None:
            print(f">>> CA information for {a}\{b} already deleted.")

json_out = json.dumps(data, indent=4)

with open(settings_file, "w") as f_handle:
    f_handle.write(json_out)
