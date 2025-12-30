#
# Example file for retrieving data from the internet
#
import urllib
from urllib import request

webUrl = request.urlopen("http://www.example.com")
print("Respose code: ", webUrl.getcode())
data = webUrl.read()
print("Response data:\n", data)