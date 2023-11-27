from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("catalog_develop/", views.catalog_develop, name="catalog_develop"),
    path("projects/", views.projects, name="projects"),
    path("catalog_develop/<int:pk>/", views.develop_detail, name="develop-detail"),
    path("update_description/", views.index, name="update_description"),
    path("add_section/", views.add_section, name="add-section"),
    path("add_card/", views.add_card, name="add-card"),
    path("catalog_view/", views.catalog_view, name="catalog_view"),
    path("manager/", views.manager, name="manager"),
    path("projects/", views.projects_info, name='projects_info'),
]