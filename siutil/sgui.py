#!/usr/bin/env python3
"""A very small tool to load one or several geometries using sisl and then show them using ase gui.
"""
import sisl as si
from ase.visualize import view
import argparse as ap


def main():
    p = ap.ArgumentParser(help=__doc__)
    a = p.add_argument
    a("files", nargs="+")
    args = p.parse_args()
    for file in args.files:
        view(si.get_sile(file).read_geometry().toASE())


if __name__ == "__main__":
    main()
