import argparse
import cowsay

def main():
    animals = cowsay.char_names
    parser = argparse.ArgumentParser(
        description="Make animals say things!"
    )
    parser.add_argument(
        '--animal', '-a',
        choices=animals,
        default='cow',
        help='The animal to be saying things (default: cow)'
    )
    parser.add_argument('message',nargs='+',help='The message to say')
    args = parser.parse_args()
    text = ' '.join(args.message)

    try:
        output = cowsay.get_output_string(char=args.animal, text=text)
        print(output)
    except cowsay.CowsayError as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == '__main__':
    main()