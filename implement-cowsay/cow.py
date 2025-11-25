import cowsay
import sys
args=sys.argv[1:]
print(sys.argv)
flags=list(filter(lambda arg : arg.startswith("-"),args))
print(flags)
if len(flags)==0 : 
    cowsay.cow(" ".join(sys.argv[1:]))
elif "--help" in flags or "--h" in flags :
    print("help!!!!!!!!!!!!!!!!")
elif "--animal" in flags :
    animalName=args[args.index("--animal")+1]
    print(animalName)
    message=" ".join(args[args.index("--animal")+2:])
    print(message)

