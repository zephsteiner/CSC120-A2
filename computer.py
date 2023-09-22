"""
   Filename: computer.py
Description: This file creates the Computer class, which stores information about a given
             computer. It contains functions to update some of this information.
     Author: Zephyr Steiner
       Date: 21 September 2022
"""

class Computer:
    """
    A class to represent a computer.

    ...

    Attributes
    ----------
    description: str
    processorType: str
    hardDriveCapacity: int
    memory: int
    operatingSystem: str
    yearMade: int
    price: int

    Methods
    -------
    updateOS(new_os):
        Takes in a new_os and updates the operatingSystem attribute with new information
    updatePrice():
        Based on the yearMade, updates the price attribute with new information
    """

    description: str = ""
    processorType: str = ""
    hardDriveCapacity: int = 0
    memory: int = 0
    operatingSystem: str = ""
    yearMade: int = 0
    price: int = 0

    def __init__(self, description: str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int ):
        self.description = description
        self.processorType = processor_type
        self.hardDriveCapacity = hard_drive_capacity
        self.memory = memory
        self.operatingSystem = operating_system
        self.yearMade = year_made
        self.price = price
        
    def updateOS(self, new_os):
        """
        Takes in a new_os and updates the operatingSystem attribute with new information
        """
        self.operatingSystem = new_os
        print(f"Update to {new_os} complete.")

    def updatePrice(self):
        """
        Based on the yearMade, updates the price attribute with new information
        """
        if self.yearMade < 2000:
            self.price = 0 # too old to sell, donation only
        elif self.yearMade < 2012:
            self.price = 250 # heavily-discounted price on machines 10+ years old
        elif self.yearMade < 2018:
            self.price = 550 # discounted price on machines 4-to-10 year old machines
        else:
            self.price = 1000 # recent stuff