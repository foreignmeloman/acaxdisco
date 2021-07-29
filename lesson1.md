# Lesson 1: The Shell

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

A good practice is to use `${variable}` syntax.
```bash
foo_baz=bard
echo $foo_baz
echo ${foo}_baz
unset foo
```

Almost all commands are programs. POSIX paths are usually delimited with ':' symbol.
```bash
which echo
echo $PATH
```

We can call each program directly:
```bash
/bin/echo $PATH
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
mv file1 dir1/
cp file1 file2
cp -r dir1 dir2
```

Command arguments, POSIX standards.
```bash
ls -l
man ls
ls -a
ls -al
ls --all -l
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


## Connecting programs

There are several common file descriptors of the running process:
* stdout
* stdin
* stderr

File descriptors of the process are accessible through the filesystem.
```bash
ls /proc/<pid>/fd
```

Basic redirections.
```bash
echo hello > hello.txt
cat hello.txt
cat < hello.txt
cat < hello.txt > hello2.txt
cat hello2.txt
```

Demonstrated in the example above, cat is a program that concatenates files. When given file names as arguments, it prints the contents of each of the files in sequence to its output stream. But when cat is not given any arguments, it prints contents from its input stream to its output stream (like in the third example above).

`>` overwrites the file contents, while `>>` appends to the end of the file.
```bash
echo hola > hello.txt
cat hello.txt
echo world >> helo.txt
cat hello.txt
```

The pipes are where the real fun begins. `|` lets you redirect `stdout` of one program to `stdin` of another one.
```bash
ls -l | tail -2
```

More on redirections: https://www.gnu.org/software/bash/manual/html_node/Redirections.html

Using grep with pipes.
```bash
ls /tmp|grep username
ls /tmp|grep -v username
ls /tmp|grep -E regex
```
