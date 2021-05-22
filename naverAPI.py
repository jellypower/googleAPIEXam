import xml.etree.ElementTree as ET
import urllib.request

CLIENT_ID = "pu8qXcGXBhLD__SaDdSS"
CLIENT_SECRET = "JAqZiBsAtl"
NUM_OF_SEARCHING = 10
encText = urllib.parse.quote("어벤져스")

url = "https://openapi.naver.com/v1/search/movie.xml?query=%s&display=%d" %(encText,NUM_OF_SEARCHING) 


request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",CLIENT_ID)
request.add_header("X-Naver-Client-Secret",CLIENT_SECRET)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    
    response_xml_str = response_body.decode('utf-8')
    
    root = ET.fromstring(response_xml_str) #parsing XMLstring
    
    print(root.findall("./channel/item"))

else:
    print("Error Code:" + rescode)

