destinations = ["Bora Bora", "Miami", "Cancun", "Panama", "Puerto Rico", "Egypt"]
restaurants = ["eat SteakHouse", "get Shake Shack", "eat some Surf n Turf", "eat McDonalds"]
mode_of_transportation = ["drive a Dodge Challenger", "drive a Chevy Avalanche", "drive a Tahoe", "ride in a taxi"]
entertainment = ["go bowling", "go to the beach", "go skydiving", "go sight seeing"]

while valid_response == False:
    rand_destination = random.choice(destinations)
    dest_mess = input(f"would you like to go to {rand_destination} y/n ")
    if dest_mess =="y":
        valid_response = True

while valid_response2 == False:
    rand_transportation = random.choice(mode_of_transportation) 
    transp_mess = input(f"would you like to {rand_transportation} y/n ")
    if transp_mess == "y":
        valid_response2 = True
    
while valid_response3 == False:
    rand_entertainment = random.choice(entertainment)
    ent_mess = input(f"would you like to {rand_entertainment} y/n ")
    if ent_mess == "y":
        valid_response3 = True

while valid_response4 == False:
    rand_restaurants = random.choice(restaurants)
    rest_mess = input(f"would you like to {rand_restaurants} y/n ")
    if rest_mess == "y":
        valid_response4 = True
