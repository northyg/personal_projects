Giselle Northy - link_maker.py
 
Tired of having to manually build out Document hyperlinks with Markdown in Zendesk?! I was, too!
  Now all you need is a URL and the magic of link_maker!
  Watch in amazement as this link copied via cmd + c https://docs.newrelic.com/docs/apm becomes...Apm 

But wait, there's more! It automatically copies the modified string to your clipboard!!
  Now simply repaste with cmd + v and you have [Apm] (https://docs.newrelic.com/docs/apm)
  Wow! Truly amazing.
 
Disclaimer: Ok it really just runs some formatting magic on a string, takes the words after the final
forward slash, and makes them into the link title.

Getting it to work:
  Used Python3 - Runs in the Terminal; Control + c to quit
  Had issues getting pyperclip installed because Python was defaulting to Python 2 (confusing mess)
  
So I ran through the steps here - Skip down to "What we should do"
  https://opensource.com/article/19/5/python-3-default-mac
  Not sure if that's the best way, but that finally got it to work

Then pip install --user pyperclip
  https://pypi.org/project/pyperclip/
  
If you can't get pyperclip to work, you can always comment it out and use the console print instead.

Feel free to submit improvements!
