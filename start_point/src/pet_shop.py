# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# function below works for both adding or removing cash
def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount
    # get_total_cash(pet_shop) += amount

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

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, amount):
    customer["cash"] -= amount 

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

# optional functions

def customer_can_afford_pet(customer, pet):
    # if customer["cash"] >= pet["price"]:
    #     return True
    # else:
    #     return False
    return customer["cash"] >= pet["price"]

# intergration tests

def sell_pet_to_customer(pet_shop, pet, customer):
    add_pet_to_customer(customer, pet)
    increase_pets_sold(pet_shop, 1)
    remove_customer_cash(customer, pet["price"])
    add_or_remove_cash(pet_shop, pet["price"])