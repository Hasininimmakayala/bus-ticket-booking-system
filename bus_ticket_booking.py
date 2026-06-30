print("===== BUS TICKET BOOKING SYSTEM =====")

# Taking input from user
name = input("Enter passenger name: ")
age = int(input("Enter age: "))
source = input("Enter starting place: ")
destination = input("Enter destination: ")
distance = float(input("Enter distance in km: "))

# Fare calculation
rate_per_km = 2.5
fare = distance * rate_per_km

# Discount
if age < 12:
    discount = 0.5 * fare  # 50% discount for children
elif age >= 60:
    discount = 0.4 * fare  # 40% discount for senior citizens
else:
    discount = 0

# Final amount
final_fare = fare - discount

# Display ticket
print("\n----- TICKET DETAILS -----")
print(f"Passenger Name : {name}")
print(f"Age            : {age}")
print(f"From           : {source}")
print(f"To             : {destination}")
print(f"Distance       : {distance} km")
print(f"Base Fare      : ₹{fare:.2f}")
print(f"Discount       : ₹{discount:.2f}")
print(f"Final Fare     : ₹{final_fare:.2f}")
print("---------------------------")
