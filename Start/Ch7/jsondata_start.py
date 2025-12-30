# 
# Example file for parsing and processing JSON
#

import urllib
from urllib import request
import json

# Open the URL and read the data
webUrl = request.urlopen("https://uselessfacts.jsph.pl/api/v2/facts/random")
print("Response code:", webUrl.getcode())

# Read the JSON data from the source
data = webUrl.read()
print("Response data:\n", data)

# Print the content of the 'text' field
jsonParsed = json.loads(data)
print("The random fact text:", jsonParsed["text"])