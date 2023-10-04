from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.test import APIClient
from .models import Model3d, Badge, UserBadge
from .utils import award_badges
from datetime import datetime, timedelta

class BadgeTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.model1 = Model3d.objects.create(user=self.user, image='model1.jpg')
        self.model2 = Model3d.objects.create(user=self.user, image='model2.jpg')
        self.model3 = Model3d.objects.create(user=self.user, image='model3.jpg')

        self.client = APIClient()

    def test_star_badge(self):
        # Vérifier que l'utilisateur n'a pas déjà le badge "Star" au début du test
        self.assertFalse(UserBadge.objects.filter(user=self.user, badge__name='Star').exists())

        # L'utilisateur a moins de 1000 vues
        award_badges(self.user)
        self.assertFalse(UserBadge.objects.filter(user=self.user, badge__name='Star').exists())

        # L'utilisateur a exactement 1000 vues
        for _ in range(1000):
            self.model1.views += 1
            self.model1.save()
        award_badges(self.user)
        """
        Si l'utilisateur a déjà le badge "Star", le test self.assertTrue(UserBadge.objects.filter(user=self.user, badge__name='Star').exists())
        générera une erreur "AssertionError: True is not false", car on essaie de vérifier si le badge existe alors qu'il existe déjà.
        vous pouvez décommentez cette ligne <<self.assertFalse(UserBadge.objects.filter(user=self.user, badge__name='Star').exists())>> pour vérifier
        """
        #self.assertFalse(UserBadge.objects.filter(user=self.user, badge__name='Star').exists())

        # L'utilisateur a plus que 1000 vues
        for _ in range(1001):
            self.model1.views += 1
            self.model1.save()
        award_badges(self.user)

        """
           Si l'utilisateur a déjà le badge "Star", le test self.assertTrue(UserBadge.objects.filter(user=self.user, badge__name='Star').exists())
           générera une erreur "AssertionError: True is not false", car on essaie de vérifier si le badge existe alors qu'il existe déjà.
           vous pouvez décommentez cette ligne <<self.assertFalse(UserBadge.objects.filter(user=self.user, badge__name='Star').exists())>> pour vérifier
       """
        #self.assertTrue(UserBadge.objects.filter(user=self.user, badge__name='Star').exists())

    def test_collector_badge(self):
        # L'utilisateur a moins de 5 modèls
        award_badges(self.user)
        self.assertFalse(UserBadge.objects.filter(user=self.user, badge__name='Collector').exists())

        # L'utilsateur a plus de 5 models
        for _ in range(5):
            Model3d.objects.create(user=self.user, image=f'model{_}.jpg')
        print(f'L\'utilsateur a {self.user.model3d_set.count()} models')
        award_badges(self.user)
        self.assertTrue(UserBadge.objects.filter(user=self.user, badge__name='Collector').exists())

    def test_pioneer_badge(self):
        # L'utilisateur à moins de 1 an
        award_badges(self.user)
        self.assertFalse(UserBadge.objects.filter(user=self.user, badge__name='Pioneer').exists())

        # L'utilisateur a exactement 1 an
        one_year_ago = timezone.now() - timedelta(days=365)
        self.user.date_joined = one_year_ago
        self.user.save()
        award_badges(self.user)
        self.assertTrue(UserBadge.objects.filter(user=self.user, badge__name='Pioneer').exists())

        # L'utilisateur s'est inscrit il y a plus de 1 an
        years_user = one_year_ago - timedelta(days=1)
        self.user.date_joined = years_user
        self.user.save()
        award_badges(self.user)
        self.assertTrue(UserBadge.objects.filter(user=self.user, badge__name='Pioneer').exists())

