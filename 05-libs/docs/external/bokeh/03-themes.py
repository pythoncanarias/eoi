#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as np

from bokeh.plotting import figure, show
from bokeh.io import curdoc

curdoc().theme = "dark_minimal"

x = np.array([1, 2, 3, 4, 5])
y = np.array([6, 7, 2, 4, 5])
y2 = np.array([7, 10, 6, 5, 6])
p = figure(title="Simple line example", x_axis_label='x', y_axis_label='y')
p.vbar(x=x, top=y, legend_label="Temp.", width=0.4, color="coral")
p.vbar(x=x, top=y2, legend_label="Y^2", width=0.2, color="firebrick")
show(p)
