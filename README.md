# Virtual-assistant-ChatBot-for-a-website
This is a simple rule driven Virtual Assistant/Chatbot that was designed for a college website.


template hierarchy:
-templates
---new.html  (templates/new.html)
-static
---css
------new.css  (static/css/new.css)


Note : I tried using the "nltk" package directly, but it has no return method for some of the functions(converse() would only print on screen). I had to open the code of the nltk package and add a return statement to the converse() method. I've renamed this altered package as "nltkutil.py"
