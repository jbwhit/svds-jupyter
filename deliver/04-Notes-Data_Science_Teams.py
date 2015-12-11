
# coding: utf-8

# # Questions to ask to organize workflow
# 
# this is a real cell that i can evaluate.

# - How many data scientists are working on one problem?
# 

#  - Different data sources and problems? Different git repositories.

#  - Less than 10 data scientists working on the same data but different problems? Same git repository.

#  - More than 10 data scientists working on the same data but different problems? Different git repositories.

#  - Where is the data hosted?
#   - Local laptop?
#    - Consider just doing your own Jupyter Notebook server locally.
#    
#   - Server? 
#    - Can be accessed via SSH? Jupyter server running on server that you SSH tunnel into.
#    - Consider [JupyterHub](https://github.com/jupyter/jupyterhub).
# 

# # How to organize the work into two kinds of Notebooks
# 
#  - Laboratory
#  - Deliverable

# ## Lab Notebooks

#  - Keeps a historical record of the analysis explored

#  - Meant to be a development or scratch place

#  - Each notebook is controlled by a single Data Scientist

# ## Lab Notebooks

#  - Split the notebooks when they get too long (turn the page)

#  - Split the notebooks by topic if it makes sense.

# ## Deliverable Notebooks

#  - Any Notebook that will be referenced in the future.

#  - How raw data was transformed into cleaned data.

#  - The fully polished and final outputs of the analysis.

# ## Deliverable Notebooks

#  - Peer reviewed via pull requests (other members will review before accepted).

#  - These notebooks are controlled by the whole Data Science team.

# ## Get organized -- High level directories

#  - `data` # Backed up outside of version control
#  - `deliver` # Final polished Notebooks for consumption
#  - `develop` # Lab Notebooks stored here
#  - `figures` # 
#  - `src` # Scripts/modules stored here

# # Name the lab-notebooks with the following convention:
#  - **[ISO 8601 date]**-[DS-initials]-[2-4 word description].ipynb
#  - **2015-11-21**-JBW-coal-predict-RF-regression.ipynb

# # Name the lab-notebooks with the following convention:
#  - [ISO 8601 date]-**[DS-initials]**-[2-4 word description].ipynb
#  - 2015-11-21-**JBW**-coal-predict-RF-regression.ipynb

# # Name the lab-notebooks with the following convention:
#  - [ISO 8601 date]-[DS-initials]-**[2-4 word description]**.ipynb
#  - 2015-11-21-JBW-**coal-predict-RF-regression**.ipynb

# ## Version Control
# 
# How do you peer review code and store analysis in version control?
# 
# Further constraints: 
# 
#  - Project manager who wants to see notebooks but doesn't want to install IPython
#  - Not using Github which renders figure diffs nicely
#  - Want to review the Python code itself

# ## My Answer
# 
#  - Each Data Scientist has their own dev branch
#  - Work is saved and pushed on dev branch daily
#  - When ready to merge to master, pull request

# ## What to commit?
# 
#  - .ipynb
#  - .py
#  - .html
#  
# of all Notebooks (develop and deliver).
# 
#  - and [figures](https://github.com/jbwhit/OSCON-2015/commit/6750b962606db27f69162b802b5de4f84ac916d5)
# 

# # Benefits
# 
#  - Record of analysis including dead-ends
#  - Ability to easily peer review analysis and dead-ends
#  - Project managers can easily see and read the analysis with GitHub .ipynb or .html without installing ipython

# # Final organization thoughts
# 
#  - Organization of workflows in teams is difficult
#  - Having some standards is better than none
#  - Sometimes the "wrong thing" exactly solves a problem
#  - Storing output figures
#  - Having rendered .html files in commits
#  - Open to new ideas -- have a better method let me know!

# 
# For static slides: 
# 
#     jupyter nbconvert my_r_notebook.ipynb --to slides --post serve
# 
# For interactive "live" slides:
# 
# https://github.com/damianavila/RISE

# In[ ]:



