import os
import requests
# os.system("pip show requests")
res = requests.get("http://www.google.com/")
print(res)