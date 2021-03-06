#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import numpy as np
from ph_plotter.points_sf_plotter import PointsSFPlotter


__author__ = "Yuji Ikeda"


class PointsSFE1Plotter(PointsSFPlotter):
    def plot_q(self, ax, iq):
        selected_irreps = self._variables['selected_irreps']
        if selected_irreps is None:
            lines_total = self.plot_total_q(ax, iq)
            lines_symbols = self.plot_element_pairs_q(ax, iq)
        else:
            lines_total = self.plot_q_selected_irreps_total(ax, iq, selected_irreps)
            lines_symbols = self.plot_q_selected_irreps(ax, iq, selected_irreps)
        return lines_total, lines_symbols

    def plot_element_pairs_q(self, ax, iq):

        elements = self._data_points[iq]['elements']

        partial_sf = self._data_points[iq]['partial_sf_e']
        sf_element_pair = np.sum(partial_sf, axis=(1, 3))

        for i1, e1 in enumerate(elements):
            for i2, e2 in enumerate(elements):
                if i2 < i1:
                    continue
                label='{}–{}'.format(e1, e2)

                if i1 == i2:
                    sf = sf_element_pair[:, i1, i2]
                else:
                    sf = sf_element_pair[:, i1, i2] + sf_element_pair[:, i2, i1]
                sf = sf.real

                self._plot_curve(ax, iq, sf, label=label)

        return

    def plot_q_selected_irreps_total(self, ax, iq, irs_selected):

        variables = self._variables

        data_point = self._data_points[iq]

        pg_symbol = str(data_point['pointgroup_symbol'])
        ir_labels = data_point['ir_labels']

        if pg_symbol not in irs_selected:
            return None

        tmp = data_point['total_sf']
        sf = np.zeros_like(tmp)  # Initialization

        for ir_label_selected in irs_selected[pg_symbol]:
            indices = np.where(ir_labels == ir_label_selected)
            for index in indices:
                sf += data_point['partial_sf_s'][:, index[0]]

        if self._is_horizontal:
            xs = self._frequencies[iq] * variables["unit"]
            ys = sf
        else:
            xs = sf
            ys = self._frequencies[iq] * variables["unit"]

        lines_total = ax.plot(
            xs,
            ys,
            color=variables["linecolor"],
            dashes=variables["dashes"],
            linewidth=variables["linewidth"],
            label="Total",
        )

        return lines_total

    def plot_q_selected_irreps(self, ax, iq, irs_selected):

        elements = self._data_points[iq]['elements']

        data_point = self._data_points[iq]

        pg_symbol = str(data_point['pointgroup_symbol'])
        ir_labels = data_point['ir_labels']

        if pg_symbol not in irs_selected:
            return None

        tmp = data_point['partial_sf_e']
        partial_sf = np.zeros_like(tmp)  # Initialization

        for ir_label_selected in irs_selected[pg_symbol]:
            indices = np.where(ir_labels == ir_label_selected)
            for index in indices:
                partial_sf += data_point['partial_sf_s_e'][:, index[0]]

        for i1, e1 in enumerate(elements):
            for i2, e2 in enumerate(elements):
                if i2 < i1:
                    continue
                label='{}–{}'.format(e1, e2)
                sf_element_pair = np.sum(partial_sf, axis=(1, 3))

                if i1 == i2:
                    sf = sf_element_pair[:, i1, i2]
                else:
                    sf = sf_element_pair[:, i1, i2] + sf_element_pair[:, i2, i1]
                sf = sf.real

                self._plot_curve(ax, iq, sf, label=label)

        return

    def create_figure_name(self):
        variables = self._variables
        figure_name = "points_sf_e1_{}.{}".format(
            variables["freq_unit"],
            variables["figure_type"])
        return figure_name
