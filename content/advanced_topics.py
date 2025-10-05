"""Advanced level content for the Linux TUI Tutorial"""


class AdvancedTopicsContent:
    """Content for advanced Linux topics"""
    
    @staticmethod
    def get_menu_content() -> str:
        """Get the advanced topics menu content"""
        return """
🚀 Advanced Topics Menu

Select a subtopic for expert-level Linux knowledge:

🔧 Kernel & Modules
Low-level system management, kernel compilation, and module development.
Commands: lsmod, modprobe, rmmod, modinfo, dkms, make menuconfig

🌐 Advanced Networking
Network security, traffic shaping, VPNs, and complex configurations.
Tools: iptables, tc, OpenVPN, WireGuard, netfilter, bridge-utils

🔐 Security Hardening
System security, mandatory access controls, and vulnerability mitigation.
Topics: SELinux, AppArmor, audit system, secure boot, hardening guides

🐳 Virtualization
Container technologies, orchestration, and virtual machine management.
Tools: Docker, Kubernetes, LXC, KVM, QEMU, libvirt

🏗️ High Availability
Clustering, load balancing, and fault-tolerant system design.
Tools: Pacemaker, Corosync, HAProxy, keepalived, DRBD

🔍 System Internals
Deep understanding of kernel internals, memory management, and debugging.
Topics: /proc, /sys, system calls, memory mapping, kernel debugging

⚡ Performance Tuning
System optimization, profiling, and advanced performance analysis.
Tools: perf, strace, ltrace, valgrind, SystemTap, eBPF

Click on a subtopic or use arrow keys to navigate and press Enter to select.
Press Escape or click '← Back' to return to the main menu.
        """
    
    @staticmethod
    def get_topic_content(topic_id: str) -> str:
        """Get content for a specific advanced topic"""
        content_map = {
            "kernel": AdvancedTopicsContent._get_kernel_content(),
            "network": AdvancedTopicsContent._get_networking_content(),
            "security": AdvancedTopicsContent._get_security_content(),
            "virtual": AdvancedTopicsContent._get_virtualization_content(),
            "ha": AdvancedTopicsContent._get_ha_content(),
            "internals": AdvancedTopicsContent._get_internals_content(),
            "performance": AdvancedTopicsContent._get_performance_content(),
        }
        return content_map.get(topic_id, f"Content for {topic_id} coming soon!")
    
    @staticmethod
    def _get_kernel_content() -> str:
        """Kernel and modules content"""
        return """
🔧 Kernel & Modules - Low-Level System Management

Master kernel management, module development, and system customization:

📋 Kernel Information:
• uname -r - Show kernel version
• cat /proc/version - Detailed kernel information
• cat /proc/cmdline - Kernel boot parameters
• dmesg | head - Kernel boot messages
• lscpu - CPU and architecture details
• cat /proc/cpuinfo - Detailed CPU information

🔌 Module Management:
• lsmod - List loaded kernel modules
• modinfo module_name - Show module information
• modprobe module_name - Load a module with dependencies
• modprobe -r module_name - Remove module and dependencies
• rmmod module_name - Remove module (no dependency handling)
• depmod -a - Update module dependency database

🏗️ Kernel Compilation:
• make menuconfig - Configure kernel options (ncurses interface)
• make xconfig - Configure kernel options (Qt interface)
• make defconfig - Use default configuration
• make -j$(nproc) - Compile kernel using all CPU cores
• make modules - Compile kernel modules
• make modules_install - Install compiled modules
• make install - Install kernel to /boot

📦 DKMS (Dynamic Kernel Module Support):
• dkms status - Show DKMS module status
• dkms add module/version - Add module to DKMS
• dkms build module/version - Build module
• dkms install module/version - Install DKMS module
• dkms remove module/version --all - Remove module

🔧 Kernel Parameters:
• sysctl -a - Show all kernel parameters
• sysctl kernel.hostname - Show specific parameter
• sysctl -w net.ipv4.ip_forward=1 - Set parameter temporarily
• echo 'net.ipv4.ip_forward=1' >> /etc/sysctl.conf - Permanent setting
• sysctl -p - Reload sysctl configuration

💾 Memory Management:
• cat /proc/meminfo - Memory information
• cat /proc/slabinfo - Slab allocator information
• echo 3 > /proc/sys/vm/drop_caches - Drop page caches
• cat /proc/buddyinfo - Buddy allocator information
• cat /proc/pagetypeinfo - Page type information

🔍 Kernel Debugging:
• dmesg -w - Follow kernel messages in real-time
• journalctl -k - Show kernel messages from journal
• cat /proc/kallsyms - Kernel symbol table
• crash vmlinux vmcore - Kernel crash analysis
• kexec - Kernel execution for crash dumps

⚡ Real-Time Kernel:
• chrt -f -p 99 PID - Set real-time FIFO priority
• chrt -r -p 50 PID - Set real-time round-robin priority
• cat /sys/kernel/realtime - Check if RT kernel
• cyclictest - Real-time latency testing

Press Escape to return to Advanced Topics menu.
        """
    
    @staticmethod
    def _get_networking_content() -> str:
        """Advanced networking content"""
        return """
🌐 Advanced Networking - Network Security & Configuration

Master network administration, security, and troubleshooting:

🔥 Firewall Management (iptables):
• iptables -L -v -n - List all rules with verbose output
• iptables -A INPUT -p tcp --dport 22 -j ACCEPT - Allow SSH
• iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
• iptables -A INPUT -j DROP - Default deny
• iptables-save > /etc/iptables/rules.v4 - Save rules
• iptables-restore < /etc/iptables/rules.v4 - Restore rules

🛡️ Advanced Firewall (nftables):
• nft list tables - List all tables
• nft add table inet filter - Add new table
• nft add chain inet filter input { type filter hook input priority 0 \; }
• nft add rule inet filter input tcp dport ssh accept
• nft list ruleset - Show complete ruleset

🌉 Network Bridging:
• brctl addbr br0 - Create bridge
• brctl addif br0 eth0 - Add interface to bridge
• brctl show - Show bridge information
• ip link add br0 type bridge - Modern bridge creation
• ip link set dev eth0 master br0 - Add interface to bridge

🔗 Network Bonding:
• modprobe bonding - Load bonding module
• echo +bond0 > /sys/class/net/bonding_masters - Create bond
• echo balance-rr > /sys/class/net/bond0/bonding/mode - Set mode
• echo +eth0 > /sys/class/net/bond0/bonding/slaves - Add slave

🌐 VLAN Configuration:
• modprobe 8021q - Load VLAN module
• vconfig add eth0 100 - Create VLAN 100 on eth0
• ip link add link eth0 name eth0.100 type vlan id 100 - Modern VLAN
• ip addr add 192.168.100.10/24 dev eth0.100 - Assign IP to VLAN

🔒 VPN Technologies:
• openvpn --config client.ovpn - OpenVPN client connection
• wg genkey | tee privatekey | wg pubkey > publickey - WireGuard keys
• wg-quick up wg0 - Bring up WireGuard interface
• ipsec status - Check IPSec status
• strongswan status - StrongSwan IPSec status

📊 Traffic Control (tc):
• tc qdisc add dev eth0 root handle 1: htb default 12 - HTB qdisc
• tc class add dev eth0 parent 1: classid 1:1 htb rate 1000mbit
• tc class add dev eth0 parent 1:1 classid 1:12 htb rate 100mbit ceil 200mbit
• tc filter add dev eth0 protocol ip parent 1:0 prio 1 handle 1 fw classid 1:12

🔍 Network Troubleshooting:
• tcpdump -i any -n host 192.168.1.100 - Capture packets for host
• wireshark - GUI packet analyzer
• nmap -sS -O target - TCP SYN scan with OS detection
• hping3 -S -p 80 target - Custom packet crafting
• mtr target - Network path analysis
• ss -tulpn - Show listening services

🌍 Advanced Routing:
• ip route add 10.0.0.0/8 via 192.168.1.1 - Add static route
• ip route add default via 192.168.1.1 table 100 - Route table
• ip rule add from 192.168.2.0/24 table 100 - Policy routing
• bird - Dynamic routing daemon
• quagga - Routing software suite

Press Escape to return to Advanced Topics menu.
        """
    
    @staticmethod
    def _get_security_content() -> str:
        """Security hardening content"""
        return """
🔐 Security Hardening - System Security & Protection

Master system security, access controls, and vulnerability mitigation:

🛡️ SELinux (Security-Enhanced Linux):
• getenforce - Check SELinux status
• setenforce 1 - Enable enforcing mode
• sestatus - Detailed SELinux status
• ls -Z file - Show SELinux context
• chcon -t httpd_exec_t /usr/bin/httpd - Change context
• setsebool -P httpd_can_network_connect on - Set boolean
• semanage fcontext -a -t httpd_exec_t "/custom/httpd"

🔒 AppArmor:
• aa-status - Show AppArmor status
• aa-enforce /etc/apparmor.d/usr.bin.firefox - Enforce profile
• aa-complain /etc/apparmor.d/usr.bin.firefox - Complain mode
• aa-genprof /usr/bin/newprogram - Generate new profile
• aa-logprof - Process audit logs for profile updates

🕵️ Audit System:
• auditctl -l - List audit rules
• auditctl -w /etc/passwd -p wa -k passwd_changes - Watch file
• auditctl -a always,exit -F arch=b64 -S openat -k file_access
• ausearch -k passwd_changes - Search audit logs
• aureport -au - Authentication report
• auditd - Audit daemon management

🔐 Access Control & Authentication:
• getfacl /path/to/file - Get ACL permissions
• setfacl -m u:username:rwx /path/to/file - Set user ACL
• setfacl -x u:username /path/to/file - Remove user ACL
• visudo - Edit sudoers file safely
• pam_tally2 --user username --reset - Reset failed login attempts

🛡️ System Hardening:
• chattr +i /etc/passwd - Make file immutable
• mount -o remount,noexec /tmp - Remount with noexec
• echo 0 > /proc/sys/net/ipv4/ip_forward - Disable IP forwarding
• sysctl net.ipv4.conf.all.send_redirects=0 - Disable redirects
• ulimit -c 0 - Disable core dumps

🔍 Vulnerability Assessment:
• lynis audit system - Security audit tool
• chkrootkit - Rootkit checker
• rkhunter --check - Rootkit hunter
• clamav-freshclam - Update antivirus signatures
• clamscan -r /home - Scan directory for malware

🚫 Intrusion Detection:
• fail2ban-client status - Show fail2ban status
• fail2ban-client status sshd - Show SSH jail status
• aide --init - Initialize AIDE database
• aide --check - Check for file changes
• tripwire --check - File integrity checking

🔑 Encryption & PKI:
• gpg --gen-key - Generate GPG key pair
• gpg --encrypt --recipient user@domain file - Encrypt file
• openssl genrsa -out private.key 2048 - Generate RSA key
• openssl req -new -x509 -key private.key -out cert.crt - Self-signed cert
• cryptsetup luksFormat /dev/sdb1 - LUKS encrypt device
• cryptsetup luksOpen /dev/sdb1 encrypted_device - Open LUKS device

⚡ Secure Boot & UEFI:
• mokutil --sb-state - Check Secure Boot state
• efibootmgr - Manage UEFI boot entries
• sbctl status - Secure Boot control (if available)
• pesign --verify /boot/vmlinuz - Verify kernel signature

🔐 Container Security:
• docker run --security-opt apparmor=profile container - AppArmor profile
• docker run --cap-drop=ALL container - Drop all capabilities
• docker run --read-only container - Read-only filesystem
• podman run --userns=keep-id container - User namespace mapping

Press Escape to return to Advanced Topics menu.
        """
    
    @staticmethod
    def _get_virtualization_content() -> str:
        """Virtualization content"""
        return """
🐳 Virtualization - Containers & Virtual Machines

Master containerization, orchestration, and virtualization technologies:

🐋 Docker Fundamentals:
• docker run -it ubuntu:latest /bin/bash - Interactive container
• docker build -t myapp:latest . - Build image from Dockerfile
• docker ps -a - List all containers
• docker images - List all images
• docker exec -it container_name /bin/bash - Execute in running container
• docker logs container_name - View container logs
• docker stop container_name - Stop running container
• docker rm container_name - Remove container

🔧 Docker Advanced:
• docker run -v /host/path:/container/path image - Volume mounting
• docker run -p 8080:80 image - Port mapping
• docker run --network=host image - Host networking
• docker run --memory=512m --cpus=1.0 image - Resource limits
• docker system prune - Clean up unused resources
• docker inspect container_name - Detailed container info

🚢 Docker Compose:
• docker-compose up -d - Start services in background
• docker-compose down - Stop and remove services
• docker-compose logs service_name - View service logs
• docker-compose scale web=3 - Scale service to 3 replicas
• docker-compose exec service_name /bin/bash - Execute in service

☸️ Kubernetes Basics:
• kubectl get pods - List all pods
• kubectl get services - List all services
• kubectl describe pod pod_name - Detailed pod information
• kubectl logs pod_name - View pod logs
• kubectl exec -it pod_name -- /bin/bash - Execute in pod
• kubectl apply -f deployment.yaml - Apply configuration
• kubectl delete -f deployment.yaml - Remove configuration

🎛️ Kubernetes Management:
• kubectl create namespace dev - Create namespace
• kubectl get nodes - List cluster nodes
• kubectl top pods - Resource usage by pods
• kubectl rollout status deployment/app - Check rollout status
• kubectl scale deployment app --replicas=5 - Scale deployment
• helm install myapp ./mychart - Install Helm chart

📦 Container Management:
• podman run --rm -it fedora:latest - Podman container
• buildah from fedora:latest - Build container with Buildah
• skopeo copy docker://image:tag containers-storage:image:tag
• runc run container_name - Low-level container runtime
• crun run container_name - Alternative container runtime

🖥️ Virtual Machine Management (KVM/QEMU):
• virsh list --all - List all VMs
• virsh start vm_name - Start virtual machine
• virsh shutdown vm_name - Gracefully shutdown VM
• virsh destroy vm_name - Force stop VM
• virsh console vm_name - Connect to VM console
• virsh edit vm_name - Edit VM configuration
• virt-install --name test --memory 1024 --vcpus 1 --disk size=10

🔧 VM Advanced Operations:
• virt-clone --original vm1 --name vm2 --auto-clone - Clone VM
• virsh snapshot-create-as vm_name snapshot1 - Create snapshot
• virsh snapshot-revert vm_name snapshot1 - Revert to snapshot
• qemu-img create -f qcow2 disk.qcow2 10G - Create virtual disk
• qemu-img convert -f raw -O qcow2 disk.raw disk.qcow2 - Convert format

🌐 Network Virtualization:
• virsh net-list --all - List virtual networks
• virsh net-start default - Start virtual network
• docker network create --driver bridge mynetwork - Docker network
• docker run --network=mynetwork image - Use custom network
• kubectl create network-policy - Kubernetes network policy

💾 Storage for Containers:
• docker volume create myvolume - Create Docker volume
• docker run -v myvolume:/data image - Use named volume
• kubectl create pv pv_name - Kubernetes persistent volume
• kubectl create pvc pvc_name - Kubernetes persistent volume claim

🔍 Container Monitoring:
• docker stats - Real-time container resource usage
• kubectl top nodes - Node resource usage
• kubectl top pods - Pod resource usage
• cAdvisor - Container monitoring (Google)
• Prometheus + Grafana - Full monitoring stack

Press Escape to return to Advanced Topics menu.
        """
    
    @staticmethod
    def _get_ha_content() -> str:
        """High availability content"""
        return """
🏗️ High Availability - Clustering & Fault Tolerance

Master building resilient, fault-tolerant systems:

🔧 Pacemaker & Corosync Clustering:
• pcs cluster setup --name mycluster node1 node2 - Create cluster
• pcs cluster start --all - Start cluster on all nodes
• pcs status - Show cluster status
• pcs resource create vip IPaddr2 ip=192.168.1.100 - Virtual IP
• pcs resource create webserver apache - Apache resource
• pcs constraint colocation add webserver with vip - Colocation constraint
• pcs constraint order vip then webserver - Order constraint

🌐 Load Balancing with HAProxy:
• haproxy -f /etc/haproxy/haproxy.cfg - Start HAProxy
• echo "show stat" | socat stdio /var/run/haproxy.sock - Show statistics
• echo "disable server web/server1" | socat stdio /var/run/haproxy.sock
• echo "enable server web/server1" | socat stdio /var/run/haproxy.sock
• haproxy -f config.cfg -c - Check configuration syntax

⚖️ nginx Load Balancing:
• nginx -t - Test nginx configuration
• nginx -s reload - Reload configuration
• upstream backend { server web1:80; server web2:80; } - Backend definition
• proxy_pass http://backend - Load balance requests
• ip_hash; - Session persistence based on client IP

🔄 keepalived for VRRP:
• keepalived -f /etc/keepalived/keepalived.conf - Start keepalived
• systemctl status keepalived - Check keepalived status
• vrrp_instance VI_1 { state MASTER; priority 100; } - VRRP config
• virtual_ipaddress { 192.168.1.100/24; } - Virtual IP config

💾 DRBD (Distributed Replicated Block Device):
• drbdadm create-md resource_name - Initialize metadata
• drbdadm up resource_name - Bring up DRBD resource
• drbdadm primary resource_name - Set as primary node
• cat /proc/drbd - Check DRBD status
• drbdadm invalidate-remote resource_name - Force resync

🗄️ Database High Availability:
• mysql --defaults-extra-file=/etc/mysql/debian.cnf - MySQL admin
• SHOW MASTER STATUS; - MySQL master status
• CHANGE MASTER TO MASTER_HOST='master_ip'; - Setup replication
• SHOW SLAVE STATUS\G - MySQL slave status
• pg_basebackup -h master -D /var/lib/postgresql/replica - PostgreSQL replica

📊 Cluster Monitoring:
• crm_mon -A - Pacemaker cluster monitor
• pcs status resources - Resource status
• pcs status nodes - Node status
• corosync-quorumtool -s - Quorum status
• systemctl status corosync pacemaker - Service status

🔍 Health Checks & Monitoring:
• pcs resource op add webserver monitor interval=30s - Add monitor
• pcs resource meta webserver migration-threshold=3 - Failover threshold
• pcs stonith create fence_node fence_ipmilan - STONITH configuration
• pcs constraint location webserver prefers node1=100 - Location preference

⚡ Split-Brain Prevention:
• pcs stonith confirm - Confirm STONITH configuration
• pcs property set stonith-enabled=true - Enable STONITH
• pcs property set no-quorum-policy=ignore - Quorum policy
• crm configure primitive stonith-sbd stonith:external/sbd

🏭 Service Dependencies:
• pcs resource group add webgroup vip webserver - Resource group
• pcs resource clone webserver clone-max=2 - Clone resource
• pcs resource master/slave drbd_resource - Master/slave resource
• pcs constraint order promote drbd_resource then start webserver

🔧 Maintenance Operations:
• pcs cluster standby node1 - Put node in standby
• pcs cluster unstandby node1 - Remove from standby
• pcs resource cleanup webserver - Cleanup resource failures
• pcs resource move webserver node2 - Move resource to node
• pcs resource ban webserver node1 - Ban resource from node

📈 Performance & Scaling:
• pcs resource utilization webserver cpu=2 memory=1024 - Resource utilization
• pcs node utilization node1 cpu=4 memory=4096 - Node capacity
• pcs constraint order set webserver db sequential=true - Ordered sets
• pcs resource clone webserver globally-unique=true - Unique clones

Press Escape to return to Advanced Topics menu.
        """
    
    @staticmethod
    def _get_internals_content() -> str:
        """System internals content"""
        return """
🔍 System Internals - Kernel Internals & Debugging

Deep dive into Linux kernel internals, memory management, and debugging:

📋 Exploring /proc Filesystem:
• cat /proc/cpuinfo - Detailed CPU information
• cat /proc/meminfo - Memory usage details
• cat /proc/interrupts - Interrupt usage
• cat /proc/devices - Registered devices
• cat /proc/filesystems - Supported filesystems
• cat /proc/mounts - Current mounts

🗂️ Exploring /sys Filesystem:
• cat /sys/block/sda/queue/scheduler - I/O scheduler
• echo deadline > /sys/block/sda/queue/scheduler - Set scheduler
• cat /sys/class/net/eth0/speed - Network interface speed
• cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
• echo performance > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor

🔧 System Calls:
• strace -c -p PID - Count system calls for process
• strace -o trace.txt command - Trace system calls
• ltrace -c command - Trace library calls
• sysdig -c topcalls - Top system calls system-wide
• getpid() - Get process ID (example syscall)
• openat(AT_FDCWD, "file.txt", O_RDONLY) - Example file syscall

💾 Memory Management Internals:
• cat /proc/zoneinfo - Memory zone information
• cat /proc/buddyinfo - Buddy allocator details
• cat /proc/pagetypeinfo - Page type information
• cat /proc/slabinfo - Slab allocator statistics
• echo 3 > /proc/sys/vm/drop_caches - Drop caches
• vmstat -m - Memory slab statistics

🔍 Kernel Debugging Tools:
• dmesg -T - Kernel messages with timestamps
• journalctl -k - Kernel logs from systemd
• cat /proc/kallsyms - Kernel symbol table
• crash vmlinux vmcore - Analyze kernel crash dump
• kdump-config status - Check kdump status
• gdb vmlinux /proc/kcore - Debug running kernel

⚙️ Process and Thread Internals:
• cat /proc/PID/status - Process status and memory usage
• cat /proc/PID/maps - Process memory mappings
• cat /proc/PID/fd - Open file descriptors
• cat /proc/PID/task - Thread information
• pmap -x PID - Detailed process memory map
• lsof -p PID - List open files by process

📊 I/O and Scheduling:
• iostat -c - CPU statistics
• iostat -d - Device statistics
• cat /proc/sched_debug - Scheduler debug info
• chrt -r -p 50 PID - Set real-time scheduling
• taskset -cp 0-3 PID - Pin process to CPUs 0-3
• ionice -c 3 PID - Set I/O scheduling class

🔧 eBPF for Internals:
• bpftool prog list - List loaded eBPF programs
• bpftool map list - List eBPF maps
• bcc-tools (e.g., execsnoop) - Trace process execution
• bcc-tools (e.g., opensnoop) - Trace file opens
• bpftrace -e 'kprobe:do_sys_open { printf("%s opened %s\n", comm, str(arg1)); }'

💡 Internals Tips:
• Use /proc for runtime system information
• Be cautious when writing to /sys or /proc
• strace/ltrace for debugging application issues
• Use crash or gdb for kernel crash analysis
• eBPF requires modern kernels (4.1+)

⚠️ Safety Tips:
• Avoid modifying /proc or /sys without understanding
• Test kernel debugging in a VM or non-production system
• Backup crash dumps before analysis
• Ensure kdump is configured for crash recovery
• Monitor system stability after changing scheduling

[Interactive system internals exercises coming soon!]

Press Escape to return to Advanced Topics menu.
        """
    
    @staticmethod
    def _get_performance_content() -> str:
        """Performance tuning content"""
        return """
⚡ Performance Tuning - System Optimization & Profiling

Master system optimization and advanced performance analysis:

📊 Performance Profiling with perf:
• perf stat command - Collect performance statistics
• perf record -p PID - Record performance data
• perf report - Analyze recorded data
• perf top - Real-time system profiling
• perf record -g command - Include call graphs
• perf annotate function_name - View annotated assembly

🔍 System Call Tracing:
• strace -t -p PID - Trace system calls with timestamps
• strace -c command - Summarize system call counts
• sysdig -c topcalls - System-wide syscall statistics
• strace -e openat,read command - Trace specific syscalls
• bpftrace -e 'tracepoint:syscalls:sys_enter_openat { @count++ }'

📚 Library Call Tracing:
• ltrace -c command - Summarize library calls
• ltrace -S command - Include system calls
• ltrace -o trace.txt command - Output to file
• ltrace -f command - Trace child processes
• ltrace -e malloc,free command - Trace specific calls

🔧 Memory Profiling with valgrind:
• valgrind --tool=memcheck command - Check memory leaks
• valgrind --tool=massif command - Profile heap usage
• valgrind --tool=cachegrind command - Cache performance
• valgrind --leak-check=full command - Detailed leak check
• massif-visualizer massif.out.* - Visualize heap data

⚙️ SystemTap Profiling:
• stap -v script.stp - Run SystemTap script
• stap -e 'probe kernel.function("do_sys_open") { println(execname(), " opened ", user_string($filename)) }'
• stap --example cpu.stp - Example CPU probe
• staprun -L - List available probes
• stap -o output.txt script.stp - Output to file

📈 eBPF Performance Tools:
• bpftool prog show - Show loaded eBPF programs
• bcc-tools/biosnoop - Trace block I/O latency
• bcc-tools/execsnoop - Trace new process execution
• bcc-tools/opensnoop - Trace file opens
• bpftrace -e 'kprobe:do_sys_open { @opens[comm] = count(); }' - Count opens

🔍 CPU and Scheduling Tuning:
• taskset -c 0-3 command - Pin to specific CPUs
• chrt -r -p 50 PID - Set real-time priority
• cpupower frequency-set -g performance - Set CPU governor
• cat /proc/cpuinfo - Check CPU capabilities
• tuned-adm profile throughput-performance - Set tuned profile

💾 Memory Tuning:
• sysctl vm.swappiness=10 - Adjust swap usage
• sysctl vm.dirty_ratio=20 - Control dirty page flush
• echo 3 > /proc/sys/vm/drop_caches - Clear caches
• vmstat -SM - Memory stats in MB
• free -m - Memory usage summary

💿 I/O Tuning:
• ionice -c 2 -n 4 command - Set I/O priority
• echo deadline > /sys/block/sda/queue/scheduler - Set I/O scheduler
• iostat -x 1 - Extended I/O statistics
• hdparm -tT /dev/sda - Disk performance test
• fio --name=test --filename=/dev/sda --rw=read - I/O benchmark

🌐 Network Tuning:
• sysctl net.core.somaxconn=1024 - Increase socket backlog
• sysctl net.ipv4.tcp_max_syn_backlog=4096 - TCP backlog
• ethtool -G eth0 rx 4096 tx 4096 - Adjust ring buffers
• ethtool -K eth0 tso off gso off - Disable offloading
• sysctl net.ipv4.tcp_congestion_control=bbr - Set BBR

💡 Performance Tips:
• Use perf for high-level profiling
• Combine strace and perf for detailed insights
• Test tuning in a non-production environment
• Monitor with top, htop, or glances during tuning
• Save profiles for reproducible results

⚠️ Safety Tips:
• Backup sysctl.conf before modifying
• Test performance changes incrementally
• Avoid aggressive tuning on production systems
• Monitor system stability after changes
• Use VMs or containers for experiments

[Interactive performance tuning exercises coming soon!]

Press Escape to return to Advanced Topics menu.
        """
