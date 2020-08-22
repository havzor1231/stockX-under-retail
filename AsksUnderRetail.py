from stockxsdk import Stockx

stockx = Stockx()

while True:
    sneaker = input('What are you looking for?:')
    if sneaker == "":
        print('Invalid Input. Please try again.')
        break

    productId = stockx.get_first_product_id('{}'.format(sneaker))
    product = stockx.get_product(productId)
    print()
    prices = stockx.get_asks(productId)
    print("{} - ${}".format(product.title, product.retail_price))
    print()
    res = []

    for price in prices:
        if product.retail_price >= price.order_price:
            res.append(price)
            margin = product.retail_price - price.order_price
            if margin != 0:
                price_diff = '${} Under Retail'.format(margin)
            else:
                price_diff = "At Retail"
            print("Size: {} ${} ({})".format(price.shoe_size, price.order_price, price_diff))
            print('=====================================')
            
    if not res:
        print('No Shoes Under Retail!')
        print()
