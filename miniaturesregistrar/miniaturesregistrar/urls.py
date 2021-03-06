"""miniaturesregistrar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import logout_then_login
from minis.views import AddMiniView, MiniColorsView, ElementView, MainView, \
    RegisterView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'logout/$', logout_then_login, name="site-logout"),
    url(r'^add_mini/$', AddMiniView.as_view(), name='add-mini'),
    url(r'^minicolors/(?P<miniature_id>\d+)/?$', MiniColorsView.as_view(),
        name="mini-colors"),
    url(r'^element_view/(?P<id>(\d)+)$', ElementView.as_view(),
        name="element"),
    url(r'^$', MainView.as_view(), name="main"),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^register/$', RegisterView.as_view(), name="register"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
