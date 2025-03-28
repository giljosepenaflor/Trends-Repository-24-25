from django.contrib import admin
from django.urls import path, include
from members import views  # ✅ Import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.members, name='members'),  # ✅ Route to `members` directly
    # OR if using app URLs:
    # path('members/', include('members.urls')),  
]
