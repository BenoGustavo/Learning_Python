from accounts import Account

class Person():
    def __init__(self,name: str,age:int,sex: str) -> None:
        self._name = name
        self._age = age
        self._sex = sex
        self._checkingAccount = None
        self._savingsAccount = None
    
    @property
    def checkingAccount(self) -> Account:
        return self._checkingAccount

    @checkingAccount.setter
    def checkingAccount(self,account: Account):
        ...
    
    @property
    def savingsAccount(self) -> Account:
        return self._savingsAccount

    @savingsAccount.setter
    def savingsAccount(self,account: Account):
        ...

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self,newName:str) ->None:
        ...
    
    @property
    def age(self) ->int:
        return self._age

    @age.setter
    def age(self,newAge) -> int:
        ...

class Costumer(Person):
    def __init__(self, name: str, age: int, sex: str) -> None:
        super().__init__(name, age, sex)

    @Person.checkingAccount.setter
    def checkingAccount(self,newAccount : Account):
        self._checkingAccount = newAccount

    @Person.savingsAccount.setter
    def savingsAccount(self,newAccount : Account):
        self._savingsAccount = newAccount

    @Person.name.setter
    def name(self,newName:str):
        if not isinstance(newName,str):
            raise ValueError("Your name needs to be a valid string")
        
        self._name = newName

    @Person.age.setter
    def age(self,newAge:int):
        if not isinstance(newAge,int):
            raise ValueError("Your age needs to be a valid intenger")
        
        self._age = newAge