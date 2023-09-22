"""
   Filename: oo_resale_shop.py
Description: This file creates the ResaleShop class, which stores information about a
             computer resale store. It contains methods to update and display this
             information.
     Author: Zephyr Steiner
       Date: 21 September 2022
"""
# import functions from the typing module
from typing import Dict, Optional

# import class and methods created in computer.py
from computer import Computer

class ResaleShop:
    """
    A class to represent a computer resale store.

    ...

    Attributes
    ----------
    itemID : int
        the number of computers that have ever been in the store's inventory
    inventory : Dict
        a dictionary where we'll store our inventory
        The key is an int representing the item number
        The value is an object containing information about the machine 

    Methods
    -------
    buy(computer: object):
        Takes in an object containing all the information about a computer,
        adds it to the inventory, returns the assigned item_id
    sell(item_id: int):
        Takes in an item_id, removes the associated computer if it is the inventory, 
        prints error message otherwise
    refurbish(item_id: int, new_os: Optional[str] = None):
        Takes in an item_id and optional new_os, updates the price and operating system
        attributes of the associated computer object if it is in the inventory, 
        prints error message otherwise
    print_inventory():
        prints the entire inventory if it is not empty, returns error message otherwise
    """
    
    itemID: int = 0
    inventory : Dict[int, Computer] = {}

    def __init__(self, item_id: int, inventory: Dict):
        self.itemID = item_id
        self.inventory = inventory
    
    def buy(self, computer: object):
        """
        Takes in an object containing all the information about a computer,
        adds it to the inventory, returns the assigned item_id
        """
        self.itemID += 1
        self.inventory[self.itemID] = computer
        return self.itemID

    def sell(self, item_id: int):
        """
        Takes in an item_id, removes the associated computer if it is the inventory, 
        prints error message otherwise
        """
        if item_id in self.inventory:
            del self.inventory[item_id]
            print(f"Item {item_id} sold.")
        else:
            print(f"Item {item_id} not found. Please select another item to sell.")

    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        """
        Takes in an item_id and optional new_os, updates the price and operating system
        attributes of the associated computer object if it is in the inventory, 
        prints error message otherwise
        """
        if item_id in self.inventory:
            self.inventory[item_id].updatePrice()
            if new_os is not None:
                self.inventory[item_id].updateOS(new_os)
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")

    def print_inventory(self):
        """
        prints the entire inventory if it is not empty, returns error message otherwise

        """
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for item_id in self.inventory:
                # Print its details
                print(f'Item ID: {item_id} : {self.inventory[item_id].__dict__}')
        else:
            print("No inventory to display.")