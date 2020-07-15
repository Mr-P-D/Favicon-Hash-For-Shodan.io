import requests,mmh3,base64
inp = input("Enter Favicon URL to get the mmh3-HASH: ") 
response = requests.get(inp)
favicon = base64.encodebytes(response.content)
hash = mmh3.hash(favicon)
print (hash)
print ("Now Use this on Shodan For Searching,http.favicon.hash:" + str(hash))

	