import cowsay
import sys
import argparse

parser=argparse.ArgumentParser(prog="cowsay",
                               description="Make animals say things.")
parser.add_argument("message",help="The message to say.")
valid_animals=cowsay.char_names;
parser.add_argument("--animal",
                    choices=valid_animals,
                    help=" The animal to be saying things.")

args=parser.parse_args();
# args=sys.argv[1:]
# print(sys.argv)
# flags=list(filter(lambda arg : arg.startswith("-"),args))
# print(flags)
# validAnimals=cowsay.char_names;
# print(validAnimals)

# if len(flags)==0 : 
#     cowsay.cow(" ".join(sys.argv[1:]))
# elif "--help" in flags or "--h" in flags :
#     print("help!!!!!!!!!!!!!!!!")
# elif "--animal" in flags :
#     animalName=args[args.index("--animal")+1]
#     print(animalName)
#     message=" ".join(args[args.index("--animal")+2:])
#     print(message)
#     if hasattr(cowsay,animalName) :
#         getattr(cowsay,animalName)(message)
       