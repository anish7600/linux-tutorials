# Linux TUI Tutorial - Documentation

## Project Overview

The Linux TUI Tutorial is an interactive terminal-based application built with Python's Textual framework. It provides a comprehensive learning platform for Linux concepts, from basic file operations to advanced system administration.

### Key Features
- Interactive terminal user interface (TUI)
- Hierarchical content organization (Basic → Intermediate → Advanced)
- Comprehensive Linux command reference
- Real-time navigation with keyboard shortcuts
- Responsive design with sidebar navigation

### Architecture
- **Framework**: Textual (modern TUI framework)
- **Python Version**: 3.7+
- **Structure**: Modular component-based architecture
- **Design Pattern**: Event-driven with reactive state management

## Installation & Setup

### Prerequisites
```bash
# Python 3.7 or higher required
python --version

# Install Textual framework
pip install textual
```

### Running the Application
```bash
# Clone or download the project
cd linux-tui-tutorial

# Make main.py executable (optional)
chmod +x main.py

# Run the application
python main.py
# or
./main.py
```

### Project Structure
```
linux-tui-tutorial/
├── main.py                    # Application entry point
├── Readme.md                  # Project documentation
├── .gitignore                 # Git ignore rules
├── components/                # UI components
│   ├── main_content.py       # Main content display area
│   └── sidebar.py            # Navigation sidebar
├── content/                   # Content modules
│   ├── welcome.py            # Welcome and help content
│   ├── basic_topics.py       # Basic Linux topics
│   ├── intermediate_topics.py # Intermediate topics
│   └── advanced_topics.py    # Advanced topics
├── data/                      # Data structures
│   └── navigation.py         # Navigation state and menu data
├── handlers/                  # Event handling
│   └── event_handlers.py     # Button press and navigation logic
└── styles/                    # CSS styling
    └── app.css               # Application styles
```

## Core Components

### 1. Main Application (`main.py`)

#### `LinuxTutorialApp`
Main application class inheriting from Textual's App and EventHandlerMixin.

**Class Definition:**
```python
class LinuxTutorialApp(App, EventHandlerMixin):
    """Main application class for the Linux TUI Tutorial"""
```

**Key Attributes:**
- `CSS_PATH`: Path to styling file
- `TITLE`: Application title
- `BINDINGS`: Keyboard shortcuts configuration
- `current_state`: Reactive navigation state

**Key Methods:**

##### `compose() -> ComposeResult`
Creates the application layout structure.

**Returns:**
- `ComposeResult`: Textual composition result with header, sidebar, content area, and footer

**Layout Structure:**
```
Header (with clock)
├── Main Container
    └── Horizontal Layout
        ├── Sidebar (navigation menu)
        └── Main Content (tutorial content)
Footer (keyboard shortcuts)
```

##### `on_mount() -> None`
Initializes the application after mounting, configuring layout properties and styling.

**Functionality:**
- Sets application title and subtitle
- Configures container dimensions and layout
- Sets up sidebar positioning and borders
- Initializes content area properties

### 2. Sidebar Component (`components/sidebar.py`)

#### `Sidebar`
Navigation container with dynamic menu generation.

**Class Definition:**
```python
class Sidebar(Container):
    """Sidebar container for navigation menu"""
```

**Key Attributes:**
- `current_state`: Reactive navigation state tracker

**Key Methods:**

##### `compose() -> ComposeResult`
Creates sidebar structure with title and menu container.

##### `watch_current_state(state: NavigationState) -> None`
Reactively updates sidebar content when navigation state changes.

**Parameters:**
- `state` (NavigationState): New navigation state

##### `update_menu(state: NavigationState) -> None`
Updates menu buttons based on current navigation state.

**Functionality:**
- Removes existing menu items
- Adds back button for submenus
- Creates new menu buttons from MenuStructure data
- Applies appropriate CSS classes

#### `MenuButton`
Custom button class for menu items with enhanced functionality.

**Class Definition:**
```python
class MenuButton(Button):
    """Custom button for menu items with hover effects"""
```

### 3. Main Content Component (`components/main_content.py`)

#### `MainContent`
Scrollable content area displaying tutorial content.

**Class Definition:**
```python
class MainContent(VerticalScroll):
    """Main content area that displays tutorial content with scrolling"""
```

**Key Attributes:**
- `current_view`: Reactive view state tracker

**Key Methods:**

##### `compose() -> ComposeResult`
Creates scrollable content area with initial welcome message.

##### `update_content(content: str) -> None`
Updates content area with new text and resets scroll position.

**Parameters:**
- `content` (str): New content to display

##### Navigation Methods:
- `show_welcome()`: Display welcome screen
- `show_basic_menu()`: Display basic topics menu
- `show_intermediate_menu()`: Display intermediate topics menu
- `show_advanced_menu()`: Display advanced topics menu
- `show_help()`: Display help information
- `show_topic_content(topic_level: str, topic_id: str)`: Display specific topic content

### 4. Content Modules (`content/`)

#### `WelcomeContent`
Static content provider for welcome and help screens.

**Methods:**
- `get_welcome_message() -> str`: Returns main welcome message
- `get_help_content() -> str`: Returns help and navigation guide

#### Topic Content Classes
Each topic level has its own content class with similar structure:

**`BasicTopicsContent`**, **`IntermediateTopicsContent`**, **`AdvancedTopicsContent`**

**Common Methods:**
- `get_menu_content() -> str`: Returns topic category menu
- `get_topic_content(topic_id: str) -> str`: Returns specific topic content
- Private methods for individual topic content (e.g., `_get_files_content()`)

