# *** Algorithm ***

# city_flight = user input
# num_nights = user input
# rental_days = user input

# function hotel_cost(num_nights):
#    return num_nights * price_per_night

# function plane_cost(city_flight):
#    return city_dict[city_flight]

# function car_rental(rental_days):
#    return rental_days * daily_cost_of_rentals


# **** CODE ****

city_dict: dict = {'cordoba': 70, 'madrid': 100, 'catalonia': 75}

city_flight: str = input("Which city is your flight header? (cordoba/madrid/catalonia) \n").lower()
num_nights: int = int(input("How many nights will you be spending in the city? \n"))
rental_days: int = int(input("How many days will you be renting for? \n"))

def hotel_cost(num_nights: int) -> int:
    return num_nights * 75

def plane_cost(city_flight: str) -> int:
    return city_dict[city_flight]

def car_rental(rental_days: int) -> int:
    return rental_days * 50

def holiday_cost(hotel_cost, plane_cost, car_rental) -> None:
    hotel = hotel_cost(num_nights)
    plane = plane_cost(city_flight)
    car = car_rental(rental_days)

    print("==================> TRAVEL INVOICE <=====================")
    print(f">> Hotel (75/night): {hotel :.2f} euros")
    print(f">> Flight : {plane :.2f} euros to {city_flight}")
    print(f">> Car (50/day): {car :.2f} euros")
    print(f"\n \n Total : {hotel + car + plane} euros")

holiday_cost(hotel_cost, plane_cost, car_rental)
