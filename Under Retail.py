from stockxsdk import Stockx

stockx = Stockx()

while True:
    sneaker = input('What are you looking for?:')
    if sneaker == "":
        print('Invalid Input')
        break

    productId = stockx.get_first_product_id('{}'.format(sneaker))
    product = stockx.get_product(productId)
    print()
    prices = stockx.get_asks(productId)
    print("{} - ${}".format(product.title, product.retail_price))
    print()
    mylist = []

    for ask in prices:
        if product.retail_price >= ask.order_price:
            mylist.append(ask)
            if product.retail_price-ask.order_price == 0:
                price_diff = "At Retail"
            else:
                price_diff = '${} Under Retail'.format(product.retail_price-ask.order_price)
            print("Size: {} ${} ({})".format(ask.shoe_size, ask.order_price, price_diff))
            print('=====================================')
    if not mylist:
        print('No Shoes Under Retail!')
        print()
