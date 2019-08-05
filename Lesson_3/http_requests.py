import requests

def decoder(func):
    def Http_request():
        for a in range(1, 5):
            func()
    return Http_request

@decoder
def request():
    req = requests.get('https://www.google.com')
    print ("Time spent on this function: ", req.elapsed)

request()
