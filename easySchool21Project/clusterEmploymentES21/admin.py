from django.contrib import admin
from clusterEmploymentES21.models import user
from clusterEmploymentES21.models import image
from clusterEmploymentES21.models import hydrogenPlaces
from clusterEmploymentES21.models import carbonPlaces

admin.site.register(user)
admin.site.register(image)
admin.site.register(hydrogenPlaces)
admin.site.register(carbonPlaces)
