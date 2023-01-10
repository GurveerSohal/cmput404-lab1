import os
import requests
# os.system("pip show requests")
res = requests.get("https://raw.githubusercontent.com/GurveerSohal/cmput404-lab1/main/printversion.py")
print(res.content.decode())