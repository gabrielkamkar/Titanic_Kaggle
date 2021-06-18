
# This is the initial sratch work page for the Kaggle Titanic project.
# I want to look at and analyse the data
# as well as look at previous people's code.

# I'm gonna have to import pandas and all the other shit  I need to
# manipulate datasets and run regressions and
# whatnot.

# -----------------------------------------------------------------------------------------

import os

os.getcwd()
os.chdir('C:\\Users\\kamka\\Documents\\titanic')
os.getcwd()

import pandas as pd

gender = pd.read_csv('gender_submission.csv')
test = pd.read_csv('test.csv')
train = pd.read_csv('train.csv')

# I can view the data as a dataframe
# lets look at the website again to see exactly what I have in each set

# gender_submission is an example of what a submission will look like
# except this one only assumes that females survive

# test and train data are exactly what they seem like
# Parameters:

# ----------------------------------------------------------------------------------

# Variable	Definition	         Key
# survival	Survival	         0 = No, 1 = Yes
# pclass	Ticket class	     1 = 1st, 2 = 2nd, 3 = 3rd
# sex	    Sex
# Age	    Age in years
# sibsp	    # of siblings / spouses aboard the Titanic
# parch	    # of parents / children aboard the Titanic
# ticket	Ticket number
# fare	    Passenger fare
# cabin	    Cabin number
# embarked	Port of Embarkation	  C = Cherbourg, Q = Queenstown, S = Southampton

# pclass: A proxy for socio-economic status (SES)
# 1st = Upper
# 2nd = Middle
# 3rd = Lower

# age: Age is fractional if less than 1. If the age is estimated,
# is it in the form of xx.5

# sibsp: The dataset defines family relations in this way...
# Sibling = brother, sister, stepbrother, stepsister
# Spouse = husband, wife (mistresses and fiancés were ignored)

# parch: The dataset defines family relations in this way...
# Parent = mother, father
# Child = daughter, son, stepdaughter, stepson
# Some children travelled only with a nanny, therefore parch=0 for them.

# ---------------------------------------------------------------------------------

# Now I don't really know what to do? I think I should start off
# with some data visualization to get
# a better understanding of the training data


import ggplot


ggplot()