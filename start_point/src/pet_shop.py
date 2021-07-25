# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# function below works for both adding or removing cash
def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, number_sold):
    pet_shop["admin"]["pets_sold"] += number_sold

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

# this function works for breeds in our given list and breeds not in given list
def get_pets_by_breed(pet_shop, breed):
    all_pets = pet_shop["pets"]
    found_pets = []

    for pet in all_pets:
        if pet["breed"] == breed:
            found_pets.append(pet)
        
    return found_pets

# this function will return none if there is no pet with the name given
def find_pet_by_name(pet_shop, name):
    all_pets = pet_shop["pets"]
    
    for pet in all_pets:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(pet_shop, name):
    all_pets = pet_shop["pets"]

    for pet in all_pets:
        if pet["name"] == name:
            all_pets.remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)
