import json

path = "/var/folders/17/l_8j2jv562d_mkrf3n4lc56m0000gn/T/hermes-results/4437i14a.txt"
with open(path, "r") as f:
    data = json.load(f)

for res in data.get("results", []):
    print(f"Session: {res.get('session_id')}, Match role: {res.get('matched_role')}")
    print(f"Snippet: {res.get('snippet')}")
    print("="*40)
