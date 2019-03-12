def get_demographic_name(city, country, population=''):
    if population:
        city_country = city + ' ' + country + ' ' + population
    else:
        city_country = city + ' ' + country
    return city_country.title() 

