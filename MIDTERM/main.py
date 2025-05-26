#范權榮 111210557 27/05/2025
from vm import SimpleVM

def main():
    """Main function to run the VM."""
    import sys
    import os
    
    if len(sys.argv) < 2:
        print("Usage: python main.py <program_file> [--debug]")
        print("Available example programs:")
        examples_dir = os.path.join(os.path.dirname(__file__), "examples")
        if os.path.exists(examples_dir):
            for file in os.listdir(examples_dir):
                if file.endswith(".asm"):
                    print(f"  - {file}")
        return
    
    vm = SimpleVM()
    
    try:
        program_file = sys.argv[1]
        
        if program_file.endswith(".asm"):
            from assembler import Assembler
            
            assembler = Assembler()
            binary_file = program_file.replace(".asm", ".bin")
            
            print(f"Assembling {program_file} to {binary_file}...")
            assembler.assemble_file(program_file, binary_file)
            
            program_file = binary_file
        
        print(f"Loading program from {program_file}...")
        vm.load_program_from_file(program_file)
        
        debug = "--debug" in sys.argv
        print(f"Running program{' in debug mode' if debug else ''}...")
        vm.run(debug=debug)
        
        print("Program execution completed.")
    except FileNotFoundError:
        print(f"File not found: {sys.argv[1]}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

#范權榮 111210557 27/05/2025