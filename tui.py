#!/usr/bin/env python3
"""
Linux TUI Tutorial - A terminal-based interactive Linux learning application
Built with Textual for a modern, responsive TUI experience.
"""

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Button, Static, Header, Footer, ListView, ListItem, Label
from textual.binding import Binding
from textual.reactive import reactive
from textual import events
from enum import Enum


class NavigationState(Enum):
    """Enum to track current navigation state"""
    MAIN_MENU = "main_menu"
    BASIC_SUBMENU = "basic_submenu"
    INTERMEDIATE_SUBMENU = "intermediate_submenu"
    ADVANCED_SUBMENU = "advanced_submenu"


class MenuButton(Button):
    """Custom button for menu items with hover effects"""
    
    def __init__(self, label: str, id: str = None):
        super().__init__(label, id=id)
        self.can_focus = True


class Sidebar(Container):
    """Sidebar container for navigation menu"""
    
    current_state = reactive(NavigationState.MAIN_MENU)
    
    def compose(self) -> ComposeResult:
        yield Static("📚 Linux Tutorial", classes="sidebar-title")
        yield Container(id="menu-container")
    
    def watch_current_state(self, state: NavigationState) -> None:
        """Update sidebar content based on current state"""
        self.update_menu(state)
    
    def update_menu(self, state: NavigationState) -> None:
        """Update the menu based on current navigation state"""
        menu_container = self.query_one("#menu-container", Container)
        menu_container.remove_children()
        
        if state == NavigationState.MAIN_MENU:
            menu_container.mount(MenuButton("Basic Topics", id="basic"))
            menu_container.mount(MenuButton("Intermediate Topics", id="intermediate"))
            menu_container.mount(MenuButton("Advanced Topics", id="advanced"))
            menu_container.mount(MenuButton("Exit", id="exit"))
        
        elif state == NavigationState.BASIC_SUBMENU:
            back_btn = MenuButton("← Back", id="back")
            back_btn.add_class("back-button")
            menu_container.mount(back_btn)
            
            title = Static("Basic Topics:")
            title.add_class("submenu-title")
            menu_container.mount(title)
            
            menu_container.mount(MenuButton("File Commands", id="basic-files"))
            menu_container.mount(MenuButton("Directory Navigation", id="basic-nav"))
            menu_container.mount(MenuButton("File Viewing", id="basic-view"))
            menu_container.mount(MenuButton("Permissions", id="basic-perms"))
        
        elif state == NavigationState.INTERMEDIATE_SUBMENU:
            back_btn = MenuButton("← Back", id="back")
            back_btn.add_class("back-button")
            menu_container.mount(back_btn)
            
            title = Static("Intermediate Topics:")
            title.add_class("submenu-title")
            menu_container.mount(title)
            
            menu_container.mount(MenuButton("Shell Scripting", id="inter-shell"))
            menu_container.mount(MenuButton("Process Management", id="inter-process"))
            menu_container.mount(MenuButton("User Management", id="inter-users"))
            menu_container.mount(MenuButton("Package Management", id="inter-packages"))
        
        elif state == NavigationState.ADVANCED_SUBMENU:
            back_btn = MenuButton("← Back", id="back")
            back_btn.add_class("back-button")
            menu_container.mount(back_btn)
            
            title = Static("Advanced Topics:")
            title.add_class("submenu-title")
            menu_container.mount(title)
            
            menu_container.mount(MenuButton("Networking", id="adv-network"))
            menu_container.mount(MenuButton("System Monitoring", id="adv-monitor"))
            menu_container.mount(MenuButton("Kernel Modules", id="adv-kernel"))
            menu_container.mount(MenuButton("Virtualization", id="adv-virtual"))


