bill_total = 210

dicount1 = 10
dicount2 = 20

if bill_total > 100 and bill_total < 200:
    print("Bill is greater than 100!")
    bill_total = bill_total - dicount1
elif bill_total > 200:
    print("Bill is grater than 200!")
    bill_total = bill_total - dicount2
else:
    print("Bill is less than 100")
print("Total Bill " +str(bill_total))