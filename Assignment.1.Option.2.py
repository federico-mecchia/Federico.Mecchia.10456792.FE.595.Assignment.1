"""
Assignment 1
"""

"""
For "Assignment 1" I have come up with two possible
solutions, identified by "Option 1" and "Option 2".
"Option 1" can be found in the file in ".py format"
named "Assignment.1.Option.1" and "Option.2" can be
found in the file in ".py format" named
"Assignment.1.Option.2".
"""

"""
Option 2
"""


import numpy as np
import matplotlib.pyplot as plt


def sincos_option2():

    xop2 = np.arange(0, 2 * np.pi, step=0.001)
    y1op2 = np.sin(xop2)
    y2op2 = np.cos(xop2)

    plt.plot(xop2, y1op2, "red", label="Sine Function")
    plt.plot(xop2, y2op2, "blue", label="Cosine Function")
    plt.grid("True")
    plt.title("Graph of One Period of Sine and Cosine functions", fontsize=15)
    plt.xlabel("x")
    plt.ylabel("sin(x) and cos(x)")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    sincos_option2()


"""

Comment

The comment regarding "Option 2" can be found in the file in ".py format"
named "Assignment.1.Option.1". The main difference between the code of
the file named "Assignment.1.Option.1" and the code of the file named
"Assignment.1.Option.2" is the fact that in "Option 1" I create "xop1"
by using "np.linspace()", while in "Option 2" I use "np.arange()" to
create "xop2".
As I did for the code of "Option 1", lastly I type "black" in the
terminal followed by the path of the file in ".py format" in order to
format the whole code contained in the file taken into consideration
(basically the code of the file you are reading and so the code of the
file in ".py format" named "Assignment.1.Option.2").

"""
