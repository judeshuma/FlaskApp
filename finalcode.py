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
    values_Ab = ["Ab", "Bbm", "Cm", "Db", "Eb", "Fm", "F#"]
    values_A = ["A", "Bm", "C#m", "D", "E", "F#m", "G"]
    values_Bb = ["Bb", "Cm", "Dm", "Eb", "F", "Gm", "Ab"]
    values_B = ["B", "C#m", "D#m", "E", "F#", "G#m", "A"]
    selection = request.form.get('keysig')
    numselection = request.form.get('numchords')
    numselection1 = int(numselection)
    final_list = []
    if selection == "C Major":
        for i in range(0,numselection1):
            selection1 = values_C
            num = random.choice(selection1)
            chord = selection1.remove(num)
            numselection1 = numselection1 -1
            final_list.append(num)
            finale = str(final_list)
        return render_template('index.html', final_list=final_list)
    elif selection == "C# Major":
        for i in range(0,numselection1):
            selection1 = values_C1
            num = random.choice(selection1)
            chord = selection1.remove(num)
            numselection1 = numselection1 -1
            final_list.append(num)
            finale = str(final_list)
        return render_template('index.html', final_list=final_list)
    elif selection == "D Major":
        for i in range(0,numselection1):
            selection1 = values_D
            num = random.choice(selection1)
            chord = selection1.remove(num)
            numselection1 = numselection1 -1
            final_list.append(num)
            finale = str(final_list)
        return render_template('index.html', final_list=final_list)
    elif selection == "Eb Major":
        for i in range(0,numselection1):
            selection1 = values_Eb
            num = random.choice(selection1)
            chord = selection1.remove(num)
            numselection1 = numselection1 -1
            final_list.append(num)
            finale = str(final_list)
        return render_template('index.html', final_list=final_list)
    elif selection == "E Major":
        for i in range(0,numselection1):
            selection1 = values_E
            num = random.choice(selection1)
            chord = selection1.remove(num)
            numselection1 = numselection1 -1
            final_list.append(num)
            finale = str(final_list)
        return render_template('index.html', final_list=final_list)
    elif selection == "F Major":
        for i in range(0,numselection1):
            selection1 = values_F
            num = random.choice(selection1)
            chord = selection1.remove(num)
            numselection1 = numselection1 -1
            final_list.append(num)
            finale = str(final_list)
        return render_template('index.html', final_list=final_list)
    elif selection == "F# Major":
        for i in range(0,numselection1):
            selection1 = values_F1
            num = random.choice(selection1)
            chord = selection1.remove(num)
            numselection1 = numselection1 -1
            final_list.append(num)
            finale = str(final_list)
        return render_template('index.html', final_list=final_list)
    elif selection == "G Major":
        for i in range(0,numselection1):
            selection1 = values_G
            num = random.choice(selection1)
            chord = selection1.remove(num)
            numselection1 = numselection1 -1
            final_list.append(num)
            finale = str(final_list)
        return render_template('index.html', final_list=final_list)
    elif selection == "Ab Major":
        for i in range(0,numselection1):
            selection1 = values_Ab
            num = random.choice(selection1)
            chord = selection1.remove(num)
            numselection1 = numselection1 -1
            final_list.append(num)
            finale = str(final_list)
        return render_template('index.html', final_list=final_list)
    elif selection == "A Major":
        for i in range(0,numselection1):
            selection1 = values_A
            num = random.choice(selection1)
            chord = selection1.remove(num)
            numselection1 = numselection1 -1
            final_list.append(num)
            finale = str(final_list)
        return render_template('index.html', final_list=final_list)
    elif selection == "Bb Major":
        for i in range(0,numselection1):
            selection1 = values_Bb
            num = random.choice(selection1)
            chord = selection1.remove(num)
            numselection1 = numselection1 -1
            final_list.append(num)
            finale = str(final_list)
        return render_template('index.html', final_list=final_list)
    elif selection == "B Major":
        for i in range(0,numselection1):
            selection1 = values_B
            num = random.choice(selection1)
            chord = selection1.remove(num)
            numselection1 = numselection1 -1
            final_list.append(num)
            finale = str(final_list)
        return render_template('index.html', final_list=final_list)
    else:
        return "Sorry Please Try That Again"        



if __name__ == "__main__":
    app.run(debug=True)


#create a global variable for my keysig selection
