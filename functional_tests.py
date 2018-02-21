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

  def check_for_row_in_list_table(self, row_text):
    table = self.browser.find_element_by_id('id_post_tutor_table') # id_post_tutor_table is id table in tutorpost.html
    rows = table.find_elements_by_tag_name('tr')
    self.assertIn(row_text, [row.text for row in rows])

  #def checheck_for_row_in_list_table
  # Nut has heard about web application 'Welearn'.
  # He goes to check out its homepage
  # nut saw the title name 'Welearn'
  def test_can_start_a_list_and_retrieve_it_later(self):
    self.browser.get('http://localhost:8000')
    self.assertIn('Welearn', self.browser.title)

    # นัทเห็นปุ่ม “บอร์ดรวม”  “Tutor”  “Examination”  “Problem”  และปุ่มตั้งกระทู้
    check_button_board = self.browser.find_element_by_name('name_board')
    self.assertEqual(check_button_board.get_attribute('value'), 'board')

    check_button_tutor = self.browser.find_element_by_name('name_tutor')
    self.assertEqual(check_button_tutor.get_attribute('value'), 'Tutor')

    check_button_examination = self.browser.find_element_by_name('name_examination')
    self.assertEqual(check_button_examination.get_attribute('value'), 'Examination')

    check_button_problem = self.browser.find_element_by_name('name_problem')
    self.assertEqual(check_button_problem.get_attribute('value'), 'Problem')

    check_button_problem = self.browser.find_element_by_name('name_board_post')
    self.assertEqual(check_button_problem.get_attribute('value'), 'Creat Post')
    time.sleep(10)

    # นัทเห็นกระทู้ทั้งหมดที่มีในบอร์ด


    # นัทกดที่ปุ่ม “Tutor” จากนั้นจะเปลี่ยนหน้าเพจไปที่หมวด Tutor
    check_button_tutor.click()
    check_url_tutor = self.browser.current_url
    self.assertRegex(check_url_tutor, '/WelearnApp/tutor')
    time.sleep(10)

    # นัทกดปุ่มตั้งกระทู้
    check_button_post_tutor = self.browser.find_element_by_name('name_tutor_post')
    self.assertEqual(check_button_post_tutor.get_attribute('value'), 'Creat Post')
    check_button_post_tutor.click()
    check_url_post_tutor = self.browser.current_url
    self.assertRegex(check_url_post_tutor, '/WelearnApp/tutor/post')

    # He open new url for create post.
    inputbox = self.browser.find_element_by_id('id_new_post_tutor')
    # id_new_post_tutor is variable in tutorpost.html
    self.assertEqual(inputbox.get_attribute('placeholder'),'Enter your post')
    inputbox.send_keys('I want someone to be my tutor in Math')
    #check_button_tutor = self.browser.find_element_by_name('name_post')
    inputbox.send_keys(Keys.ENTER)
    time.sleep(10)
    #check_button_tutor.click()
    self.check_for_row_in_list_table('1: I want someone to be my tutor in Math')

    # He add another item. She enters 'Hi! I am Tutor Math'
    inputbox = self.browser.find_element_by_id('id_new_post_tutor')
    # id_new_post_tutor is variable in tutorpost.html
    self.assertEqual(inputbox.get_attribute('placeholder'),'Enter your post')
    inputbox.send_keys('I will teach you all in Circuit, who is interested?')
    #check_button_tutor = self.browser.find_element_by_name('name_post')
    inputbox.send_keys(Keys.ENTER)
    time.sleep(10)
    #check_button_tutor.click()
    # The page updates again, and now shows both items on her list
    self.check_for_row_in_list_table('1: I want someone to be my tutor in Math')
    self.check_for_row_in_list_table('2: I will teach you all in Circuit, who is interested?')
    

    self.fail('Finish the test!')

if __name__ == '__main__':
   unittest.main(warnings='ignore')
