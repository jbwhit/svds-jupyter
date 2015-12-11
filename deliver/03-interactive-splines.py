
# coding: utf-8

# In[1]:

get_ipython().magic(u'matplotlib inline')

from matplotlib.collections import LineCollection
import matplotlib.pyplot as plt
from scipy import interpolate
import numpy as np
from numpy.random import rand

from ipywidgets import FloatSlider, interactive, IntSlider


# In[2]:

def spline_demo(num=14, smooth=0, seed=10, brush_strokes=30, alpha=0.5):
    a = np.random.RandomState(seed=seed)
    x = a.rand(num)
    y = a.rand(num)
    t = np.arange(0, 1.1, .1)
    plt.rcParams['figure.figsize'] = 8,8
    plt.figure()
    for _ in xrange(brush_strokes):
        tck, u = interpolate.splprep([x+a.rand(num)/10.0,y+a.rand(num)/10.0], s=smooth)
        unew = np.arange(0, 1.01, 0.001)
        out = interpolate.splev(unew, tck)
        plt.plot(out[0], out[1], alpha=alpha, c='black', linewidth=3.0)
    plt.xlim(-1.5, 2.5)
    plt.ylim(-1.5, 2.5)
    plt.axis('off')

smooth_slider = FloatSlider(value=0, min=0, max=20.0, step=.1)
num_points_slider = IntSlider(value=8, min=4, max=20)
seed_slider = IntSlider(value=4, min=4, max=20)
brush_slider = IntSlider(value=1, min=1, max=20)
alpha_slider = FloatSlider(value=.5, min=0, max=1.0, step=.05)

w=interactive(spline_demo,
              smooth=smooth_slider, 
              num=num_points_slider, 
              seed=seed_slider, 
              brush_strokes=brush_slider,
              alpha=alpha_slider)
w


# In[ ]:



