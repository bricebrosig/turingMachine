"""This python program simulates a simple turing machine"""

tape = [0 for n in range(0,1000)]  # start out with 1000 addresses
head = 0  # read write head in the memory array 
program_counter = 0

def inc(*args):
    """move head up on the tape"""
    global head
    head = head + 1
    
def dec(*args):
    """move head back on the tape"""
    global head
    head = head - 1
    
def add(*args):
    """increment the value on tape at the head by 1"""
    global head, tape
    tape[head] = tape[head] + 1
    
def sub(*args):
    """decrement the value on the tape at the head by 1"""
    global head, tape
    tape[head] = tape[head] - 1

def my_write(*args):
    """print value at the head"""
    global head, tape
    print(tape[head])
    
def put(i=0, *args):  # if none given, puts a zero in the cell
    """write a given value to the tape at the head; if none given write zero"""
    global head, tape
    tape[head] = int(i)

def get_while(local_prog_count, *args):  # note that this is a local program counter
    """get the instructions to repeat in a while loop, then call the while
    
    also put the program counter at the end of the while loop for when we get done
    """
    global head, tape, prog, program_counter
    instructions = prog[local_prog_count+1:prog.index('}', local_prog_count)]
    program_counter = prog.index('}', local_prog_count) + 1
    my_while(instructions)

def my_while(instructions, *args):
    """repeat instructions until value on tape at head is 0"""
    global head, tape, prog
    i = 0  # a sort of temp program counter
    while(tape[head]):
        table[instructions[i][0]](instructions[i][1] if len(instructions[i]) > 1 else head)
        i = (i+1) if i < len(instructions) - 1 else 0

def end_while(*args):
    """a no-op if we see a closed while"""
    ...

table = {  # the instruction set for the program
    '>': inc,  # ++head
    '<': dec,  # --head
    '+': add,  # ++value at head
    '-': sub,  # --value at head
    '^': my_write,  # print value at head
    '.': put,   # write input to cell
    '{': get_while,  # begin while
    '}': end_while  # do nothing...
}

prog = ['>', '.5', '{', '^', '-', '}']  # our program

for j in range(0, len(prog)):  # run the program and increment program counter each time
    if program_counter >= len(prog): break
    table[prog[program_counter][0]](prog[program_counter][1] if len(prog[program_counter]) > 1 else j)
    program_counter = program_counter + 1