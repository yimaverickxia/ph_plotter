#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from .dos_plotter import DOSPlotter


__author__ = "Yuji Ikeda"


class PartialDOSPlotter(DOSPlotter):
    def load_data(self, data_file='partial_dos.dat'):
        super(PartialDOSPlotter, self).load_data(data_file)
        return self

    def run(self):

        variables = self._variables

        primitive = self.create_primitive()
        natoms = primitive.get_number_of_atoms()
        symbols = primitive.get_chemical_symbols()
        print("natoms:", natoms)
        print("symbols:", symbols)

        self.set_figure_name_prefix("partial_dos")
        self.set_plot_symbol(True)
        self.set_plot_atom(False)
        self.load_data(variables["data_file"])

        variables.update({
            "freq_unit": "THz",
            "unit": 1.0,
            "natoms": natoms,
            "symbols": symbols,
        })
        self.update_variables(variables)
        # self.set_is_horizontal(True)
        # self.plot_dos()
        self.set_is_horizontal(False)
        self.create_figure()

        return

        from scipy.constants import eV, Planck
        THz2meV = Planck / eV * 1e+15  # 4.135667662340164

        # meV
        variables.update({
            "freq_unit": "meV",
            "unit": THz2meV,
        })
        scale = 4.0
        variables["f_min"]  *= scale
        variables["f_max"]  *= scale
        variables["d_freq"] *= scale
        variables["dos_min"]   /= scale
        variables["dos_max"]   /= scale
        variables["dos_ticks"] /= scale
        self.update_variables(variables)
        # self.set_is_horizontal(True)
        # self.plot_dos()
        self.set_is_horizontal(False)
        self.create_figure()
