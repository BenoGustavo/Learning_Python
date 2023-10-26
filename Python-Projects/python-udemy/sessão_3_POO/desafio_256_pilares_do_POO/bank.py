from accounts import SavingsAccount,CheckingAccount
from Costumer import Costumer

class Bank():
    def __init__(self,agencys:list,costumer: Costumer,checkingAccount: CheckingAccount = None, savingsAccount: SavingsAccount = None) -> None:
        self.__agencys = agencys
        self.__owner = costumer
        self.__checkingAccount = checkingAccount
        self.__savingsAccount = savingsAccount

    def setCheckingAccount(self, newCheckingAccount: CheckingAccount):
        self.__checkingAccount = newCheckingAccount

    def setSavingsAccount(self,newSavingsAccount: SavingsAccount):
        self.__savingsAccount = newSavingsAccount

    def authCostumer(self) -> bool:
        if self.__owner.savingsAccount.agency in self.__agencys and self.__owner.checkingAccount.agency in self.__agencys:
            return True
        return False