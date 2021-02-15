import http_helper
import re
import time

http = http_helper.HTTP()

def footlocker_buy_product(product_url):
    url = product_url
    response = http.get(url)

    ts = int(round(time.time() * 1000))

    countdown_data = re.search('"displayCountDownTimer":true,"skuLaunchDate":(\d+)', response)
    if(countdown_data != None):
        time_left = int((int(countdown_data.group(1))-ts)/1000)
        print("Product unreleased. Waiting "+str(time_left)+" seconds")
        time.sleep(time_left)
    else:
        print("Product is released, BUY BUY BUY BUY!")
    
    
    # print(response)