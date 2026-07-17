products={
    'salt':{'stock':20,'discount':20,'price':60},
    'sugar':{'stock':0,'discount':12,'price':70},
    'chilli':{'stock':10,'discount':0,'price':50},
    'bread':{'stock':22,'discount':15,'price':40},
    'butter':{'stock':11,'discount':10,'price':80},
    'honey':{'stock':0,'discount':50,'price':160},
    }
for i in products:
    if products[i]['stock']:
        print(i)
        products[i]['price']-=products[i]['price']*(products[i]['discount'])/100
        
        print(products[i]['price'])
        