class MainContent(Container):
    """Main content area that displays tutorial content"""
    
    current_view = reactive("welcome")
    
    def compose(self) -> ComposeResult:
        yield Static(self.get_welcome_message(), id="content-text", classes="content")
    
    def get_welcome_message(self) -> str:
        return """
🐧 Welcome to the Linux TUI Tutorial! 🐧

This interactive tutorial will guide you through essential Linux concepts,
from basic file operations to advanced system administration.

📖 What you'll learn:

• Basic Topics: File system navigation, file operations, viewing files, permissions
• Intermediate Topics: Shell scripting, process management, user management, packages  
• Advanced Topics: Networking, system monitoring, kernel modules, virtualization

🎯 How to navigate:

• Use arrow keys ↑↓ or click to navigate the menu
• Press Enter or click to select a topic
• Use number keys 1, 2, 3 for quick access to main categories
• Press 'Escape' or click '← Back' to return to previous menu
• Press 'q' to quit at any time
• Press 'h' for help

🚀 Getting Started:

Choose a topic category from the sidebar to explore subtopics and start learning!
Each section will include explanations, examples, and interactive quizzes.

Good luck on your Linux journey! 🎓
        """
    
    def update_content(self, content: str):
        """Update the main content area"""
        content_widget = self.query_one("#content-text", Static)
        content_widget.update(content)


class LinuxTutorialApp(App):
    """Main application class for the Linux TUI Tutorial"""
    
    CSS = """
    /* Global styles */
    Screen {
        background: $background;
        color: $text;
    }
    
    /* Header and Footer */
    Header {
        dock: top;
        height: 3;
        background: $primary;
        color: $text;
    }
    
    Footer {
        dock: bottom;
        height: 3;
        background: $primary;
    }
    
    /* Main layout */
    #main-container {
        layout: horizontal;
        height: 1fr;
    }
    
    /* Sidebar styles */
    Sidebar {
        dock: left;
        width: 25;
        background: $surface;
        border-right: thick $primary;
        padding: 1;
    }
    
    .sidebar-title {
        text-align: center;
        text-style: bold;
        color: $accent;
        margin-bottom: 1;
        padding-bottom: 1;
        border-bottom: solid $primary;
    }
    
    .submenu-title {
        text-align: center;
        text-style: bold;
        color: $warning;
        margin: 1 0;
        padding: 1 0;
        border-bottom: solid $warning;
    }
    
    /* Menu container */
    #menu-container {
        height: auto;
    }
    
    /* Menu button styles */
    MenuButton {
        width: 100%;
        height: 3;
        margin-bottom: 1;
        background: $surface;
        border: solid $primary;
        text-align: center;
    }
    
    MenuButton:hover {
        background: $primary;
        color: $text;
        text-style: bold;
    }
    
    MenuButton:focus {
        background: $accent;
        color: $background;
        text-style: bold;
    }
    
    MenuButton#exit {
        margin-top: 2;
        background: $error;
        border: solid $error;
    }
    
    MenuButton#exit:hover {
        background: $error-darken-1;
    }
    
    .back-button {
        background: $warning;
        border: solid $warning;
        color: $background;
        text-style: bold;
    }
    
    .back-button:hover {
        background: $warning-darken-1;
    }
    
    /* Main content styles */
    MainContent {
        padding: 2;
        background: $background;
    }
    
    .content {
        height: auto;
        background: $surface;
        border: solid $primary;
        padding: 2;
        margin: 1;
        text-align: left;
        scrollbar-size: 1 1;
        scrollbar-size-horizontal: 1;
        overflow: auto;
    }
    """
    
    TITLE = "Linux TUI Tutorial"
    SUBTITLE = "Interactive Terminal-Based Linux Learning"
    
    BINDINGS = [
        Binding("q", "quit", "Quit", priority=True),
        Binding("h", "help", "Help"),
        Binding("1", "select_basic", "Basic Topics"),
        Binding("2", "select_intermediate", "Intermediate Topics"),
        Binding("3", "select_advanced", "Advanced Topics"),
        Binding("escape", "back_to_main", "Back"),
        Binding("up", "focus_previous", "Up", show=False),
        Binding("down", "focus_next", "Down", show=False),
        Binding("enter", "select_focused", "Select", show=False),
    ]
    
    current_state = reactive(NavigationState.MAIN_MENU)
    
    def compose(self) -> ComposeResult:
        """Create the application layout"""
        yield Header(show_clock=True)
        with Container(id="main-container"):
            yield Sidebar(id="sidebar")
            yield MainContent(id="main-content")
        yield Footer()
    
    def on_mount(self) -> None:
        """Initialize the application"""
        self.title = self.TITLE
        self.sub_title = self.SUBTITLE
        # Sync sidebar state with app state
        sidebar = self.query_one("#sidebar", Sidebar)
        sidebar.current_state = self.current_state
    
    def watch_current_state(self, state: NavigationState) -> None:
        """Update sidebar when navigation state changes"""
        sidebar = self.query_one("#sidebar", Sidebar)
        sidebar.current_state = state
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events"""
        button_id = event.button.id
        
        # Main menu navigation
        if button_id == "basic":
            self.action_select_basic()
        elif button_id == "intermediate":
            self.action_select_intermediate()
        elif button_id == "advanced":
            self.action_select_advanced()
        elif button_id == "exit":
            self.action_quit()
        elif button_id == "back":
            self.action_back_to_main()
        
        # Basic topics submenu
        elif button_id == "basic-files":
            self.show_basic_topic("File Commands")
        elif button_id == "basic-nav":
            self.show_basic_topic("Directory Navigation")
        elif button_id == "basic-view":
            self.show_basic_topic("File Viewing")
        elif button_id == "basic-perms":
            self.show_basic_topic("Permissions")
        
        # Intermediate topics submenu
        elif button_id == "inter-shell":
            self.show_intermediate_topic("Shell Scripting")
        elif button_id == "inter-process":
            self.show_intermediate_topic("Process Management")
        elif button_id == "inter-users":
            self.show_intermediate_topic("User Management")
        elif button_id == "inter-packages":
            self.show_intermediate_topic("Package Management")
        
        # Advanced topics submenu
        elif button_id == "adv-network":
            self.show_advanced_topic("Networking")
        elif button_id == "adv-monitor":
            self.show_advanced_topic("System Monitoring")
        elif button_id == "adv-kernel":
            self.show_advanced_topic("Kernel Modules")
        elif button_id == "adv-virtual":
            self.show_advanced_topic("Virtualization")
    
    def action_select_basic(self) -> None:
        """Navigate to Basic Topics submenu"""
        self.current_state = NavigationState.BASIC_SUBMENU
        content = self.query_one("#main-content", MainContent)
        content.update_content("""
