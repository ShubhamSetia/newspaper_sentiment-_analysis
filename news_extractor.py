import newspaper


class newsExtractor(object):
	"""docstring for newsExtractor"""
	def __init__(self, url):
		self.url = url
		self.paper = newspaper.build(url,memoize_articles=False)
		self.result=[["Title","Article"]]

	def extract_article():
		length = self.paper.size()
		
		for i in range(length):
			article=self.paper.articles[i]
			article.download()
			article.parse()
			articleText=article.text
			articleTitle=article.title
			self.result.append([articleTitle,articleText])

	
