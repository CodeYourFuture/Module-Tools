import cowsay
import sys


args = sys.argv[1:]

cowsay.cow(' '.join(args))