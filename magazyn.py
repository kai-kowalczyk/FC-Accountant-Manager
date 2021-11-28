import sys
from accountant_lib import manager

filename = sys.argv[1]
items = sys.argv[2:]

manager.run_command(
            'magazyn',
            filename,
            *items
)