import customers


CUSTOMERS = [
    {
      "email": "dillonbdraper@gmail.com",
      "password": "password",
      "name": "Dillon Draper",
      "id": 1
    },
    {
        "email": "dummymail@gmail.com",
        "password": "password",
        "name": "Dumb guy",
        "id": 2
    }
  ]

def get_all_customers():
    return CUSTOMERS


# Function with a single parameter
def get_single_customer(id):
    # Variable to hold the found animal, if it exists
    requested_customer = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

def create_customer(customer):
    max_id = CUSTOMERS[-1]["id"]

    new_id = max_id + 1

    customer["id"] = new_id

    CUSTOMERS.append(customer)

    return customer