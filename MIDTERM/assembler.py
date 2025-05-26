#范權榮 111210557 27/05/2025
import re
import sys

class Assembler:
    
    def __init__(self):
        
        self.instructions = {
            'HALT': 0x00,
            'LOAD': 0x01,
            'STORE': 0x02,
            'MOVE': 0x03,
            'ADD': 0x04,
            'SUB': 0x05,
            'MUL': 0x06,
            'DIV': 0x07,
            'JMP': 0x08,
            'JZ': 0x09,
            'JNZ': 0x0A,
            'JGT': 0x0B,
            'JLT': 0x0C,
            'PRINT': 0x0D,
            'LOAD_M': 0x0E,
            'AND': 0x0F,
            'OR': 0x10,
            'XOR': 0x11,
            'NOT': 0x12
        }
        
        # Register mapping
        self.registers = {
            'R0': 0,
            'R1': 1,
            'R2': 2,
            'R3': 3,
            'R4': 4,
            'R5': 5,
            'R6': 6,
            'R7': 7
        }
        
        # Symbol table for labels
        self.symbols = {}
        
        # Current address
        self.address = 0
        
        # Output bytecode
        self.bytecode = []
        
        # Unresolved references (label, address, position in bytecode)
        self.unresolved = []
    
    def assemble(self, source):
        
        # Reset state
        self.symbols = {}
        self.address = 0
        self.bytecode = []
        self.unresolved = []
        
        # First pass: collect labels
        self._first_pass(source)
        
        # Reset address for second pass
        self.address = 0
        
        # Second pass: generate bytecode
        self._second_pass(source)
        
        # Resolve unresolved references
        self._resolve_references()
        
        return self.bytecode
    
    def _first_pass(self, source):
        
        for line in source.splitlines():
            # Remove comments
            line = re.sub(r';.*$', '', line).strip()
            
            if not line:
                continue
            
            # Check for label
            match = re.match(r'^([A-Za-z0-9_]+):(.*)$', line)
            if match:
                label, rest = match.groups()
                self.symbols[label] = self.address
                line = rest.strip()
            
            if not line:
                continue
            
            # Split instruction and operands
            parts = line.split()
            mnemonic = parts[0].upper()
            
            if mnemonic in self.instructions:
                # Calculate instruction size
                size = 1  # Opcode
                
                if mnemonic in ['HALT']:
                    size += 0
                elif mnemonic in ['PRINT', 'NOT']:
                    size += 1
                else:
                    size += 2
                
                self.address += size
    
    def _second_pass(self, source):
        
        for line in source.splitlines():
            # Remove comments
            line = re.sub(r';.*$', '', line).strip()
            
            if not line:
                continue
            
            # Check for label
            match = re.match(r'^([A-Za-z0-9_]+):(.*)$', line)
            if match:
                label, rest = match.groups()
                line = rest.strip()
            
            if not line:
                continue
            
            # Split instruction and operands
            parts = line.split()
            mnemonic = parts[0].upper()
            operands = parts[1:]
            
            if mnemonic in self.instructions:
                # Add opcode
                opcode = self.instructions[mnemonic]
                self.bytecode.append(opcode)
                self.address += 1
                
                # Process operands
                if mnemonic in ['HALT']:
                    pass  # No operands
                elif mnemonic in ['PRINT', 'NOT']:
                    # One operand: register
                    reg = self._parse_register(operands[0])
                    self.bytecode.append(reg)
                    self.address += 1
                elif mnemonic in ['LOAD', 'LOAD_M', 'JZ', 'JNZ', 'JGT', 'JLT']:
                    # Two operands: register, value/address/label
                    reg = self._parse_register(operands[0])
                    self.bytecode.append(reg)
                    self.address += 1
                    
                    # Second operand could be a value, address, or label
                    if mnemonic == 'LOAD':
                        value = self._parse_value(operands[1])
                        self.bytecode.append(value)
                    else:
                        addr = self._parse_address(operands[1])
                        if addr is None:
                            # Unresolved label
                            self.unresolved.append((operands[1], self.address, len(self.bytecode)))
                            self.bytecode.append(0)  # Placeholder
                        else:
                            self.bytecode.append(addr)
                    self.address += 1
                elif mnemonic in ['STORE']:
                    # Two operands: address/label, register
                    addr = self._parse_address(operands[0])
                    if addr is None:
                        # Unresolved label
                        self.unresolved.append((operands[0], self.address, len(self.bytecode)))
                        self.bytecode.append(0)  # Placeholder
                    else:
                        self.bytecode.append(addr)
                    self.address += 1
                    
                    reg = self._parse_register(operands[1])
                    self.bytecode.append(reg)
                    self.address += 1
                elif mnemonic in ['JMP']:
                    # One operand: address/label
                    addr = self._parse_address(operands[0])
                    if addr is None:
                        # Unresolved label
                        self.unresolved.append((operands[0], self.address, len(self.bytecode)))
                        self.bytecode.append(0)  # Placeholder
                    else:
                        self.bytecode.append(addr)
                    self.address += 1
                else:
                    # Two operands: register, register
                    reg1 = self._parse_register(operands[0])
                    reg2 = self._parse_register(operands[1])
                    self.bytecode.append(reg1)
                    self.bytecode.append(reg2)
                    self.address += 2
    
    def _resolve_references(self):
        """Resolve unresolved label references."""
        for label, addr, pos in self.unresolved:
            if label in self.symbols:
                self.bytecode[pos] = self.symbols[label]
            else:
                raise ValueError(f"Undefined label: {label}")
    
    def _parse_register(self, operand):
       
        operand = operand.upper()
        if operand in self.registers:
            return self.registers[operand]
        else:
            raise ValueError(f"Invalid register: {operand}")
    
    def _parse_value(self, operand):
       
        try:
            if operand.startswith('0x'):
                return int(operand, 16)
            elif operand.startswith('0b'):
                return int(operand, 2)
            else:
                return int(operand)
        except ValueError:
            raise ValueError(f"Invalid value: {operand}")
    
    def _parse_address(self, operand):
        
        # Check if it's a label
        if re.match(r'^[A-Za-z0-9_]+$', operand):
            if operand in self.symbols:
                return self.symbols[operand]
            else:
                return None  # Unresolved label
        else:
            return self._parse_value(operand)
    
    def assemble_file(self, input_file, output_file):
        
        with open(input_file, 'r') as f:
            source = f.read()
        
        bytecode = self.assemble(source)
        
        with open(output_file, 'wb') as f:
            f.write(bytes(bytecode))


def main():
    """Main function to run the assembler."""
    if len(sys.argv) < 3:
        print("Usage: python assembler.py <input_file> <output_file>")
        return
    
    assembler = Assembler()
    
    try:
        assembler.assemble_file(sys.argv[1], sys.argv[2])
        print(f"Assembled {sys.argv[1]} to {sys.argv[2]}")
    except FileNotFoundError:
        print(f"File not found: {sys.argv[1]}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

#范權榮 111210557 27/05/2025
