#lancement du programme
import customtkinter as ctk
from model import CalculatorModel
from view import CalculatorView
from controller import CalculatorController

win_view=ctk.CTk()

model = CalculatorModel()
view = CalculatorView(win_view)
controller = CalculatorController(model,view)

win_view.mainloop()