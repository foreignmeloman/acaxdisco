# Lesson 2: Shell scripting


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
## WIP

* $0 - Name of the script/shell
* $1 to $9 - Arguments to the script. $1 is the first argument and so on.
* $@ - All the arguments
* $# - Number of arguments
* $? - Return code of the previous command
* $$ - Process identification number (PID) for the current script/shell
* !! - Entire last command, including arguments. A common pattern is to
