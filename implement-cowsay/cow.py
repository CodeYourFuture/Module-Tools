import cowsay
import sys
# Join all arguments after the script name into one string
message = " ".join(sys.argv[1:]) or "MOO MOOO"
cowsay.cow(message)
