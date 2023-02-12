from django.test import TestCase

from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Skin, Offer


class SkinsTestCase(TestCase):
    def setUp(self):
        self.skin = Skin.objects.create(
            name="Skin object (1)", price=1.99, stock=20, exterior_quality=0.9, rarity="Uncommon", image_url="https"
                                                                                                       "://csgobluegem.com/wp-content/uploads/2020/03/Five-SeveN.png "
        )
        self.offer = Offer.objects.create(
            code="Offer object (1)", description="10% off", discount=0.1
        )
        self.user = User.objects.create_user(
            username='testuser', email='testuser@test.com', password='secret123'
        )

    def test_skin_creation(self):
        self.assertTrue(isinstance(self.skin, Skin))
        self.assertEqual(self.skin.__str__(), self.skin.name)

    def test_offer_creation(self):
        self.assertTrue(isinstance(self.offer, Offer))
        self.assertEqual(self.offer.__str__(), self.offer.code)

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_index_view(self):
        response = self.client.get(reverse('skins'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_gmail_view(self):
        response = self.client.get(reverse('gmail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gmail.html')

    def test_search_skins_view(self):
        response = self.client.get(reverse('search_skins'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_skins.html')

