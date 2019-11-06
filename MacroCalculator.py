import tkinter as tk
from tkinter import *
from tkinter import font
WIDTH = 1000
HEIGHT =690


root = tk.Tk()
root.title("Seismic Training Macro Calculator")
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg="grey")
canvas.pack()

def submitbutton():
    global advice
    advice = v3.get()

    global selection
    selection = v2.get()

    threegram = 3
    onegram = 1
    halfgram = 0.5
    fourgram = 4
    onepointonegram = 1.1
    pointsevengram = 0.7
    onepointfourgram = 1.4
    fivegram = 5
    twogram = 2
    tengram = 10
    eightgram = 6
    onepointsixgram = 1.6
    threepointfivegram = 3.5
    poundTokg = 2.205

    global selection2

    selection2 = WeightEntry.get()

    onehourlesscarbfatloss = float(selection2)/float(poundTokg)*float(threegram)
    onehourlessproteinfatloss = float(selection2)/float(poundTokg)*float(onegram)
    onehourlessfatfatloss = float(selection2)/float(poundTokg)*float(halfgram)
    onehourlesscarbgain = float(selection2)/float(poundTokg)*float(fourgram)
    onehourlessproteingain = float(selection2)/float(poundTokg)*float(onepointonegram)
    onehourlessfatgain = float(selection2)/float(poundTokg)*float(pointsevengram)

    onehourmorecarbfatloss = float(selection2)/float(poundTokg)*float(threepointfivegram)
    onehourmoreproteinfatloss = float(selection2)/float(poundTokg)*float(onepointfourgram)
    onehourmorefatfatloss = float(selection2)/float(poundTokg)*float(halfgram)
    onehourmorecarbgain = float(selection2)/float(poundTokg)*float(fivegram)
    onehourmoreproteinggain = float(selection2)/float(poundTokg)*float(onepointsixgram)
    onehourmorefatgain = float(selection2)/float(poundTokg)*float(onegram)

    athletecarbfatloss = float(selection2)/float(poundTokg)*float(eightgram)
    athleteproteinfatloss = float(selection2)/float(poundTokg)*float(twogram)
    athletefatfatloss = float(selection2)/float(poundTokg)*float(onegram)
    athletecarbgain = float(selection2)/float(poundTokg)*float(tengram)
    athleteproteingain = float(selection2)/float(poundTokg)*float(twogram)
    athletefatgain = float(selection2)/float(poundTokg)*float(onegram)


    if selection == 1 and advice == 1:
        displayLable['text'] = "\n  " + str(round(onehourlesscarbfatloss)) + " grams of carbs \n\n\n  " + str(round(onehourlessproteinfatloss)) + "grams of protein \n\n\n  " + str(round(onehourlessfatfatloss)) + "grams of fat \n"
    if selection == 1 and advice == 2:
        displayLable['text'] = "\n  " + str(round(onehourmorecarbfatloss)) + "grams of carbs \n\n\n  " + str(round(onehourmoreproteinfatloss)) + "grams of protein \n\n\n  " + str(round(onehourmorefatfatloss)) + "grams of fat \n"
    if selection == 1 and advice == 3:
        displayLable['text'] = "\n  " + str(round(athletecarbfatloss)) + "grams of carbs \n\n\n  " + str(round(athleteproteinfatloss)) + "grams of protein \n\n\n  " + str(round(athletefatfatloss)) + "grams of fat \n"
    if selection == 2 and advice == 1:
        displayLable['text'] = "\n  " + str(round(onehourlesscarbgain)) + "grams of carbs \n\n\n  " + str(round(onehourlessproteingain)) + "grams of protein \n\n\n  " + str(round(onehourlessfatgain)) + "grams of fat \n"
    if selection == 2 and advice == 2:
        displayLable['text'] = "\n  " + str(round(onehourmorecarbgain)) + "grams of carbs \n\n\n  " + str(round(onehourmoreproteinggain)) + "grams of protein \n\n\n  " + str(round(onehourmorefatgain)) + "grams of fat \n"
    if selection == 2 and advice == 3:
        displayLable['text'] = "\n  " + str(round(athletecarbgain)) + "grams of carbs \n\n\n  " + str(round(athleteproteingain)) + "grams of protein \n\n\n  " + str(round(athletefatgain)) + "grams of fat \n"



