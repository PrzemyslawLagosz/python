

class Result:
    """docstring for Resoult."""

    def __init__(self, isSuccess: bool, message, value=None):
        self.isSuccess = isSuccess
        self.message = message
        self.value = value

    def __str__(self):
        lista = [self.isSuccess, self.message, self.value]
        return str(self.isSuccess) + ' ' + str(self.message) + ' '+ str(self.value)



class BankAccount:
 
    def __init__(self, balance=0):

        self.balance = balance

    def deposit(self, amount):

        self.balance += amount
        print('You just deposit: ', amount)
        print('You actual balance is: ', self.balance)

    def withdrawl(self, amount):

        if self.balance >= amount:

            self.balance -= amount
            print('You just withdraw: ', amount)
            print('You actual balance is: ', self.balance)

            return Result(True, 'Wpłacono kasę', amount)

        else:

            print('Not enough money')
            print('You actual balance is: ', self.balance)

            return Result(False, 'Wpłacono kasę', amount)

    def __str__(self) -> str:
        return str(self.balance)


# Klasa dziecko rozniaca sie od wyzej klasy RODZIC kwotą minimalna poniezej korej nie mozna zejsc

class MinimumBalanceAccount(BankAccount):

    def __init__(self, balance=0, minimumBalance=1000):
        super().__init__(balance)
        self.minimumBalance = minimumBalance

    def withdrawl(self, amount):
        if self.balance - amount > self.minimumBalance:
            return super().withdrawl(amount)

        else:
            print('Przekroczono minimalny balans konta')

        return Result(False, 'Przekroczono minimalny balans konta')


min_przemo = MinimumBalanceAccount()

min_przemo.deposit(1500)
# You just deposit:  1500
# You actual balance is:  1500

min_przemo.withdrawl(400)
#You just withdraw:  400
#You actual balance is:  1100

min_przemo.withdrawl(1400)
#Przekroczono minimalny balans konta


