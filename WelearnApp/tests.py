from django.template.loader import render_to_string
from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from WelearnApp.views import home_page
from WelearnApp.models import Item

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
        pass
        '''response = self.client.post('/WelearnApp/tutor/post', data={'post_tutor_item':'A new list item'})# >>post_tutor_item is variable in tutorpost.html
        
        self.assertEqual(Item.objects.count(), 1)
        post_item = Item.objects.first()
        self.assertEqual(post_item.text, 'A new list item')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/WelearnApp/tutor/post')

        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'tutorpost.html')'''

class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        frist_item = Item()
        frist_item.post_text = 'The first (ever) list item'
        frist_item.save()

        second_item = Item()
        second_item.post_text = 'Item the second'
        second_item.save()

        saved_item = Item.objects.all()
        self.assertEqual(saved_item.count(),2)

        first_saved_item = saved_item[0]
        second_saved_item =saved_item[1]
        self.assertEqual(first_saved_item.post_text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.post_text, 'Item the second')

    def test_can_delete_post(self):
        frist_item = Item()
        frist_item.post_text = 'The first (ever) list item'
        frist_item.save()

        second_item = Item()
        second_item.post_text = 'Item the second'
        second_item.save()

        saved_item = Item.objects.all()
        print("Befor delete post", saved_item)
        a = saved_item.filter(id=1)
        a.delete()
        print("After delete post", saved_item)

    def test_can_comment(self):
        frist_item = Item()
        frist_item.comment = 'The first comment'
        frist_item.save()

        second_item = Item()
        second_item.comment = 'Item the second comment'
        second_item.save()

        saved_item = Item.objects.all()
        print("MYYYYY comments", saved_item)

