# This is a sample Python script.

import argparse

parser = argparse.ArgumentParser(description="Lowercase")

parser.add_argument('-insert', metavar ='path', type = str, default ='No path' , help ="A text to convert into lowercase")
parser.add_argument('-out', type=str.lower, help="output of the text")

args = parser.parse_args()
print(args)
