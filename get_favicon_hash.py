import requests,mmh3,base64
inp = input("Enter Favicon URL to get the mmh3-HASH: ") 
#check if the URL has a generic schema.
#Since we don't know the schema, we will check for the presence of :// in the URL.
while inp.find("://") == -1:
    inp = input("Enter a valid URL (with schema): ")
response = requests.get(inp)
favicon = base64.encodebytes(response.content)
hash = mmh3.hash(favicon)
print (hash)
print ("Now Use this on Shodan For Searching,http.favicon.hash:" + str(hash))