"""Event handling logic for the Linux TUI Tutorial"""

from textual.widgets import Button

from data.navigation import NavigationState
from components.main_content import MainContent


class EventHandlerMixin:
    """Mixin class containing all event handling logic"""
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events"""
        button_id = event.button.id
        
        # Navigation buttons
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
        
        # Basic topic buttons
        elif button_id.startswith("basic-"):
            topic_id = button_id.replace("basic-", "")
            self.show_topic("basic", topic_id)
        
        # Intermediate topic buttons
        elif button_id.startswith("inter-"):
            topic_id = button_id.replace("inter-", "")
            self.show_topic("intermediate", topic_id)
        
        # Advanced topic buttons
        elif button_id.startswith("adv-"):
            topic_id = button_id.replace("adv-", "")
            self.show_topic("advanced", topic_id)
    
    def action_select_basic(self) -> None:
        """Navigate to Basic Topics submenu"""
        self.current_state = NavigationState.BASIC_SUBMENU
        content = self.query_one("#main-content", MainContent)
        content.show_basic_menu()
    
    def action_select_intermediate(self) -> None:
        """Navigate to Intermediate Topics submenu"""
        self.current_state = NavigationState.INTERMEDIATE_SUBMENU
        content = self.query_one("#main-content", MainContent)
        content.show_intermediate_menu()
    
    def action_select_advanced(self) -> None:
        """Navigate to Advanced Topics submenu"""
        self.current_state = NavigationState.ADVANCED_SUBMENU
        content = self.query_one("#main-content", MainContent)
        content.show_advanced_menu()
    
    def action_back_to_main(self) -> None:
        """Return to the main menu"""
        self.current_state = NavigationState.MAIN_MENU
        content = self.query_one("#main-content", MainContent)
        content.show_welcome()
    
    def action_select_focused(self) -> None:
        """Select the currently focused button"""
        focused = self.focused
        if isinstance(focused, Button):
            focused.press()
    
    def action_help(self) -> None:
        """Show help information"""
        content = self.query_one("#main-content", MainContent)
        content.show_help()
    
    def show_topic(self, topic_level: str, topic_id: str) -> None:
        """Show specific topic content"""
        content = self.query_one("#main-content", MainContent)
        content.show_topic_content(topic_level, topic_id)
