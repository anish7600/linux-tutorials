"""Basic level content for the Linux TUI Tutorial"""


class BasicTopicsContent:
    """Content for basic Linux topics"""
    
    @staticmethod
    def get_menu_content() -> str:
        """Get the basic topics menu content"""
        return """
📰 Basic Topics Menu

Select a subtopic to begin learning:

📁 File Commands
Learn essential file operations like creating, copying, moving, and deleting files.
Commands: touch, cp, mv, rm, mkdir

📂 Directory Navigation  
Master navigating the Linux file system and understanding directory structures.
Commands: cd, ls, pwd, find, tree

👁️ File Viewing
Discover different ways to view and examine file contents.
Commands: cat, less, more, head, tail, grep

🔒 Permissions
Understand Linux file permissions and ownership concepts.
Commands: chmod, chown, chgrp, umask

Click on a subtopic or use arrow keys to navigate and press Enter to select.
Press Escape or click '← Back' to return to the main menu.
        """
    
    @staticmethod
    def get_topic_content(topic_id: str) -> str:
        """Get content for a specific basic topic"""
        content_map = {
            "files": BasicTopicsContent._get_files_content(),
            "nav": BasicTopicsContent._get_navigation_content(),
            "view": BasicTopicsContent._get_viewing_content(),
            "perms": BasicTopicsContent._get_permissions_content(),
        }
        return content_map.get(topic_id, f"Content for {topic_id} coming soon!")
    
    @staticmethod
    def _get_files_content() -> str:
        """File commands content"""
        return """
📁 File Commands - Basic File Operations

Essential commands for creating, copying, moving, and deleting files:

🆕 Creating Files and Directories:
• touch filename.txt - Create an empty file
• touch file1.txt file2.txt file3.txt - Create multiple files
• mkdir directory_name - Create a new directory
• mkdir -p path/to/nested/dirs - Create nested directories
• mkdir dir1 dir2 dir3 - Create multiple directories

📋 Copying Files and Directories:
• cp source.txt destination.txt - Copy a file
• cp source.txt /path/to/directory/ - Copy file to directory
• cp -r source_dir/ dest_dir/ - Copy directory recursively
• cp -i source.txt dest.txt - Interactive copy (ask before overwrite)
• cp -v source.txt dest.txt - Verbose copy (show what's happening)
• cp -p source.txt dest.txt - Preserve timestamps and permissions

🚚 Moving and Renaming:
• mv old_name.txt new_name.txt - Rename a file
• mv file.txt /path/to/directory/ - Move file to directory
• mv dir1/ /path/to/new/location/ - Move directory
• mv -i source.txt dest.txt - Interactive move (ask before overwrite)
• mv *.txt /backup/ - Move all .txt files to backup directory

🗑️ Removing Files and Directories:
• rm filename.txt - Remove a file
• rm file1.txt file2.txt - Remove multiple files
• rm -i filename.txt - Remove with confirmation prompt
• rm -r directory/ - Remove directory recursively
• rm -rf directory/ - Force remove directory (be careful!)
• rmdir empty_directory - Remove empty directory only

🔍 Useful File Operations:
• ls -la - List files with detailed information
• file filename.txt - Determine file type
• stat filename.txt - Show detailed file statistics
• wc filename.txt - Count lines, words, and characters
• du -h filename.txt - Show file size in human-readable format
• df -h - Show disk space usage

⚠️ Safety Tips:
• Always use -i flag when removing important files
• Double-check paths before using rm -r or rm -rf
• Use ls to verify file locations before operations
• Test commands on unimportant files first
• Consider using trash-cli instead of rm for safety

💡 Pro Tips:
• Use Tab completion to avoid typos in filenames
• Wildcards: * (any characters), ? (single character)
• Use quotes for filenames with spaces: "my file.txt"
• Combine commands: mkdir project && cd project

[Interactive exercises and quizzes coming soon!]

Press Escape to return to Basic Topics menu.
        """
    
    @staticmethod
    def _get_navigation_content() -> str:
        """Directory navigation content"""
        return """
📂 Directory Navigation - Moving Around the File System

Master the art of navigating Linux directories and file system:

🧭 Basic Navigation Commands:
• pwd - Print working directory (where am I?)
• cd directory_name - Change to a specific directory
• cd .. - Move up one directory level
• cd ../.. - Move up two directory levels
• cd ~ - Go to home directory
• cd / - Go to root directory
• cd - - Go to previous directory

📋 Listing Directory Contents:
• ls - List files and directories in current location
• ls -l - Long format listing with permissions and details
• ls -la - List all files including hidden ones (starting with .)
• ls -lh - List with human-readable file sizes
• ls -lt - Sort by modification time (newest first)
• ls -lS - Sort by file size (largest first)
• ls -R - Recursive listing of subdirectories

🔍 Finding Files and Directories:
• find /path -name "filename" - Search for files by name
• find . -name "*.txt" - Find all .txt files in current directory
• find /home -type d -name "Documents" - Find directories named Documents
• find . -size +100M - Find files larger than 100MB
• find . -mtime -7 - Find files modified in last 7 days
• locate filename - Quick file search using database
• which command_name - Find location of a command
• whereis command_name - Find binary, source, and manual pages

📁 Understanding Directory Structure:
• / - Root directory (top of filesystem)
• /home - User home directories
• /etc - System configuration files
• /var - Variable data (logs, databases)
• /tmp - Temporary files
• /usr - User programs and data
• /bin - Essential user binaries
• /sbin - System administration binaries

🌳 Advanced Navigation:
• tree - Display directory structure as a tree
• tree -L 2 - Limit tree depth to 2 levels
• tree -a - Show hidden files in tree
• dirs - Show directory stack
• pushd /path - Push directory onto stack and cd to it
• popd - Pop directory from stack and cd to it

💡 Navigation Shortcuts and Tips:
• Tab completion - Press Tab to auto-complete paths
• .. means parent directory, . means current directory
• ~ is your home directory shortcut
• Use / at the start for absolute paths
• No / at start means relative path from current location
• Use history to see previous commands: history | grep cd

🔧 Path and Environment:
• echo $HOME - Show home directory path
• echo $PWD - Show current directory
• echo $PATH - Show command search paths
• export PATH=$PATH:/new/path - Add directory to PATH
• basename /path/to/file.txt - Get filename from path
• dirname /path/to/file.txt - Get directory from path

🗂️ Working with Multiple Locations:
• ls /path1 /path2 - List contents of multiple directories
• cd /path && ls - Change directory and list contents
• (cd /tmp && ls) - Execute commands in subshell
• pushd /dir1; pushd /dir2; popd; popd - Directory stack

[Interactive navigation practice coming soon!]

Press Escape to return to Basic Topics menu.
        """
    
    @staticmethod
    def _get_viewing_content() -> str:
        """File viewing content"""
        return """
👁️ File Viewing - Examining File Contents

Learn different ways to view and examine files safely and effectively:

📖 Basic File Viewing:
• cat filename.txt - Display entire file contents
• cat file1.txt file2.txt - Display multiple files
• cat -n filename.txt - Show line numbers
• tac filename.txt - Display file in reverse order
• less filename.txt - View file page by page (recommended)
• more filename.txt - Similar to less, but simpler

🔍 Partial File Viewing:
• head filename.txt - Show first 10 lines
• head -n 20 file.txt - Show first 20 lines
• head -c 100 file.txt - Show first 100 characters
• tail filename.txt - Show last 10 lines
• tail -n 5 file.txt - Show last 5 lines
• tail -f logfile.txt - Follow file changes in real-time
• tail -F logfile.txt - Follow file even if it’s rotated

🔎 Searching File Contents:
• grep pattern filename.txt - Search for pattern in file
• grep -i pattern filename.txt - Case-insensitive search
• grep -r pattern /path - Recursive search in directory
• grep -n pattern filename.txt - Show line numbers
• grep -v pattern filename.txt - Show lines not matching pattern
• grep -c pattern filename.txt - Count matching lines
• egrep "pattern1|pattern2" file.txt - Search multiple patterns
• fgrep "literal string" file.txt - Literal string search

📄 Advanced File Viewing:
• view filename.txt - Open file in read-only vi/vim
• nano filename.txt - Open file in nano editor (read-only with Ctrl+R)
• vim -R filename.txt - Open file in read-only mode
• less +F filename.txt - Start less in follow mode (like tail -f)
• cut -d',' -f1 file.csv - Extract first column from CSV
• sort filename.txt - Sort file contents
• uniq filename.txt - Remove duplicate lines
• wc -l filename.txt - Count lines in file

🔧 File Type and Metadata:
• file filename - Determine file type
• stat filename.txt - Show file metadata (size, permissions, timestamps)
• xxd filename - Display file in hexadecimal
• od -tx4 filename - Display file in octal or hex
• strings filename - Extract printable strings from binary files

💡 Tips for Effective Viewing:
• Use less for large files (faster than cat)
• Press q to quit less or more
• In less: /pattern to search, n for next match, N for previous
• Combine with pipes: cat file.txt | grep pattern | less
• Use -F with tail for log files that rotate
• Save output: grep pattern file.txt > output.txt
• Use Tab completion to avoid typos in filenames

⚠️ Safety Tips:
• Avoid cat for binary files (use strings or file instead)
• Use less or more for large files to avoid terminal overload
• Double-check file paths before viewing
• Be cautious with sensitive files (e.g., /etc/passwd)

[Interactive file viewing exercises coming soon!]

Press Escape to return to Basic Topics menu.
        """
    
    @staticmethod
    def _get_permissions_content() -> str:
        """Permissions content"""
        return """
🔒 Permissions - File and Directory Access Control

Understand Linux file permissions and ownership concepts:

🔐 Understanding Permissions:
• ls -l - Show permissions, owner, and group
• Permissions format: rwxr-xr-x (owner, group, others)
• r = read (4), w = write (2), x = execute (1)
• Example: rwxr-xr-x = 755 (owner: 7, group: 5, others: 5)
• - = regular file, d = directory, l = symbolic link

👤 Changing File Ownership:
• chown username filename.txt - Change file owner
• chown username:groupname filename.txt - Change owner and group
• chown -R username:groupname directory/ - Recursive change
• chgrp groupname filename.txt - Change group only
• chgrp -R groupname directory/ - Recursive group change
• chown -h username link - Change symbolic link ownership

🔧 Modifying Permissions:
• chmod 755 filename - Set permissions numerically (rwxr-xr-x)
• chmod u+rwx,g+rx,o+rx filename - Set permissions symbolically
• chmod -R 644 directory/ - Recursive permissions change
• chmod u+x script.sh - Add execute permission for owner
• chmod g-w filename - Remove write for group
• chmod o-rwx filename - Remove all permissions for others

📌 Special Permissions:
• chmod u+s filename - Set SUID (run as owner)
• chmod g+s directory - Set SGID (inherit group for new files)
• chmod +t directory - Set sticky bit (only owner can delete)
• Example: rwxr-sr-t = SUID and sticky bit set
• ls -l /usr/bin/passwd - See SUID in action (rwsr-xr-x)

🎭 Default Permissions with umask:
• umask - Show current umask value
• umask 022 - Set umask (new files: 644, directories: 755)
• umask 027 - Restrict others (new files: 640, directories: 750)
• umask -S - Show umask symbolically
• echo "umask 022" >> ~/.bashrc - Set permanent umask

🔍 Viewing Permissions:
• ls -l filename - Show permissions and ownership
• stat filename - Detailed permission and metadata
• getfacl filename - Show Access Control Lists (if used)
• namei -f /path/to/file - Show permissions along path
• lsattr filename - List extended attributes

💡 Permissions Tips:
• Use numeric mode for quick changes (e.g., 755, 644)
• Symbolic mode is more readable: u=user, g=group, o=others
• SUID/SGID useful for scripts and shared directories
• Sticky bit common for /tmp (drwxrwxrwt)
• Always verify with ls -l after changes

⚠️ Safety Tips:
• Avoid 777 permissions unless absolutely necessary
• Be cautious with SUID/SGID (security risks)
• Test permission changes on non-critical files
• Use chown/chmod -R carefully to avoid affecting unintended files
• Backup important files before modifying permissions

[Interactive permissions exercises coming soon!]

Press Escape to return to Basic Topics menu.
        """
