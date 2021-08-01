# Lesson 2: Shell scripting

## Text file processing

### grep

Say we have a `file.txt` with this content:
```
ostechnix
Ostechnix
0stechnix
05technix
o$technix
linux
linu
linus
unix
technology
hello world
HELLO world
look!
wooow
```

Let's find strings containing `nix`
```bash
grep nix file.txt
grep -n nix file.txt
```

`grep` is case-sensitive:
```bash
grep os file.txt
grep -i os file.txt 
grep -i 'hello world' file.txt 
```

Basic regular expressions:
```bash
grep '^tech' file.txt
grep 'x$' file.txt
grep '.n' file.txt
```

> Write a grep statement which will match lines starting with `linu` followed by one character.

Extended regular expressions with `egrep` (same as `grep -E`):
```bash
egrep '^[l-u]' file.txt
egrep '^[0-9]+' file.txt
egrep '^[0-9]*' file.txt
egrep 'o{2}' file.txt
egrep 'o{2,3}' file.txt
egrep '^[^o]' file.txt
egrep '^(l|o)' file.txt
egrep '^o\$' file.txt
```

> More on regular expressions: https://www.regular-expressions.info/quickstart.html  
> Practice regex: https://regex101.com/

Use `fgrep` (same as `grep -F`) to ignore the special characters.
```bash
fgrep 'x$' file.txt
fgrep 'o$' file.txt
```

### cut and awk

We can use `cut` to select one or more column from a file, using a delimiter:
```bash
cut -d':' -f1 /etc/passwd
cut -d':' -f1,3 /etc/passwd --output-delimiter=' ### '
```

`awk` is also a good tool for column selction:
```bash
ls -l | awk '{print $9}'
cat /etc/passwd | awk -F':' '{print $1}'
cat /etc/passwd | awk -F':' '{print $1" ### "$2}'
# we can use long delimiters
cat /etc/group | awk -F':x:' '{print $1}'
```

## Connecting programs

There are several common file descriptors of the running process:
* 0 - stdin
* 1 - stdout
* 2 - stderr

File descriptors of the process are accessible through the filesystem.
```bash
ls /proc/<pid>/fd
```

`stdout` redirections:
```bash
echo hello > hello.txt
cat hello.txt
cat < hello.txt
cat < hello.txt > hello2.txt
cat hello2.txt
```

`stderr` redirections:
```bash
# This will not write the output to the file, since the errors go to stderr
ls no_file > error.txt
# This way we redirect stderr to the file.
ls no_file 2> error.txt
# We can also redirect stderr into stdout and then redirect stdout to file
ls no_file > error.txt 2>&1
```

### Subshell redirections

Here `cmd1 <(cmd2)` construct executes the `cmd2` in the subshell and creates a temporary file which then gets passed to `cmd1` as an argument:
```bash
cat <(date)
cat /etc/timezone <(date) <(echo hello)
cat <(ls no_file) > subsh_error.txt
cat <(ls no_file 2>&1) > subsh_error.txt
```

Here `cmd1 $(cmd2)` construct executes the `cmd2` in the subshell and passes the stdout of `cmd2` to `cmd1` as an argument directly:
```bash
# Use stdout of the subshell as an argument
echo $(date)
d=$(date)
echo $d
```

### Redirecting and appending

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

Using grep with pipes:
```bash
ls /tmp | grep systemd
ls /tmp | grep systemd | cut -d'-' -f4
```

> More on redirections: https://www.gnu.org/software/bash/manual/html_node/Redirections.html

## Exit codes and boolean operators

`$?` - Return code of the previous command:
```bash
ls no_file
echo $?
ls ~
echo $?
```
As you can see on successful execution the exit code is `0`. `1` and other exit codes mean that something went wrong. Exit code is an 8 bit unsigned integer so the possible values are `0-255`.

We can conditionally run a command based on exit code of a previous one.
```bash
false || echo "Oops, fail"
# Oops, fail

true || echo "Will not be printed"
#

true && echo "Things went well"
# Things went well

false && echo "Will not be printed"
#

true ; echo "This will always run"
# This will always run

false ; echo "This will always run"
# This will always run
```

