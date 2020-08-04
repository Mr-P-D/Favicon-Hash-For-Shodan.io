# Favicon-Hash-For-Shodan.io
this script will help you find favicon hashes which you can use in shodan to widened your attack surface

Pre-requisite:
pip3 install mmh3

Usage:
python3 get_favicon_hash.py URL containing favicon.ico

Example:
root@Kali:~/Desktop/Favicon_Hash# python3 get_favicon_hash.py  
Enter Favicon URL to get the mmh3-HASH: https://facebook.com/favicon.ico  
-1321378357  
Now Use this on Shodan For Searching,http.favicon.hash:-1321378357


