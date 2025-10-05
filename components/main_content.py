"""Main content display component for the Linux TUI Tutorial"""

from textual.app import ComposeResult
from textual.containers import VerticalScroll
from textual.widgets import Static
from textual.reactive import reactive

from content.welcome import WelcomeContent
from content.basic_topics import BasicTopicsContent
from content.intermediate_topics import IntermediateTopicsContent
from content.advanced_topics import AdvancedTopicsContent


class MainContent(VerticalScroll):
    """Main content area that displays tutorial content with scrolling"""

    current_view = reactive("welcome")
    
    def compose(self) -> ComposeResult:
        """Compose the main content area with a scrollable static widget"""
        yield Static(WelcomeContent.get_welcome_message(), id="content-text", classes="content")
    
    def update_content(self, content: str):
        """Update the main content area with scrollable content"""
        content_widget = self.query_one("#content-text", Static)
        content_widget.update(content)
        # Reset scroll position to top when updating content
        self.scroll_to(y=0, animate=False)
    
    def show_welcome(self):
        """Show the welcome screen"""
        self.current_view = "welcome"
        self.update_content(WelcomeContent.get_welcome_message())
    
    def show_basic_menu(self):
        """Show basic topics menu with scrolling"""
        self.current_view = "basic_menu"
        content = BasicTopicsContent.get_menu_content()
        self.update_content(content)
    
    def show_intermediate_menu(self):
        """Show intermediate topics menu with scrolling"""
        self.current_view = "intermediate_menu"
        content = IntermediateTopicsContent.get_menu_content()
        self.update_content(content)
    
    def show_advanced_menu(self):
        """Show advanced topics menu with scrolling"""
        self.current_view = "advanced_menu"
        content = AdvancedTopicsContent.get_menu_content()
        self.update_content(content)
    
    def show_help(self):
        """Show help information"""
        self.current_view = "help"
        content = WelcomeContent.get_help_content()
        self.update_content(content)
    
    def show_topic_content(self, topic_level: str, topic_id: str):
        """Show specific topic content"""
        self.current_view = f"{topic_level}_{topic_id}"
        if topic_level == "basic":
            content = BasicTopicsContent.get_topic_content(topic_id)
        elif topic_level == "intermediate":
            content = IntermediateTopicsContent.get_topic_content(topic_id)
        elif topic_level == "advanced":
            content = AdvancedTopicsContent.get_topic_content(topic_id)
        else:
            content = f"Content for {topic_id} coming soon!"
        
        self.update_content(content)
    
    def on_mount(self) -> None:
        """Initialize the content area and set layout properties"""
        # Configure content area styles programmatically
        self.styles.width = "100%"
        self.styles.height = "100%"
        self.styles.padding = 0
        
        # Configure content text widget
        content_widget = self.query_one("#content-text")
        content_widget.styles.width = "100%"
        content_widget.styles.height = "auto"
        content_widget.styles.min_height = "100%"
        content_widget.styles.padding = 1
        content_widget.styles.margin = 0
        
        # Ensure the content starts at the top
        self.scroll_to(y=0, animate=False)
