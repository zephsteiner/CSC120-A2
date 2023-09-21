from typing import Dict, Union, Optional

class Computer:
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
        self.operatingSystem = new_os
        if new_os is not None:
            self.operatingSystem = new_os # update details after installing new OS
        print(f"Update to {new_os} complete.")

    def updatePrice(self):
        if self.yearMade < 2000:
            self.price = 0 # too old to sell, donation only
        elif self.yearMade < 2012:
            self.price = 250 # heavily-discounted price on machines 10+ years old
        elif self.yearMade < 2018:
            self.price = 550 # discounted price on machines 4-to-10 year old machines
        else:
            self.price = 1000 # recent stuff

def main():
    newComputer: Computer = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)

if __name__ == "__main__":
    main()