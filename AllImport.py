from tweepy import Cursor
from tweepy import OAuthHandler
from tweepy import API
import pandas as pd
import twitter_credentials
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

# importing algorithms from our modules
import LinearRegression
import MultinomialNaiveBayes
import MultinomialLogisitcRegression
import BinaryLogisticRegression
import DecisionTreeClassifier
import LinearSupportVectorClassifier
import RandomForestClassifier
import ExtraTreeClassifier
import LinearClassifier

# importing pre process from our module to pre-process the raw tweet text into useful information
import PreProcess
pp = PreProcess

# created Algorithms Object of our imported algorithms
mnb = MultinomialNaiveBayes
mlr = MultinomialLogisitcRegression
blr = BinaryLogisticRegression
lr = LinearRegression
lsvc = LinearSupportVectorClassifier
dtc = DecisionTreeClassifier
rfc = RandomForestClassifier
etc = ExtraTreeClassifier
lc = LinearClassifier
