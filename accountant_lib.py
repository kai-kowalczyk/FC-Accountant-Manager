import sys

class Manager:

    def __init__(self):
        self.allowed_commands = {}

    def assign(self, command):
        print('in assign')
        print(command)
        def add_command(func):
            print('in add_command')
            print(command)
            self.allowed_commands[command] = func
            print(self.allowed_commands)
        return add_command
        

    def run_command(self, command):
        print('in run_command')
        print(command)
        print(self.allowed_commands)
        if command not in self.allowed_commands:
            print('Wprowadzono nieprawidłową komendę.')
        else:
            print('good')
            self.allowed_commands[command](self)

manager = Manager()

@manager.assign('saldo')
def saldo(
        manager, 
        filename=sys.argv[1], 
        amount=sys.argv[2], 
        comment=sys.argv[3]
        ):
        with open(filename) as store:
            acc_balance = store.readline()
            products = store.readlines()
            acc_balance = float(acc_balance) + float(amount)     
        with open(filename, 'w') as store:
            store.write(str(acc_balance) + '\n')
            for product in products:
                store.write(product)
        with open('logs.txt', 'a') as logs:
            logs.write(f'Stan konta zmienił się o {amount}. Komentarz: {comment}. Saldo bieżące: {acc_balance}' + '\n')

