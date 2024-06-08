from flask import Flask, render_template, url_for, request
from waitress import serve
import random

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
    return render_template('index.html')

@app.route("/calculate", methods = ['GET','POST'])

def calculate():

    selection = request.form.get('keysig')
    numselection = request.form.get('numchords')
    numselection1 = int(numselection)
    final_list = []

    values = [
    ["C Major", "C", "Dm", "Em", "F", "G", "Am", "Bb"],
    ["C# Major", "C# Major", "C#", "D#m", "Fm", "F#", "G#", "A#", "B"],
    ["D Major", "D", "Em", "F#m", "G", "A", "Bm", "C"],
    ["Eb Major", "Eb", "Fm", "Gm", "Ab", "Bb", "Cm", "Db"],
    ["E Major", "E", "F#m", "G#m", "A", "B", "C#m", "D"],
    ["F Major", "F", "Gm", "Am", "Bb", "C", "Dm", "Eb"],
    ["F# Major", "F#", "G#m", "A#m", "B", "C#", "D#m", "E"],
    ["G Major", "G", "Am", "Bm", "C", "D", "Em", "F"],
    ["Ab Major", "Ab", "Bbm", "Cm", "Db", "Eb", "Fm", "Gb"],
    ["A Major", "A", "Bm", "C#m", "D", "E", "F#m", "G"],
    ["Bb Major", "Bb", "Cm", "Dm", "Eb", "F", "Gm", "Ab"],
    ["B Major", "B", "C#m", "D#m", "E", "F#", "G#m", "A"],
]

    choice = selection

    length = len(values)

    for i in range(length):
        if values[i][0] == choice:
            y = int(i)

    
    final = (values[y][slice(1,8)])


    for i in range(0,numselection1):
            selection1 = final
            num = random.choice(selection1)
            chord = selection1.remove(num)
            numselection1 = numselection1 -1
            final_list.append(num)
            finale = str(final_list)
    return render_template('index.html', final_list=final_list)
      

if __name__ == "__main__":
    app.run(debug=False)