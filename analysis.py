import csv
from os import path
from textblob import TextBlob
import statistics
import matplotlib.pyplot as plt

filename = ['hindu_5_Aug.csv','ht_5_Aug.csv','dh_5_Aug.csv','toi_5_Aug.csv','tribune_5_Aug.csv']
pol = []
sub = []
for x in filename:
	l =[]
	s =[]
	d = path.dirname(__file__)
	with open(x,'r') as f:
		reader= csv.reader(f)
		for row in reader:
		    #print(row[1])
		    s.append(row[0])
		    l.append(row[1])

	t1=[]
	t2 = []
	for text in l:
		#print(text)
		analysis = 	TextBlob(text)
		#print(analysis.sentiment)
		a=analysis.sentiment.polarity
		b=analysis.sentiment.subjectivity
		print(analysis.sentiment)
		t1.append(a)
		t2.append(b)
	pol.append(statistics.mean(t1))
	sub.append(statistics.mean(t2))
	print(x+' pol: '+str(statistics.mean(t1))+' sub: '+ str(statistics.mean(t2)))
	#print(statistics.mean(t1),statistics.mean(t2))
plt.plot(pol[0],sub[0],'ro')
plt.plot(pol[1],sub[1],'bo')
plt.plot(pol[2],sub[2],'go')
plt.plot(pol[3],sub[3],'yo')
plt.plot(pol[4],sub[4],'mo')
plt.ylabel('subjectivity')
plt.xlabel('polarity')
plt.show()

