import sys
from accountant_lib import manager

filename = sys.argv[1]
manager.run_command('konto', filename)