class Atm:
    def __init__(self,cardNumber,pin):
        self.cardNumber = cardNumber
        self.pin = pin
         

    def checkBalance(self):
       print('your balance is')
    def withdraw(self, ammount):
        newAmmount=5000 - ammount
        print("you have withdwrawn ammount"+str(ammount)+'your remaining balance is'+str(newAmmount))
# Define some students
john = Atm("xxxxxx9090", 1010)
jane = Atm("xxxxxx1010", 9090)

