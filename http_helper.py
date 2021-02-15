import urllib.parse
import urllib.request
import urllib.error
import http.cookiejar
from http.client import IncompleteRead
import gzip

import time
import random

headers = {
    'accept': 'application/json',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-CA,en;q=0.9',
    'dnt': '1',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
    'x-api-lang': 'en-CA',
}

class HTTP():
    def __init__(self):
        self.cookiejar = http.cookiejar.CookieJar()
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cookiejar))

    def get(self, url):
        return self._req(url)

    def post(self, url, data):
        if((type(data) == dict) or (type(data) == list)):
            data = urllib.parse.urlencode(data).encode("utf-8")
        return self._req(url, data)

    def _req(self, url, data=None):
        # EXPERIMENTAL: humanize?
        time.sleep(random.uniform(0.25, 0.5))

        req = urllib.request.Request(url, data, headers)

        retries = 3
        while(retries > 0):
            try:
                response = self.opener.open(req).read()
            except (urllib.error.HTTPError, ConnectionResetError, IncompleteRead):
                print("Attempting to recover "+str(retries))
                retries-=1
                response = None
                time.sleep(1)
                continue
            break
        return gzip.decompress(response).decode(self.opener.open(req).headers.get_content_charset())
    
    def appendHeader(self, key, value):
        headers[key] = value
    
    def removeHeader(self, key):
        try:
            headers.pop(key)
        except:
            print("FAILED: Removing "+key+" from header ")

    def getContentLength(self, data):
        return len(urllib.parse.urlencode(data).encode("utf-8"))