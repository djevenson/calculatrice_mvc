#controler (connection model<-->view)
import customtkinter as ctk
class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view



        for btn2 in self.view.btn2_list : 
            btn2.configure(command=lambda b=btn2: 
                           self.on_click(b.cget("text")))
        


        for btn1 in self.view.btn1_list :
            btn1.configure(
                command=lambda b=btn1: 
                           self.on_click(b.cget("text"))
                           )
         
            
        for btn0 in self.view.btn0_list :
            btn0.configure(
                command=lambda b=btn0: 
                           self.on_click(b.cget("text"))
                           )
            
        
        self.view.btn3_list[2].configure(
            command = lambda :
                       self.on_click("^")
                       )
       
        self.view.btn3_list[2].configure(
            command=self.delete
            )
        
        self.view.btn3_list[0].configure(
            command=self.clear
            )

        self.view.egal_btn.configure(
            command=self.calculate
            )

        self.view.btn3_list[1].configure(
            command = self.modulo
            )

        self.view.btn0_list[0].configure(
            command = self.parenthese
            )

        self.view.btn0_list[2].configure(
            command = self.racine
            )

        self.view.btn2_list[9].configure(
            command = lambda : self.on_click("(-")
            )

        self.view.btn0_list[1].configure(
            command = lambda : self.on_click("^")
            )
        
        self.view.histbtn.configure(command=self.ouvrir_historique)

        self.view.btn_fermer.configure(command=self.fermer_historique)

        self.view.btn_suprimer_hist.configure(command=self.suprimer_historique)     

    def ouvrir_historique(self):
        self.view.historique_frame.grid(row=0,column=1,sticky="nsew")
        self.view.win_view.geometry("500x380")

    def fermer_historique(self):
        self.view.historique_frame.grid_forget()
        self.view.win_view.geometry("300x380")

    def calculate(self):
        
        
        value = self.model.calculate()
        self.view.set_entrer(value)
        if self.model.history_list:
            a = self.model.history_list[-1].split(" = ")[0]
            b = self.model.history_list[-1].split(" = ")[1]
            if  a != b :
                ctk.CTkButton(
                    self.view.historique_scrollframe,
                    text=self.model.history_list[-1],
                    font=("Cascadia Code",14),
                    text_color= "#40E0D0",
                    fg_color="transparent",
                    hover_color= "#2C2C2C",
                    width=200 ,
                    command=lambda v=self.model.history_list[-1]: self.on_click2(v.split(" = ")[0])           
                ).pack(anchor="w", padx=2, pady=2)

    

    def suprimer_historique(self):
        self.model.history_list.clear()
        for widget in self.view.historique_scrollframe.winfo_children():
            widget.destroy()
        
    
    def on_click(self, value):
        value = self.model.add(value)
        self.view.set_entrer(value)

    def on_click2(self, value):
        value = self.model.remplacer(value)
        self.view.set_entrer(value)

    def delete(self):
        value = self.model.delete()
        self.view.set_entrer(value)


    def clear(self):
        value = self.model.clear()
        self.view.set_entrer(value)


    def modulo (self) :      
        value = self.model.modulo()  
        self.view.set_entrer(value)  


    def parenthese (self) :
        value = self.model.parenthese()
        self.view.set_entrer(value)

    def racine (self) :
        value = self.model.racine()
        self.view.set_entrer(value)