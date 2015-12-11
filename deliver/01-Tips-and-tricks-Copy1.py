
# coding: utf-8

# # Best practices
# 
# Let's start with pep8 (https://www.python.org/dev/peps/pep-0008/)
# 
# > Imports should be grouped in the following order:
# 
# > - standard library imports
# > - related third party imports
# > - local application/library specific imports
# 
# > You should put a blank line between each group of imports.
# Put any relevant __all__ specification after the imports.
# 
# 

# In[2]:

# Best practice for loading libraries?
# Couldn't find what to do with 'magic' imports at the top

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

plt.rcParams['figure.figsize'] = (12, 8)
sns.set_style("darkgrid")
sns.set_context("poster", font_scale=1.3)


# # Pivot Tables w/ pandas
# 
# http://nicolas.kruchten.com/content/2015/09/jupyter_pivottablejs/

# In[3]:

YouTubeVideo("ZbrRrXiWBKc", width=800, height=600)


# In[4]:

get_ipython().system(u'pip install pivottablejs')


# In[5]:

df = pd.read_csv("../data/mps.csv")


# In[6]:

df.head()


# In[7]:

from pivottablejs import pivot_ui
pivot_ui(df)
# Province, Party, Average, Age, Heatmap


# # Keyboard shortcuts

# In[8]:

# in select mode, shift j/k (to select multiple cells at once)
# split cell with ctrl shift -


# In[9]:

first = 1

second = 2

third = 3


# # Floating Table of Contents
# 
# Creates a new button on the `toolbar` that pops up a table of contents that you can navigate by.

# In your documentation if you indent by 4 spaces, you get monospaced code-style code so you can embed in a Markdown cell:
# 
# 
#     $ mkdir toc
#     $ cd toc
# 
#     $ wget https://raw.githubusercontent.com/minrk/ipython_extensions/master/nbextensions/toc.js
# 
#     $ wget https://raw.githubusercontent.com/minrk/ipython_extensions/master/nbextensions/toc.css
#     $ cd ..
# 
#     $ jupyter-nbextension install --user toc
# 
#     $ jupyter-nbextension enable toc/toc

# You can also get syntax highlighting if you tell it the language that you're including: 
# 
# ```bash
# mkdir toc
# cd toc
# 
# wget https://raw.githubusercontent.com/minrk/ipython_extensions/master/nbextensions/toc.js
# 
# wget https://raw.githubusercontent.com/minrk/ipython_extensions/master/nbextensions/toc.css
# cd ..
# 
# jupyter-nbextension install --user toc
# jupyter-nbextension enable toc/toc
# ```

# # R
# 
#  - [pyRserve](https://pypi.python.org/pypi/pyRserve)
#  - [rpy2](http://rpy.sourceforge.net/)

# In[10]:

import rpy2


# In[11]:

get_ipython().magic(u'load_ext rpy2.ipython')


# In[12]:

X = np.array([0,1,2,3,4])
Y = np.array([3,5,4,6,7])


# In[13]:

get_ipython().run_cell_magic(u'R', u'-i X,Y -o XYcoef', u'XYlm = lm(Y~X)\nXYcoef = coef(XYlm)\nprint(summary(XYlm))\npar(mfrow=c(2,2))\nplot(XYlm)')


# # Tech_Vault additions

# ## Miniconda + conda environments
# 
# Probably the best way to go -- there should be an updated document in tech_vault that describes the way to setup py2, and py3 environments.

# ## SVDS Template 
# 
#  - color/seaborn template
#  - standards of organization (imports all at the top)

# # R&D Project: Projects that would be great to support
# 
#  - http://nbdiff.org/
#  - statsmodels

# In[ ]:



