"""
hpka.py
A hybrid qm and mm method for pKa prediction

Handles the primary functions
"""


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


def usage():
  print("3 stages of work : \n 1. QM level \n 2. Parameterization \n 3. Solvation free energy difference")

def main():
  usage()

if __name__ == "__main__":
  # Do something if this file is invoked on its own
  #print(canvas())
  main()
