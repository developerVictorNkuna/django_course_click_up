from django.test import TestCase
from MeetUps.models import Meetup


class MeetupModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        #set up non-modified objects used by all test methods
        Meetup.objects.create(title="Sex on the beach",
                                slug="Weekend Entertainment",
                                description="The event mainly is about a cocktail event I will be doing with couple of my friends")


    def test_title_field_label(self):
        meetup =Meetup.objects.get(id=1)
        field_label =meetup.__meta.get_field('title').verbose_name
        self.assertEqual(field_label,'title')

    def test_slug_field_label(self):
        meetup =Meetup.objects.get(id=1)
        field_label=meetup.__meta.get_field('slug').verbose_name
        self.assertEqual(field_label,'slug')
        
    
    def test_description_field_label(self):
        meetup =Meetup.objects.get(id=1)
        field_label=meetup.__meta.get_field('description').verbose_name
        self.assertEqual(field_label,'description')

    def test_title_field_max_length(self):
        meetup =Meetup.objects.get(id=1)
        max_length =meetup.__meta.get_field('title').max_length
        self.assertEqual(max_length,200)







