weight = 41.5

# Ground Shipping
if weight <= 2:
  cost = weight * 1.50 + 20 
elif weight <= 6:
  cost = weight * 3.00 + 20
elif weight <= 10:
  cost = weight * 4.00 + 20
elif weight > 10 :
  cost = weight * 4.75 + 20
print("Ground Shipping:", cost)

# Ground Shipping Premium
cost_premium = 125
print("Ground Shipping Premium:", cost_premium)

# Drone Shipping
if weight <= 2:
  cost = 4.50 * weight
elif weight <= 6 : 
  cost = 9 * weight
elif weight <= 10:
  cost = 12 * weight
elif weight > 10:
  cost = 14.25 * weight
print("Drone Shipping:", cost)

# THE END
