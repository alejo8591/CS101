def remove_tags(page):
    data = []
    start_link = page.find('<')
    while start_link != -1:
        end_link = page.find('>', start_link)
        data = data + page[start_link+1:end_link].strip().split()
        start_link = page.find('<')
    return data   