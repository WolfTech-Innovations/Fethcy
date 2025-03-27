# Made by WolfTech Innovations
import sys
import os
import time
import subprocess
from art import *
import colorama
import curses
from curses import wrapper
from colorama import init, Fore, Style
init()

tprint("Welcome To Fetchy")
time.sleep(4)
subprocess.run("clear")

stdscr = curses.initscr()
curses.noecho()
stdscr.keypad(True)

def client(stdscr, cmd):
    stdscr.clear()
    stdscr.addstr(2, 0, "[STARTING] " + ' '.join(cmd), curses.A_BOLD)
    stdscr.refresh()
    time.sleep(1)

    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate()

        if process.returncode == 0:
            stdscr.clear()
            stdscr.addstr(2, 0, "[FINISHED] Success.", curses.A_BOLD)
            stdscr.addstr(4, 0, output)
        else:
            stdscr.clear()
            stdscr.addstr(2, 0, "[ERROR] " + error, curses.A_BOLD)
    except subprocess.CalledProcessError:
        stdscr.clear()
        stdscr.addstr(2, 0, "[NO INTERNET] Connection issue.", curses.A_BOLD)
    except Exception as e:
        stdscr.clear()
        stdscr.addstr(2, 0, "[ERROR] " + str(e), curses.A_BOLD)

    stdscr.refresh()
    stdscr.getch()

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()

    stdscr.addstr(0, 0, "Fetchy - Select command", curses.A_BOLD)
    stdscr.addstr(1, 0, "Press 'Q' to quit.", curses.A_DIM)
    stdscr.refresh()

    cmds = [
        ["git", "status"],
        ["git", "pull"],
        ["git", "push"],
        ["git", "clone"]
    ]

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Fetchy - Select command", curses.A_BOLD)
        stdscr.addstr(2, 0, "Choose command:")

        for i, cmd in enumerate(cmds):
            stdscr.addstr(4 + i, 0, f"{i + 1}: {' '.join(cmd)}")

        stdscr.refresh()
        key = stdscr.getch()

        if key == ord('q'):
            break
        elif ord('1') <= key <= ord('4'):
            selected_cmd = cmds[key - ord('1')]

            if selected_cmd[1] == "clone" or selected_cmd[1] == "push":
                stdscr.clear()
                stdscr.addstr(6, 0, "Enter repository URL:")
                stdscr.refresh()
                curses.echo()
                repo_url = stdscr.getstr(7, 0, 80).decode("utf-8")
                curses.noecho()
                selected_cmd.append(repo_url)

            client(stdscr, selected_cmd)
        else:
            continue

curses.wrapper(main)
