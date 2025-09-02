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
        """Update the main content area"""
        content_widget = self.query_one("#content-text", Static)
        content_widget.update(content)
        # Reset scroll position to top when updating content
        self.scroll_to(y=0)
    
    def show_welcome(self):
        """Show the welcome screen"""
        self.current_view = "welcome"
        self.update_content(WelcomeContent.get_welcome_message())
    
    def show_basic_menu(self):
        """Show basic topics menu"""
        self.current_view = "basic_menu"
        self.update_content(BasicTopicsContent.get_menu_content())
    
    def show_intermediate_menu(self):
        """Show intermediate topics menu"""
        self.current_view = "intermediate_menu"
        self.update_content(IntermediateTopicsContent.get_menu_content())
    
    def show_advanced_menu(self):
        """Show advanced topics menu"""
        self.current_view = "advanced_menu"
        self.update_content(AdvancedTopicsContent.get_menu_content())
    
    def show_help(self):
        """Show help information"""
        self.current_view = "help"
        self.update_content(WelcomeContent.get_help_content())
    
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
