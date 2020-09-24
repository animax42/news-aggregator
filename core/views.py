#python imports
from datetime import datetime

#django imports
from django.views.generic import TemplateView

#local imports

#inter app imports
from shared.mixins import CacheMixin
from article.models import Article

#third party imports

class HomePageView(CacheMixin,TemplateView):
	cache_timeout = 60
	template_name = "index.html"

	def get_context_data(self,**kwargs):
		print("Hello World")
		context = super(HomePageView,self).get_context_data(**kwargs)
		filter_kwargs = {}
		if(self.request.GET.get("q")):
			filter_kwargs.update({"keywords__icontains":self.request.GET.get("q")})

		if(self.request.GET.get("sdate")):
			filter_kwargs.update({"publish_date__gte":datetime.strptime(self.request.GET.get("sdate"),"%Y-%m-%d")})

		if(self.request.GET.get("edate")):
			filter_kwargs.update({"publish_date__lte":datetime.strptime(self.request.GET.get("edate"),"%Y-%m-%d")})

		context.update({"recent_articles":Article.objects.filter(**filter_kwargs).order_by('-id')[:10]})
		return context
