# Write Python code that assigns to the 
# variable url a string that is the value 
# of the first URL that appears in a link 
# tag in the string page.

# page = contents of a web page
page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://www.xkcd.com">')
start_link = page.find('<a href=')
start_link = page.find('href=', start_link)
start_link = page.find('"', start_link)
end_link = page.find('"', (start_link+1))
url = page[(start_link+1):end_link]
