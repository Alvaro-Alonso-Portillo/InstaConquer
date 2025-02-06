from django.test import TestCase
from django.urls import reverse

from profiles.models import UserProfile, Follow
from django.contrib.auth.models import User

class UserProfileViews(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='john', email='john@lennon.com', password='password123')
        self.user2 = User.objects.create_user(username='paul', email='paul@mccatney.com', password='password123')
        self.profile1 = UserProfile.objects.create(user=self.user1, bio="I'm a musician", birth_date='1940-10-09')
        self.profile2 = UserProfile.objects.create(user=self.user2, bio="I'm also musician", birth_date='1942-06-18')
        
    def test_profile_list_views(self):
        url = reverse('profile_list')
        response = self.client.get(url) 
        self.assertEqual(response.status_code, 200)
        
    def test_profile_detail_views(self):
        self.client.login(username='john', password='password123')
        url = reverse('profile_detail', args=[self.profile.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        