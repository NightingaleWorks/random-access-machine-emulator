random-access-machine-emulator

RAM is an abstract machine that is turing complete and can compute any partial recursive function. Find out more here https://en.wikipedia.org/wiki/Random-access_machine

This is the modified version GabrieleMaurina's machine to count steps and see much more details.

https://github.com/GabrieleMaurina/random-access-machine/

Usage:
Download ram.py & run in terminal or PS: 

python ram.py doubling.txt 4

--- or if you would like to have the output in file, just pipe it ---

python ram.py doubling.txt 4 > output.txt

Instructions:
A ram machine supports only 3 basic instructions:

Increment register k by 1:

inc k

Decrement register k by 1:

dec k

Jump to instruction i if register k is zero:

jz k i

Example
An example program that will double whatever input you give to the machine (doubling.txt):

jz 1 6
inc 0
inc 0
dec 1
jz 2 1
dec 1
