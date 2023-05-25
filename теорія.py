# знайомство з стардатними бібліотеками
import urllib.request
opener = urllib.request.build_opener()
responce = opener.open("https://httpbin.org/get")
print(responce.read())
print("")