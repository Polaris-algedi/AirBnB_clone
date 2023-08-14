#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class_dict = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    """
        Class for the command interpreter.

        Attributes:
            prompt (str): Prompt text for the command line.
    """

    prompt = "(hbnb) "

    def do_create(self, class_name):
        """
        Create a new instance of the specified class.

        Args:
            class_name (str): The name of the class.

        Usage: create <class_name>
        """
        if class_name:
            if class_name in class_dict:
                new_instance = class_dict[class_name]()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def _validate_instance_command(self, line):
        """
        Helper method to validate and extract information from a command line.

        Args:
            line (str): The input command line.

        Returns:
            str: The instance key if valid and found, otherwise False.
        """
        if line:
            commands = shlex.split(line)
            if commands[0] in class_dict:
                if len(commands) >= 2:
                    objs = storage.all()
                    key = f"{commands[0]}.{commands[1]}"
                    if key in objs:
                        return key
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        return False

    def do_show(self, line):
        """
        Display information about a specified instance.

        Args:
            line (str): The input command line.

        Usage: show <class_name> <instance_id>
        """
        key = self._validate_instance_command(line)
        if key:
            objs = storage.all()
            print(objs[key])

    def do_destroy(self, line):
        """
        Delete a specified instance.

        Args:
            line (str): The input command line.

        Usage: destroy <class_name> <instance_id>
        """
        key = self._validate_instance_command(line)
        if key:
            objs = storage.all()
            del objs[key]
            storage.save()

    def do_all(self, line):
        """
        Display information about all instances or instances
        of a specific class.

        Args:
            line (str): The input command line.

        Usage: all [class_name]
        """
        objs = storage.all()
        if objs:
            objs_list = list(objs.values())
            if not line:
                objs_list = [str(o) for o in objs_list]
                print(objs_list)
            else:
                objs_list = [str(o) for o in objs_list
                             if type(o).__name__ == line]
                if objs_list:
                    print(objs_list)
                else:
                    print("** class doesn't exist **")

    def do_update(self, line):
        """
        Update attributes of a specified instance.

        Args:
            line (str): The input command line.

        Usage: update <class_name> <instance_id> <attribute_name>
        <attribute_value>
        """
        key = self._validate_instance_command(line)
        commands = shlex.split(line)
        if key:
            if len(commands) < 3:
                print("** attribute name missing **")
                return
            if len(commands) < 4:
                print("** value missing **")
                return

            objs = storage.all()
            setattr(objs[key], commands[2], commands[3])
            objs[key].save()

    def count(self, cls_name):
        """
        Count the number of instances of a specified class.

        Args:
            cls_name (str): The name of the class.

        This method counts the instances of the specified class
        and prints the count.
        """
        objs = list(storage.all().values())
        count = sum(1 for o in objs if type(o).__name__ == cls_name)
        print(count)

    def default(self, line):
        """
        Default method called for unrecognized commands.

        Args:
            line (str): The input command line.

        This method checks for specific patterns of commands
        and delegates to corresponding methods.

        Available Patterns:
            - "<class name>.all()":
                Calls the "do_all()" method with the class name.
            - "<class name>.count()":
                Calls the "count()" method with the class name.
        """
        cmd = {
            "all()": self.do_all,
            "count()": self.count
        }

        commands = line.split(".")
        if len(commands) > 1 and commands[1] in cmd:
            cmd[commands[1]](commands[0])

    def do_EOF(self, line):
        """Handles the end-of-file condition,
        by exiting gracefully
        """
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
