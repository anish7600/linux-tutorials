#!/usr/bin/env python3
"""
Linux TUI Tutorial - A terminal-based interactive Linux learning application
Built with Textual for a modern, responsive TUI experience.
"""

from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Button, Static, Header, Footer
from textual.binding import Binding
from textual.reactive import reactive
from textual import events


class MenuButton(Button):
    """Custom button for menu items with hover effects"""
    
    def __init__(self, label: str, id: str = None):
        super().__init__(label, id=id)
        self.can_focus = True


class Sidebar(Container):
    """Sidebar container for navigation menu"""
    
    def compose(self) -> ComposeResult:
        yield Static("📚 Linux Tutorial", classes="sidebar-title")
        yield MenuButton("Basic Topics", id="basic")
        yield MenuButton("Intermediate Topics", id="intermediate")
        yield MenuButton("Advanced Topics", id="advanced")
        yield MenuButton("Exit", id="exit")


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

🎯 How to use this tutorial:

• Use arrow keys or click to navigate the menu
• Press Enter to select a topic
• Press 'q' to quit at any time
• Press 'h' for help

Choose a topic from the sidebar to get started!

Good luck on your Linux journey! 🚀
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
    
    /* Responsive design - handled programmatically */
    """
    
    TITLE = "Linux TUI Tutorial"
    SUBTITLE = "Interactive Terminal-Based Linux Learning"
    
    BINDINGS = [
        Binding("q", "quit", "Quit", priority=True),
        Binding("h", "help", "Help"),
        Binding("1", "select_basic", "Basic Topics"),
        Binding("2", "select_intermediate", "Intermediate Topics"),
        Binding("3", "select_advanced", "Advanced Topics"),
        Binding("escape", "back_to_main", "Back to Main"),
    ]
    
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
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events"""
        button_id = event.button.id
        
        if button_id == "basic":
            self.action_select_basic()
        elif button_id == "intermediate":
            self.action_select_intermediate()
        elif button_id == "advanced":
            self.action_select_advanced()
        elif button_id == "exit":
            self.action_quit()
    
    def action_select_basic(self) -> None:
        """Navigate to Basic Topics"""
        content = self.query_one("#main-content", MainContent)
        content.update_content("""
🔰 Basic Topics - Coming Soon!

This section will cover fundamental Linux concepts:

📁 File System Navigation
• ls - List directory contents
• cd - Change directory
• pwd - Print working directory

📄 File Operations  
• touch - Create empty files
• mkdir - Create directories
• rm - Remove files and directories
• cp - Copy files and directories
• mv - Move/rename files

👁️ Viewing Files
• cat - Display file contents
• less - Page through file contents
• head - Show first lines of a file
• tail - Show last lines of a file

🔐 Permissions
• chmod - Change file permissions
• chown - Change file ownership

Stay tuned for interactive lessons and quizzes!
        """)
    
    def action_select_intermediate(self) -> None:
        """Navigate to Intermediate Topics"""
        content = self.query_one("#main-content", MainContent)
        content.update_content("""
⚡ Intermediate Topics - Coming Soon!

This section will cover more advanced Linux concepts:

💻 Shell Scripting Basics
• Bash script fundamentals
• Variables and environment
• Loops and conditionals

⚙️ Process Management
• ps - View running processes
• kill - Terminate processes
• top - Monitor system processes
• bg/fg - Background/foreground jobs

👥 User and Group Management
• useradd - Add new users
• passwd - Change passwords
• sudo - Execute as another user

📦 Package Management
• apt/yum/dnf basics
• Installing and removing software

Stay tuned for hands-on exercises!
        """)
    
    def action_select_advanced(self) -> None:
        """Navigate to Advanced Topics"""
        content = self.query_one("#main-content", MainContent)
        content.update_content("""
🚀 Advanced Topics - Coming Soon!

This section will cover expert-level Linux concepts:

🌐 Networking
• Network interface configuration
• Network diagnostics and monitoring
• Firewall configuration

📊 System Monitoring and Logging
• System logs and journalctl
• Performance monitoring
• Log analysis

🔧 Kernel Modules and Customization
• Loading and unloading modules
• Kernel configuration basics

🐳 Virtualization Basics
• Docker fundamentals
• Virtual machine concepts

Stay tuned for advanced simulations!
        """)
    
    def action_back_to_main(self) -> None:
        """Return to the main welcome screen"""
        content = self.query_one("#main-content", MainContent)
        content.update_content(content.get_welcome_message())
    
    def action_help(self) -> None:
        """Show help information"""
        content = self.query_one("#main-content", MainContent)
        content.update_content("""
❓ Help - Keyboard Shortcuts

Navigation:
• Arrow Keys - Navigate menu items
• Enter - Select menu item
• Tab - Focus next element
• Shift+Tab - Focus previous element

Quick Access:
• 1 - Jump to Basic Topics
• 2 - Jump to Intermediate Topics  
• 3 - Jump to Advanced Topics
• Escape - Return to main menu
• h - Show this help
• q - Quit application

Mouse Support:
• Click buttons to navigate
• Scroll in content areas

Tips:
• Content areas are scrollable if text is long
• The app is responsive to terminal resizing
• All progress will be saved automatically (coming soon!)

Press Escape to return to the main menu.
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
