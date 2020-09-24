#python imports
import sys,os,django
from datetime import datetime

#Settings import
# from django.conf import settings
sys.path.append("/".join(os.path.dirname(__file__).split("/")[:-1]))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.main")
django.setup()
from django.conf import settings

#local imports

#inter app imports
from article.models import Article

#third party imports
import requests

if __name__=="__main__":

	#Clear the DB first
	Article.objects.delete()

	base_url = "http://newsapi.org/v2/everything?q=bitcoin&from=2020-08-22&sortBy=publishedAt&apiKey=5772ce9eacc6480694f47a42d9f95958&page={}"
	for i in range(1,6):
		url_to_hit = base_url.format(i)
		response = requests.get(url_to_hit)
		json_response = response.json()
		articles = json_response["articles"]

		for article in articles:

			obj = Article()
			obj.title = article.get("title")
			obj.short_description = article.get("description")
			obj.image = article.get("urlToImage")
			obj.publish_date = datetime.strptime(article.get("publishedAt"), "%Y-%m-%dT%H:%M:%SZ")
			print(article.get("author"))
			obj.author = article.get("author")
			obj.source = article.get("source",{}).get("name","")
			obj.landing_url = article.get("url")
			obj.published = True
			keywords = []
			if (obj.author):
				keywords.append(obj.author)
			if (obj.source):
				keywords.append(obj.source)

			obj.keywords = ",".join(keywords)

			obj.save()