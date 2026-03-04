#RESTAURANT BILLING
print("----------------------  MAA ANNAPURNA RESTAURANT  ----------------------")

GST = 5 
Discount = 20

#ORDERS
n = int(input("TOTAL ORDERS: "))
total_amt = 0
orders = []

for i in range(1, n+1) :
    name = input(f"ORDER{i}: ")
    qty = int(input(f"QTY: "))
    price = float(input(f"Price: Rs."))
    print("\n")

    item_total = qty*price
    orders.append((name, qty, price, item_total))
    total_amt += item_total

#CALCULATIONS
discount_amt = (Discount/100)*total_amt
amt_after_discount = total_amt - discount_amt
gst_amt = (GST/100)*amt_after_discount
final_bill = amt_after_discount + gst_amt


#Dispaly Bill
print("\n========== RESTAURANT BILL ========== ")
print("\n ITEM NAME \t \tQTY \tAMOUNT")
print("------------------------------------")
    
for item, qty, price, item_total in orders :
    print(f"{item:<20} {qty:<7} Rs.{price:<9.2f} Rs.{item_total: .2f}")

print("--------------------------------------")
print(f"Total Amount        : ₹ {total_amt:.2f}")
print(f"Discount (10%)      : ₹ {discount_amt:.2f}")
print(f"GST (5%)            : ₹ {gst_amt:.2f}")
print("--------------------------------------")
print(f"Final Bill Amount   : ₹ {final_bill:.2f}")
print("======================================")