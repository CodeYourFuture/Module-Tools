import sys
import os

def main():
    argv = sys.argv[1:]
    
    dash = [arg for arg in argv if arg.startswith('-')]
    file_paths = [arg for arg in argv if not arg.startswith('-')]
    
    show_line_numbers = '-n' in dash
    show_non_blank = '-b' in dash
    
    line_counter = 1
    
    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as fs:
                content = fs.read()
        except (FileNotFoundError, IsADirectoryError):
            print(f"cat: {file_path}: No file or directory exists", file=sys.stderr)
            sys.exit(1)
        
        lines = content.split('\n')
        
        if lines and lines[-1] == '':
            lines.pop()
        
        for line in lines:
            is_blank = line.strip() == ''
            
            if show_non_blank:
                if is_blank:
                    print('')
                else:
                    print(f"{str(line_counter).rjust(6)}\t{line}")
                    line_counter += 1
            elif show_line_numbers:
                print(f"{str(line_counter).rjust(6)}\t{line}")
                line_counter += 1
            else:
                print(line)

if __name__ == "__main__":
    main()