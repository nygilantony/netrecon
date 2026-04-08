import json
from datetime import datetime

def save_reports(results):
    filename = f"netrecon_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(filename, "w") as f:
        json.dump(results, f, indent=4)

    print(f"[+] Report saved: {filename}")
