import argparse
import cowsay #to do the ascii art with animals

def main():
    #getlistof animals within cowsay
    animals = cowsay.char_names
    #create a parser for command line argument
    parser = argparse.ArgumentParser(
        description="Make animals say things!"
    )
    parser.add_argument(
        '--animal', '-a',
        choices=animals,
        default='cow',
        help='The animal to be saying things (default: cow)'
    )
    #argument for the message
    parser.add_argument('message',nargs='+',help='The message to say')
    #to parse the arguments from the command line
    args = parser.parse_args()
    #the messageword into a single string
    text = ' '.join(args.message)

    try:
        output = cowsay.get_output_string(char=args.animal, text=text)
        print(output)
    except cowsay.CowsayError as e:
        print(f"Error: {e}")
        exit(1)
#run main function only if this script is run directly
if __name__ == '__main__':
    main()