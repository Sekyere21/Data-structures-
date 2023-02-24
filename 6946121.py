#https://github.com/Sekyere21/Data-structures-.git
#script for car sales
#dictionary of cars brands and prices
car_inventory={"Toyota Yaris":70000,
      "Range Rover Velar":75000,
      "Lotus":90000, 
      "Ferrari":60000,
      "Corolla":75000,
      "Kia Sportage":100050,
      "Honda Accord":62000,
      "Honda Civic":75800,
      "Cadillac":500950,
      "Hyundai Sonata":70000,
      "Tesla Model 4":850000,
      "Ford":90000,
      "Honda CR-V":75000,
      "Lincoln":390000,
      "Apollo":70800,
      "Chevrolet Cruze":55000,
      "Kia Rio":86000,
      "Chrysler":805000,
      "Bentley":600005,
      "Bugatti Chiron":550000,
      "Porche":120000,
      "Rolls Royce":100250,
      "G Wagon":95000,
      "Lamboghini":84000,
      "Jeep Wrangler":44000, 
      "Pajero":45500,
      "Dodge Viper":35600,
      "Kia Picanto":63600,
      "Camry":70000,
      "Tundra":57200,
      "Santafe":45220,
      "Highlander":82500,
      "Escalade":85000,
      "Vitz":35000,}
 #Get user imput for car brand
car_name=input("Enter a car brand:")
#Function to check car availability
if car_name in car_inventory:
    print(f"Yes, {car_name} is available")
#Function to get prices
    car_price=car_inventory[car_name]
    print(f"The price of {car_name} is {car_price} cedis")
else:
    print(f"Sorry,{car_name} is not available")

    