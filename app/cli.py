
import sys
import importlib.resources as res

from app.commands import search as search_command

def main():

    if len(sys.argv) == 1:
        print("help.txt")
        return

    args = sys.argv
    flag = flag_check(args)
    print(flag)
    cmd = args[1]

    if cmd == "search":
        search_command.run(flag, args[2:])

    else:
        search_command.run(flag, args[1:])


def flag_check(args):
    for arg in args:
        if "-" in arg:
            args.remove(arg)
            return arg[1:]


if __name__ == "__main__":
    main()
