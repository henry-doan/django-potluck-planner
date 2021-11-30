"""potluck URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as authentication_views
from django.conf import settings
from django.conf.urls.static import static
from planner import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact/', views.contact, name="contact"),
    path('contacts/', views.contacts, name="contacts"),
    path('contacts/<int:pk>', views.contact_details, name="contact_details"),
    path('contacts/<int:id>/delete/', views.delete_contact, name="delete_contact"),
    path('contacts/<int:id>/update/', views.update_contact, name="update_contact"),
    path('events/', views.events, name="events"),
    path('add_event/', views.add_event, name="add_event"),
    path('events/<int:pk>', views.event_details, name="event_details"),
    path('events/<int:id>/download', views.dlevent, name="dlevent"),
    path('events/<int:id>/delete/', views.delete_event, name="delete_event"),
    path('events/<int:id>/update/', views.update_event, name="update_event"),
    path('events/<int:pk>/addEntree', views.add_entree, name="add_entree"),
    path('events/<int:pk>/addSide', views.add_side, name="add_side"),
    path('events/<int:pk>/addDessert', views.add_dessert, name="add_dessert"),
    path('events/<int:pk>/addDrink', views.add_drink, name="add_drink"),
    path('events/<int:pk>/addSupplie', views.add_side, name="add_supplie"),
    path('items/<int:id>/update/', views.update_item, name="update_item"),
    path('items/<int:id>/delete/', views.delete_item, name="delete_item"),
    path('register/', user_views.register, name='register'),
    path('login/', authentication_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', authentication_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]

urlpatterns += [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
