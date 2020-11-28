from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index , name = "index"),
    path('new', views.new , name = "new"),
    path("<int:num>" , views.diary , name="diary"),
    path( "ckeditor/", include("ckeditor_uploader.urls")),
    path("accounts/" , include("django.contrib.auth.urls")),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
