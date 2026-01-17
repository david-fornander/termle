
import sys

from app.commands import browse as browse_command
from app.commands import word as word_command

def main():

    if len(sys.argv) == 1:
        print("help.txt")
        return

    args = sys.argv
    args = args[1:] # Removes termle as a command which has a "-" in it int the path
    flags = flag_check(args)
    cmd = args[0]

    if cmd == "browse":
        browse_command.run(flags, args[1:])
    elif cmd == "word":
        word_command.run(flags, args[1:])
    else:
        browse_command.run(flags, args[0:])


def flag_check(args):
    flags = []
    for i in range(len(args) - 1, 0, -1):
        if "-" in args[i]:
            flags.append(args[i][1:])
            args.remove(args[i])
    return flags


if __name__ == "__main__":
    main()
