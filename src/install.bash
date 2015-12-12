# Written by Colin Higgins.
# Updated to run as a script by Jonathan Whitmore.
# Ping me if you have questions or issues, but I might not be able to diagnose much since this worked perfectly for me.

# 1. download miniconda python 2.7 mac 64-bit bash installer
# go to http://conda.pydata.org/miniconda.html
# ~direct link

# step1
wget https://repo.continuum.io/miniconda/Miniconda-latest-MacOSX-x86_64.sh

# 2. Navigate to Downloads folder
# $ cd Downloads

# 3. Make the installer executable
# $

# step2
chmod +x Miniconda-latest-MacOSX-x86_64.sh

# 4. Run the installer
# $

# step3 -- have to type spacebar and "yes"
./Miniconda-latest-MacOSX-x86_64.sh

# ~press enter to continue when prompted
# ~hold spacebar to scroll through license agreement quickly
# ~type yes when prompted
# ~press enter when prompted
# ~type yes when prompted (or press enter)

# 5. Change back to home directory
# $ cd ~
# $ source .bash_profile

# step4
source ~/.bashrc

# ~You should now be able to type "conda info" and see that conda is installed.
# ~My output for this was:
# $ conda info
# Current conda install:

#              platform : osx-64
#         conda version : 3.18.8
#   conda-build version : not installed
#        python version : 2.7.11.final.0
#      requests version : 2.8.1
#      root environment : /Users/testuser/miniconda2  (writable)
#   default environment : /Users/testuser/miniconda2
#      envs directories : /Users/testuser/miniconda2/envs
#         package cache : /Users/testuser/miniconda2/pkgs
#          channel URLs : https://repo.continuum.io/pkgs/free/osx-64/
#                         https://repo.continuum.io/pkgs/free/noarch/
#                         https://repo.continuum.io/pkgs/pro/osx-64/
#                         https://repo.continuum.io/pkgs/pro/noarch/
#           config file : None
#     is foreign system : False

# 6. Update conda
# $

# step5
conda update conda -y

# ~you can see a list of your environments (currently only root since we haven’t installed any others yet)
# $ conda info -e
# # conda environments:
# #
# root                  *  /Users/testuser/miniconda2

# ~you can check what you have installed under your root environment with:
# colin-svds:~ testuser$ conda list
# # packages in environment at /Users/testuser/miniconda2:
# #
# conda                     3.18.9                   py27_0
# conda-env                 2.4.5                    py27_0
# openssl                   1.0.2d                        0
# pip                       7.1.2                    py27_0
# pycosat                   0.6.1                    py27_0
# pycrypto                  2.6.1                    py27_0
# python                    2.7.11                        0
# pyyaml                    3.11                     py27_1
# readline                  6.2                           2
# requests                  2.8.1                    py27_0
# setuptools                18.5                     py27_0
# sqlite                    3.8.4.1                       1
# tk                        8.5.18                        0
# wheel                     0.26.0                   py27_1
# yaml                      0.1.6                         0
# zlib                      1.2.8                         0


# 7. Create an environment and install R and anaconda
# $

# step6
conda create -y -n anaconda_r -c r r-irkernel r-recommended r-essentials anaconda

# ~lots of things should download. This may take 5-10 minutes
# ~at the end, you should see this message:
# Extracting packages ...
# [      COMPLETE      ]|###################################################| 100%
# Linking packages ...
# [      COMPLETE      ]|###################################################| 100%
# #
# # To activate this environment, use:
# # $ source activate anaconda_r
# #
# # To deactivate this environment, use:
# # $ source deactivate
# #


# 8. Look at the list of your environments again
# $ conda info -e
# # conda environments:
# #
# anaconda_r               /Users/testuser/miniconda2/envs/anaconda_r
# root                  *  /Users/testuser/miniconda2

# 9. Activate your new environment
# $ source activate anaconda_r
# discarding /Users/testuser/miniconda2/bin from PATH
# prepending /Users/testuser/miniconda2/envs/anaconda_r/bin to PATH

# 10. Install ryp2
# $

# step7
conda install -c r rpy2 -y

# ~type ‘y’ to proceed when prompted

# 11. Try it out!
# $ jupyter notebook
# ~you should see both “Python 2” and “R” under the “New” button on the upper right
# ~download the testing_rpy2.ipynb file in this directory to test rpy2 for yourself