## Shell scripting

Let's write our first script:
```bash
nano script.sh
```

Every script starts with a shebang `#!/bin/bash`. The shebang shows us which program will execute the script when called.
```bash
#!/bin/bash
# This is a comment!
echo "My first script, yay!"  # This is a comment too!
```

> What do we need to do to make `script.sh` executable?

If the script is not available through any path in `$PATH` environment variable, then we have to call it directly:
```bash
$ ./script.sh "arg1" "arg2" ...
```

There are some special variables, which we can use inside the script files.

`$0` - Name of the script/shell
```bash
#!/bin/bash
echo "My name is $0"
```

`$1` to `$9` - Arguments to the script. `$1` is the first argument and so on.
```bash
#!/bin/bash
echo "Hello $1, good to see you and your friend $2!" 
```

We can also read the data interactively.
```bash
#!/bin/sh
echo What is your name?
read my_name
echo "Hello $my_name - hope you're well."
```

`$$` - Process identification number (PID) for the current script/shell

`$@` - All the arguments. We can it to create a simple `python3` wrapper script named `py3wrap.sh`, which would look like this:
```bash
#!/bin/bash
export MY_VAR=1
exec python3 "$@"
```

Now if we use the wrapper, we will see the value of `MY_VAR` avalable inside of python3 environment:
```bash
# This will print 'None'
python3 -c 'import os; print(os.environ.get("MY_VAR"))'
# This will print the value of 'MY_VAR'
./py3wrap.sh -c 'import os; print(os.environ.get("MY_VAR"))'
```

`exec` replaces the current shell with the command execution. `eval` evaluates the command in the current shell:

```bash
bash -c 'echo $$ ; exec ls -l /proc/self ; echo foo'
bash -c 'echo $$ ; eval ls -l /proc/self ; echo foo'
```

We can modify `py3wrap.sh` to see the difference:

```bash
#!/bin/bash
export MY_VAR=1=1
eval python3 "$@"
echo this line will not be printed
```

```bash
#!/bin/bash
export MY_VAR=1=1
exec python3 "$@"
echo this line will be printed
```

`$#` - Number of arguments.

> Try to guess what's the purpose of the following script and if it works correctly? (the importance of the curly bracets)
```bash
#!/bin/sh
echo "What is your name?"
read USER_NAME
echo "Hello $USER_NAME"
touch $USER_NAME_file
```

### Conditionals

Use `test` to perform various checks.

> Open `man` for `test` and tell me which option checks whether file exists.
```bash
#/bin/bash
test -f "$1" && cat "$1" || echo "No such file as $1"
```

Use `if` for conditionals.
```bash
#/bin/bash
if test -f "$1"
then
  cat "$1"
else
  echo "No such file as $1"
fi
```

We can use `[` instesd of `test`, ***why***? Spaces are important.
```bash
#/bin/bash
if [ -f $1 ]; then
  cat $1
else
  echo "No such file as $1"
fi
```

`elif` statement and string comparison:
```bash
if [ "$1" == "opt1" ]; then
  echo "Option 1"
elif [ "$1" == "opt2" ]; then
  echo "Option 2"
else
  echo "Unknown option"
fi
```

We can use `case` statement if options are numerous.
```bash
#!/bin/bash
case $1 in
hello)
  echo "Hello yourself!"
  ;;
whatsup)
  echo "Not much. What about you?"
  ;;
bye|farewell)
  echo "See you again!"
  ;;
*)
  echo "Sorry, I don't understand that."
  ;;
esac
```

### Loops

Basic for loops:

```bash
#!/bin/bash
var="a b c"
for char in ${var}; do
  echo "${char}"
done
```

```bash
#!/bin/bash
for i in {1..5}; do
  echo "Looping ... number $i"
done
```

Basic while loop:
```bash
#!/bin/bash
INPUT_STRING=hello
while [ "${INPUT_STRING}" != "bye" ]; do
  echo "Please type something in (bye to quit)"
  read INPUT_STRING
  echo "You typed: ${INPUT_STRING}"
done
```

Read file line by line:
```bash
while read -r line; do
  echo "${line}"
done < file.txt
```
