import os
def check_file(filename): #read file
    products=[]
    if os.path.isfile(filename): #test file exist status
        print("Yes, the file is here")
    else:
        print("No found file")
    return products

def read_file(filename):
    products = []
    with open(filename, "r") as f:  # read file
        for line in f:
            if "商品,價格" in line:
                continue
            name, price = line.strip().split(",")  # 從左而右，先strip()把前後空格與換行符號\n除掉，然後slipt(",")把line以逗號為分隔
            products.append([name, price])
    print(products)
    return products

def user_input(products):# user enter
    while True:
        name = input("Please enter the product")
        if name == "q":
            break
        price = input("Please enter the price")
        price = int(price)
        products.append([name,price])
    return products

def print_products(products):
    for p in products:
        print(f"{p[0]}'s price is {p[1]}")

def write_file(filename,products):# with open("products.csv", "w", encoding="utf-8") as f:
    with open(filename, "w") as f:  #utf-8編號可以解決中文亂碼現象
        f.write("商品,價格\n")
        # f.write("products,price\n")
        for p in products:
            f.write(f"{p[0]},{p[1]}\n")

def main():
    filename = input("Please enter the file name")
    if os.path.isfile(filename) :
        print("Yes, the file is here")
        products = read_file("products.csv")
        products = user_input(products)
        print_products(products)
        write_file(filename, products)
    else:
        print("No found file")

main()



# for product in products:
#     if int(product[1]) > 10:
#         print(product)
