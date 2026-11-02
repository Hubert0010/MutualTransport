"""
Views for MutualTransport - Frontend only (no backend logic).
Each view simply renders the corresponding template.
"""
from django.shortcuts import render


# ============================================================
# Authentification
# ============================================================

def login_view(request):
    """Page de connexion (compagnie / administrateur)."""
    return render(request, 'core/login.html')


def register_view(request):
    """Page d'inscription compagnie (BF-28)."""
    return render(request, 'core/register.html')


# ============================================================
# Espace Administrateur
# ============================================================

def admin_dashboard(request):
    """Tableau de bord administrateur."""
    return render(request, 'core/admin/dashboard.html')


def admin_compagnies(request):
    """Gestion des compagnies en attente (BF-37)."""
    return render(request, 'core/admin/compagnies.html')


def admin_utilisateurs(request):
    """Supervision des utilisateurs (BF-38, BF-39)."""
    return render(request, 'core/admin/utilisateurs.html')


def admin_reservations(request):
    """Supervision des réservations et paiements (BF-39)."""
    return render(request, 'core/admin/reservations.html')


def admin_collecte(request):
    """Couverture réseau mutualisé (BF-57)."""
    return render(request, 'core/admin/collecte.html')


# ============================================================
# Espace Compagnie
# ============================================================

def compagnie_dashboard(request):
    """Tableau de bord compagnie (BF-35)."""
    return render(request, 'core/compagnie/dashboard.html')


def compagnie_vehicules(request):
    """Gestion des véhicules (BF-30)."""
    return render(request, 'core/compagnie/vehicules.html')


def compagnie_trajets(request):
    """Gestion des trajets (BF-31)."""
    return render(request, 'core/compagnie/trajets.html')


def compagnie_reservations(request):
    """Réservations reçues et paiements (BF-34)."""
    return render(request, 'core/compagnie/reservations.html')


def compagnie_profil(request):
    """Profil de la compagnie (BF-29)."""
    return render(request, 'core/compagnie/profil.html')


def compagnie_regles(request):
    """Règles d'annulation et de remboursement (BF-32)."""
    return render(request, 'core/compagnie/regles.html')


def compagnie_import(request):
    """Import de données CSV/Excel (BF-50, BF-51)."""
    return render(request, 'core/compagnie/import_donnees.html')
