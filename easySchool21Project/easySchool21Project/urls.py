"""
URL configuration for easySchool21Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from clusterEmploymentES21.views import index_page
from clusterEmploymentES21.views import hydrogenGraphicPage
from clusterEmploymentES21.views import carbonGraphicPage
from clusterEmploymentES21.views import sulfurGraphicPage
from clusterEmploymentES21.views import hydrogenTextPage
from clusterEmploymentES21.views import carbonTextPage
from clusterEmploymentES21.views import sulfurTextPage
from clusterEmploymentES21.views import carbonPage
from clusterEmploymentES21.views import hydrogenPage
from clusterEmploymentES21.views import sulfurPage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('hydrogenText/', hydrogenTextPage),
    path('carbonText/', carbonTextPage),
    path('sulfurText/', sulfurTextPage),
    path('hydrogenGraphic/', hydrogenGraphicPage),
    path('carbonGraphic/', carbonGraphicPage),
    path('sulfurGraphic/', sulfurGraphicPage),
    path('hydrogen/', hydrogenPage),
    path('carbon/', carbonPage),
    path('sulfur/', sulfurPage),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
