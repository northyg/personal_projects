# Giselle Northy - link_maker.py

import pyperclip # required for copying the string back to clipboard

while(True):
  urlString = input('Enter a URL\n').strip()
  stringList = urlString.split('/') #take this, create array, and then everything between a / is an element in the array
  stringTitle = stringList[len(stringList)-1]
  
  if(stringTitle.isdecimal()):
    stringTitle = stringList[len(stringList)-2] # if contains only numbers, get previous URI component
  
  stringTitle = stringTitle.replace('-', " ").title()
  stringTitle = stringTitle.replace('#', " - ").title()
  print ('[' + stringTitle + ']' + '(' + urlString + ')')
  pyperclip.copy('[' + stringTitle + ']' + '(' + urlString + ')') # puts new string in clipboard
