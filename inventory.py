
# Store Product Inventory System
# Prelim Exam - 2nd Year IT

def get_price_category(price):
    if price < 500:
        return "Budget"
    elif price < 1500:
        return "Mid-range"
    else:
        return "Premium"

def check_stock_level(stock):
    if stock >= 10: 
        return "OK"
    else:
        return "LOW STOCK - Reorder needed"

def save_product(name, price, category, stock, stock_status, total_price):
    with open('inventory.txt', "a") as file:
        file.write(f"Product: {name} | Price: P{price:.2f} | Qty: {stock} | Total: P{total_price:.2f} | Category: {category} | Status: {stock_status}\n")


grand_total = 0

while True:
    # 1. COLLECTION
    print("\n--- Product Entry ---")
    name = input("Enter Product Name: ")
    
    try:
        price = float(input("Enter Price: "))
        stock = int(input("Enter Stock Quantity: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        continue

    # 2. PROCESSING
    category = get_price_category(price)
    stock_status = check_stock_level(stock)
    

    current_total_price = price * stock
    
    
    grand_total += current_total_price

    # 3. OUTPUT
    print(f"\nResults for: {name}")
    print(f"Price Category: {category}")
    print(f"Stock Status: {stock_status}")
    print(f"Current Item Total Value: P{current_total_price:.2f}")
    print(f"--- RUNNING GRAND TOTAL: P{grand_total:.2f} ---")

    save_product(name, price, category, stock, stock_status, current_total_price)
    print("Product recorded in inventory.txt.")

    choice = input("\nAdd another product? (yes/no): ").lower()
    if choice != "yes":
        # EXIT SECTION: Ipapakita ang huling total bago mag-close
        print("-" * 30)
        print(f"FINAL INVENTORY GRAND TOTAL: P{grand_total:.2f}")
        print("-" * 30)
        print("Closing system. Thank you!")
        break