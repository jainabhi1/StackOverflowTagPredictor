import pandas as pd 
from nltk import PorterStemmer
import csv
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

data = pd.read_csv('/home/abhi/Desktop/Questions.csv')

l = []
l.append(['Id','Title'])
count = 0
for index,rows in data.iterrows():
	" ".join(PorterStemmer().stem_word(word) for word in rows['Title'].split(" "))
	l.append( [ rows['Id'] , rows['Title'] ] )
	count += 1
	if(count > 100000):
		break



with open('test.csv', 'w') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(l)
