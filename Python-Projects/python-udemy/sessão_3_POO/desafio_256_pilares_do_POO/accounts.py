class Account():
    def __init__(self,agency:int,accountNumber:int,Initialbalance :float|int|None = None) -> None:
        self.agency = agency
        self.NUMBER = accountNumber

        if Initialbalance != None:
            self.balance = Initialbalance
    
    def deposit(self,value:float) -> None:
        if value < 0:
            raise ValueError("Your deposit needs to be greather then 0")
        
        if isinstance(value,float | int) == False:
            raise ValueError("Your value needs to be an int or float value")
        
        self.balance = self.balance + value
    
    def withdraw(self,value:float) -> None:
        if isinstance(value,float | int) == False:
            raise ValueError("Your value needs to be an int or float value")
        
        if not value <= self.balance:
            print("Your withdraw can't be greather then you account balance.")
        else:
            self.balance -= value

    def __eq__(self, __value: int|float) -> bool:
        if self.balance == __value:
            return True
        return False
    
    def __gt__(self, __value: int|float) -> bool:
        if self.balance > __value:
            return True
        return False
    
    def __lt__(self, __value: int|float) -> bool:
        if self.balance < __value:
            return True
        return False

class CheckingAccount(Account):
    def __init__(self, agency: int, accountNumber: int, Initialbalance: float | int | None = None) -> None:
        super().__init__(agency, accountNumber, Initialbalance)

    def withdraw(self,value:float) -> None:
        if isinstance(value,float | int) == False:
            raise ValueError("Your value needs to be an int or float value")
        
        if not value <= self.balance + 100:
            print("Your withdraw can't be greather then you account balance.")
        else:
            self.balance -= value

class SavingsAccount(Account):
    def __init__(self, agency: int, accountNumber: int, limit  :int |float = 0 , Initialbalance: float | int | None = None) -> None:
        super().__init__(agency, accountNumber, Initialbalance)
        self.limit = -limit

    def withdraw(self, value: float|int) -> None:
        if isinstance(value,float | int) == False:
            raise ValueError("Your value needs to be an int or float value")
        
        balancePreview = self.balance - value

        if self.balance <= self.limit or balancePreview < self.limit:
            print("Limit reached")

        if not value <= self.balance:
            print("Your withdraw can't be greather then you account balance.")
        else:
            self.balance -= value