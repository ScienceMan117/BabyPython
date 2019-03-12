import unittest
from city_functions import get_demographic_name

class CountryCityCase(unittest.TestCase):
    
    def test_city_country(self):
        formatted_country = get_demographic_name('santiago', 'chile')
        self.assertEqual(formatted_country, 'Santiago Chile')
    
    def test_city_country_population(self):
        formatted_country = get_demographic_name('santiago', 'chile',
        'population=5000000')
        self.assertEqual(formatted_country,
        'Santiago Chile Population=5000000')
        
        
unittest.main()


        
