import http_helper
import re
import time

http = http_helper.HTTP()

def footlocker_buy_product(product_url):
    countdown_data = 1

    while(countdown_data != None):
        url = product_url
        response = http.get(url)

        ts = int(round(time.time() * 1000))

        countdown_data = re.search('"displayCountDownTimer":true,"skuLaunchDate":(\d+)', response)

        time_left = int((int(countdown_data.group(1))-ts)/1000)
        print("Product unreleased. Waiting "+str(time_left)+" seconds")
        frantic_refresh_offset = 60
        if(time_left > frantic_refresh_offset):
            time.sleep(time_left-frantic_refresh_offset)
    else:
        print("Product is released, BUY BUY BUY BUY!")
    
    
    

    # print(response)