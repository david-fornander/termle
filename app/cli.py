
import sys
import importlib.resources as res

from app.commands import browse as browse_command

def main():

    if len(sys.argv) == 1:
        print("help.txt")
        return

    args = sys.argv
    flags = flag_check(args)
    cmd = args[1]

    if cmd == "browse":
        browse_command.run(flags, args[2:])

    else:
        browse_command.run(flags, args[1:])


def flag_check(args):
    flags = []
    for arg in args:
        if "-" in arg:
            flags.append(arg[1:])
            args.remove(arg)
    return flags


if __name__ == "__main__":
    main()
