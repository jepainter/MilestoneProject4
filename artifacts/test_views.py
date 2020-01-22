from django.test import TestCase
from artifacts.models import Artifact
from categories.models import Category

class TestViews(TestCase):
    
    def test_get_artifacts_page(self):
        page = self.client.get("/artifacts/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "artifacts.html")
    
    def test_get_detailed_artifact_page(self):
        category=Category(
            category_name="Test Category",
            category_description="Test Category",
        )
        category.save()
        artifact=Artifact(
            name="Test",
            reserve_price="1.11",
            purchase_price="1.11",
            quantity=1,
            category=category,
        )
        artifact.save()
        page = self.client.get("/artifacts/view/{0}".format(artifact.id) )
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "artifact_detail.html")
        
    def test_get_detailed_artifact_that_does_not_exist(self):
        page = self.client.get("/artifacts/view/{0}".format(99) )
        self.assertEqual(page.status_code, 404)