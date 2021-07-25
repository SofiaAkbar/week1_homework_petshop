# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

# function below works for both adding or removing cash
def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount

