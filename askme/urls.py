from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

import ask.views

urlpatterns = [
    path('', ask.views.hello),
    path('like/', ask.views.like),
    path('login/', ask.views.login_view),
    path('register/', ask.views.register),
    path('secret/', ask.views.secret),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