🔰 Basic Topics Menu

Select a subtopic to begin learning:

📁 File Commands
Learn essential file operations like creating, copying, moving, and deleting files.
Commands: touch, cp, mv, rm

📂 Directory Navigation  
Master navigating the Linux file system and understanding directory structures.
Commands: cd, ls, pwd, find

👁️ File Viewing
Discover different ways to view and examine file contents.
Commands: cat, less, more, head, tail, grep

🔐 Permissions
Understand Linux file permissions and ownership concepts.
Commands: chmod, chown, chgrp, umask

Click on a subtopic or use arrow keys to navigate and press Enter to select.
Press Escape or click '← Back' to return to the main menu.
        """)
    
    def action_select_intermediate(self) -> None:
        """Navigate to Intermediate Topics submenu"""
        self.current_state = NavigationState.INTERMEDIATE_SUBMENU
        content = self.query_one("#main-content", MainContent)
        content.update_content("""
⚡ Intermediate Topics Menu

Select a subtopic to continue your Linux journey:

💻 Shell Scripting
Learn to write bash scripts, use variables, loops, and conditionals.
Topics: Variables, loops, functions, conditionals, script execution

⚙️ Process Management
Master controlling and monitoring system processes.
Commands: ps, kill, killall, top, htop, bg, fg, jobs, nohup

👥 User Management
Understand user accounts, groups, and privilege escalation.
Commands: useradd, userdel, usermod, passwd, su, sudo, groups

📦 Package Management
Learn to install, update, and remove software packages.
Commands: apt, yum, dnf, snap, flatpak (distribution-specific)

Click on a subtopic or use arrow keys to navigate and press Enter to select.
Press Escape or click '← Back' to return to the main menu.
        """)
    
    def action_select_advanced(self) -> None:
        """Navigate to Advanced Topics submenu"""
        self.current_state = NavigationState.ADVANCED_SUBMENU
        content = self.query_one("#main-content", MainContent)
        content.update_content("""
