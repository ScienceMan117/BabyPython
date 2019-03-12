from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    if country_name == 'Yemen, Rep.':
        return 'ye'
    elif country_name == 'Venezuela, Bolivarian Republic of':
        return 've'
    elif country_name == 'Boliva, Plurinational State of':
        return 'bo'
    elif country_name == 'Congo':
        return 'cg'
    elif country_name == 'Congo, Democratic Republic of the':
        return 'cd'
    elif country_name == 'Tanzania, United Republic of':
        return 'tz'
    elif country_name == 'Uganda':
        return 'tz'
    elif country_name == 'Libyan, Arab Jamahiriya':
        return 'ly'
    elif country_name == 'Eypgt':
        return 'eg'
    elif country_name == 'Antartica':
        return 'aq'
    elif country_name == "Korea, Democractic People's Republic of":
        return 'kp'
    elif country_name == 'Korea, Republic of':
        return 'kr'
        
    # If the country wasn't found, return None.
    return None
    
print(get_country_code('Andorra'))
print(get_country_code('United Arab Emirates'))
print(get_country_code('Afghanistan'))

