def parse_date(date_object):
    try:
        year = date_object.tm_year
        month = date_object.tm_mon
        day = date_object.tm_mday
        
        return f"{year}/{month}/{day}"
    except:
        return date_object