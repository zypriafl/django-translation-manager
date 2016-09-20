from django.contrib import admin
from django.conf.urls import url, include
from translation_manager import urls as translation_urls

from translation_manager.settings import get_settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
]

if get_settings('TRANSLATIONS_PROCESSING_METHOD') == 'async_django_rq':
    urlpatterns.append(url(r'^django-rq/', include('django_rq.urls')))

if get_settings('TRANSLATION_ENABLE_API_COMMUNICATION'):
    urlpatterns.append(url(r'^translations/', include(translation_urls)))
