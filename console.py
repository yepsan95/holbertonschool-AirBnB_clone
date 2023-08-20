#!/usr/bin/python3
"""
Defines the HBNB command interpreter.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the Holberton AirBnb clone project.

    Attributes:
        prompt (str): The prompt to be shown in the command interpreter.
    """

    prompt = "(hbnb) "

    def emptyline(self):
        """
        Do nothing when receiving an empty line.
        """

        pass

    def do_quit(self, arg):
        """
        Exits the program.
        """

        return True

    def do_EOF(self, arg):
        """
        EOF signal to exit the program.
        """

        print("")
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
