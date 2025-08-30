import curses
import subprocess
import os

def draw_border(win, height, width):
    win.border(0)

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.timeout(-1)  # Blocking input
    height, width = stdscr.getmaxyx()

    # Welcome Screen
    stdscr.clear()
    draw_border(stdscr, height, width)
    stdscr.addstr(2, 2, "Welcome to Linux Tutorial Series: Tutorial 1 - Introduction to the Terminal")
    stdscr.addstr(4, 2, "Learn basic commands: ls, cd, and pwd.")
    stdscr.addstr(6, 2, "Press any key to start the lesson (or Ctrl+C to exit)...")
    stdscr.refresh()
    try:
        stdscr.getch()
    except KeyboardInterrupt:
        # Jump to exit screen on Ctrl+C
        stdscr.clear()
        draw_border(stdscr, height, width)
        stdscr.addstr(2, 2, "Exiting Tutorial 1...")
        stdscr.addstr(4, 2, "Press any key to exit...")
        stdscr.refresh()
        stdscr.getch()
        return

    # Lesson Screen
    stdscr.clear()
    draw_border(stdscr, height, width)
    lesson_text = [
        "Lesson: Basic Terminal Commands",
        "",
        "1. ls - List directory contents",
        "   Example: ls",
        "   Try it in the prompt below!",
        "",
        "2. cd - Change directory",
        "   Example: cd ~/Documents, cd .., cd ~",
        "   Try navigating to a directory!",
        "",
        "3. pwd - Print working directory",
        "   Example: pwd",
        "   Shows your current directory.",
        "",
        "Type a command and press Enter to test it. Press Ctrl+C to exit."
    ]
    for i, line in enumerate(lesson_text):
        stdscr.addstr(2 + i, 2, line)
    stdscr.addstr(height - 3, 2, "Press any key to start the interactive shell...")
    stdscr.refresh()
    try:
        stdscr.getch()
    except KeyboardInterrupt:
        # Jump to exit screen on Ctrl+C
        stdscr.clear()
        draw_border(stdscr, height, width)
        stdscr.addstr(2, 2, "Exiting Tutorial 1...")
        stdscr.addstr(4, 2, "Press any key to exit...")
        stdscr.refresh()
        stdscr.getch()
        return

    # Interactive Shell Setup
    stdscr.clear()
    draw_border(stdscr, height, width)
    output_win = curses.newwin(height - 5, width - 4, 2, 2)  # Output area
    prompt_win = curses.newwin(3, width - 4, height - 5, 2)  # Prompt at bottom
    output_win.border(0)
    prompt_win.border(0)
    output_win.refresh()
    prompt_win.refresh()
    output_lines = []  # Store command outputs
    current_dir = os.getcwd()  # Track current working directory
    input_str = ""
    last_prompt = ""
    curses.curs_set(1)  # Show cursor

    # Initial prompt display
    prompt_win.addstr(1, 1, f"{current_dir}$ {input_str}"[:width - 6])
    prompt_win.refresh()

    while True:
        try:
            ch = stdscr.getch()
        except KeyboardInterrupt:
            break  # Exit on Ctrl+C

        if ch == 10:  # Enter key
            if input_str.lower() in ["exit", "quit"]:
                break

            # Clear input string
            command = input_str
            input_str = ""

            # Handle 'cd' command
            if command.startswith("cd "):
                target_dir = command[3:].strip()
                if target_dir == "~":
                    target_dir = os.path.expanduser("~")
                elif target_dir == "..":
                    target_dir = os.path.dirname(current_dir)
                try:
                    os.chdir(target_dir)
                    current_dir = os.getcwd()
                    output_lines.append(f"Changed directory to {current_dir}")
                except FileNotFoundError:
                    output_lines.append(f"Error: Directory '{target_dir}' not found")
                except PermissionError:
                    output_lines.append(f"Error: Permission denied for '{target_dir}'")
                except Exception as e:
                    output_lines.append(f"Error: {str(e)}")
            else:
                # Execute other commands
                try:
                    result = subprocess.run(
                        command,
                        shell=True,
                        capture_output=True,
                        text=True,
                        cwd=current_dir,
                        timeout=5
                    )
                    output = (result.stdout or result.stderr).strip()
                    if output:
                        output_lines.extend(output.split("\n"))
                    else:
                        output_lines.append("(no output)")
                except subprocess.TimeoutExpired:
                    output_lines.append("Error: Command timed out")
                except Exception as e:
                    output_lines.append(f"Error: {str(e)}")

            # Update output window
            output_win.clear()
            output_win.border(0)
            max_lines = height - 7  # Available lines in output window
            start_idx = max(0, len(output_lines) - max_lines)
            for i, line in enumerate(output_lines[start_idx:]):
                output_win.addstr(i + 1, 1, line[:width - 6])
            output_win.refresh()

            # Update prompt
            new_prompt = f"{current_dir}$ {input_str}"[:width - 6]
            if new_prompt != last_prompt:
                prompt_win.addstr(1, 1, " " * (width - 6))  # Clear previous text
                prompt_win.addstr(1, 1, new_prompt)
                prompt_win.refresh()
                last_prompt = new_prompt
        elif ch == 127:  # Backspace
            input_str = input_str[:-1]
            # Update prompt only if changed
            new_prompt = f"{current_dir}$ {input_str}"[:width - 6]
            if new_prompt != last_prompt:
                prompt_win.addstr(1, 1, " " * (width - 6))  # Clear previous text
                prompt_win.addstr(1, 1, new_prompt)
                prompt_win.move(1, 1 + len(new_prompt))  # Move cursor
                prompt_win.refresh()
                last_prompt = new_prompt
        elif ch == 9:  # Tab key (ignore)
            continue
        elif 32 <= ch <= 126:  # Printable characters
            input_str += chr(ch)
            # Update prompt only if changed
            new_prompt = f"{current_dir}$ {input_str}"[:width - 6]
            if new_prompt != last_prompt:
                prompt_win.addstr(1, 1, " " * (width - 6))  # Clear previous text
                prompt_win.addstr(1, 1, new_prompt)
                prompt_win.move(1, 1 + len(new_prompt))  # Move cursor
                prompt_win.refresh()
                last_prompt = new_prompt

    # Exit Screen
    stdscr.clear()
    draw_border(stdscr, height, width)
    stdscr.addstr(2, 2, "Thanks for completing Tutorial 1!")
    stdscr.addstr(4, 2, "Press any key to exit...")
    stdscr.refresh()
    try:
        stdscr.getch()
    except KeyboardInterrupt:
        pass  # Allow clean exit even if Ctrl+C is pressed

if __name__ == "__main__":
    curses.wrapper(main)
