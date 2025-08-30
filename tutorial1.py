import curses
import subprocess
import time

def draw_border(win, height, width):
    win.border(0)

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.timeout(-1)  # Blocking input
    height, width = stdscr.getmaxyx()

    # Welcome Screen
    stdscr.clear()
    draw_border(stdscr, height, width)
    stdscr.addstr(2, 2, "Welcome to Linux Tutorial Series: Tutorial 1 - Introduction to the Linux Terminal")
    stdscr.addstr(4, 2, "In this tutorial, you'll learn basic Linux commands: ls, cd, and pwd.")
    stdscr.addstr(6, 2, "Press any key to start the lesson...")
    stdscr.refresh()
    stdscr.getch()

    # Lesson Screen
    stdscr.clear()
    draw_border(stdscr, height, width)
    lesson_text = [
        "Lesson: Basic Linux Commands",
        "",
        "1. ls - List directory contents",
        "   Example: ls",
        "   Try it in the prompt below!",
        "",
        "2. cd - Change directory",
        "   Example: cd /home",
        "   Try navigating to a directory!",
        "",
        "3. pwd - Print working directory",
        "   Example: pwd",
        "   Shows your current directory.",
        "",
        "Type a command in the prompt below and press Enter to test it."
    ]
    for i, line in enumerate(lesson_text):
        stdscr.addstr(2 + i, 2, line)
    
    # Command Prompt
    prompt_win = curses.newwin(3, width - 4, height - 5, 2)
    prompt_win.border(0)
    prompt_win.addstr(1, 1, "Enter command: ")
    stdscr.refresh()
    prompt_win.refresh()

    # Input handling
    curses.curs_set(1)  # Show cursor
    input_str = ""
    while True:
        prompt_win.clear()
        prompt_win.border(0)
        prompt_win.addstr(1, 1, f"Enter command: {input_str}")
        prompt_win.refresh()
        ch = stdscr.getch()
        
        if ch == 10:  # Enter key
            if input_str.lower() in ["exit", "quit"]:
                break
            try:
                # Execute command and capture output
                result = subprocess.run(input_str, shell=True, capture_output=True, text=True)
                output = result.stdout or result.stderr
            except Exception as e:
                output = f"Error: {str(e)}"
            
            # Display output
            output_win = curses.newwin(5, width - 4, height - 10, 2)
            output_win.border(0)
            output_win.addstr(1, 1, output[:width - 6])
            output_win.refresh()
            input_str = ""
            time.sleep(2)  # Show output briefly
        elif ch == 127:  # Backspace
            input_str = input_str[:-1]
        elif 32 <= ch <= 126:  # Printable characters
            input_str += chr(ch)

    # Exit Screen
    stdscr.clear()
    draw_border(stdscr, height, width)
    stdscr.addstr(2, 2, "Thanks for completing Tutorial 1!")
    stdscr.addstr(4, 2, "Press any key to exit...")
    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
