import json, os, sys

payload = sys.stdin.read().strip()
print(json.dumps({"agent": "agent-demo", "echo": payload or None, "ok": True}))
