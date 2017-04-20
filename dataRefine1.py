import pandas as pd 
from nltk import PorterStemmer
import csv
import sys
from nltk.corpus import stopwords
import math

reload(sys)
sys.setdefaultencoding('utf-8')

data = pd.read_csv('test.csv')

l = []
l.append(['Id','Title','Tags'])

stop = set(stopwords.words('english'))

for i in range(100000):
	s1 = " ".join(PorterStemmer().stem_word(word) for word in data['Title'][i].split(" "))
	s2 = " ".join(word for word in data['Title'][i].lower().split(" ") if word not in stop)
	s2 = s2.translate(None,'?(),""""{}\/')
	if False == math.isnan(data['Id'][i]):
		l.append( [ int(data['Id'][i]) , s2 ] )

tags_id = {}
data = pd.read_csv('Tags.csv')

count=0
for index,rows in data.iterrows():
	count += 1
	if tags_id.has_key(rows['Id']) == False:
		tags_id[rows['Id']] = []
	tags_id[rows['Id']].append(rows['Tag'])
	if count > 100000:
		break

size = len(l)
l1 = []
for i in range(1,100000):
	s = l[i][0]
	if tags_id.has_key(s):
		if type(tags_id[s]) != float:
			l1.append([s, l[i][1], " ".join(tags_id[s])])

with open('test1.csv', 'w') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(l1)