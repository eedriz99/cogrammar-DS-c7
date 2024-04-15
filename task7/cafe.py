
menu: list[str]  = ["tea", "coffee", "cappucino", "soda"]

stock: dict[int] = {"tea": 10, "coffee": 15, "cappucino": 12, "soda": 10}
price: dict[float] = {"tea": 2.5, "coffee": 3, "cappucino": 5, "soda": 3.5}

def calculate_total_stock(menu_list: list, stock: dict, price: dict) -> float:
    stock_total: int = 0
    for item in menu_list:
        stock_total += stock[item]*price[item]
    return stock_total

print(calculate_total_stock(menu, stock, price))
