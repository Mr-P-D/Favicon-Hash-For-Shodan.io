import requests, mmh3, base64
import favicon

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
headers = {"User-Agent": user_agent}

inp = input("Enter URL to get the mmh3-HASH: ")
# check if the URL has a generic schema.
# Since we don't know the schema, we will check for the presence of :// in the URL.
while inp.find("://") == -1:
    inp = input("Enter a valid URL (with schema): ")
# if url is already favicon file (.ico, .jpg, .png or .gif), skip the reconnaissance.
if (
    not inp.lower().endswith(".ico")
    and not inp.lower().endswith(".jpg")
    and not inp.lower().endswith(".png")
    and not inp.lower().endswith(".gif")
):
    icons = favicon.get(inp, headers=headers)
    icon = icons[0]
    favicon_url = icon.url
else:
    favicon_url = inp
#get the icon from the favicon url.
response = requests.get(favicon_url, headers=headers)
#convert to base64
icon_data = base64.encodebytes(response.content)
#hash it
hash = mmh3.hash(icon_data)

print(hash)
print("Now Use this on Shodan For Searching,http.favicon.hash:" + str(hash))
print(
    "\t or press here: https://www.shodan.io/search?query=http.favicon.hash%3A"
    + str(hash)
)
