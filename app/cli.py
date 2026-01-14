
import sys

from app.commands import search as search_command

def main():

    if len(sys.argv) == 1:
        print("help.txt")
        return

    cmd = sys.argv[1]

    if cmd == "search":
        search_command.run(sys.argv[2:])

    else:
        search_command.run(sys.argv[1:])


if __name__ == "__main__":
    main()
