#!/usr/bin/env python
def remove_tags(page):
    data=[]
    start_link = page.find('<')
    start_link_close = page.find('>')
    end_link = page.find('</')
    end_link_close = page.find('>', start_link_close+1)
    if(page[end_link_close+1]=='<'):
    # eliminando espacios en blanco innecesarios
      data = str(page[start_link_close+1:end_link].strip())
      return data.split()
