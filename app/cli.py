
import sys

from app.commands import search as search_command

def main():

    if len(sys.argv) == 1:
        print("Help...")
        return

    cmd = sys.argv[1]

    if cmd == "search":
        search_command.run(" ".join(sys.argv[2:]))


if __name__ == "__main__":
    main()
