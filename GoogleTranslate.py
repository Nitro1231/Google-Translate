# Nitro
# nitro0@naver.com
# 2/18/2020

import requests
import urllib.parse

def translate(sl, tl, text):
    URL = f"https://translate.google.co.kr/?sl={sl}&tl={tl}&text={urllib.parse.quote(text)}"
    r = requests.post(url = URL) # Post the requests to checker

    webResult = r.text.replace("\n", "")
    result = webResult[webResult.find('<span title="" class="">') + 25:webResult.find("</span>")].strip()[0:-1] # Find the data of checker from the javascript data of the checker.
    print("JSON: %s"%result)

translate("ko", "en", "안녕")