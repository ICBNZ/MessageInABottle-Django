# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from aldryn_django.utils import i18n_patterns
import aldryn_addons.urls
#import filer.server.urls
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.views.generic import RedirectView
import accounts.views, blog.views, about.views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views  # Social Auth

from django.conf.urls.static import static


urlpatterns = [
    # add your own patterns here
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('accounts/', include('accounts.urls')),
    path('blog/', include('blog.urls')),
    path('about/', include('about.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('social-auth/', include('social_django.urls', namespace="social")),
    url(r'^messageinabottle.us.aldryn.io$', RedirectView.as_view(url='accounts/'), name='home'),
    #url(r'^', include('filer.server.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + aldryn_addons.urls.patterns() + i18n_patterns(

    # add your own i18n patterns here
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
)
