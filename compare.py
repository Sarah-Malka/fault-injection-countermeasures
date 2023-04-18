import sys
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots


folder_name = sys.argv[1]
title = "Compare Emulator simulation on the code with and without protection and the differences as well"
is_total = False
if len(sys.argv) > 2:
    title = sys.argv[2]
    if len(sys.argv) > 3:
        is_total = True
attacks = ['opt', 'time']
for i in range(1, 25):
    attacks.append(str(i))

results_game = [['O1', 'O2', 'O3', 'O4'],[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
results_countermeasure = [['O1', 'O2', 'O3', 'O4'],[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
diff = [['O1', 'O2', 'O3', 'O4'],[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
total_game = [['O1', 'O2', 'O3', 'O4'],[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
total_countermeasure = [['O1', 'O2', 'O3', 'O4'],[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

for i in range(1, 5):
    os.system(f"python run_code.py {folder_name} {i} > output.txt") 
    f = open("output.txt", "r")
    j = 2
    for l in f:
        if "Total" in l:
            faults = l.split(" ")[1]
            if faults.isdigit():
                results_game[j].append(faults)
        if "Injected" in l:
            total = l.split(" ")[1]
            if total.isdigit():
                total_game[j].append(total)
            j += 1

for i in range(1, 5):
    os.system(f"python run_code.py {folder_name}_countermeasure {i} > output.txt") 
    f = open("output.txt", "r")
    j = 2
    for l in f:
        if "Total" in l:
            faults = l.split(" ")[1]
            if faults.isdigit():
                results_countermeasure[j].append(faults)
        if "Injected" in l:
            total = l.split(" ")[1]
            if total.isdigit():
                total_countermeasure[j].append(total)
            j += 1

for row in range(2, 26):
    for col in range(4):
        res = int(results_countermeasure[row][col]) - int(results_game[row][col])
        if res > 0:
            res = "+" + str(res)
        diff[row].append(res)
if is_total:
    for row in range(2, 26):
        for col in range(4):
            results_countermeasure[row][col] = str(results_countermeasure[row][col]) + '--' + str(total_countermeasure[row][col])
            results_game[row][col] = str(results_game[row][col]) + '--' + str(total_game[row][col])

fig = make_subplots(
    rows=3, cols=1,
    shared_xaxes=True,
    vertical_spacing=0.03,
    specs=[[{"type": "table"}],
           [{"type": "table"}],
           [{"type": "table"}]]
)

colors = ['darkslategray', 'darkslategray']
for i in range(2, 26):
    colors.append(['green' if int(x) < 0 else "red" if int(x) > 0 else "gray" for x in diff[i]])

fig.add_trace(go.Table(header=dict(values=attacks), cells=dict(values=results_game)), row=1, col=1)
fig.add_trace(go.Table(header=dict(values=attacks), cells=dict(values=results_countermeasure)), row=2, col=1)
fig.add_trace(go.Table(header=dict(values=attacks), cells=dict(values=diff, font_color=colors)), row=3, col=1)

fig.update_layout(
    height=600,
    showlegend=False,
    title_text=title,
)

fig.show()