def date_converter(language, dates):
        english = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May",
                   6:"June", 7:"July", 8:"August", 9:"September",10:"October",
                   11:"November", 12:"December"}
        
        swedish = {1:"januari", 2:"februari", 3:"mars", 4:"april", 5:"maj",
                   6:"juni", 7:"juli", 8:"augusti", 9:"september",10:"oktober",
                   11:"november", 12:"december"}
        position_a = dates.find('/')
        position_b = dates.find('/', position_a+1)
        month = language[int(dates[:position_a])]
        dates = dates[position_a+1:position_b]+" "+month+" "+dates[position_b+1:]
        return dates 