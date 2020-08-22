from stockxsdk import Stockx

stockx = Stockx()

while True:
    item = input('What are you looking for?:')
    if item == "":
        print('Program Ended')
        break

    product_id = stockx.get_first_product_id('{}'.format(item))
    product = stockx.get_product(product_id)
    print()
    asks = stockx.get_asks(product_id)
    print("{} - ${}".format(product.title, product.retail_price))
    print()
    mylist = []

    for ask in asks:
        if product.retail_price >= ask.order_price:
            mylist.append(ask)
            if product.retail_price-ask.order_price == 0:
                underr = "At Retail"
            else:
                underr = '${} Under Retail'.format(product.retail_price-ask.order_price)
            print("Size: {} ${} ({})".format(ask.shoe_size, ask.order_price, underr))
            print('----------------------------------------')
    if not mylist:
        print('No Asks Under Retail')
        print()
