# Qubic


3D Tic-Tac-Toe game using Pygame.

## Installing Requirements
### Python3/pip3

This software requires _PyGame_.
To install (requires [python3](https://www.python.org/downloads/)):

The pip3 python package manager should be automatically available after Python3
is installed. To install it, if required:

Ubuntu, Debian, and other Linux distros that use _apt_:

```
sudo apt update
sudo apt install python3-pip
```

In Arch Linux/Manjaro Linux distros, using _pacman_:

```
pacman -S python-pip
```

To verify pip3 installation:

```
pip3 --version
```

### Installation of game dependencies

This version of Qubic uses _PyGame_ as its engine, and the repositories' automated tests
make use of the _PyTest_ library;

To install all of the repositories' dependencies on your system:

```
pip3 install -r requirements.txt
```
### Verify correct installation of the dependencies

To verify PyGame's correct installation:

```
python3 -m pygame.examples.aliens
```

And to verify PyTest's correct installation:
```
pytest -v
```


### Running the game


Clone the repository to your preferred location by using the command:

```
git clone https://github.com/cmpsvictor/qubic/
cd qubic
```
And run the game with

```
python3 main.py
```

In the event that you wish to make your own changes to this code, you can run its automated tests with:

```
pytest --verbose testes.py
``` 

### How to play

To achieve victory, a player has to manage to insert four consecutive pieces in a straight sequence - be it
on a single surface or on all four. Notice that you'll also need to defend yourself from all of those possibilities,
as your opponent'll have the same offensive opportunities laid out before him.

Write your desired spot to place a piece on the screen, with 1 being the first square on the upper surface and 64 being
the final square on the last surface. The game will return an error message if you attempt an illegal spot, but will still
allow you to play normally.

For more information, refer to the game's [Wikipedia page](https://en.wikipedia.org/wiki/3D_tic-tac-toe).


### Credits

Originally written as a project for the _Técnicas de Programação I_ freshman course in Computer Science class.

Authors:

* João Renner Rudge
* Lucas Medeiros Cornetta
* Victor Aristóteles Rocha Campos

