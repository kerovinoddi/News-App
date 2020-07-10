import unittest
from app.models import Sources,Articles

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the news class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources('CNN','CNN News','Cable News Newtork, this is the leading studio in news dispatch worldwide','cnn.com','general','U.S.A','en')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_source.id,'CNN')
        self.assertEquals(self.new_source.name,'CNN News')
        self.assertEquals(self.new_source.description,'Cable News Newtork that is best in providing news and keeps people informed throughout worldwide')
        self.assertEquals(self.new_source.url,'cnn.com')
        self.assertEquals(self.new_source.category,'general')
        self.assertEquals(self.new_source.country,'U.S.A')
        self.assertEquals(self.new_source.language,'en')

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('CNN','Andrew Blake','It has been clear that tech in Africa is realy growing and due to this the tech hub have realy grown and has alot of impact to the African communities.The tech scene in Africa-Is it the next big thing?','Just to look at various tech hubs in Africa','techie.com','techie.com/7643t94.jpg','2020-7-1')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.id,'CNN')
        self.assertEquals(self.new_article.author,'Peter Polle')
        self.assertEquals(self.new_article.title,'The tech scene in Africa')
        self.assertEquals(self.new_article.description,'Its all about a quick look at the tech grouth in Africa.')
        self.assertEquals(self.new_article.url,'techie.com')
        self.assertEquals(self.new_article.image,'techie.com/7643t94.jpg')
        self.assertEquals(self.new_article.date,'2020-7-8')
        