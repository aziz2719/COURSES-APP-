from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from categorys.views import BranchView, ContactView
from rest_framework import routers



router = routers.DefaultRouter()

router.register(r'branch', BranchView)
router.register(r'contact', ContactView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', include('categorys.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += router.urls