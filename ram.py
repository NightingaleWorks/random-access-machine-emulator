import sys
from collections import defaultdict

class RAM:
        def compute(self, program, data):
                self._parse(program)
                self.registers = defaultdict(int)
                self.registers[1] = data
                self.program_counter = 0
                self.steps = 0
                while self.program_counter < len(self.program):
                        self._compute_inst(self.program[self.program_counter])
                return self.registers[0]

        def _compute_inst(self, inst):
                self.steps += 1
                if inst == None:
                        print("PC " + ";" + str(self.program_counter))
                        print("Registers " + ";" + str(self.registers))
                        self.program_counter += 1

                elif inst[0] == 0:
                        print("PC " + ";" + str(self.program_counter))
                        self.registers[inst[1]] += 1
                        print("Registers " + ";" + str(self.registers))
                        self.program_counter += 1
                elif inst[0] == 1:
                        print("PC " + ";" + str(self.program_counter))
                        self.registers[inst[1]] = max(0, self.registers[inst[1]]-1)
                        print("Registers " + ";" + str(self.registers))
                        self.program_counter += 1
                elif inst[0] == 2:
                        if self.registers[inst[1]] == 0:
                                print("PC " + ";" + str(self.program_counter))
                                print("Registers " + ";" + str(self.registers))
                                self.program_counter = inst[2]
                        else:
                                print("PC " + ";" + str(self.program_counter))
                                print("Registers " + ";" + str(self.registers))
                                self.program_counter += 1

        def _parse(self, program):
                instructions = program.split('\n')
                max_jump = len(instructions)
                self.program = list(self._parse_inst(max_jump, index, inst) for index, inst in enumerate(instructions, 1))
                print("Parsed Program " + ";" + str(self.program))

        def _parse_inst(self, max_jump, index, inst):
                try:
                        inst = inst.split(' ')
                        if not len(inst) or (len(inst) == 1 and inst[0] == ''):
                                return None
                        if len(inst) == 2:
                                if inst[0].lower() == 'inc':
                                        r = int(inst[1])
                                        if r >= 0:
                                                return 0, r
                                elif inst[0].lower() == 'dec':
                                        r = int(inst[1])
                                        if r >= 0:
                                                return 1, r
                        elif len(inst) == 3:
                                if inst[0].lower() == 'jz':
                                        r = int(inst[1])
                                        i = int(inst[2])
                                        if r >= 0 and i > 0 and i <= max_jump:
                                                return 2, r, i-1
                except Exception as e:
                        raise Exception(f'Syntax error on line {index}:\n{e}')
                print(max_jump, index, inst)
                raise Exception(f'Syntax error on line {index}')



def main():
        try:
                with open(sys.argv[1], 'r') as program:
                        program = program.read()
                data = int(sys.argv[2])
        except:
                print('Usage: python ram.py <ram source file> <input integer> [OPTIONAL (pipe stdout) > outfile]')
        else:
                ram = RAM()
                output = ram.compute(program, data)
                print("Output " + ";" + str(output))
                print("Number of steps " + ";" + str(ram.steps-1))

if __name__ == '__main__':
        main()