from django.contrib import admin
from django.urls import path
from sampleapp.views import GetNamedEnts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ner', GetNamedEnts.as_view())
]
# Register your models here.
