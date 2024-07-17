# HYDRALang

HYDRALang is a tape-based esoteric programming language inspired by languages like Brainf**k. HYDRAlang has 8 different commands that perform bit-wise operations on a series of bytes, called "heads".

## Table of Contents

---
* [Running a HYDRALang Program](#running-a-hydralang-program)
* [HYDRALang Programming](#hydralang-programming)
  * [The Environment](#the-environment)
  * [Commands](#commands)
* [License](#license)

## Running a HYDRAlang Program

--- 
[Back to top](#table-of-contents)  
HYDRALang programs can be run in three different ways. The first method involves passing a string sequence of commands as a command-line argument into the HYDRALang Python script:
```
python hydralang.py "-!"
```
The second method involves `echo`ing a string sequence of commands and piping the command to the HYDRALang Python script:
```
echo "-!" | python hydralang.py
```
The third method is similar to the second, but involves writing the sequence of commands in a file, using `cat` or `head` to output the contents of the file, and piping the output to the HYDRALang Python script.

For example, given a file named `commands.hydralang`:
```
-!
```
Its commands can be executed by entering the following in the command-line:
```
cat "commands.hydralang" | python hydralang.py
```

## HYDRALang Programming

---
[Back to top](#table-of-contents)  
As stated earlier, HYDRALang has 8 commands that perform bit-wise operations on a series of bytes, called "heads".

### The Environment
Only one head exists at the beginning of every HYDRALang program, and it's initialized to a value of zero. This head is the "current head" at the start of the HYDRALang program. More heads can be added through usage of the `%` command. The current head can be changed by using the `>` command. These commands are explained in further detail in the following section.

> It's important to note that HYDRALang does not use the two's complement when representing numbers as bytes (e.g. `0b10000000` is `128` in HYDRALang not `-128`).

### Commands
HYDRALang has 8 commands that can be used to perform various operations on the heads present during the program's execution:

* `-` inverts the leftmost bit of the current head. E.g. if the current head's value is `0` (`0b00000000` in binary), it would become `128` (`0b10000000` in binary).
* `;` moves the leftmost bit of the current head to the rightmost spot. E.g. if the current head's value is `128` (`0b10000000` in binary), it would become `1` (`0b00000001`).
* `%` creates a new head that's a copy of the current head. This does **NOT** change the current head, however. Heads in HYDRALang are stored as a list, and this command appends the new head to the end of the list.
* `>` changes the current head to the next head in the list. If there are no more heads left in the list, the current head becomes the first head in the list.
* `!` outputs the character representation of the byte value of the current head.
* `#` deletes the current head. The new current head becomes the head before the most recently deleted head, or the last head in the list if the recently deleted head was the first head in the list. If deleting a head would cause there to be no heads left, the program terminates.
* `[` skips to the command past its matching `]` if the decimal value of the current head is less than `128`.
* `]` goes back to its matching `[` command if the decimal value of the current head is greater than or equal to `128`.
