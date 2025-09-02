"""Intermediate level content for the Linux TUI Tutorial"""


class IntermediateTopicsContent:
    """Content for intermediate Linux topics"""
    
    @staticmethod
    def get_menu_content() -> str:
        """Get the intermediate topics menu content"""
        return """
⚡ Intermediate Topics Menu

Select a subtopic to advance your Linux skills:

⚙️ Process Management
Master controlling and monitoring system processes, job control, and systemd.
Commands: ps, kill, killall, top, htop, systemctl, jobs, nohup

📊 System Monitoring  
Learn performance analysis, resource monitoring, and log management.
Tools: iostat, vmstat, sar, journalctl, dmesg, free, df

💾 Storage & Filesystems
Advanced disk management, LVM, RAID, and filesystem optimization.
Topics: LVM, RAID, filesystem tuning, quotas, ACLs

💻 Shell Scripting
Write advanced bash scripts with functions, loops, and error handling.
Topics: Variables, functions, conditionals, loops, parameter expansion

👥 User Management
Understand user accounts, groups, sudo configuration, and PAM.
Commands: useradd, usermod, passwd, sudo, groups, id

📦 Package Management
Learn software installation, dependency management, and repository configuration.
Tools: apt, yum, dnf, snap, flatpak, rpm, dpkg

🌐 Network Basics
Basic network configuration, troubleshooting, and monitoring.
Commands: ip, netstat, ss, ping, traceroute, wget, curl

Click on a subtopic or use arrow keys to navigate and press Enter to select.
Press Escape or click '← Back' to return to the main menu.
        """
    
    @staticmethod
    def get_topic_content(topic_id: str) -> str:
        """Get content for a specific intermediate topic"""
        content_map = {
            "process": IntermediateTopicsContent._get_process_content(),
            "monitor": IntermediateTopicsContent._get_monitoring_content(),
            "storage": IntermediateTopicsContent._get_storage_content(),
            "shell": IntermediateTopicsContent._get_shell_content(),
            "users": IntermediateTopicsContent._get_users_content(),
            "packages": IntermediateTopicsContent._get_packages_content(),
            "network": IntermediateTopicsContent._get_network_content(),
        }
        return content_map.get(topic_id, f"Content for {topic_id} coming soon!")
    
    @staticmethod
    def _get_process_content() -> str:
        """Process management content"""
        return """
⚙️ Process Management - Advanced Process Control

Master the art of managing system processes and services:

🔍 Process Monitoring:
• ps aux - Show all running processes with detailed info
• ps -ef - Alternative process listing format  
• pstree - Display processes in tree format
• top - Real-time process monitor (interactive)
• htop - Enhanced version of top (if installed)
• pgrep pattern - Find processes by name pattern

🎯 Process Control:
• kill PID - Terminate process by ID
• kill -9 PID - Force kill process (SIGKILL)
• kill -15 PID - Graceful termination (SIGTERM)
• killall process_name - Kill all processes by name
• pkill pattern - Kill processes matching pattern

⚡ Job Control:
• command & - Run command in background
• jobs - List active jobs
• fg %1 - Bring job 1 to foreground
• bg %1 - Send job 1 to background
• nohup command & - Run command immune to hangups
• disown - Remove job from shell's job table

🔧 systemd Service Management:
• systemctl status service - Check service status
• systemctl start service - Start a service
• systemctl stop service - Stop a service
• systemctl restart service - Restart a service
• systemctl enable service - Enable service at boot
• systemctl disable service - Disable service at boot
• systemctl daemon-reload - Reload systemd configuration

📊 Resource Management:
• nice -n 10 command - Run with lower priority
• renice 5 PID - Change process priority
• ionice -c 2 -n 5 PID - Set I/O priority
• ulimit -a - Show resource limits
• cgroups - Control groups for resource isolation

Press Escape to return to Intermediate Topics menu.
        """
    
    @staticmethod
    def _get_monitoring_content() -> str:
        """System monitoring content"""
        return """
📊 System Monitoring - Performance Analysis & Diagnostics

Learn to monitor system health and troubleshoot performance issues:

🏃 CPU & Load Monitoring:
• uptime - System load averages and uptime
• lscpu - Display CPU architecture information
• vmstat 2 - Virtual memory statistics every 2 seconds
• iostat 2 - I/O and CPU statistics
• sar -u 2 5 - CPU utilization every 2 seconds, 5 times
• mpstat - Multi-processor statistics

💾 Memory Monitoring:
• free -h - Memory usage in human-readable format
• cat /proc/meminfo - Detailed memory information
• vmstat -s - Virtual memory statistics summary
• slabtop - Kernel slab cache information
• pmap PID - Memory map of a process

💿 Disk I/O Monitoring:
• iotop - Real-time I/O usage by process (requires root)
• iostat -x 2 - Extended I/O statistics
• lsblk - List block devices
• df -h - Disk space usage
• du -sh /path/* - Directory sizes
• fuser /path/file - Show processes using a file

🌐 Network Monitoring:
• ss -tuln - Show listening ports
• netstat -i - Network interface statistics
• iftop - Real-time network usage by connection
• nethogs - Network usage by process
• tcpdump -i eth0 - Packet capture on interface

📝 Log Analysis:
• journalctl - View systemd logs
• journalctl -f - Follow log in real-time
• journalctl -u service - Logs for specific service
• dmesg - Kernel ring buffer messages
• tail -f /var/log/syslog - Follow system log
• grep ERROR /var/log/* - Search for errors in logs

🔧 System Information:
• lshw - Detailed hardware information
• lspci - PCI devices
• lsusb - USB devices
• dmidecode - DMI/SMBIOS information
• sensors - Temperature and voltage readings

Press Escape to return to Intermediate Topics menu.
        """
    
    @staticmethod
    def _get_storage_content() -> str:
        """Storage and filesystems content"""
        return """
💾 Storage & Filesystems - Advanced Disk Management

Master storage technologies and filesystem management:

🏗️ LVM (Logical Volume Management):
• pvcreate /dev/sdb - Create physical volume
• vgcreate vg_name /dev/sdb - Create volume group
• lvcreate -L 10G -n lv_name vg_name - Create logical volume
• lvextend -L +5G /dev/vg_name/lv_name - Extend volume
• resize2fs /dev/vg_name/lv_name - Resize filesystem

⚡ RAID Configuration:
• mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sdb /dev/sdc
• cat /proc/mdstat - Check RAID status
• mdadm --detail /dev/md0 - Detailed RAID information
• mdadm --fail /dev/md0 /dev/sdb - Mark device as failed
• mdadm --remove /dev/md0 /dev/sdb - Remove failed device

📁 Filesystem Management:
• mkfs.ext4 /dev/device - Create ext4 filesystem
• mkfs.xfs /dev/device - Create XFS filesystem
• tune2fs -l /dev/device - Display filesystem information
• fsck -f /dev/device - Force filesystem check
• mount -o remount,rw /filesystem - Remount with different options

🔐 Advanced Features:
• setfacl -m u:user:rwx /path - Set ACL permissions
• getfacl /path - View ACL permissions
• setquota -u user 1000000 1200000 0 0 /filesystem - Set user quota
• quota -u user - Check user quota usage
• lsattr /path/file - List file attributes
• chattr +i /path/file - Make file immutable

🔧 Filesystem Tuning:
• tune2fs -o journal_data_writeback /dev/device - Change journal mode
• xfs_info /mount/point - XFS filesystem geometry
• btrfs filesystem show - Btrfs filesystem information
• zfs list - ZFS datasets (if ZFS is available)

💿 Device Management:
• blkid - Display block device attributes
• lsblk -f - Show filesystem information
• findmnt - Display mounted filesystems
• mount | column -t - Formatted mount table
• fuser -v /mount/point - Show processes using filesystem

🔄 Backup & Snapshots:
• lvcreate -L 1G -s -n snap_name /dev/vg/lv - LVM snapshot
• btrfs subvolume snapshot /source /dest - Btrfs snapshot
• rsync -av --progress /source/ /destination/ - Efficient backup

Press Escape to return to Intermediate Topics menu.
        """
    
    @staticmethod
    def _get_shell_content() -> str:
        """Shell scripting content"""
        return """
💻 Shell Scripting - Advanced Bash Programming

Master automation and scripting for system administration:

🔧 Script Structure & Basics:
• #!/bin/bash - Shebang line
• chmod +x script.sh - Make script executable
• ./script.sh - Execute script
• bash -x script.sh - Debug script execution
• set -e - Exit on error
• set -u - Exit on undefined variable

📊 Variables & Parameters:
• variable="value" - Variable assignment
• $1, $2, $3 - Positional parameters
• $# - Number of parameters
• $@ - All parameters as separate words
• $* - All parameters as single word
• $? - Exit status of last command
• $$ - Process ID of script

🔄 Control Structures:
• if [ condition ]; then ... fi - Conditional execution
• for var in list; do ... done - For loop
• while [ condition ]; do ... done - While loop
• case $var in pattern) ... ;; esac - Case statement
• [ -f file ] - Test if file exists
• [ -d directory ] - Test if directory exists

🛠️ Functions:
• function_name() { commands; } - Function definition
• local var="value" - Local variable in function
• return 0 - Return from function with status
• $1, $2 in functions - Function parameters

📝 Advanced Parameter Expansion:
• ${var:-default} - Use default if var is unset
• ${var:=default} - Set var to default if unset
• ${var:+alternate} - Use alternate if var is set
• ${var#pattern} - Remove shortest match from beginning
• ${var##pattern} - Remove longest match from beginning
• ${var%pattern} - Remove shortest match from end

🔗 Process Management:
• command1 | command2 - Pipe output
• command1 && command2 - Execute if first succeeds
• command1 || command2 - Execute if first fails
• command & - Run in background
• wait $! - Wait for background job
• trap 'cleanup' EXIT - Execute cleanup on exit

📁 File Operations:
• read -p "Prompt: " variable - Read user input
• while IFS= read -r line; do ... done < file - Read file line by line
• exec 3< file; read -u 3 line - File descriptor operations
• find /path -name "*.txt" -exec rm {} \; - Find and execute

🔍 Error Handling:
• if ! command; then echo "Failed"; exit 1; fi
• command || { echo "Error"; exit 1; }
• set -o pipefail - Catch pipeline failures
• logger "Script message" - Log to syslog

Press Escape to return to Intermediate Topics menu.
        """
    
    @staticmethod
    def _get_users_content() -> str:
        """User management content"""
        return """
👥 User Management - Managing Accounts & Permissions

Learn to manage user accounts, groups, and advanced permissions:

🔧 User Account Management:
• useradd -m username - Create user with home directory
• usermod -aG groupname username - Add user to group
• userdel -r username - Delete user and home directory
• passwd username - Change user password
• chage -E 2025-12-31 username - Set account expiration
• id username - Display user and group information
• who - Show currently logged-in users
• w - Show detailed user login information

👥 Group Management:
• groupadd groupname - Create a new group
• groupdel groupname - Delete a group
• gpasswd -a username groupname - Add user to group
• gpasswd -d username groupname - Remove user from group
• groups username - List groups for a user
• getent group groupname - Display group details
• cat /etc/group - View all groups

🔐 Sudo Configuration:
• visudo - Edit sudoers file safely
• usermod -aG sudo username - Add user to sudo group
• sudo -l - List user’s sudo privileges
• echo "username ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/username - Custom rule
• sudo -u username command - Run command as another user
• sudo -i - Login as root (or another user)

🔒 PAM (Pluggable Authentication Modules):
• cat /etc/pam.d/sshd - View SSH PAM configuration
• pam_tally2 --user username - Check login attempts
• pam_tally2 --user username --reset - Reset login attempts
• /etc/security/limits.conf - Set resource limits for users
• authconfig --update - Update PAM configuration
• pam_env - Set environment variables via PAM

📋 Password Management:
• passwd -l username - Lock user account
• passwd -u username - Unlock user account
• chpasswd < users.txt - Bulk update passwords
• cat /etc/shadow - View hashed passwords
• pwgen 12 - Generate secure 12-character passwords
• mkpasswd - Generate hashed passwords (requires whois)

🔍 Auditing & Monitoring:
• last - Show last login history
• lastlog - Display last login details for all users
• faillog - Display failed login attempts
• auditctl -w /etc/passwd -k passwd_changes - Watch password file
• ausearch -k passwd_changes - Search audit logs
• journalctl -u sshd - View SSH login attempts

💡 User Management Tips:
• Use -m with useradd to create home directories
• Always use visudo to edit sudoers to avoid syntax errors
• Check /etc/passwd and /etc/group for user/group details
• Use id or groups to verify user settings
• Set restrictive umask for new users in /etc/profile

⚠️ Safety Tips:
• Backup /etc/passwd, /etc/shadow, /etc/group before changes
• Avoid direct edits to /etc/sudoers without visudo
• Test sudo rules with sudo -l before relying on them
• Use strong passwords and consider password policies
• Monitor last and faillog for suspicious activity

[Interactive user management exercises coming soon!]

Press Escape to return to Intermediate Topics menu.
        """
    
    @staticmethod
    def _get_packages_content() -> str:
        """Package management content"""
        return """
📦 Package Management - Software Installation & Repositories

Learn to install, manage, and configure software packages:

🛠️ Debian-based Systems (apt):
• apt update - Update package lists
• apt upgrade - Upgrade installed packages
• apt install package_name - Install a package
• apt remove package_name - Remove a package (keep configs)
• apt purge package_name - Remove package and configs
• apt autoremove - Remove unneeded dependencies
• apt search keyword - Search for packages
• apt show package_name - Show package details

🔧 Red Hat-based Systems (yum/dnf):
• yum update - Update package lists and packages
• dnf update - Update (dnf is newer than yum)
• yum install package_name - Install a package
• dnf install package_name - Install with dnf
• yum remove package_name - Remove a package
• dnf autoremove - Remove unneeded dependencies
• yum search keyword - Search for packages
• dnf info package_name - Show package details

📦 RPM and DPKG (Low-level Tools):
• rpm -ivh package.rpm - Install RPM package
• rpm -e package_name - Remove RPM package
• rpm -qa - List all installed packages
• rpm -qi package_name - Show package information
• dpkg -i package.deb - Install DEB package
• dpkg -r package_name - Remove DEB package
• dpkg -l - List installed packages
• dpkg -L package_name - List files installed by package

📲 Snap Packages:
• snap install package_name - Install a snap package
• snap remove package_name - Remove a snap package
• snap list - List installed snaps
• snap refresh - Update all snap packages
• snap info package_name - Show snap details
• snap find keyword - Search for snap packages

📥 Flatpak Packages:
• flatpak install flathub app_name - Install from Flathub
• flatpak uninstall app_name - Remove a flatpak app
• flatpak list - List installed flatpaks
• flatpak update - Update all flatpaks
• flatpak search keyword - Search for flatpak apps
• flatpak info app_name - Show app details

🔗 Repository Management:
• add-apt-repository ppa:name - Add PPA (Ubuntu)
• apt edit-sources - Edit /etc/apt/sources.list
• dnf config-manager --add-repo url - Add DNF repository
• yum-config-manager --add-repo url - Add YUM repository
• cat /etc/apt/sources.list - View Debian repositories
• cat /etc/yum.repos.d/*.repo - View Red Hat repositories

🔍 Package Verification & Queries:
• apt-cache depends package_name - Show dependencies
• dnf repoquery --requires package_name - Show dependencies
• rpm -V package_name - Verify package integrity
• dpkg --verify package_name - Verify DEB package
• apt-file search filename - Find package providing file
• dnf provides filename - Find package providing file

💾 Local Package Management:
• dpkg -i package.deb - Install local DEB file
• rpm -Uvh package.rpm - Upgrade/install RPM file
• apt install ./package.deb - Install local DEB with apt
• dnf install ./package.rpm - Install local RPM with dnf
• tar -xzvf package.tar.gz - Extract tarball source

⚙️ Package Cleanup:
• apt autoclean - Remove old package files
• dnf clean all - Clean DNF cache
• yum clean all - Clean YUM cache
• snap refresh --hold - Hold snap updates
• flatpak uninstall --unused - Remove unused runtimes

💡 Package Management Tips:
• Always run update before install/upgrade
• Use apt over dpkg, dnf over rpm for dependency handling
• Check repository sources for security/stability
• Use snap/flatpak for sandboxed apps
• Regularly clean caches to save disk space

⚠️ Safety Tips:
• Verify repository sources to avoid malicious packages
• Backup /etc/apt or /etc/yum.repos.d before changes
• Test package installs in a VM or container first
• Avoid mixing package managers (e.g., apt and snap)
• Monitor package changelogs for breaking changes

[Interactive package management exercises coming soon!]

Press Escape to return to Intermediate Topics menu.
        """
    
    @staticmethod
    def _get_network_content() -> str:
        """Network basics content"""
        return """
🌐 Network Basics - Configuration & Troubleshooting

Learn basic network configuration, troubleshooting, and monitoring:

🔌 Network Configuration:
• ip addr show - Display network interfaces and IPs
• ip link set eth0 up - Enable network interface
• ip link set eth0 down - Disable network interface
• ip addr add 192.168.1.100/24 dev eth0 - Assign IP address
• ip route show - Show routing table
• ip route add default via 192.168.1.1 - Set default gateway

📡 Network Status:
• nmcli device status - Show network device status
• nmcli connection show - List network connections
• nmcli con up connection_name - Activate connection
• nmcli con down connection_name - Deactivate connection
• cat /etc/resolv.conf - Show DNS servers
• hostname -i - Show host IP address

🔍 Network Troubleshooting:
• ping 8.8.8.8 - Test connectivity to Google DNS
• ping -c 4 google.com - Send 4 pings to domain
• traceroute google.com - Trace route to destination
• mtr google.com - Continuous ping and traceroute
• dig google.com - DNS lookup
• nslookup google.com - Alternative DNS lookup

🌐 Network Monitoring:
• ss -tuln - Show listening TCP/UDP ports
• netstat -tuln - Alternative to ss
• netstat -i - Show interface statistics
• ifconfig - Show interface details (older systems)
• ip -s link - Show interface statistics
• netcat -zv host port - Test port connectivity

📥 Data Transfer:
• wget http://example.com/file - Download file
• curl http://example.com - Fetch URL content
• curl -O http://example.com/file - Download with original name
• scp file.txt user@host:/path - Secure copy to remote
• rsync -av file.txt user@host:/path - Sync with remote
• ftp host - Connect to FTP server

🔧 Network Configuration Files:
• cat /etc/hosts - Local hostname mappings
• cat /etc/network/interfaces - Debian network config
• cat /etc/sysconfig/network-scripts/ifcfg-* - Red Hat network config
• nmcli con mod connection_name ipv4.addresses 192.168.1.100/24
• nmcli con mod connection_name ipv4.dns 8.8.8.8 - Set DNS

💡 Network Tips:
• Use ip instead of ifconfig (modern systems)
• Check /etc/resolv.conf for DNS issues
• Use -c with ping to limit attempts
• Combine curl/wget with pipes: curl url | grep pattern
• Test connectivity with ping before complex tasks

⚠️ Safety Tips:
• Avoid exposing unnecessary ports (check with ss)
• Use scp or rsync for secure file transfers
• Verify hostnames in /etc/hosts to avoid DNS issues
• Backup network configs before editing
• Test network changes in a safe environment

[Interactive network exercises coming soon!]

Press Escape to return to Intermediate Topics menu.
        """
