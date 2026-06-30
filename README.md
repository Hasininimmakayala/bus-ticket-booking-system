# 🚌 Bus Ticket Booking System

A simple command-line Python application that calculates bus ticket fares based on distance traveled, with automatic discounts for children and senior citizens.

## Features

- Collects passenger details (name, age, source, destination, distance)
- Calculates fare based on distance (₹2.5 per km)
- Applies automatic discounts:
  - **50% off** for passengers under 12 years
  - **40% off** for passengers 60 years and above
  - No discount for all other passengers
- Displays a clean, formatted ticket summary

## Demo

```
===== BUS TICKET BOOKING SYSTEM =====
Enter passenger name: John Doe
Enter age: 65
Enter starting place: Hyderabad
Enter destination: Bangalore
Enter distance in km: 570

----- TICKET DETAILS -----
Passenger Name : John Doe
Age            : 65
From           : Hyderabad
To             : Bangalore
Distance       : 570.0 km
Base Fare      : ₹1425.00
Discount       : ₹570.00
Final Fare     : ₹855.00
---------------------------
```

## Requirements

- Python 3.x (no external libraries needed)

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/bus-ticket-booking-system.git
   cd bus-ticket-booking-system
   ```
2. Run the script:
   ```bash
   python bus_ticket_booking.py
   ```
3. Follow the on-screen prompts to enter passenger details.

## Fare Calculation Logic

| Condition          | Discount |
|---------------------|----------|
| Age < 12             | 50%      |
| Age >= 60            | 40%      |
| All other ages       | 0%       |

Final Fare = (Distance × Rate per km) − Discount

## Possible Improvements

- Input validation (handle non-numeric age/distance gracefully)
- Support for multiple passengers in one booking
- Save ticket details to a file or database
- Add seat selection and booking IDs
- Build a GUI or web interface (Flask/Streamlit)

## License

This project is open source and available under the [MIT License](LICENSE).
