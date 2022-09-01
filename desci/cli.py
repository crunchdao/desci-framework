import click
import matplotlib.pyplot as plt
import numpy as np


@click.group(
    context_settings={"help_option_names": ["-h", "--help"]},
)
def cli():
    """Management CLI for desci"""


@cli.command(name="helloworld")
def helloworld():
    """Hello World."""
    print("Hello World!")
    print("This line was produced during the video presentation.")


@cli.command(name="helloplot")
def helloplot():
    """Hello Plot."""
    # evenly sampled time at 200ms intervals
    t = np.arange(0.0, 5.0, 0.2)

    # red dashes, blue squares and green triangles
    plt.plot(t, t, "r--", t, t**2, "bs", t, t**3, "g^")
    plt.savefig("paper/figures/helloplot.png")
