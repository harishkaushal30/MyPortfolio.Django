from django.test import TestCase
#from selenium import webdriver

# class Function_Test_Case(TestCase):

#     def setUp(self):
#         self.browser = webdriver.Firefox()

#     def test_there_is_homepage(self):
#         self.browser.get('http://localhost:8000')
#         self.assertIn('about', self.browser.page_source)

#     def test_contact_form(self):
#         self.browser.get('http://localhost:8000')
#         name = self.browser.find_element_by_id('id_name')
#         name.send_keys("Harish")
#         email = self.browser.find_element_by_id('id_email_id')
#         email.send_keys("Harish@test.com")
#         subject = self.browser.find_element_by_id('id_subjct')
#         subject.send_keys("Test case")
#         message = self.browser.find_element_by_id('id_message')
#         message.send_keys("Test case message Test case message Test case message Test case message Test case message Test case message") 
#         self.browser.find_element_by_type("submit").click()
#         self.assertIn('Message Sent !!', self.browser.page_source)

#     def tearDown(self):
#         self.browser.quit()

class UnitTestCase(TestCase):

    def test_home_homepage_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')
    
    