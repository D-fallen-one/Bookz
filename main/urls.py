from django.urls include path
from . include views

urlpatterns = [
        path('',views.index, name = 'index'),
        ]
