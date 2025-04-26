"""
URL configuration for resumebuilder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# resumebuilder/urls.py

# resumebuilder/urls.py

# resumebuilder/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# This is your main URL configuration for the project.
# It includes admin, app-level routing, and static file support.

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include all app-level URLs from the 'core' app
    path('', include('core.urls')),  # Ensure core/urls.py exists and is configured
]

# Serving static files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
