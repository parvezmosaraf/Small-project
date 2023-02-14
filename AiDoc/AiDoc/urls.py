from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('authentication.urls')),
] + static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

admin.site.site_header = "AI DOC Panel"
admin.site.site_title = "AI DOC ADMINPANEL"
admin.site.index_title = "Welcome To AIDOC"
