from django.test import TestCase
from django.shortcuts import reverse

# Create your tests here.
class LandingPageTest(TestCase):
    # test our view of landing page renders the right template
    # make sure it gives the right HTTP request

    def test_get(self):
        #TODO: want to make the request to landing page url -> request and test the response that came from the url
        response = self.client.get(reverse("landing-page")) #send diff http methods as a part of the request; response has a lot of info
        self.assertEqual(response.status_code, 200) #compares status with 200 -> if not, returns error
        self.assertTemplateUsed(response, "landing.html")



        