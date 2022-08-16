#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# -----------------------------------------
# The entire code is to plot curve!
# -----------------------------------------

from __future__ import print_function
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import cairosvg
import os

# -----------------------------------------
# styles
# -----------------------------------------
params = {
    # color
    'colors': ['#cbe6b6', '#ff8243', '#c043ff', '#82ff43'],
    
    
    'markers': ['v', '*', 'o', '^', '<', '>'], # refer to https://matplotlib.org/stable/api/markers_api.html
    'marker_size': 12,
    
    'bar_width': 0.45,
    
    'error_capsize': 5,
    
    'xaxis_fontsize': 12,
    'xaxis_degree': 0,
    'xaxis_fontweight': 'normal',
    'xlabel_fontsize': 18,
    'xlabel_fontweight': 'bold',
    'xlim_min': 1,
    'xlim_max': 10,

    'yaxis_fontsize': 12,
    'yaxis_degree': 90,
    'yaxis_fontweight': 'normal',
    'ylabel_fontsize': 18,
    'ylabel_fontweight': 'bold',
    'ylim_min': 70,
    'ylim_max': 92,

    'legend_fontsize': 18,
    
    'figure_weight': 8,
    'figure_height': 4,
    
    'grid': True,

    'fill_transparent': 0.5,

    'line_width': 2,
    
    'fig_name': 'fig_test',
    'fig_svg': 'svg',
    'fig_png': 'png',
    'fig_jpeg': 'jpeg',
    'fig_pdf': 'pdf',
    'fig_transparent': False,
}

# -----------------------------------------
# X values and their labels
# -----------------------------------------
X = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
xticks = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10']

# -----------------------------------------
# Y values for method 1
# -----------------------------------------
Y1 = np.array([734.67,755,702.67,637.33,648,656.67,637.33,720.33,744.33,712])
Y1_std = np.array([25.17,14,55.08,44.38,30.05,43.66,49.69,21.36,27.5,56.4])

Y2 = np.array([724.67,745,702.67,737.33,618,656.67,687.33,710.33,714.33,702])
Y2_std = np.array([25.17,14,55.08,44.38,30.05,43.66,49.69,21.36,27.5,56.4])

# -----------------------------------------
# create a figure
# -----------------------------------------
fig, ax = plt.subplots()

# -----------------------------------------
# plot X and Y
# -----------------------------------------
ax.plot(X, Y1, marker=params['markers'][0], color=params['colors'][0], label='Label1', linewidth=2.0, mec='black', markersize=10)
ax.fill_between(X, Y1-Y1_std, Y1+Y1_std, alpha=0.5, color=params['colors'][0])

ax.plot(X, Y2, marker=params['markers'][0], color=params['colors'][1], label='Label2', linewidth=2.0, mec='black', markersize=10)
ax.fill_between(X, Y2-Y2_std, Y2+Y2_std, alpha=0.5, color=params['colors'][1])

# -----------------------------------------
# xlabel
# -----------------------------------------
ax.set_xlabel('parameter', fontsize=params['xlabel_fontsize'], fontweight=params['xlabel_fontweight'])
ax.set_xticks(X)
ax.set_xticklabels(xticks, fontsize=params['xaxis_fontsize'], rotation=params['xaxis_degree'])

# -----------------------------------------
# ylabel
# -----------------------------------------
ax.set_ylabel('metric', fontsize=params['ylabel_fontsize'], fontweight=params['ylabel_fontweight'])
ax.tick_params(axis='y', labelsize=params['yaxis_fontsize'], rotation=params['yaxis_degree'])
ax.legend()

# -----------------------------------------
# styles
# -----------------------------------------
fig.tight_layout()
plt.grid(True)

# -----------------------------------------
# show or save figure
# -----------------------------------------
# plt.show()
plt.savefig(params['fig_name'] + '.' + params['fig_png'], format=params['fig_png'], transparent= params['fig_transparent'])

# note, if you want to get a pdf file, it is recommended to convert svg to pdf
# plt.savefig(params['fig_name'] + '.' + params['fig_svg'], format=params['fig_svg'], transparent= params['fig_transparent'])
# cairosvg.svg2pdf(url=params['fig_name'] + '.' + params['fig_svg'], write_to=params['fig_name'] + '.' + params['fig_pdf'])
# os.remove(params['fig_name'] + '.' + params['fig_svg'])