### 5. Navigation System (`data/navigation.py`)

#### `NavigationState`
Enumeration defining application navigation states.

```python
class NavigationState(Enum):
    MAIN_MENU = "main_menu"
    BASIC_SUBMENU = "basic_submenu"
    INTERMEDIATE_SUBMENU = "intermediate_submenu"
    ADVANCED_SUBMENU = "advanced_submenu"
```

#### `MenuItem`
Data class representing menu items.

**Attributes:**
- `label` (str): Display text for menu item
- `id` (str): Unique identifier for the item
- `description` (str): Optional description

#### `MenuStructure`
Centralized menu configuration and management.

**Class Attributes:**
- `MAIN_MENU_ITEMS`: Main menu configuration
- `BASIC_MENU_ITEMS`: Basic topics submenu
- `INTERMEDIATE_MENU_ITEMS`: Intermediate topics submenu  
- `ADVANCED_MENU_ITEMS`: Advanced topics submenu

**Methods:**
- `get_menu_items(state: NavigationState) -> List[MenuItem]`: Returns menu items for state
- `get_menu_title(state: NavigationState) -> str`: Returns title for navigation state

### 6. Event Handling (`handlers/event_handlers.py`)

#### `EventHandlerMixin`
Mixin class containing all event handling logic.

**Key Methods:**

##### `on_button_pressed(event: Button.Pressed) -> None`
Central event handler for all button press events.

**Parameters:**
- `event` (Button.Pressed): Textual button press event

**Functionality:**
- Routes button presses based on button ID
- Handles navigation between menus
- Manages topic selection and content display

##### Navigation Action Methods:
- `action_select_basic()`: Navigate to basic topics
- `action_select_intermediate()`: Navigate to intermediate topics
- `action_select_advanced()`: Navigate to advanced topics
- `action_back_to_main()`: Return to main menu
- `action_help()`: Display help content

## Usage Examples

### Basic Usage
```python
from main import LinuxTutorialApp

# Create and run the application
app = LinuxTutorialApp()
app.run()
```

### Extending Content
```python
# Add new topic to BasicTopicsContent
@staticmethod
def _get_new_topic_content() -> str:
    return """
    Your new topic content here...
    """

# Add to content_map in get_topic_content method
content_map = {
    "files": BasicTopicsContent._get_files_content(),
    "new_topic": BasicTopicsContent._get_new_topic_content(),
    # ... other topics
}
```

### Custom Menu Items
```python
# Add new menu item to MenuStructure
BASIC_MENU_ITEMS = [
    MenuItem("File Commands", "basic-files", "Creating, copying, moving files"),
    MenuItem("New Topic", "basic-newtopic", "Description of new topic"),
    # ... other items
]
```

## Keyboard Shortcuts

| Key | Action | Description |
|-----|--------|-------------|
| `q` | Quit | Exit the application |
| `h` | Help | Show help information |
| `1` | Basic Topics | Jump to basic topics menu |
| `2` | Intermediate Topics | Jump to intermediate topics menu |
| `3` | Advanced Topics | Jump to advanced topics menu |
| `Escape` | Back | Return to previous menu |
| `↑/↓` | Navigate | Move through menu items |
| `Enter` | Select | Activate focused item |
| `Tab` | Focus Next | Move to next focusable element |

## Configuration

### Styling (`styles/app.css`)
The application uses CSS for styling Textual components:

```css
Screen {
    layout: vertical;
    color: white;
}

/* Uncomment for themed appearance
Button {
    color: yellow;
    background: blue;
}
*/
```

### Adding Custom Styles
```python
# In component classes
def on_mount(self) -> None:
    self.styles.width = "100%"
    self.styles.background = "blue"
    self.styles.border = ("solid", "white")
```

## Error Handling

The application includes basic error handling:

```python
def main():
    app = LinuxTutorialApp()
    try:
        app.run()
    except KeyboardInterrupt:
        print("\n Thanks for using Linux Ref. Guide!")
    except Exception as e:
        print(f"❌ Error running application: {e}")
        print("Make sure you have textual installed: pip install textual")
```

## Development Guidelines

### Adding New Topics
1. Add menu item to appropriate `MENU_ITEMS` list in `MenuStructure`
2. Create content method in corresponding content class
3. Add mapping in `get_topic_content()` method
4. Update event handler if needed

### Code Style
- Use type hints for all method parameters and returns
- Follow PEP 8 naming conventions
- Document classes and methods with docstrings
- Keep methods focused on single responsibilities

### Testing
```python
# Manual testing approach
python main.py

# Test navigation flows:
# 1. Main menu → Basic → Topic → Back
# 2. Keyboard shortcuts functionality  
# 3. Content scrolling behavior
# 4. Menu state persistence
```

## Dependencies

### Required Packages
```requirements.txt
textual>=0.40.0
```

### System Requirements
- Python 3.7+
- Terminal with Unicode support
- Minimum terminal size: 80x24 characters

## Troubleshooting

### Common Issues

**"ModuleNotFoundError: No module named 'textual'"**
```bash
pip install textual
```

**Content not scrolling properly**
- Check terminal size (minimum 80x24)
- Verify VerticalScroll container configuration

**Keyboard shortcuts not working**
- Ensure terminal supports key combinations
- Check BINDINGS configuration in main.py

**Styling issues**
- Verify app.css file exists in styles/ directory
- Check CSS_PATH configuration

## Future Enhancements

Potential improvements for the project:
- Interactive command execution
- Progress tracking for completed topics
- Bookmarks for favorite topics
- Search functionality across content
- Export content to text files
- Multi-language support
- Custom themes and color schemes
