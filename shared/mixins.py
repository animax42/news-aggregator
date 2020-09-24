#python imports

#django imports
from django.views.decorators.cache import cache_page

#local imports

#inter app imports

#third party imports


class CacheMixin(object):
	cache_timeout = 10

	def get_cache_timeout(self):
		return self.cache_timeout

	def dispatch(self, *args, **kwargs):
		method_call = super(CacheMixin, self).dispatch
		return cache_page(self.get_cache_timeout())(method_call)(*args, **kwargs)