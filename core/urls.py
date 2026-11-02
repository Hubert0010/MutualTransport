"""URL configuration for core app - MutualTransport."""
from django.urls import path
# pyrefly: ignore[missing-import]
from . import views

app_name = 'core'

urlpatterns = [
    # --- Authentification ---
    path('', views.login_view, name='login'),
    path('connexion/', views.login_view, name='connexion'),
    path('inscription/', views.register_view, name='inscription'),

    # --- Espace Administrateur ---
    path('admin/tableau-de-bord/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/compagnies/', views.admin_compagnies, name='admin_compagnies'),
    path('admin/utilisateurs/', views.admin_utilisateurs, name='admin_utilisateurs'),
    path('admin/reservations/', views.admin_reservations, name='admin_reservations'),
    path('admin/collecte/', views.admin_collecte, name='admin_collecte'),

    # --- Espace Compagnie ---
    path('compagnie/tableau-de-bord/', views.compagnie_dashboard, name='compagnie_dashboard'),
    path('compagnie/vehicules/', views.compagnie_vehicules, name='compagnie_vehicules'),
    path('compagnie/trajets/', views.compagnie_trajets, name='compagnie_trajets'),
    path('compagnie/reservations/', views.compagnie_reservations, name='compagnie_reservations'),
    path('compagnie/profil/', views.compagnie_profil, name='compagnie_profil'),
    path('compagnie/regles/', views.compagnie_regles, name='compagnie_regles'),
    path('compagnie/import-donnees/', views.compagnie_import, name='compagnie_import'),
]
