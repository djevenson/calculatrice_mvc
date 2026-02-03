#pour ajouter la fenetre
import tkinter as tk
class CalculatorView:
    def __init__(self,win_view):     
        self.win_view=win_view
        self.win_view.title("MVC Calculatrice CSI")
        
        self.entry = tk.Entry(win_view,font=("Arial",18),justify="right")
        self.entry.grid(row=0,column=0,columnspan=3,padx=2,pady=2)

        self.buttons=[]

        for i in range (9):
            btn=tk.Button(win_view,text=str(i+1),width=5,height=2)
            btn.grid(
                row=i//3 + 2,
                column= i % 3,
                padx=2,
                pady=2
            )
            self.buttons.append(btn)

            zero=tk.Button(win_view,text=str(0),width=5,height=2)
            zero.grid(row=5,column=1,padx=2,pady=2)
            self.buttons.append(zero)

        
        self.clear_btn=tk.Button(win_view,text="C",width=5,height=2)
        self.clear_btn.grid(row=1,column=0,padx=2,pady=2)
        
        self.addition_btn=tk.Button(win_view,text="+",width=5,height=2)
        self.addition_btn.grid(row=1,column=3,padx=2,pady=2)
        self.buttons.append(self.addition_btn)

        self.soustraction_btn=tk.Button(win_view,text="-",width=5,height=2)
        self.soustraction_btn.grid(row=2,column=3,padx=2,pady=2)
        self.buttons.append(self.soustraction_btn)

        self.multiplication_btn=tk.Button(win_view,text="×",width=5,height=2)
        self.multiplication_btn.grid(row=3,column=3,padx=2,pady=2)
        self.buttons.append(self.multiplication_btn)

        self.division_btn=tk.Button(win_view,text="÷",width=5,height=2)
        self.division_btn.grid(row=4,column=3,padx=2,pady=2)
        self.buttons.append(self.division_btn)
        
        self.exposant_btn=tk.Button(win_view,text="^",width=5,height=2)
        self.exposant_btn.grid(row=1,column=1,padx=2,pady=2)
        self.buttons.append(self.exposant_btn)

        self.radical_btn=tk.Button(win_view,text="√",width=5,height=2)
        self.radical_btn.grid(row=1,column=2,padx=2,pady=2)
        self.buttons.append(self.radical_btn)

        self.egal_btn=tk.Button(win_view,text="=",width=14,height=2)
        self.egal_btn.grid(row=5,column=2,columnspan=3,padx=2)

    def set_entry(self,value):
        self.entry.delete(0,tk.END)
        self.entry.insert(0,value)
