def remove_tags(page):
    data = []
    start_link = page.find('<')
    while start_link != -1:
        end_link = page.find('>', start_link)
        page = page[:start_link]+""+page[end_link+1:]
        start_link = page.find('<')
    return page.split()  