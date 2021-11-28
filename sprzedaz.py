import sys
from accountant_lib import manager

manager.run_command(
            'sprzedaz',
            filename=sys.argv[1],
            item_id=sys.argv[2],
            price=sys.argv[3],
            amount=sys.argv[4]
)