🚀 Advanced Topics Menu

Select a subtopic for expert-level Linux knowledge:

🌐 Networking
Master network configuration, troubleshooting, and security.
Commands: ip, ifconfig, netstat, ss, iptables, ufw, ping, traceroute

📊 System Monitoring
Learn advanced system monitoring and log analysis.
Commands: journalctl, systemctl, sar, iostat, vmstat, dmesg

🔧 Kernel Modules
Understand kernel module management and system customization.
Commands: lsmod, modprobe, rmmod, modinfo, dkms

🐳 Virtualization
Explore containerization and virtual machine concepts.
Topics: Docker basics, systemd containers, VM management

Click on a subtopic or use arrow keys to navigate and press Enter to select.
Press Escape or click '← Back' to return to the main menu.
        """)
    
    def show_basic_topic(self, topic: str) -> None:
        """Display content for a basic topic"""
        content = self.query_one("#main-content", MainContent)
        
        topic_content = {
            "File Commands": """
📁 File Commands - Basic File Operations

Essential commands for creating, copying, moving, and deleting files:

🆕 Creating Files and Directories:
• touch filename.txt - Create an empty file
• mkdir directory_name - Create a new directory
• mkdir -p path/to/nested/dirs - Create nested directories

📋 Copying and Moving:
• cp source.txt destination.txt - Copy a file
• cp -r source_dir/ dest_dir/ - Copy a directory recursively
• mv old_name.txt new_name.txt - Rename/move a file
• mv file.txt /path/to/directory/ - Move file to directory

🗑️ Removing Files:
• rm filename.txt - Remove a file
• rm -r directory/ - Remove directory recursively
• rm -i filename.txt - Remove with confirmation prompt
• rmdir empty_directory - Remove empty directory

⚠️ Safety Tips:
• Always use -i flag when removing important files
• Double-check paths before using rm -r
• Use ls to verify file locations before operations

[Interactive lesson and quiz coming soon!]

Press Escape to return to Basic Topics menu.
            """,
            
            "Directory Navigation": """
📂 Directory Navigation - Moving Around the File System

Master the art of navigating Linux directories:

🧭 Basic Navigation:
• pwd - Print working directory (where am I?)
• ls - List files and directories in current location
• cd directory_name - Change to a specific directory
• cd .. - Move up one directory level
• cd ~ - Go to home directory
• cd / - Go to root directory

📋 Advanced Listing:
• ls -la - List all files with detailed information
• ls -lh - List with human-readable file sizes
• ls -t - Sort by modification time
• ls -R - Recursive listing of subdirectories

🔍 Finding Your Way:
• find /path -name "filename" - Search for files
• which command_name - Find location of a command
• locate filename - Quick file search (if available)

💡 Pro Tips:
• Use Tab completion for faster navigation
• .. means parent directory, . means current directory
• Absolute paths start with /, relative paths don't

[Interactive navigation practice coming soon!]

Press Escape to return to Basic Topics menu.
            """,
            
            "File Viewing": """
👁️ File Viewing - Examining File Contents

Learn different ways to view and examine files:

📖 Basic Viewing:
• cat filename.txt - Display entire file contents
• less filename.txt - View file page by page (q to quit)
• more filename.txt - Similar to less, but simpler
• head filename.txt - Show first 10 lines
• tail filename.txt - Show last 10 lines

🔢 Customizing Output:
• head -n 20 file.txt - Show first 20 lines
• tail -n 5 file.txt - Show last 5 lines
• tail -f logfile.txt - Follow file changes in real-time

🔍 Searching Within Files:
• grep "search_term" filename.txt - Find lines containing text
• grep -i "term" file.txt - Case-insensitive search
• grep -n "term" file.txt - Show line numbers
• grep -r "term" directory/ - Search recursively in directory

💡 Navigation in less/more:
• Space - Next page
• b - Previous page
• q - Quit
• / - Search within file

[Interactive file viewing exercises coming soon!]

Press Escape to return to Basic Topics menu.
            """,
            
            "Permissions": """
