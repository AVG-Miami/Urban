
import threading
balanse=1000
class BankAccount():
    global balanse
    def deposit(self,amount):
        global balanse
        with threading.Lock():
            balanse+=amount
        print("Deposited {}, new balance is {}".format(amount, balanse))
    def withdraw(self,amount):
        global balanse
        with threading.Lock():
            balanse= balanse - amount
        print("Withdrew {}, new balance is {}".format(amount, balanse))


def deposit_task(account, amount):
  for _ in range(5):
    account.deposit(amount)

def withdraw_task(account, amount):
  for _ in range(5):
    account.withdraw(amount)
account = BankAccount()

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()