#include <stdlib.h>
#include <ncurses.h>
#include <stdio.h>

int main(void) {
    initscr();
    keypad(stdscr, TRUE);
    noecho();
    curs_set(0);

    const char *options[] = {
        "Start PythOS normally",
        "Start setup wizard",
        "Boot directly to logon",
        "Shutdown system"
    };

    const int n_options = sizeof(options) / sizeof(options[0]);

    int choice = 0;
    while (1) {
        clear();
        mvprintw(0, 0, "PythOS Boot Menu");
        mvprintw(1, 0, "Use arrow keys to navigate and Enter to select.");
        for (int i = 0; i < n_options; i++) {
            if (i == choice) {
                attron(A_REVERSE);
            }
            mvprintw(i + 2, 2, "%s", options[i]); /* use "%s" to avoid format-security warning */
            if (i == choice) {
                attroff(A_REVERSE);
            }
        }
        int input = getch();
        if (input == KEY_UP) {
            choice = (choice - 1 + n_options) % n_options;
        } else if (input == KEY_DOWN) {
            choice = (choice + 1) % n_options;
        } else if (input == '\n' || input == KEY_ENTER || input == 10 || input == 13) {
            endwin();
            if (choice == 0) {
                printf("Booting PythOS...\n");
                system("python3 boot.py");
            } else if (choice == 1) {
                printf("Starting setup wizard...\n");
                system("python3 setup.py");
            } else if (choice == 2) {
                printf("Booting directly to logon...\n");
                system("python3 logon.py");
            } else if (choice == 3) {
                printf("Shutting down...\n");
                system("shutdown now");
            }
            break;
        }
    }
    return 0;
}