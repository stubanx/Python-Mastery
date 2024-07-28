import pyshorteners
url=input("Enter the URL: ")
s_url=pyshorteners.Shortener().tinyurl.short(url)
print(s_url)