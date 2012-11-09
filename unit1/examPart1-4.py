#!/usr/bin/env python
def remove_tags(page, start_link=-1, start_link_close=-1, end_link=-1, end_link_close=-1, data = []):
    if(start_link == -1):
        start_link = page.find('<')
        start_link_close = page.find('>')
        end_link = page.find('</')
        end_link_close = page.find('>', start_link_close+1)
        if(start_link == -1):
            return data
        else:
            page = page
            data = page[start_link_close+1:end_link].strip().split()
            return remove_tags(page, start_link, start_link_close, end_link, end_link_close, data)
    elif(start_link < page.find('<', end_link_close)):
        start_link = page.find('<', end_link_close)
        start_link_close = page.find('>', start_link)
        end_link = page.find('</', start_link)
        end_link_close = page.find('>', end_link)
        data = data + (page[start_link_close+1:end_link].strip().split())
        start_link_diff = page.find('<', end_link_close)
        if(start_link_diff == -1):
            return data
        else:
            return remove_tags(page, start_link, start_link_close, end_link, end_link_close, data)
    else:
        return data