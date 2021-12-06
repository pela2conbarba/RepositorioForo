from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'blog'

urlpatterns = [
    path('blog/', views.listarblog, name = 'listar_blog')
]


urlpatterns += staticfiles_urlpatterns()