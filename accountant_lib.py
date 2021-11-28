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

@manager.assign('sprzedaz')
def sprzedaz(
        manager,
        filename=sys.argv[1], 
        item_id=sys.argv[2], 
        price=sys.argv[3], 
        amount=sys.argv[4]
        ):

    with open(filename) as store:
        acc_balance = store.readline()
        products = store.readlines()
        sale = False
        for line in products:
            if item_id in line:
                product_data = line.split(';')
                product_id = product_data[0]
                product_price = float(product_data[1])
                product_amount = int(product_data[2])
                if product_amount >= int(amount):
                    updated_amount = product_amount - int(amount)
                    updated_data = f'{item_id};{float(price)};{updated_amount}'
                    i = products.index(line)
                    products[i] = updated_data + '\n'
                    acc_balance = float(acc_balance) + (float(amount) * float(price))
                    sale = True
                else:
                    print(f'W magazynie jest za mało towaru! Stan: {product_amount} szt.')
                break
            else:
                continue
    if not sale:
        print('Brak produktu w magazynie!')  
    else:
        with open(filename, 'w') as store:
            store.write(str(acc_balance) + '\n') 
            for line in products:
                store.write(line)    
        with open('logs.txt', 'a') as logs:
            logs.write(f'Sprzedano {amount} szt. towaru: {item_id}. Saldo bieżące: {acc_balance} '+ '\n')
    

