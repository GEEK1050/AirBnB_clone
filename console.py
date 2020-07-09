#!/usr/bin/python3
"""command interpreter"""

import cmd
import shlex
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """commandLine Class"""
    my_classes = ["BaseModel", "User", "State", "City", "Place", "Amenity",
                  "Review"]
    my_args = ['all', 'count', 'show', 'destroy', 'update']

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

    def do_create(self, args):
        """create new instance of the class passed as args"""
        args = shlex.split(args)
        if not len(args):
            print("** class name missing **")
        elif args[0] not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
        else:
            my_obj = eval(args[0])()
            my_obj.save()
            print(my_obj.id)

    def do_show(self, args):
        """Prints the string representation of an instance"""
        if not len(args):
            print("** class name missing **")
            return
        arguments = shlex.split(args)
        className = arguments[0]
        if className not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
            return
        if len(arguments) is not 2:
            print("** instance id missing **")
            return

        instanceId = arguments[1]
        key_ins = arguments[0] + "." + arguments[1]
        my_obj = storage.all()

        if key_ins not in my_obj.keys():
            print("** no instance found **")
        else:
            print(my_obj[key_ins])

    def do_destroy(self, args):
        """delete object"""
        if not len(args):
            print("** class name missing **")
            return
        arguments = shlex.split(args)
        className = arguments[0]

        if className not in HBNBCommand.my_classes:

            print("** class doesn't exist **")
            return
        if len(arguments) != 2:
            print("** instance id missing **")
            return

        instanceId = arguments[1]
        key_ins = arguments[0] + "." + arguments[1]
        my_obj = storage.all()

        if key_ins not in my_obj.keys():
            print("** no instance found **")
        else:
            del my_obj[key_ins]
            storage.save()

    def do_all(self, args):
        """print all objects stocked"""
        list_obj = []
        if not len(args):
            all_obj = storage.all()
            for element in all_obj.values():
                list_obj.append(str(element))
            if len(list_obj):
                print(list_obj)
            return

        first_arg = args.split(" ")
        if first_arg[0] not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
        else:
            all_obj = storage.all()
            for element in all_obj.values():
                if element.__class__.__name__ == first_arg[0]:
                    list_obj.append(str(element))
            if len(list_obj):
                print(list_obj)

    def do_update(self, args):
        """update instance based in the class name ans id"""
        args = shlex.split(args)
        my_obj = storage.all()
        try:
            basic = args[0] + "." + args[1]
        except Exception:
            pass

        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1 and args[0] in self.my_classes:
            print("** instance id missing **")
        elif args[0] not in self.my_classes:
            print("** class doesn't exist **")
        elif basic not in my_obj.keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            setattr(my_obj[basic], args[2], args[3])
            storage.save()

    def default(self, args):
        """parsing line"""
        if len(args):
            cmmd = args.split('.')
            if cmmd[0] in HBNBCommand.my_classes:
                cmmd[1] = cmmd[1].split('(')
                arg = cmmd[1][1].strip(')')
                cmmd[1] = cmmd[1][0]
                if cmmd[1] in HBNBCommand.my_args and not len(arg):
                    li = "HBNBCommand.do_{}(self, '{}')".format(
                          cmmd[1], cmmd[0])
                    eval(li)
                elif cmmd[1] in HBNBCommand.my_args:
                    arg = cmmd[0] + ' ' + arg.strip("'").strip('"')
                    li = "HBNBCommand.do_{}(self, '{}')".format(
                          cmmd[1], arg)
                    eval(li)

    def do_count(self, args):
        """counting key number passing in prompt"""
        list_obj = []
        all_obj = storage.all()
        for element in all_obj.values():
            if element.__class__.__name__ == args:
                list_obj.append(str(element))
        print(len(list_obj))

if __name__ == "__main__":
    HBNBCommand().cmdloop()
