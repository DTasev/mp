import sys
import json

data = "".join(sys.stdin.readlines())
json_data = json.loads(data)
last_build = json_data["builds"][0]
if last_build["state"] == "passed":
    sys.exit(0)
sys.exit(1)
