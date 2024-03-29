import sys
from app.commands import Command


class ExitCommand(Command):
    def execute(self):
        super().__init__()
        self.name = "exit"
        sys.exit("Exiting...")