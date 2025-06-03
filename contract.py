from algopy import ARC4Contract, abi
from algopy.stdlib import Txn, Global, Box
from algopy.abi import String

class Mywallet(ARC4Contract):

    @abi.abimethod()
    def deposit(self, name: abi.String) -> abi.String:
        # Store the name in a box called "adeelarifkhan" keyed by sender
        Box("adeelarifkhan")[Txn.sender].set(name.get())

        # Return confirmation message
        return abi.String("Deposit received from: " + name.get())

    @abi.abimethod()
    def withdraw(self, name: abi.String) -> abi.String:
        # Optional: Verify sender is in box or logic to control access
        # Return withdrawal message
        return abi.String("Withdrawal requested by: " + name.get())
