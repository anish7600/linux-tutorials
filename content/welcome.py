"""Welcome screen and help content for the Linux TUI Tutorial"""


class WelcomeContent:
    """Static content for welcome screen and help"""
    
    @staticmethod
    def get_welcome_message() -> str:
        """Get the main welcome message"""
        return """
🐧 Welcome to the Linux TUI Tutorial! 🐧

This interactive tutorial will guide you through essential Linux concepts,
from basic file operations to advanced system administration.

📖 What you'll learn:

• Basic Topics: File system navigation, file operations, viewing files, permissions
• Intermediate Topics: Process management, system monitoring, shell scripting, storage
• Advanced Topics: Kernel management, networking, security, virtualization

🎯 How to navigate:

• Use arrow keys ↑↓ or click to navigate the menu
• Press Enter or click to select a topic
• Use number keys 1, 2, 3 for quick access to main categories
• Press 'Escape' or click '← Back' to return to previous menu
• Press 'q' to quit at any time
• Press 'h' for help

🚀 Getting Started:

Choose a topic category from the sidebar to explore subtopics and start learning!
Each section will include explanations, examples, and interactive exercises.

Good luck on your Linux journey! 🎓
        """
    
    @staticmethod
    def get_help_content() -> str:
        """Get the help screen content"""
        return """
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

🎓 Learning Features:
• Comprehensive tutorials with real-world examples
• Command explanations and usage patterns
• Best practices and safety tips
• Progressive difficulty levels

🔧 System Requirements:
• Python 3.7+
• Textual library (pip install textual)
• Terminal with Unicode support

Press Escape to return to your previous location.
        """
