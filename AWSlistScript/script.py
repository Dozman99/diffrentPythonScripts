import subprocess
import json


def get_available_ebs():
  result = subprocess.check_output('aws ec2 describe-volumes')
  print(result)
  result_object = json.loads(result)  
  volumes = []
  for v in result_object["Volumes"]:
    if v["State"] == "available":
      name = [t["Value"] for t in v.get("Tags") if t["Key"] == "Name"] if v.get("Tags") != None else []
      tags = v.get("Tags")
      volumes.append({ "Name": name[0] if len(name) > 0 else None, "VolumeId": v["VolumeId"], "State": v["State"], "Tags": tags })
  return volumes

print(get_available_ebs())

