units = int(input())
if units < 200:
 cost_per_unit = 1.20
elif units >= 200 and units < 400:
 cost_per_unit = 1.40
elif units >= 400 and units < 600:
 cost_per_unit = 1.60
elif units >= 600 and units < 800:
 cost_per_unit = 1.80
else:
 cost_per_unit = 2.00
bill = cost_per_unit * units
surcharge = bill * 0.15 if bill > 400 else 0.0
total_amount = bill + surcharge
print(f"Units Consumed: {units}")
print(f"Cost per Unit: {cost_per_unit:.2f}")
print(f"Bill: {bill:.2f}")
print(f"Surcharge: {surcharge:.2f}")
print(f"Total Amount: {total_amount:.2f}")