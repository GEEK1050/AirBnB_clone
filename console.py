#!/usr/bin/python3
"""command interpreter"""

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """commandLine Class"""
    def emptyline(self):
        """emptyline"""
        pass

    def do_EOF(self, args):
        """ctrl+d"""
        print()
        return True

    def do_quit(self, args):
        """ctrl+z"""
        quit()
        return True

    if sys.stdin.isatty():
        prompt = "(hbnb)"
    else:
        prompt = "(hbnb)\n"

    def main():
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
