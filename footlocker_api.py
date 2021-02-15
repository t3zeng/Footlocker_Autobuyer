import http_helper

http = http_helper.HTTP()

def footlocker_buy_product(product_url):
    url = product_url
    response = http.get(url)
    print(response)