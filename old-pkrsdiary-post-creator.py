def start():
    print('What to add first? [t] - textbox, [i] - image')
    answer = input()
    if answer == 't':
        addtextbox()
    elif answer == 'i':
        addimage()
    else:
        print('Dobra weź spierdalaj co')
        start()

def ending():
    print('Anything else? Options: [n] - No, [t] - add a textbox, [i] - add an image')
    answer = input()
    if answer.lower() == 'n':
        saveandquit()
    elif answer.lower() == 't':
        addtextbox()
    elif answer.lower() == 'i':
        addimage()
    #elif answer.lower() == 'e': left to add an edit option later maybe
    else:
        print('Dobra weź spierdalaj co')
        ending()

def addtextbox():
    print('Input text, use \'<br><br>\' to indicate a new paragraph.')
    text = input()
    for i in range(10):
        if 'txt'+str(i) not in htmldict.keys():
            htmldict['txt'+str(i)] = f'<p id="textbox">\n{text}<br><br>\n</p>'
            break
    cssdict['p'] = '''p {
    	text-align:justify;
    	max-width:600px;
    }

    #textbox {
    	margin:auto
    }'''
    ending()

def addimage():
    print('Image filename:')
    imagefilename = input()
    print('Image height:')
    imageheight = input()
    for i in range(10):
        if 'img'+str(i) not in htmldict.keys():
            htmldict['img'+str(i)] = f'<img src="{imagefilename}" height="{imageheight}"><br>'
            break
    cssdict['img'] = '''img {
      display: block;
      margin-left: auto;
      margin-right: auto;
      width: auto;
    }'''
    ending()

def saveandquit():
    with open(f'{title}.html', 'w', encoding='utf-8') as htmlfile:
        htmldict['ending'] = '</body>\n</html>'
        for h in htmldict.values():
            htmlfile.write(f'{h}\n')
        htmlfile.close()
    with open(f'{title}.css', 'w', encoding='utf-8') as cssfile:
        for c in cssdict.values():
            cssfile.write(f'{c}\n\n')
        cssfile.close()
    quit()

#adding everything that's identical across all posts, with just the title and
#the date as variables before actually adding content
htmldict = {}
cssdict = {}
htmldict['intro'] = '''<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">'''
cssdict['#link-glowna'] = '''#link-glowna {
	font-size:40px;
	font-weight:bold;
	text-align:center;
}'''
cssdict['a'] = '''a:link, a:visited {
  color: white;
  text-decoration:none;
}'''
cssdict['body'] = '''body {
  background-color: black;
  color: white;
}'''
cssdict['h1'] = '''h1 {
	text-align:center;
}'''

print('HTML title:')
title = input()

htmldict['title'] = f'<title>{title}</title>'
htmldict['css-link'] = f'<link rel="stylesheet" type="text/css" href="{title}.css">'

htmldict['main-page-button'] = '''<div style="text-align:center">
	<link><a href="../index.html" id="link-glowna">Poker's Diary</a></link>
</div>'''
htmldict[r'/head'] = '</head>'
htmldict['body'] = '<body>'

print('Date/Hour:')
date = input()
htmldict['date'] = f'<h1>{date}</h1>'

start()
