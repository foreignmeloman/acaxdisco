# Lesson 3: sudo, storage and systemd

## sudo

`sudo` gives us option to perform commands as root user.
```bash
# This will not work for an unprivileged user
apt update
# But this will
sudo apt update
```

Only users or groups described in file `/etc/sudoers` of directory `/etc/sudoers.d` will be able to use `sudo`.
```
user host=(user_as) command
```

Example:
```bash
sudo -i
useradd testuser
passwd testuser
visudo
# Here we'll add the following line and save
testuser ALL=(myusername) /bin/ls
# Switch user to testuser
su testuser
# This will not work
ls ~myusername/.ssh
# But this will
sudo -u myusername ls ~myusername/.ssh
```

> More on sudo:  
> https://www.hostinger.com/tutorials/sudo-and-the-sudoers-file/  
> https://www.garron.me/en/linux/visudo-command-sudoers-file-sudo-default-editor.html  
> https://www.linux.com/training-tutorials/configuring-sudo-explaination-example/

## Storage

### Hands-on 1

For this task we'll need a linux machine with attached additional drive. It can be either a physical external drive or an additional virtual drive if you're using a VM.

1. Use `fdisk` and `lsblk` to locate the drive we want to mount.
```bash
# fdisk will show us all the storage devices and their partitions.
# The drive we are looking for is not a loop device and should not have any partitions
fdisk -l
# To be sure we can also use lsblk to see if the suspect drive has any mount points
lsblk
# Let's assume the dive we found is /dev/sdb
```

2. Run `fdisk` on the located drive, delete all partitions (if any) and split it into two partitions.
```bash
fdisk /dev/sdb

# Typing in 'p' we can show the existing partitions of the drive, if any exists.
# Use 'd' if there are any existing partitions.
Command (m for help): p
Disk /dev/sdb: 10 GiB, 10737418240 bytes, 20971520 sectors
Disk model: VBOX HARDDISK   
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x843c7ff7

# Create the partitions
Command (m for help): n
Partition type
   p   primary (0 primary, 0 extended, 4 free)
   e   extended (container for logical partitions)
Select (default p):

Using default response p
Partition number (1-4, default 1):
First sector (2048-20971519, default 2048): 
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-20971519, default 20971519): +5G

Created a new partition 1 of type 'Linux' and of size 5 GiB.

Command (m for help): n
Partition type
   p   primary (1 primary, 0 extended, 3 free)
   e   extended (container for logical partitions)
Select (default p): 

Using default response p.
Partition number (2-4, default 2): 
First sector (10487808-20971519, default 10487808): 
Last sector, +/-sectors or +/-size{K,M,G,T,P} (10487808-20971519, default 20971519): 

Created a new partition 2 of type 'Linux' and of size 5 GiB.
```

3. Use `mkfs` to format the first partition as `ext4` and the second one as `btrfs` and mount them to `/mnt/ext4` and `/mnt/btrfs` directories.
```bash
mkfs -t ext4 /dev/sdb1
mkfs -t btrfs /dev/sdb2
mount /dev/sdb1 /mnt/ext4
mount /dev/sdb2 /mnt/btrfs
```
4. Use `lsblk` to view the drives and partitions hierarchy.

## systemd

### Hands-on 2

1. Install `nginx` using `apt`.
```bash
apt install nginx
```

2. Enable `nginx` service and start it.
```bash
systemctl enable --now nginx
```

3. Open the nginx default page in your browser.
```bash
# Or just use curl
curl localhost
```

4. Examine `/etc/nginx/sites-enabled/default` config file to find out which directory is used for serving the web content.
```bash
# look for keyword 'root'
```

5. Add your own landing page, which would change the message to "Hello nginx!". Check it with your browser or curl.
```bash
echo "Hello nginx!" > /var/www/html/index.html
curl localhost
```

---

Now we can use `telnet` to talk to the web server directly:
```
$ telnet localhost 80
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
GET / HTTP/1.1
HOST: localhost
```

Let's check systemd commands:
```
# systemctl status nginx
# systemctl list-units | grep nginx
# systemctl enable nginx
# systemctl restart nginx
```
