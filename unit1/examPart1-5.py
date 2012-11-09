def date_converter(language, dates):
        position_a = dates.find('/')
        position_b = dates.find('/', position_a+1)
        if(language=='english'):
            english = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May",
                       6:"June", 7:"July", 8:"August", 9:"September",10:"October",
                       11:"November", 12:"December"}
            month = english[int(dates[:position_a])]
            dates = dates[position_a+1:position_b]+" "+month+" "+dates[position_b+1:]
            return dates
        # then  "5/11/2012" should be converted to "11 May 2012". 
        # If the dictionary is in Swedish
        else:
            swedish = {1:"januari", 2:"februari", 3:"mars", 4:"april", 5:"maj",
                  6:"juni", 7:"juli", 8:"augusti", 9:"september",10:"oktober",
                  11:"november", 12:"december"}
            month = swedish[int(dates[:position_a])]
            dates = dates[position_a+1:position_b]+" "+month+" "+dates[position_b+1:]
            return dates      