#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from bokeh.plotting import figure, show

# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]
y2 = y[:]
random.shuffle(y2)

p = figure(title="Simple line example", x_axis_label='x', y_axis_label='y')
p.vbar(x=x, top=y, legend_label="Temp.", width=0.2, color="coral")
p.vbar(x=x, top=y2, legend_label="Y^2", width=0.4, color="firebrick")
show(p)
