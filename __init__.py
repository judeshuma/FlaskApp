from flask import Flask, render_template, url_for, request
from waitress import serve
import random

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
    return render_template('index.html')

@app.route("/calculate", methods = ['GET','POST'])

def calculate():
    values_C = ["C", "Dm", "Em", "F", "G", "Am", "Bb"]
    values_C1 = ["C#", "D#m", "Fm", "F#", "G#", "A#", "B"]
    values_D = ["D", "Em", "F#m", "G", "A", "Bm", "C"]
    values_Eb = ["Eb", "Fm", "Gm", "Ab", "Bb", "Cm", "Db"]
    values_E = ["E", "F#m", "G#m", "A", "B", "C#m", "D"]
    values_F = ["F", "Gm", "Am", "Bb", "C", "Dm", "Eb"]
    values_F1 = ["F#", "G#m", "A#m", "B", "C#", "D#m", "E"]
    values_G = ["G", "Am", "Bm", "C", "D", "Em", "F"]
    values_Ab = ["Ab", "Bbm", "Cm", "Db", "Eb", "Fm", "Gb"]
    values_A = ["A", "Bm", "C#m", "D", "E", "F#m", "G"]
    values_Bb = ["Bb", "Cm", "Dm", "Eb", "F", "Gm", "Ab"]
    values_B = ["B", "C#m", "D#m", "E", "F#", "G#m", "A"]

    selection = request.form.get('keysig')
    numselection = request.form.get('numchords')
    numselection1 = int(numselection)
    final_list = []

    if selection == "C Major":
        chords = values_C
    elif selection == "C# Major":
        chords = values_C1
    elif selection == "D Major":
        chords = values_D
    elif selection == "Eb Major":
        chords = values_Eb
    elif selection == "E Major":
        chords = values_E
    elif selection == "F Major":
        chords = values_F
    elif selection == "F# Major":
        chords = values_F1
    elif selection == "G Major":
        chords = values_G
    elif selection == "Ab Major":
        chords = values_Ab
    elif selection == "A Major":
        chords = values_A
    elif selection == "Bb Major":
        chords = values_Bb
    elif selection == "B Major":
        chords = values_B

    for i in range(0,numselection1):
            selection1 = chords
            num = random.choice(selection1)
            chord = selection1.remove(num)
            numselection1 = numselection1 -1
            final_list.append(num)
            finale = str(final_list)
    return render_template('index.html', final_list=final_list)
      
if __name__ == "__main__":
    app.run(debug=False)


