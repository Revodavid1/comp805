from django.test import TestCase
from .models import Resume, Education, Experience
# Create your tests here.

class ResumeTestCases(TestCase):
    

    def setUp(self):
        """
        runs at beginning...
        """
        self.my_resume = Resume.objects.create(First_name='Oreva', 
            Last_name='Omu')
        self.david_resume = Resume.objects.create(First_name='David', 
            Last_name='Revo')
        self.my_education = Education.objects.create(
            parent_resume = self.my_resume, institution_name = 'UNHM', 
            location = 'NH', degree = 'Masters', 
            major = 'Information Technology', gpa = 4.0)
        self.david_education = Education.objects.create(
            parent_resume = self.david_resume, institution_name = 'UNHM',
            location = 'NH', degree = 'Masters', 
            major = 'Information Technology', gpa = 4.0)
        self.my_experience = Experience.objects.create(
            parent_resume = self.my_resume, title = 'Software Engineer',
            location = 'Spotify', start_date = '2017-09-01', 
            end_date = '2017-12-31', description = 'Full Stack Development')
        self.my_experience2 = Experience.objects.create(
            parent_resume = self.my_resume, title = 'Frontend Developer',
            location = 'Facebook', start_date = '2018-01-01', 
            end_date = '2018-02-10', description = 'Web Development')
        self.david_experience = Experience.objects.create(
            parent_resume = self.david_resume, title = 'Database Admin',
            location = 'Oracle', start_date = '2002-01-01', 
            end_date = '2016-02-10', description = 'Database Administration')
        
    def test_get_full_name(self):
        """
        Tests get_last_name_first_name method
        """
        r = Resume.objects.first()
        self.assertEqual(r.get_full_name(), 'Oreva Omu')

    def test_get_last_name_first_name(self):
        """
        Tests get_last_name_first_name method
        """
        r = Resume.objects.first()
        self.assertEqual(r.get_last_name_first_name(), 'Omu Oreva')

    def test_get_experience(self):
        """
        Tests get_experience method
        """
        r = Resume.objects.first()
        result = r.get_experience()
        self.assertTrue(len(result), 2)
        self.assertTrue(self.my_experience in result)
        self.assertTrue(self.my_experience2 in result)
        self.assertFalse(self.david_experience in result)
        

    def test_get_education(self):
        """
        Tests get_education method
        """

        r = Resume.objects.first()
        result = r.get_education()
        self.assertTrue(self.my_education in result)
        self.assertFalse(self.david_education in result)