from django.contrib import admin
from django.urls import path

from family.views import AddFamMember, FamList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-member', AddFamMember),
    path('fam-list/', FamList),]