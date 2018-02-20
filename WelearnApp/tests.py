from django.template.loader import render_to_string
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from WelearnApp.views import home_page

class HomePageTest(TestCase):

  def test_root_url_resolve_to_home_page_view(self):
    found = resolve('/')
    self.assertEqual(found.func, home_page)

  def test_home_page_returns_correct_html(self):
    request = HttpRequest()
    response = home_page(request)
    html = response.content.decode('utf8')
    expected_html = render_to_string('home.html')
    self.assertEqual(html, expected_html)

  def test_tutor_page_returns_correct_html(self):
  	response = self.client.get('/WelearnApp/tutor')

  	html = response.content.decode('utf8')
  	self.assertTrue(html.startswith('<html>'))
  	self.assertIn('<title>Tutor</title>', html)
  	self.assertTrue(html.strip().endswith('</html>'))

  	self.assertTemplateUsed(response, 'tutor.html')

  def test_can_save_a_POST_request(self):
  	response = self.client.post('/WelearnApp/tutor', data={'post_item':'A new post'})
  	self.assertIn('A new post', response.content.decode())
  	

