"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)

    Cliente
        Clente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:

Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

from accounts import SavingsAccount,CheckingAccount
from bank import Bank
from Costumer import Costumer

if __name__ == "__main__":
    costumer1 = Costumer("Gustavo",20,"Male")
    costumer1.savingsAccount = SavingsAccount(1,123,200)
    costumer1.checkingAccount = CheckingAccount(2,1234,300)
    
    bank1 = Bank([1,2],costumer1,costumer1.checkingAccount,costumer1.savingsAccount)

    bank2 = Bank([2,3],costumer1,costumer1.checkingAccount,costumer1.savingsAccount)

    if bank1.authCostumer():
        print("Bank 1 Sucess")
        
        print(costumer1.checkingAccount.balance)
        costumer1._checkingAccount.withdraw(100)
        print(costumer1.checkingAccount.balance)
    else:
        print("Bank 1 Fail")

    if bank2.authCostumer():
        print("Bank 2 Sucess")
    else:
        print("Bank 2 Fail")