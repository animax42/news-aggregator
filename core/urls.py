# python imports

# django imports
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

# local imports
from .views import HomePageView

#inter app imports
from article import views

#third party imports


urlpatterns = [
                  url(r'^$', HomePageView.as_view()),
                  url(r'^admin/', admin.site.urls),
                  url(r'^', include('article.urls')),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
