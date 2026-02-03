#lancement du programme
import tkinter as tk
from model import CalculatorModel
from view import CalculatorView
from controller import CalculatorController

win_view=tk.Tk()

model = CalculatorModel()
view = CalculatorView(win_view)
controller = CalculatorController(model,view)

win_view.mainloop()
