# Import the functions and class created in computer.py
from computer import Computer
# Import the functions and class created in oo_resale_shop.py
from oo_resale_shop import ResaleShop

def main():
    # Make the resale shop
    computerResaleStore: ResaleShop = ResaleShop(0,{})
    # Make a computer
    computer: Computer = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Add it to the resale store's inventory
    print(f"Buying {computer.description}")
    print("Adding to inventory...")
    computer_id = computerResaleStore.buy(computer)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    computerResaleStore.print_inventory()
    print("Done.\n")

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print(f"Refurbishing Item ID: {computer_id}, updating OS to {new_OS}.")
    print("Updating inventory...")
    computerResaleStore.refurbish(computer_id, new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    computerResaleStore.print_inventory()
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling Item ID:", computer_id)
    computerResaleStore.sell(computer_id)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    computerResaleStore.print_inventory()
    print("Done.\n")


# Calls the main() function when this file is run
if __name__ == "__main__": main()
