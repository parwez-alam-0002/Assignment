from bs4 import BeautifulSoup

html="""
<!DOCTYPE html>
<html>
    <head>
        <title>Page Title</title>
        <title class='he'>Page Title</title>
        <title class='he'>Page Title</title>

    </head>
    <body>
        <h1>This is a Heading</h1>
        <p id='1'>This is a paragraph1.</p>
        <p id='2'>This is a paragraph2.</p>
        <p id='3'>This is a paragraph3.</p>
        <p id='4'>This is a paragraph4.</p>
        <p id='5'>This is a paragraph5.</p>
    </body>
</html>
"""

soup=BeautifulSoup(html,'html.parser')
print('heading ', soup.h1.text)
print('Title ', soup.head.text)
print(soup.find('p',id='1').text)
print(soup.find('title',class_='he').text) #it will give you the first line