label = tk.Label(root, text="Seismic Training Macro Calculator ", fg='white', bg='grey', font=('Arial ', 17))
label.place(relx=0, rely=0.01, relwidth=1, relheight=0.07)

label2 = tk.Label(root, text="This is a macro calculator that gives you the daily range of macro nutrients and calories you need to eat in order to \n reach your fitness goal Calculations are based from NASM and ACSM Guidelines. Make sure to write what is \n prompted next to all empty entries and select an option for each group of button choices BEFORE clicking Calculate", fg='white', bg='grey', font=('Arial ', 12))
label2.place(relx=0, rely=0.08, relwidth=1, relheight=0.08)

label3 = tk.Label(root, text="Gender", bg="black", fg="white", font=('Arial', 12))
label3.place(relx=0.01, rely=0.2, relwidth=0.19, relheight=.07)

agelabel = tk.Label(root, text="Age", bg="black", fg="white", font=("Arial", 12))
agelabel.place(relx=0.01, rely=0.3, relwidth=0.19, relheight=.07)

v = IntVar()
Radiobutton(root, text="Male", variable=v, value=1, indicatoron=0).place(relx=0.2, rely=0.2, relwidth=0.05, relheight=.07)
Radiobutton(root, text="Female", variable=v, value=2, indicatoron=0).place(relx=0.25, rely=0.2, relwidth=0.05, relheight=.07)

AgeEntry = tk.Entry(root)
AgeEntry.place(relx=0.2, rely=0.3, relwidth=0.05, relheight=.07)

Weightlabel = tk.Label(root, text="Weight", font=("Arial", 12), bg="black", fg="white")
Weightlabel.place(relx=0.01, rely=0.4, relwidth=0.19, relheight=.07)

WeightEntry = tk.Entry(root)
WeightEntry.place(relx=0.2, rely=0.4, relwidth=0.05, relheight=.07)

poundlabel = tk.Label(text="lb", bg="black", fg="white")
poundlabel.place(relx=0.25, rely=0.4, relwidth=0.05, relheight=.07)


HeightLabel = tk.Label(root, bg="black", fg="white", text="Height (_',_'') Format", font=("Arial", 12))
HeightLabel.place(relx=0.01, rely=0.5, relwidth=0.19, relheight=.07)

HeightEntry = tk.Entry(root)
HeightEntry.place(relx=0.2, rely=0.5, relwidth=0.05, relheight=.07)

ActivityLevelLabel = tk.Label(root, text="How much activity do you do daily on average", bg="black", fg="white", font=("Arial", 12))
ActivityLevelLabel.place(relx=0.01, rely=0.6, relwidth=0.45, relheight=.07)


v3 = IntVar()
v3.set(0)
Radiobutton(root, text="less than 1 hour per day", variable=v3, value=1, indicatoron=0).place(relx=0.01, rely=0.67, relwidth=0.45, relheight=.05)
Radiobutton(root, text="1 hour or more per day", variable=v3, value=2,  indicatoron=0).place(relx=0.01, rely=0.72, relwidth=0.45, relheight=.05)
Radiobutton(root, text="Athlete that trains 2 hours+ a day", variable=v3, value=3,  indicatoron=0).place(relx=0.01, rely=0.77, relwidth=0.45, relheight=.05)


GoalLabel = tk.Label(root, text="Current Goal", bg="black", fg="white", font=("Arial", 12))
GoalLabel.place(relx=0.55, rely=0.2, relwidth=0.19, relheight=.07)

v2 = IntVar()
v2.set(0)
Radiobutton(root, text="Lose Fat", variable=v2, value=1, indicatoron=0).place(relx=0.74, rely=0.2, relwidth=0.07, relheight=.07)
Radiobutton(root, text="Muscle Gain", variable=v2, value=2, indicatoron=0).place(relx=0.81, rely=0.2, relwidth=0.07, relheight=.07)

SubmitButton = tk.Button(root, text="Calculate", bg="black", fg="white", command=lambda: submitbutton())
SubmitButton.place(relx=0.55, rely=0.3, relwidth=0.33, relheight=.07)

displayLable = tk.Label(root, bg="black", fg="white", font=("Arial", 20))
displayLable.place(relx=0.55, rely=0.4, relwidth=0.43, relheight=.52)

root.mainloop()