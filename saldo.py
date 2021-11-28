import sys
from accountant_lib import manager

filename = sys.argv[1]
amount = sys.argv[2]
comment = sys.argv[3]

manager.run_command('saldo', filename, amount, comment)
