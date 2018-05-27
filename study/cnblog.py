import http.client

conn = http.client.HTTPConnection("www.cnblog.com")

conn.request("GET","/")

response = conn.getresponse()

content = response.read()

content = content.decode('utf-8').split("\r\n")
print(content)
for i in content:
    print(i)


