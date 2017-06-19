import newspaper
import csv

class newsExtractor(object):
	"""docstring for newsExtractor"""
	def __init__(self, url):
		self.url = url
		self.paper = newspaper.build(url,memoize_articles=False)
		self.result=[["Title","Article"]]
		print("initialized successfully")

	def extract_article(self):
		length = self.paper.size()
		
		for i in range(length):
			article=self.paper.articles[i]
			article.download()
			article.parse()
			articleText=article.text
			articleTitle=article.title
			self.result.append([articleTitle,articleText])
		print("extracted successfully")

	def store_result(self,filename):
		with open(filename,'w') as f:
			w= csv.writer(f)
			for row in self.result:
				w.writerow(row)



hindustan_times = newsExtractor("http://www.hindustantimes.com/")
hindustan_times.extract_article()
hindustan_times.store_result("hindustan_times.csv")

