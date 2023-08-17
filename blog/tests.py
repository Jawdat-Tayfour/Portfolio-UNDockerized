from django.test import TestCase
from django.urls import reverse


from .models import Project 



class ProjectTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.project = Project.objects.create(
            title="Project title",
            body="project body",
            project_type="game-dev",
        )
        cls.project2 = Project.objects.create(
            title="Project title 2",
            body="project body 2",
            project_type="web-dev",
        )
    
    def test_project_listing(self):
        self.assertEqual(f"{self.project.title}", "Project title")
        self.assertEqual(f"{self.project.body}", "project body")
        self.assertEqual(f"{self.project.project_type}", "game-dev")    

    def test_game_dev_list_view(self):
        response =self.client.get(reverse("game_dev_project_list"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"game-dev")
        self.assertTemplateUsed(response,"game_dev_projects.html")

    def test_web_dev_list_view(self):
        response =self.client.get(reverse("web_dev_project_list"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"web-dev")
        self.assertTemplateUsed(response,"web_dev_projects.html")    


    def test_project_detail_view(self):
        response = self.client.get(self.project.get_absolute_url())
        no_response = self.client.get("blog/12345/")
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,"game-dev")
        self.assertTemplateUsed(response,"project_detail.html")
    