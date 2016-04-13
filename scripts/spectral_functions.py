#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

__author__ = "Yuji Ikeda"


def run(variables):
    from ph_plotter.spectral_functions_plotter import SpectralFunctionsPlotter
    SpectralFunctionsPlotter(variables).run()


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--f_max",
                        default=10.0,
                        type=float,
                        help="Maximum plotted frequency (THz).")
    parser.add_argument("--f_min",
                        default=-2.5,
                        type=float,
                        help="Minimum plotted frequency (THz).")
    parser.add_argument("--d_freq",
                        default=2.5,
                        type=float,
                        help="Pitch for frequency (THz).")
    parser.add_argument("--linecolor",
                        default="#ff0000",
                        type=str,
                        help="Linecolor.")
    parser.add_argument("-a", "--alpha",
                        default=0.2,
                        type=float,
                        help="Alpha for the color of low-frequency weights.")
    parser.add_argument("--sf_max",
                        type=float,
                        help="Maximum of spectral functions.")
    parser.add_argument("--sf_min",
                        type=float,
                        help="Minimum of spectral functions.")
    parser.add_argument("--d_sf",
                        type=float,
                        help="Ticks of spectral functions.")
    parser.add_argument("-t", "--figure_type",
                        default="pdf",
                        type=str,
                        help="Filetype of figures.")
    parser.add_argument("--figsize",
                        nargs=2,
                        default=(5.0, 3.5),
                        type=float,
                        help="Filesize of figures.")
    parser.add_argument("--poscar",
                        default="POSCAR",
                        type=str,
                        help="Filename of POSCAR.")
    parser.add_argument("--data_file",
                        default="band.hdf5",
                        type=str,
                        help="Filename of data.")
    args = parser.parse_args()

    print(vars(args))
    run(vars(args))


if __name__ == "__main__":
    main()