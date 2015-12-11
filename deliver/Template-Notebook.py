
# coding: utf-8

# In[1]:

get_ipython().magic(u'load_ext autoreload')
get_ipython().magic(u'autoreload 2')
get_ipython().magic(u'matplotlib inline')
get_ipython().magic(u"config InlineBackend.figure_format='retina'")

from __future__ import division

from itertools import combinations
import string

from IPython.display import IFrame, HTML, YouTubeVideo
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp
import seaborn as sns; sns.set();

sns.set_style("darkgrid")
sns.set_context("poster", font_scale=1.3)

mpl_update = {'font.size':16,
              'xtick.labelsize':14,
              'ytick.labelsize':14,
              'figure.figsize':[12.0,8.0],
              'axes.color_cycle':['#0055A7', 
                                  '#2C3E4F', 
                                  '#26C5ED', 
                                  '#00cc66', 
                                  '#D34100', 
                                  '#FF9700',
                                  '#091D32',
                                 ], 
              'axes.labelsize':20,
              'axes.labelcolor':'#677385',
              'axes.titlesize':20,
              'lines.color':'#0055A7',
              'lines.linewidth':3,
              'text.color':'#677385'}

plt.rcParams.update(mpl_update)


# In[2]:

rows = 20
df = pd.DataFrame(data=np.random.randint(0, 6, (rows, 10)), 
                  index=[x for x in string.ascii_letters[:rows]])
df['num_missing'] = (df.iloc[:, 0:4] == 0).sum(1)
df['num_bad_ratings'] = (df.iloc[:, 0:4] <= 3).sum(1)
df.head()

# If this path doesn't exist, create it (matches Paul's standards request).
import sys
sys.path.append('../src/main/python/')


# In[3]:

df


# In[ ]:



