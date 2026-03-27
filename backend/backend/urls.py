from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/complaints/', include('complaints.urls')),
    path('api/visitors/', include('visitors.urls')),
    path('api/payments/', include('payments.urls')),
    path('api/notices/', include('notices.urls')),
]

schema_view = get_schema_view(
   openapi.Info(
      title="Smart Society API",
      default_version='v1',
      description="API documentation",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger')),
]
