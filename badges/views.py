from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserBadge, Badge, Model3d
from .utils import award_badges


class UserBadgeAPIView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User,
                                 id=user_id)  # Obtenir l'utilisateur correspondant à l'ID fourni, ou renvoyer une réponse 404 si l'utilisateur n'existe pas.
        print(f"Obtained user: {user.username}")
        badges = UserBadge.objects.filter(
            user=user)  # Requête pour récupérer tous les badges associés à cet utilisateur.
        badge_list = [badge.badge.name for badge in badges]  # Liste des noms de badges.
        print(f"Badges for user: {badge_list}")
        return Response(badge_list)  # retourne la liste sous format JSON.


def view_model_3d(request, model_3d_id):
    model_3d = get_object_or_404(Model3d, pk=model_3d_id)
    model_3d.views += 1
    model_3d.save()

    award_badges(request.user)

    return JsonResponse({'message': 'Modèle 3D vu avec succès'})


def create_model_3d(request):
    # Logique pour créer un modèle 3D
    # Assurez-vous d'ajouter le modèle à la base de données et lier l'utilisateur

    # Vérifiez si l'utilisateur a créé 5 modèles
    if request.user.model3d_set.count() >= 5:
        # Appeler la fonction pour attribuer le badge "Collector"
        award_badges(request.user)

    return JsonResponse({'message': 'Modèle 3D créé avec succès'})


def register_user(request):
    # Logique pour l'inscription d'un utilisateur
    # Assurez-vous de créer un nouvel utilisateur dans la base de données

    # Créez un nouvel utilisateur (remplacez cela par votre logique d'inscription)
    new_user = User.objects.create_user(username='nouvel_utilisateur', password='mot_de_passe')

    # Appeler la fonction pour attribuer le badge "Pioneer"
    user = authenticate(username='nouvel_utilisateur', password='mot_de_passe')  # Authentification de l'utilisateur
    if user is not None:
        login(request, user)  # Connexion de l'utilisateur
        award_badges(user)
