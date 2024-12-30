# Implement cowsay

Your task is to write a command line tool which uses the `cowsay` library to show user-supplied text, as said by a specified animal.

You must use the cowsay library, and you must not write down the list of supported animals yourself - you must fetch this information from the library.

The following command lines should work as demonstrated below:

```console
% python3 cow.py Grass, delicious.
  _________________
| Grass, delicious. |
  =================
                 \
                  \
                    ^__^
                    (oo)\_______
                    (__)\       )\/\
                        ||----w |
                        ||     ||
% python3 cow.py --animal turtle Fish are cool!
  ______________
| Fish are cool! |
  ==============
                \
                 \
                  \
                   \
                                              ___-------___
                                          _-~~             ~~-_
                                       _-~                    /~-_
                     /^\__/^\         /~  \                   /    \
                   /|  O|| O|        /      \_______________/        \
                  | |___||__|      /       /                \          \
                  |          \    /      /                    \          \
                  |   (_______) /______/                        \_________ \
                  |         / /         \                      /            \
                   \         \^\\         \                  /               \     /
                     \         ||           \______________/      _-_       //\__//
                       \       ||------_-~~-_ ------------- \ --/~   ~\    || __/
                         ~-----||====/~     |==================|       |/~~~~~
                          (_(__/  ./     /                    \_\      \.
                                 (_(___/                         \_____)_)
% python3 cow.py --animal fish Turtles are cool too!
usage: cowsay [-h] [--animal {beavis,cheese,cow,daemon,dragon,fox,ghostbusters,kitty,meow,miki,milk,octopus,pig,stegosaurus,stimpy,trex,turkey,turtle,tux}] message [message ...]
cowsay: error: argument --animal: invalid choice: 'fish' (choose from 'beavis', 'cheese', 'cow', 'daemon', 'dragon', 'fox', 'ghostbusters', 'kitty', 'meow', 'miki', 'milk', 'octopus', 'pig', 'stegosaurus', 'stimpy', 'trex', 'turkey', 'turtle', 'tux')
% python3 cow.py --help
usage: cowsay [-h] [--animal {beavis,cheese,cow,daemon,dragon,fox,ghostbusters,kitty,meow,miki,milk,octopus,pig,stegosaurus,stimpy,trex,turkey,turtle,tux}] message [message ...]

Make animals say things

positional arguments:
  message               The message to say.

options:
  -h, --help            show this help message and exit
  --animal {beavis,cheese,cow,daemon,dragon,fox,ghostbusters,kitty,meow,miki,milk,octopus,pig,stegosaurus,stimpy,trex,turkey,turtle,tux}
                        The animal to be saying things.
```
