
import sys

args = sys.argv[1:]

with open(args[0], 'r') as f: 
    content = f.read()
print(content)