"""Sidebar navigation component for the Linux TUI Tutorial"""

from textual.app import ComposeResult
from textual.containers import Container
from textual.widgets import Button, Static
from textual.reactive import reactive

from data.navigation import NavigationState, MenuStructure


class MenuButton(Button):
    """Custom button for menu items with hover effects"""
    
    def __init__(self, label: str, id: str = None):
        super().__init__(label, id=id)
        self.can_focus = True


class Sidebar(Container):
    """Sidebar container for navigation menu"""
    
    current_state = reactive(NavigationState.MAIN_MENU)
    
    def compose(self) -> ComposeResult:
        yield Static("📚 Linux Ref. Guide", classes="sidebar-title")
        yield Container(id="menu-container")
    
    def watch_current_state(self, state: NavigationState) -> None:
        """Update sidebar content based on current state"""
        self.update_menu(state)
    
    def update_menu(self, state: NavigationState) -> None:
        """Update the menu based on current navigation state"""
        menu_container = self.query_one("#menu-container", Container)
        menu_container.remove_children()
        
        # Add back button for submenus
        if state != NavigationState.MAIN_MENU:
            back_btn = MenuButton("← Back", id="back")
            back_btn.add_class("back-button")
            menu_container.mount(back_btn)
            
            # Add submenu title
            title = Static(MenuStructure.get_menu_title(state))
            title.add_class("submenu-title")
            menu_container.mount(title)
        
        # Add menu items
        menu_items = MenuStructure.get_menu_items(state)
        for item in menu_items:
            button = MenuButton(item.label, id=item.id)
            if item.id == "exit":
                button.add_class("exit-button")
            menu_container.mount(button)
