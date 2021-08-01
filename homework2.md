1. Download file https://pastebin.com/raw/EjFebawG and rename it to `grepdata.txt`. Use the file with the follwing tasks.
2. Print all lines that contain a phone number with an extension (the letter x or X followed by four digits).
3. Print all lines that begin with three digits followed by a space symbol.
4. Print all lines that contain a date. Hint: this is a very simple pattern. It doesn't have to work for any year before 2000.
5. Augment command used for task 4 to get output formatted like `Month/Day` (Example: `Oct/15`). Hint: you must use pipes here.
6. Write a script, which reads two numbers through arguments or interactive input and outputs the biggest number or prints 'equal' if the numbers are equal.
7. Write a script to check to see if the file `$file_path` exists. If it does exist, print `$file_path exists.`. On success, check to see if you can write to the file. If you can, print `You have permissions to edit $file_path`. If you cant, print `You do NOT have permissions to edit $file_path.`'. Read `$file_path` from script agument. If there is no argument provided read it from standart input.
8. In this exercise, you will need to loop through and print out all even numbers from the numbers list in the same order they are received. Don't print any numbers that come after 237 in the sequence.
```bash
#!/bin/bash
NUMBERS="951 402 984 651 360 69 408 319 601 485 980 507 725 547 544 615 83 165 141 501 263 617 865 575 219 390 237 412 566 826 248 866 950 626 949 687 217 815 67 104 58 512 24 892 894 767 553 81 379 843 831 445 742 717 958 609 842 451 688 753 854 685 93 857 440 380 126 721 328 753 470 743 527"

# write your code here
```
9. Write a script that that will simulate a bash prompt and will log every command to a file, prepended by the current date.
