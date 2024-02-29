"""Argument parser example.
Call with 'python parser.py -h' to print help."""
import argparse


parser = argparse.ArgumentParser(description="Calculate the area of a square")
parser.add_argument("a")
parser.add_argument("b")

args = parser.parse_args()
print(args.a, args.b)
