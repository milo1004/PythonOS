import curses
import time
import sys
import subprocess

def get_drives():
    result = subprocess.run(['lsblk', '-dpno', 'NAME,SIZE,MODEL'], capture_output=True, text=True)
    lines = result.stdout.strip().split('\n')
    drives = []
    for line in lines:
        parts = line.split()
        if len(parts) >= 2:
            name = parts[0]
            size = parts[1]
            model = parts[2] if len(parts) == 3 else "Unknown"
            drives.append(f"{name} - {size} - {model}")
    return drives
print("Fetching drives...")
drives = get_drives()
    
menu = drives + ["Exit"]
def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    stdscr.addstr(1, w//2 - len("Select a Drive to be formatted and partitioned:")//2, "Select a Drive to be formatted and partitioned:", curses.A_BOLD)
    for idx, row in enumerate(menu): 
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx  
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y, x, row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y, x, row)
        stdscr.refresh()
def main(stdscr):
    h, w = stdscr.getmaxyx()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    stdscr
    curses.curs_set(0)
    current_row = 0
    print_menu(stdscr, current_row)
    while True:
        key = stdscr.getch()
        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
            print_menu(stdscr, current_row)    
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
            print_menu(stdscr, current_row)        
        elif key == curses.KEY_ENTER or key in [10, 13]:
            print_menu(stdscr, current_row)
            stdscr.addstr(0, 0, f"You selected '{menu[current_row]}'")
            stdscr.refresh()
            if menu[current_row] == "Exit":
                print_menu(stdscr, current_row)
                stdscr.refresh()
                stdscr.addstr(0, 0, "Exiting...")
                stdscr.refresh()
                time.sleep(1)
                sys.exit()
            else:
                stdscr.clear()
                stdscr.addstr(h//2, w//2 - len(f"Formatting the drive WILL WIPE ALL DATA ON THE DEVICE: {menu[current_row].split()[0]}, confirm?(y/n)")//2, f"Formatting the drive WILL WIPE ALL DATA ON THE DEVICE: {menu[current_row].split()[0]}, cofirm? (y/n)", curses.A_BOLD)
                stdscr.refresh()
                yn = stdscr.getch()
                if yn == ord('y') or yn == ord('Y'):
                    stdscr.clear()
                    stdscr.addstr(h//2, w//2 - len("Formatting...")//2, "Formatting...", curses.A_BOLD)
                    stdscr.refresh()
                    time.sleep(2)  # Simulate formatting time
                    stdscr.clear()
                    stdscr.addstr(h//2, w//2 - len("Format Complete!")//2, "Format Complete!", curses.A_BOLD)
                    stdscr.refresh()
                    time.sleep(1)
                else:
                    stdscr.clear()
                    stdscr.addstr(h//2, w//2 - len("Format Cancelled.")//2, "Format Cancelled.", curses.A_BOLD)
                    stdscr.refresh()
                    time.sleep(1)
curses.wrapper(main)
