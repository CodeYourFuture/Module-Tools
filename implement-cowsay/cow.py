import cowsay
import argparse

# cowsay.cow(" ".join(sys.argv[1:]))

parser = argparse.ArgumentParser(
    prog="custom-cowsay",
    description="A custom cowsay can parse in animal in command line"
)

parser.add_argument("--animal", "Parsing animal name after the flag")
parser.add_argument("message", "Message for the animal to say")

print(cowsay.char_names)