"""Navigation data structures and enums for the Linux TUI Tutorial"""

from enum import Enum
from dataclasses import dataclass
from typing import Dict, List


class NavigationState(Enum):
    """Enum to track current navigation state"""
    MAIN_MENU = "main_menu"
    BASIC_SUBMENU = "basic_submenu"
    INTERMEDIATE_SUBMENU = "intermediate_submenu"
    ADVANCED_SUBMENU = "advanced_submenu"


@dataclass
class MenuItem:
    """Data class for menu items"""
    label: str
    id: str
    description: str = ""


class MenuStructure:
    """Centralized menu structure definition"""
    
    MAIN_MENU_ITEMS = [
        MenuItem("Basic Topics", "basic", "Essential Linux fundamentals"),
        MenuItem("Intermediate Topics", "intermediate", "System administration skills"),
        MenuItem("Advanced Topics", "advanced", "Expert-level Linux mastery"),
        MenuItem("Exit", "exit", "Quit")
    ]
    
    BASIC_MENU_ITEMS = [
        MenuItem("File Commands", "basic-files", "Creating, copying, moving files"),
        MenuItem("Directory Navigation", "basic-nav", "Moving through the filesystem"),
        MenuItem("File Viewing", "basic-view", "Examining file contents"),
        MenuItem("Permissions", "basic-perms", "Understanding Linux security"),
    ]
    
    INTERMEDIATE_MENU_ITEMS = [
        MenuItem("Process Management", "inter-process", "Controlling system processes"),
        MenuItem("System Monitoring", "inter-monitor", "Performance analysis tools"),
        MenuItem("Storage & Filesystems", "inter-storage", "Advanced disk management"),
        MenuItem("Shell Scripting", "inter-shell", "Automation and scripting"),
        MenuItem("User Management", "inter-users", "Accounts and permissions"),
        MenuItem("Package Management", "inter-packages", "Software installation"),
        MenuItem("Network Basics", "inter-network", "Basic networking concepts"),
    ]
    
    ADVANCED_MENU_ITEMS = [
        MenuItem("Kernel & Modules", "adv-kernel", "Low-level system management"),
        MenuItem("Advanced Networking", "adv-network", "Network configuration & security"),
        MenuItem("Security Hardening", "adv-security", "System security & hardening"),
        MenuItem("Virtualization", "adv-virtual", "Containers and VMs"),
        MenuItem("High Availability", "adv-ha", "Clustering and load balancing"),
        MenuItem("System Internals", "adv-internals", "Deep system understanding"),
        MenuItem("Performance Tuning", "adv-performance", "Optimization techniques"),
    ]
    
    @classmethod
    def get_menu_items(cls, state: NavigationState) -> List[MenuItem]:
        """Get menu items for a specific navigation state"""
        if state == NavigationState.MAIN_MENU:
            return cls.MAIN_MENU_ITEMS
        elif state == NavigationState.BASIC_SUBMENU:
            return cls.BASIC_MENU_ITEMS
        elif state == NavigationState.INTERMEDIATE_SUBMENU:
            return cls.INTERMEDIATE_MENU_ITEMS
        elif state == NavigationState.ADVANCED_SUBMENU:
            return cls.ADVANCED_MENU_ITEMS
        else:
            return []
    
    @classmethod
    def get_menu_title(cls, state: NavigationState) -> str:
        """Get the title for a specific navigation state"""
        titles = {
            NavigationState.MAIN_MENU: "📚 Linux Ref. Guide",
            NavigationState.BASIC_SUBMENU: "Basic Topics:",
            NavigationState.INTERMEDIATE_SUBMENU: "Intermediate Topics:",
            NavigationState.ADVANCED_SUBMENU: "Advanced Topics:"
        }
        return titles.get(state, "Linux Ref. Guide")
