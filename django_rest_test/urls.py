from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from blog.views import blog_page,blog_api

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('rest-api/', include('rest_framework.urls')),
    path('rest-swagger/', schema_view),
    path('admin/', admin.site.urls),

    # blog
    path('blog/', blog_page),

    # Rest
    path('api/blog/', blog_api.as_view()),
]
