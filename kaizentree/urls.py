"""kaizentree URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from .views import user_login,user_signup,user_logout,dashboard,TagCreateView,CategoryCreateView,ObtainTokenView,ItemCreateView,CreateUserView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('logout/', user_logout, name='logout'),
    path('home/', dashboard, name='home'),
    path('api/token/', ObtainTokenView.as_view(), name='token'),
    path('api/createuser/', CreateUserView.as_view(), name='createuser'),
    path('api/tag/', TagCreateView.as_view(), name='tag-create'),
    path('api/category/', CategoryCreateView.as_view(), name='category-create'),
    path('api/item/', ItemCreateView.as_view(), name='item-create')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
