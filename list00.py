import os
products=[]
#test file exist status
if os.path.isfile("products.csv"):
    print("Yes, the file is here")
    with open("products.csv", "r") as f: # read file
        for line in f:
            if "商品,價格" in line:
                continue
            name, price = line.strip().split(",")  # 從左而右，先strip()把前後空格與換行符號\n除掉，然後slipt(",")把line以逗號為分隔
            products.append([name, price])
    print(products)
else:
    print("No found file")

# user enter
while True:
    name = input("Please enter the product")
    if name == "q":
        break
    price = input("Please enter the price")
    products.append([name,price])

# with open("products.csv", "w", encoding="utf-8") as f:
with open("products.csv", "w") as f:  #utf-8編號可以解決中文亂碼現象
    f.write("商品,價格\n")
    # f.write("products,price\n")
    for p in products:
        f.write(f"{p[0]},{p[1]}\n")



# for product in products:
#     if int(product[1]) > 10:
#         print(product)
