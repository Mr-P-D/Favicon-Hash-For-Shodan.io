# Favicon-Hash-For-Shodan.io
this script will help you find favicon hashes which you can use in shodan to widened your attack surface

<b>Pre-requisite:</b>
>pip3 install mmh3 requests favicon

<b>Usage:</b>
>python3 get_favicon_hash.py URL containing favicon.ico

<b>Example:<b>
><br>root@Kali:~/Desktop/Favicon_Hash# python3 get_favicon_hash.py  
><br>Enter Favicon URL to get the mmh3-HASH: https://facebook.com/favicon.ico  
><br>-1321378357  
><br>Now Use this on Shodan For Searching,http.favicon.hash:-1321378357


