import six

from pyfiglet import figlet_format

try:
    from termcolor import colored
except ImportError:
    colored = None

def log(string, color, font="slant", figlet=False):
    if colored:
        if not figlet:
            six.print_(colored(string, color))
        else:
            six.print_(colored(figlet_format(
                string, font=font), color))
    else:
        six.print_(string)

def main():
    """
    Simple CLI for a NUmber Guessing Game (NGG CLI).
    """
    log("NGG CLI", color="green", figlet=True)
    log("Welcome to NGG CLI!", "yellow")



if __name__ == '__main__':
    main()