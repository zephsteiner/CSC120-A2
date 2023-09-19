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
        print(f"Update to {new_os} complete.")

    def updatePrice(self, new_price):
        self.price = new_price
        print(f"Updated price to {new_price}.")
    # What methods will you need?