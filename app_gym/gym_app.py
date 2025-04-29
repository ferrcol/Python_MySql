from costumer import Costumer
from costumer_dao import CostumerDAO


print("--- App for gym costumers --- ")

option = None

while option != 5:
    print(f''' App Menu:
          1 . Costumer List
          2 . Add costumer
          3 . Edit Costumer
          4 . Delete costumer
          5 . Exit''')
    option = int(input("elect one option: "))
    if option == 1:
        costumers = CostumerDAO.select()
        print("\n --- Gym Costumer List ---")
        for costumer in costumers:
            print(costumer)

    elif option == 2:
        firs_name_var = input("First name: ")
        last_name_var = input("Last name: ")
        membership_var = input("membership: ")
        costumer = Costumer(firs_name=firs_name_var, last_name=last_name_var, membership=membership_var)
        insert_costumers = CostumerDAO.insert(costumer)
        print(f"Added costumer: {insert_costumers}")

    elif option == 3:
        id_var = int(input("Costumer id to edit: "))
        firs_name_var = input("First name to edit: ")
        last_name_var = input("Last name to edit: ")
        membership_var = input("membership to edit: ")
        costumer = Costumer(id=id_var, firs_name=firs_name_var, last_name=last_name_var, membership=membership_var)
        update_costumers = CostumerDAO.update(costumer)
        print(f"Edited costumer: {update_costumers}")

    elif option == 4:
        id_var = int(input("Costumer id to delete: "))
        costumer = Costumer(id=id_var)
        delete_costumers = CostumerDAO.delete(costumer)
        print(f"Delete costumer: {delete_costumers}")

    else:
        print("Exit the app")