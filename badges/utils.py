from .models import Badge, UserBadge
from datetime import datetime, timedelta
from django.utils import timezone

def award_badges(user):
    # Vérifier si l'utilisateur possède déjà le badge "Star".
    if not UserBadge.objects.filter(user=user, badge__name='Star').exists():
        # Vérifier l'état de l'insigne "Star"
        if user.model3d_set.filter(views__gte=1000).exists():
            star_badge, _ = Badge.objects.get_or_create(name='Star',
                                                        description='Le modèle d\'un utilisateur a plus de 1000 vues')
            UserBadge.objects.get_or_create(user=user, badge=star_badge)
            print(f'L\'utilisateur {user.username} a reçu le badge Étoile')

    # Vérifier l'état de l'insigne "Star
    if user.model3d_set.filter(views__gte=1000).exists():
        star_badge, _ = Badge.objects.get_or_create(name='Star',
                                                    description='Le modèle d\'un utilisateur a plus de 1000 vues')
        UserBadge.objects.get_or_create(user=user, badge=star_badge)
        print(f'L\'utilisateur {user.username} a reçu le badge Étoile')

    # Badge Collector
    if user.model3d_set.count() >= 5:
        _badge_collector, _ = Badge.objects.get_or_create(name='Collector',
                                                         description='Un utilisateur a téléchargé plus de 5 modèles')
        UserBadge.objects.get_or_create(user=user, badge=_badge_collector)
        print(f'L\'utilisateur {user.username} a reçu le badge de Collector')
    else:
        print(f'L\'utilisateur {user.username} ne répond pas aux critères du badge de Collector')


    # Badge Pioneer
    un_an = timezone.now() - timedelta(days=365)
    if user.date_joined < un_an and not UserBadge.objects.filter(user=user, badge__name='Pioneer').exists():
        _badge_pioneer, _ = Badge.objects.get_or_create(name='Pioneer', description='L\'utilisateur est inscrit depuis plus de 1 an')
        UserBadge.objects.get_or_create(user=user, badge=_badge_pioneer)
        print(f'L\'utilisateur {user.username} a reçu le badge Pioneer')


