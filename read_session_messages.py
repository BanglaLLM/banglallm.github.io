import json

path = "/var/folders/17/l_8j2jv562d_mkrf3n4lc56m0000gn/T/hermes-results/4437i14a.txt"
with open(path, "r") as f:
    data = json.load(f)

for res in data.get("results", []):
    print(f"Session: {res.get('session_id')}")
    print(f"Title: {res.get('title')}")
    print(f"Snippet: {res.get('snippet')}")
    print("Messages count:", len(res.get("messages", [])))
    for msg in res.get("messages", []):
        print(f"  Role: {msg.get('role')}")
        content = msg.get('content', '')
        if isinstance(content, list):
            content = " ".join([part.get('text', '') for part in content if part.get('type') == 'text'])
        print(f"  Content: {content[:300]}...")
        print("-" * 20)
    print("="*50)
