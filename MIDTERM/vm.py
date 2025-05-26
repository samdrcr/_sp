#范權榮 111210557 27/05/2025
class SimpleVM:
    
    def __init__(self):
        # 8 general-purpose registers (R0-R7)
        self.registers = [0] * 8
        # 256 memory locations (8-bit addressing)
        self.memory = [0] * 256
        # Instruction pointer
        self.ip = 0
        # Running flag
        self.running = False
        # Debug mode
        self.debug = False
        
        # Instruction set mapping
        self.instructions = {
            0x00: self._halt,     # HALT
            0x01: self._load,     # LOAD reg, value
            0x02: self._store,    # STORE address, reg
            0x03: self._move,     # MOVE dest_reg, src_reg
            0x04: self._add,      # ADD dest_reg, src_reg
            0x05: self._sub,      # SUB dest_reg, src_reg
            0x06: self._mul,      # MUL dest_reg, src_reg
            0x07: self._div,      # DIV dest_reg, src_reg
            0x08: self._jmp,      # JMP address
            0x09: self._jz,       # JZ reg, address
            0x0A: self._jnz,      # JNZ reg, address
            0x0B: self._jgt,      # JGT reg, address
            0x0C: self._jlt,      # JLT reg, address
            0x0D: self._print,    # PRINT reg
            0x0E: self._load_m,   # LOAD_M reg, address
            0x0F: self._and,      # AND dest_reg, src_reg
            0x10: self._or,       # OR dest_reg, src_reg
            0x11: self._xor,      # XOR dest_reg, src_reg
            0x12: self._not,      # NOT reg
        }
    
    def load_program(self, program):
        
        # Copy program into memory
        for i, byte in enumerate(program):
            if i < len(self.memory):
                self.memory[i] = byte
            else:
                raise ValueError("Program too large for memory")
    
    def load_program_from_file(self, filename):
        
        with open(filename, 'rb') as f:
            program = list(f.read())
            self.load_program(program)
    
    def run(self, debug=False):
        
        self.debug = debug
        self.running = True
        self.ip = 0
        
        while self.running and self.ip < len(self.memory):
            self._execute_instruction()
    
    def _execute_instruction(self):
        
        # Fetch
        opcode = self.memory[self.ip]
        
        if self.debug:
            print(f"Executing instruction at {self.ip}: {opcode:02x}")
            print(f"Registers: {self.registers}")
        
        # Decode and execute
        if opcode in self.instructions:
            # Increment IP to point to the first operand
            self.ip += 1
            # Execute the instruction
            self.instructions[opcode]()
        else:
            print(f"Unknown opcode: {opcode:02x} at address {self.ip}")
            self.running = False
    
    def _halt(self):
        """Stop execution."""
        self.running = False
    
    def _load(self):
        """Load value into register."""
        reg = self.memory[self.ip]
        value = self.memory[self.ip + 1]
        
        if 0 <= reg < len(self.registers):
            self.registers[reg] = value
        else:
            print(f"Invalid register: {reg}")
        
        self.ip += 2
    
    def _store(self):
        """Store register value to memory."""
        address = self.memory[self.ip]
        reg = self.memory[self.ip + 1]
        
        if 0 <= reg < len(self.registers) and 0 <= address < len(self.memory):
            self.memory[address] = self.registers[reg]
        else:
            print(f"Invalid register or address: reg={reg}, address={address}")
        
        self.ip += 2
    
    def _move(self):
        """Copy value from one register to another."""
        dest_reg = self.memory[self.ip]
        src_reg = self.memory[self.ip + 1]
        
        if 0 <= dest_reg < len(self.registers) and 0 <= src_reg < len(self.registers):
            self.registers[dest_reg] = self.registers[src_reg]
        else:
            print(f"Invalid register: dest_reg={dest_reg}, src_reg={src_reg}")
        
        self.ip += 2
    
    def _add(self):
        """Add two registers."""
        dest_reg = self.memory[self.ip]
        src_reg = self.memory[self.ip + 1]
        
        if 0 <= dest_reg < len(self.registers) and 0 <= src_reg < len(self.registers):
            self.registers[dest_reg] += self.registers[src_reg]
        else:
            print(f"Invalid register: dest_reg={dest_reg}, src_reg={src_reg}")
        
        self.ip += 2
    
    def _sub(self):
        """Subtract src from dest."""
        dest_reg = self.memory[self.ip]
        src_reg = self.memory[self.ip + 1]
        
        if 0 <= dest_reg < len(self.registers) and 0 <= src_reg < len(self.registers):
            self.registers[dest_reg] -= self.registers[src_reg]
        else:
            print(f"Invalid register: dest_reg={dest_reg}, src_reg={src_reg}")
        
        self.ip += 2
    
    def _mul(self):
        """Multiply two registers."""
        dest_reg = self.memory[self.ip]
        src_reg = self.memory[self.ip + 1]
        
        if 0 <= dest_reg < len(self.registers) and 0 <= src_reg < len(self.registers):
            self.registers[dest_reg] *= self.registers[src_reg]
        else:
            print(f"Invalid register: dest_reg={dest_reg}, src_reg={src_reg}")
        
        self.ip += 2
    
    def _div(self):
        """Divide dest by src."""
        dest_reg = self.memory[self.ip]
        src_reg = self.memory[self.ip + 1]
        
        if 0 <= dest_reg < len(self.registers) and 0 <= src_reg < len(self.registers):
            if self.registers[src_reg] != 0:
                self.registers[dest_reg] //= self.registers[src_reg]
            else:
                print("Division by zero")
        else:
            print(f"Invalid register: dest_reg={dest_reg}, src_reg={src_reg}")
        
        self.ip += 2
    
    def _jmp(self):
        """Jump to address."""
        address = self.memory[self.ip]
        
        if 0 <= address < len(self.memory):
            self.ip = address
        else:
            print(f"Invalid jump address: {address}")
            self.ip += 1
    
    def _jz(self):
        """Jump if zero."""
        reg = self.memory[self.ip]
        address = self.memory[self.ip + 1]
        
        if 0 <= reg < len(self.registers) and 0 <= address < len(self.memory):
            if self.registers[reg] == 0:
                self.ip = address
            else:
                self.ip += 2
        else:
            print(f"Invalid register or address: reg={reg}, address={address}")
            self.ip += 2
    
    def _jnz(self):
        """Jump if not zero."""
        reg = self.memory[self.ip]
        address = self.memory[self.ip + 1]
        
        if 0 <= reg < len(self.registers) and 0 <= address < len(self.memory):
            if self.registers[reg] != 0:
                self.ip = address
            else:
                self.ip += 2
        else:
            print(f"Invalid register or address: reg={reg}, address={address}")
            self.ip += 2
    
    def _jgt(self):
        """Jump if greater than zero."""
        reg = self.memory[self.ip]
        address = self.memory[self.ip + 1]
        
        if 0 <= reg < len(self.registers) and 0 <= address < len(self.memory):
            if self.registers[reg] > 0:
                self.ip = address
            else:
                self.ip += 2
        else:
            print(f"Invalid register or address: reg={reg}, address={address}")
            self.ip += 2
    
    def _jlt(self):
        """Jump if less than zero."""
        reg = self.memory[self.ip]
        address = self.memory[self.ip + 1]
        
        if 0 <= reg < len(self.registers) and 0 <= address < len(self.memory):
            if self.registers[reg] < 0:
                self.ip = address
            else:
                self.ip += 2
        else:
            print(f"Invalid register or address: reg={reg}, address={address}")
            self.ip += 2
    
    def _print(self):
        """Print value in register."""
        reg = self.memory[self.ip]
        
        if 0 <= reg < len(self.registers):
            print(f"Output: {self.registers[reg]}")
        else:
            print(f"Invalid register: {reg}")
        
        self.ip += 1
    
    def _load_m(self):
        """Load from memory to register."""
        reg = self.memory[self.ip]
        address = self.memory[self.ip + 1]
        
        if 0 <= reg < len(self.registers) and 0 <= address < len(self.memory):
            self.registers[reg] = self.memory[address]
        else:
            print(f"Invalid register or address: reg={reg}, address={address}")
        
        self.ip += 2
    
    def _and(self):
        """Bitwise AND."""
        dest_reg = self.memory[self.ip]
        src_reg = self.memory[self.ip + 1]
        
        if 0 <= dest_reg < len(self.registers) and 0 <= src_reg < len(self.registers):
            self.registers[dest_reg] &= self.registers[src_reg]
        else:
            print(f"Invalid register: dest_reg={dest_reg}, src_reg={src_reg}")
        
        self.ip += 2
    
    def _or(self):
        """Bitwise OR."""
        dest_reg = self.memory[self.ip]
        src_reg = self.memory[self.ip + 1]
        
        if 0 <= dest_reg < len(self.registers) and 0 <= src_reg < len(self.registers):
            self.registers[dest_reg] |= self.registers[src_reg]
        else:
            print(f"Invalid register: dest_reg={dest_reg}, src_reg={src_reg}")
        
        self.ip += 2
    
    def _xor(self):
        """Bitwise XOR."""
        dest_reg = self.memory[self.ip]
        src_reg = self.memory[self.ip + 1]
        
        if 0 <= dest_reg < len(self.registers) and 0 <= src_reg < len(self.registers):
            self.registers[dest_reg] ^= self.registers[src_reg]
        else:
            print(f"Invalid register: dest_reg={dest_reg}, src_reg={src_reg}")
        
        self.ip += 2
    
    def _not(self):
        """Bitwise NOT."""
        reg = self.memory[self.ip]
        
        if 0 <= reg < len(self.registers):
            self.registers[reg] = ~self.registers[reg]
        else:
            print(f"Invalid register: {reg}")
        
        self.ip += 1


def main():
    """Main function to run the VM."""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python vm.py <program_file> [--debug]")
        return
    
    vm = SimpleVM()
    
    try:
        vm.load_program_from_file(sys.argv[1])
        debug = "--debug" in sys.argv
        vm.run(debug=debug)
    except FileNotFoundError:
        print(f"File not found: {sys.argv[1]}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

#范權榮 111210557 27/05/2025