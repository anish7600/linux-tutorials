#!/usr/bin/env python3
"""
Linux TUI Tutorial - Main Application Entry Point
Built with Textual for a modern, responsive TUI experience.
"""

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer
from textual.binding import Binding
from textual.reactive import reactive

from components.sidebar import Sidebar
from components.main_content import MainContent
from data.navigation import NavigationState
from handlers.event_handlers import EventHandlerMixin


class LinuxTutorialApp(App, EventHandlerMixin):
    """Main application class for the Linux TUI Tutorial"""
    
    CSS_PATH = "styles/app.css"
    
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
