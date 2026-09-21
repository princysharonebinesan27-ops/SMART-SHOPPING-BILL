#smart shopping
print("\n==========SMART SHOPPING BILL==========")
productname = input("\nenter a product name:")
price = int(input("\nenter a product price:"))
quantity = int(input("\nenter a quantity:"))
subtotal = price*quantity
print("\nsubtotal:",subtotal)
discount = int(input("\nenter a discount amount:"))
print("\ndiscount amount is :",discount)
ds_amount = discount-subtotal
gst = int(input("\nenter a GST amount:"))
print("\nGST amount is :",gst)
finalamount = gst-ds_amount
print("\nfinal amount:",finalamount)
print("\nthanks you for shopping!")

