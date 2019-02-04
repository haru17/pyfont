# Author: José Almir

colors = {
    "no_color": "0m",
    "black": "30m",
    "red": "31m",
    "green": "32m",
    "yellow": "33m",
    "blue": "34m",
    "magenta": "35m",
    "cyano": "36m",
    "white": "37m"
}

backgrounds = {
    "no_bg": "0",
    "black": "40",
    "red": "41",
    "green": "42",
    "yellow": "43",
    "blue": "44",
    "magenta": "45",
    "cyano": "46",
    "white": "47"
}

styles = {
    "original": "0",
    "bold": "1",
    "reversed": "2"
}


def colorize(string, color="white", background="no_bg", style="original"):
    print("\033[{};{};{}{}\033[0;0m".format(backgrounds[
          background], styles[style], colors[color], string))


if __name__ == '__main__':
    exit()
