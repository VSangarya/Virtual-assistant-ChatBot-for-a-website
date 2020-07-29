from flask import Flask, render_template, request
from chatbot import Chat,reflections,pairs

app = Flask(__name__, template_folder='templates')

count=0
g1 = []

@app.route('/', methods=['GET', 'POST'])
def samplefunction():
  global count
  global g2

  greetIn=[0]
  greetOut=[0]
  while(1):
    if request.method == 'GET':
         return render_template('new.html')
    if request.method == 'POST':
        for i in range(1):
          human1 = request.form['human']
          greetIn[i]=human1
          greetOut[i] = c(greetIn[i])
          err="Bot : Please ask again \n"
          greetIn[i]='User : '+greetIn[i] +'\n'
          g1.append(greetIn[i])
          g1.append(greetOut[i])
          count = count + 1
          print(count)
          text = ' '.join(map(str, g1))
          text = text.split('\n')
          if greetOut[i]==err:
               print("User has given a new response - ",human1)
               return render_template('new.html', bot1=text)
    return render_template('new.html',bot1=text)

def c(x):
  chat=Chat(pairs,reflections)
  return chat.converse(x)

if __name__ == '__main__':
    app. run(host='127.0.5.145', port=5000, debug=True)