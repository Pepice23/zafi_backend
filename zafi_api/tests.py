from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from .models import Character


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.character = Character.objects.create(
            character_name="Pepó",
            character_faction="Alliance",
            character_gender="Male",
            character_race="Dwarf",
            character_class="Shaman",
        )

    def test_model_content(self):
        self.assertEqual(self.character.character_name, "Pepó")
        self.assertEqual(self.character.character_faction, "Alliance")
        self.assertEqual(self.character.character_gender, "Male")
        self.assertEqual(self.character.character_race, "Dwarf")
        self.assertEqual(self.character.character_class, "Shaman")

    def test_api_listview(self):
        response = self.client.get(reverse("character_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Character.objects.count(), 1)
        self.assertContains(response, self.character)

    def test_api_detailview(self):  # new
        response = self.client.get(
            reverse("character_detail", kwargs={"pk": self.character.character_name}),
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Character.objects.count(), 1)
        self.assertContains(response, "Pepó")
