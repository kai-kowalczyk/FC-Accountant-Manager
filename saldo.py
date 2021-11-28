import sys
from accountant_lib import manager

manager.run_command(
            'saldo', 
            filename=sys.argv[1], 
            amount=sys.argv[2], 
            comment=sys.argv[3]
)
