# Lesson 1: The Shell

## Installing Linux

* VirtualBox
* RHEL/Debian-based iso image

## What is the shell?

* An interface to give commands to the computer.
* Every major OS has an interactive shell of sorts:
	* bash, zsh, fish, csh
	* powershell, cmd
* Prompt structure

## Using the shell

```bash
whoami
who
w
uname -a
```

Commands can have arguments.
```bash
echo hello
echo hello world
echo "hello world"
echo hello\ world
```

We can have variables in the shell.
```bash
foo=bar
echo $foo
```

A good practice is to use `${variable}` syntax in the shell scripts.
```bash
foo_baz=awesome
echo $foo_baz
echo ${foo}_baz
unset foo
```

Almost all commands are programs. POSIX paths are usually delimited with `:` symbol.
```bash
which echo
echo $PATH
```

We can call each program directly:
```bash
/bin/echo $PATH
```

Environment variables.
```bash
env
# open another bash instance
echo $foo
# variable foo is not defined here
exit
export foo
# now the variable is inherited from the parent process
export -n
```

## Navigating the file system

Where am I?
```bash
pwd
ls
cd /
pwd
ls
```

Special destinations, absolute and relative paths.
```bash
cd ~
cd .
cd ..
cd -
cd
```

Creating folders and files:
```bash
touch file1
mkdir dir1
mkdir -p dir2/subdir1
mv file1 dir1/
cp file1 file2
cp -r dir1 dir1_copy
```

Command arguments, POSIX standards.
```bash
ls -l
man ls
ls -a
ls -al
ls --all -l
```

We can use wildcard operators like `*` and `?` to glob the listing.
```bash
ls *.txt
ls file.?
```

Use command `man` to discover more arguments and use cases.
```bash
man ls
ls --help
```

Aliases help to create a short callable for a command plus options.
```bash
alias ll='ls -l'
alias grep='grep --color'
alias gdiff='git diff --no-index'
unalias ll
```

Brace expansions:
```bash
echo {1..10}
echo file.{C,cpp}
```

# nano

Edit text files:
```bash
nano
```

# Hands-on tasks

1. Using `man` tool and linux handbook read about commands `ls`, `pwd`, `cd`, `mkdir`, `mv`, `cp`, `rm`, `touch`, `ln`, `cat`, `clear`, `less`, `uname`, `whoami`, `tar`, `grep`, `head`, `tail`, `diff`, `cmp`, `comm`, `wc`, `sort`, `ps`, `df`, `chmod`, `chown`, `ip`, `curl`, `wget`, `ssh`, `ssh-keygen`, `scp`, `cal`, `alias`, `truncate`, `dd`, `whereis`, `whatis`, `top`, `passwd`, `find`, `locate`, `file`. Try to get a basic idea of these commands.
2. Generate an SSH key pair.
3. Connect to your remote machine with the provieded password. Copy the generated public key to `~/.ssh/` directory of the remote host and rename it to `authorized_keys`. Try to connect to your remote machine using the identity file instead of the password and change your password.
4. Rename file `rename_me` to `renamed`.
5. Create a file named `fixed_size_file` with size 111Mb 111Kb (1Mb =1000Kb). There may be more than one way to do this.
6. Create a file named `os_info` which should include line by line:
	* complete kernel version
	* number of virtual cores
	* max available RAM
	* amount of swap memory,
	* size of configured MTU on non-loopback network interface
	* content of the file called try_to_find_me.student
7. Move all directories where name starts with `Exercise:1*` into a directory `Exercise:1`, delete the one named `Exercise:1 i$ Almost done\folder`.
