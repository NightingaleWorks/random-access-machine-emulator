# ⚙️ random-access-machine-emulator

RAM is an abstract machine that is turing complete and can compute any partial recursive function.<br>
Find out more here: https://en.wikipedia.org/wiki/Random-access_machine

This is the modified version of GabrieleMaurina's machine to count steps and see much more details.

https://github.com/GabrieleMaurina/random-access-machine/

## 🔧 How to use:

- Save your RAM program in a text file
- Make sure you have Python 3 installed
- Download ram.py & run in terminal or PS: 

```python ram.py ram_instructions.txt 4```

- where ram_instractions.txt is your RAM program and 4 is the input number

- if you would like to have the output in a file, pipe the command

```python ram.py ram_instructions.txt 4 > output.txt```

## 🧩 Instructions (Maurina, 2021):
The ram machine supports only three basic instructions:

Increment register k by 1:

inc k

Decrement register k by 1:

dec k

Jump to instruction i if register k is zero:

jz k i

## 🔍Example (Maurina, 2021):
An example program that will double whatever input you give to the machine (doubling.txt):
```
jz 1 6
inc 0
inc 0
dec 1
jz 2 1
dec 1
```
## 💡Explanation of the output:

### Parsed Program ;[(2, 1, 5), (0, 0), (0, 0), (1, 1), (2, 2, 0), (1, 1)]
So, the program has been designed in an object-oriented way.
The RAM class has _parse() and _parse_inst() methods to read the program from the txt file and returns
the list of the instructions.
As you can see, your program lines, what are numbered from 1. They are turning to be counted from 0.
I designed this row of output if you would like to analyze the internal workings of the machine.
The first numbers are the codes of the instructions. 0 is inc, 1 is dec, 2 is jz.

### PC ;0
PC is the status of the program counter.

### Registers ;defaultdict(<class 'int'>, {1: 4})
You can see the values in registers when the machine is working. 1 is the input register with value 4.

### Registers ;defaultdict(<class 'int'>, {1: 3, 0: 2, 2: 0})
It is an interesting point of the program. From where is coming register 2, with the value 0?
It is a jump instruction (2, 2, 0), so we jump to line 32:<br>
💡 if self.registers[inst[1]] == 0:<br>
This line starts to evaluate is register 2 equal to 0?
This is triggering defaultdict() to create register 2 with value 0, and it is evaluated at the same time.
Due to defeaultdict(), we don't have to pre-define registers.

PC ;0<br>
Registers ;defaultdict(<class 'int'>, {1: 0, 0: 8, 2: 0})<br>
PC ;5<br>
Registers ;defaultdict(<class 'int'>, {1: 0, 0: 8, 2: 0})<br>
Output ;8<br>
Number of steps ;21<br>

This is the end of the example. The input register (1) is 0, so the program jumps to the last line.
The last line is 'dec 1', but we can see that register 1 is still 0.

The secret is in line 27:<br>
💡self.registers[inst[1]] = max(0, self.registers[inst[1]]-1)

So we have max(0,-1), which is 0.
This line ensures that the register (and PC) will never be negative.

The output register (0) is 8. The program has been executed in 21 steps
(there are 5 instructions, which are repeated by 4 times, plus the last line = 21 steps).

The working register (2) always has the value 0.

I have used ";" separator to open the file in spreadsheets.

Happy coding! 😀 <br>
Enjoy! 🌈
