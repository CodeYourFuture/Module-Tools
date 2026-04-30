import cowsay
import sys


def main():
    animal = ""
    args = sys.argv[1:]
    if len(args) == 0:
        print("error: no arguments provided.")
        return
    if args[0] == "--animal" and len(args) > 1:
        animal = args[1]
    elif args[0] != "--animal":
        animal = "cow"
    message = ""
    for i in range(2,len(args)):
        message += args[i]
    
    try:
        getattr(cowsay, animal)(message)
    except Exception as e:
        if animal == "":
            print("error: argument --animal: invalid choice: empty string, choose from 'beavis', 'cheese', 'cow', 'daemon', 'dragon', 'fox', 'ghostbusters', 'kitty', 'meow', 'miki', 'milk', 'octopus', 'pig', 'stegosaurus', 'stimpy', 'trex', 'turkey', 'turtle', 'tux'")
        else:
            print("error: argument --animal: invalid choice: " + animal + ", choose from 'beavis', 'cheese', 'cow', 'daemon', 'dragon', 'fox', 'ghostbusters', 'kitty', 'meow', 'miki', 'milk', 'octopus', 'pig', 'stegosaurus', 'stimpy', 'trex', 'turkey', 'turtle', 'tux'")

if __name__ == "__main__":
    main()
