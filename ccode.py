
def zc(e):
    day=int(e[-2:])
    month=e[:-3]
    AS=''
    if month == 'december':
        if day<21:
            AS='Sagittarius' 
        else: 
            AS='Capricorn'

    elif month == 'january':
        if day<21:
            AS='Capricorn' 
        else: 
            AS='Aquarius'
    elif month == 'february':
        if day<21:
            AS='Aquarius' 
        else: 
            AS='Pisces'
    elif month == 'march':
        if day<21:
            AS='Pisces'
        if day>21:
            AS='Aries'
        else:
            AS=''
    elif month == 'april':
        if day<21:
            AS='Aries' 
        else:
            AS='Taurus'
    elif month == 'may':
        if day<21:
            AS='Taurus' 
        else:
            AS='Gemini'
    elif month == 'june':
        if day<21:
            AS='Gemini' 
        else:
            AS='Cancer'
    elif month == 'july':
        if day<21:
            AS='Cancer' 
        else:
            if day>21 and month=='july': 
                AS='Leo'
    elif month == 'august':
        if day<21:
    	    AS='Leo' 
        else:
            AS='Virgo'
    elif month == 'september':
        if day<21:
    	    AS='Virgo' 
        else:
            AS='Libra' 
    elif month == 'october':
        if day<21:
    	    AS='Libra' 
        else:
            AS='Scorpio' 
    elif month == 'november':
        if day<21:
    	    AS='Scorpio' 
        else:
            AS='Sagittarius'
    return AS


        




