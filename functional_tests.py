#First thing he saw is title. the title name is "Welearn".
#
#
#
#
#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
class NewVisitorTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Firefox()

  def tearDown(self):
    time.sleep(10)
    self.browser.quit()

  def test_can_start_a_list_and_retrieve_it_later(self):
    self.browser.get('http://localhost:8000')
    self.assertIn('Welearn', self.browser.title)

    check_button_tutor = self.browser.find_element_by_name('name_tutor')
    self.assertEqual(check_button_tutor.get_attribute('value'), 'Tutor')

    check_button_tutor.click()
    time.sleep(3)
    check_url_tutor = self.browser.current_url
    self.assertRegex(check_url_tutor, '/WelearnApp/tutor')

    # He create post.
    inputbox = self.browser.find_element_by_id('id_new_post')
    self.assertEqual(inputbox.get_attribute('placeholder'),'Enter your post')
    inputbox.send_keys('Hi! I am Tutor')
    #check_button_tutor = self.browser.find_element_by_name('name_post')
    #check_button_tutor.click()
    time.sleep(3)
    
    table = self.browser.find_element_by_id('id_post_table')

    
    self.fail('Finish the test!')

if __name__ == '__main__':
   unittest.main(warnings='ignore')
