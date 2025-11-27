import curses
import subprocess
import os
import sys 

def main(stdscr):
    curses.curs_set(0)
    stdscr.keypad(True)
    curses.noecho()

    options = [
        "Start PythOS normally",
        "Start setup wizard",
        "Boot directly to logon",
        "Shutdown system",
	"Reset boot sector and shutdown"
    ]
    choice = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "PythOS Boot Menu")
        stdscr.addstr(1, 0, "Use arrow keys to navigate and Enter to select.")

        for idx, option in enumerate(options):
            if idx == choice:
                stdscr.attron(curses.A_REVERSE)
            stdscr.addstr(idx + 2, 2, option)
            if idx == choice:
                stdscr.attroff(curses.A_REVERSE)

        key = stdscr.getch()
        if key == curses.KEY_UP:
            choice = (choice - 1) % len(options)
        elif key == curses.KEY_DOWN:
            choice = (choice + 1) % len(options)
        elif key in [curses.KEY_ENTER, ord('\n'), ord('\r')]:
            break

    curses.endwin()
    actions = [
        ("Booting PythOS...", ["python3", "boot.py"]),
        ("Starting setup wizard...", ["python3", "setup.py"]),
        ("Booting directly to logon...", ["python3", "logon.py"]),
        ("Shutting down...", ["shutdown", "now"]),
	    ("Resetting...", ["python3", "reset.py"])
    ]
    print(actions[choice][0])
    subprocess.run(actions[choice][1])
    os.system("clear")
    sys.exit()
if __name__ == "__main__":
    curses.wrapper(main)
