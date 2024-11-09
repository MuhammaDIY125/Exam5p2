import pandas as pd
from myFE import update_df

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
sub = pd.read_csv('sample_submission.csv')

train = update_df(train)
test = update_df(test)

X = train.drop(columns=['yield'])
y = train['yield']