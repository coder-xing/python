import http.client
import re

cnn = http.client.HTTPConnection("www.jd.com")

conn.request("GET","/vamei")

response = conn.getresponse()

content = response.read()

content = content.decode('utf-8').split("\r\n")
pattern = "posted @ (\d{4}-[0-1]\d-{0-3}\d [0-2]\:d[0-6]\d) Vamei 阅读\((\d)\+)"

for line in content:
    print(line)
    
