def remove_tags(page, start_link=-1, end_link=-1, data = []):
    if(start_link == -1):
        start_link = page.find('>')
        end_link = page.find('<', start_link)
        if(start_link == -1):
            return []
        else:
            page = page
            data = page[start_link+1:end_link].strip().split()
            return remove_tags(page, start_link, end_link, data)
    elif(page.find('>', start_link+1)>-1):
           start_link = page.find('>',start_link+1)
           end_link = page.find('<', start_link)
           data = data + page[start_link+1:end_link].strip().split()
           start_link_diff = page.find('>', end_link)
           if(start_link_diff == -1):
            return data
           else:
            return remove_tags(page, start_link, end_link, data)
    else:
            return data