🔐 Permissions - Understanding Linux File Security

Master Linux file permissions and ownership:

📊 Understanding Permissions:
• Read (r/4) - View file contents or list directory
• Write (w/2) - Modify file or create/delete in directory  
• Execute (x/1) - Run file as program or enter directory

👥 Permission Groups:
• Owner (u) - File owner permissions
• Group (g) - Group member permissions
• Others (o) - Everyone else permissions

🔧 Changing Permissions:
• chmod 755 filename - Set permissions using octal notation
• chmod u+x filename - Add execute permission for owner
• chmod g-w filename - Remove write permission for group
• chmod o=r filename - Set others to read-only

👤 Ownership Commands:
• chown user:group filename - Change owner and group
• chown user filename - Change owner only
• chgrp group filename - Change group only

📋 Viewing Permissions:
• ls -l - Long listing shows permissions (drwxrwxrwx)
• stat filename - Detailed file information

💡 Common Permission Patterns:
• 644 - Read/write for owner, read-only for others (files)
• 755 - Read/write/execute for owner, read/execute for others (dirs)
• 600 - Read/write for owner only (private files)

[Interactive permission workshop coming soon!]

Press Escape to return to Basic Topics menu.
            """
        }
        
        content.update_content(topic_content.get(topic, f"Content for {topic} coming soon!"))
    
    def show_intermediate_topic(self, topic: str) -> None:
        """Display content for an intermediate topic"""
        content = self.query_one("#main-content", MainContent)
        content.update_content(f"""
⚡ {topic} - Intermediate Level

This section is under development and will include:
• Detailed explanations and concepts
• Interactive code examples
• Hands-on exercises
• Progress tracking quizzes

Stay tuned for comprehensive {topic.lower()} lessons!

Press Escape to return to Intermediate Topics menu.
        """)
    
    def show_advanced_topic(self, topic: str) -> None:
        """Display content for an advanced topic"""
        content = self.query_one("#main-content", MainContent)
        content.update_content(f"""
🚀 {topic} - Advanced Level

This expert-level section is under development and will include:
• In-depth technical concepts
• Advanced simulations
• Real-world scenarios
• Professional best practices

Stay tuned for comprehensive {topic.lower()} mastery!

Press Escape to return to Advanced Topics menu.
        """)
    
    def action_back_to_main(self) -> None:
        """Return to the main menu"""
        self.current_state = NavigationState.MAIN_MENU
        content = self.query_one("#main-content", MainContent)
        content.update_content(content.get_welcome_message())
    
    def action_select_focused(self) -> None:
        """Select the currently focused button"""
        focused = self.focused
        if isinstance(focused, Button):
            focused.press()
    
    def action_help(self) -> None:
        """Show help information"""
        content = self.query_one("#main-content", MainContent)
        content.update_content("""
❓ Help - Navigation Guide

🎯 Keyboard Shortcuts:
• q - Quit application
• h - Show this help
• Escape - Go back to previous menu
• Enter - Select focused item
• Arrow Keys ↑↓ - Navigate menu items
• Tab/Shift+Tab - Focus next/previous element

🚀 Quick Access:
• 1 - Jump to Basic Topics
• 2 - Jump to Intermediate Topics  
• 3 - Jump to Advanced Topics

🖱️ Mouse Support:
• Click any button to select
• Scroll in content areas
• Hover for visual feedback

📚 Navigation Flow:
Main Menu → Topic Category → Subtopic → Content

Each level has a back button (← Back) or use Escape key.

🎓 Learning Features (Coming Soon):
• Interactive quizzes with instant feedback
• Progress tracking across all topics
• Hands-on command simulation
• Search functionality
• Export progress reports

Press Escape to return to your previous location.
        """)


def main():
    """Entry point for the application"""
    app = LinuxTutorialApp()
    try:
        app.run()
    except KeyboardInterrupt:
        print("\n👋 Thanks for using Linux TUI Tutorial!")
    except Exception as e:
        print(f"❌ Error running application: {e}")
        print("Make sure you have textual installed: pip install textual")


if __name__ == "__main__":
    main()
