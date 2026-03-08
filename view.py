#pour ajouter la fenetre
from tkinter import font

import customtkinter as ctk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class CalculatorView:
    def __init__(self,win_view):     
        self.win_view=win_view
        self.win_view.title("Calculatrice")
        self.win_view.geometry("300x380")
        self.win_view.resizable(False,False)
        self.win_view.iconbitmap("20260222_2226_image.ico")
        
        self.calculatrice_frame = ctk.CTkFrame(
            self.win_view,
            fg_color="transparent"
            )
        self.calculatrice_frame.grid(row=0,column=0,sticky="nsew")
        
        self.historique_frame = ctk.CTkFrame(
            self.win_view,
            fg_color="transparent"
            )

        self.btn_fermer = ctk.CTkButton(
            self.historique_frame,
            text="←",
            text_color= "#40E0D0",
            fg_color="transparent",
            font=("Cascadia Code",18),
            width = 30,
            height = 20,
            hover_color= "#2C2C2C"
        )
        self.btn_fermer.grid(row=0, column=3, padx=2, pady=2, sticky="w")

        self.btn_suprimer_hist = ctk.CTkButton(
            self.historique_frame,
            text="clear",
            text_color= "red",
            fg_color="transparent",
            font=("Cascadia Code",14),
            width = 30,
            height = 20,
            hover_color= "#2C2C2C"
        )
        self.btn_suprimer_hist.grid(row=2, column=2, padx=2, pady=2, sticky="se")

        self.label_historique = ctk.CTkLabel(
            self.historique_frame,
            text= "Historique",
            font= ("Cascadia Code",14),
            text_color= "#40E0D0"
        )
        self.label_historique.grid(row=0, column=0, columnspan = 2,padx=2, pady=2)


        self.historique_scrollframe = ctk.CTkScrollableFrame(
            self.historique_frame,
            width=184,
            height=290,
            fg_color="transparent"
        )
        self.historique_scrollframe.grid(row = 1, column=0, columnspan= 4, sticky="nsew", padx=2, pady=2)

        self.entrer = ctk.CTkEntry(
            self.calculatrice_frame,
            font=("Cascadia Code",14),
            justify = "right",
            width = 300,
            height= 50 ,
            border_width= 0,
            fg_color="transparent",
            state= "readonly"
            )
        self.entrer.grid(
            row =1, 
            columnspan = 4 , 
            sticky = "nsew" 
            )        
        
        
        self.histbtn = ctk.CTkButton(
            self.calculatrice_frame,
            text="🕒",
            text_color= "#40E0D0",
            font=("Cascadia Code",14),
            fg_color="transparent",
            hover_color=None,
            width = 20,
            height = 20
            )
        self.histbtn.grid(
            row = 0 , 
            column= 0 , 
            pady = 1 , 
            padx = 1 , 
            sticky = "nsew"
            )

        list_bouton = [
            "()","xʸ","√x",
            ]
        
        self.btn0_list = []
        for i,nom in enumerate(list_bouton):
            btn0 = ctk.CTkButton(
                self.calculatrice_frame,
                text=nom,
                font=("Cascadia Code",14),
                text_color= "#40E0D0",
                width = 70,
                height = 50,
                fg_color="#555555"
                )
            btn0.grid(
                row = 3 , 
                column = i , 
                pady = 1 , 
                padx = 1 , 
                sticky = "nsew"
                )
            self.btn0_list.append(btn0)

        
        list_bouton1 = [
            "÷","×","-","+"
            ]
        
        self.btn1_list = []
        for i,nom in enumerate(list_bouton1):
            btn1 = ctk.CTkButton(
                self.calculatrice_frame,
                text=nom,
                font=("Cascadia Code",14),
                text_color= "#40E0D0",
                width = 70,
                height = 50,
                fg_color="#555555"
                )          
            btn1.grid( 
                row = i +3, 
                column= 3 , 
                pady = 2 , 
                padx = 2 , 
                sticky = "nsew"
                )
            self.btn1_list.append(btn1)


        list_bouton2 = [
            "7","8","9",
            "4","5","6",
            "1","2","3",
            "+/-","0","."
            ]
        self.btn2_list = []
        for i , nom in enumerate(list_bouton2) :
            btn2 = ctk.CTkButton(
                self.calculatrice_frame,
                text=nom,
                font=("Cascadia Code",14),
                text_color= "#40E0D0",
                fg_color="#383838",
                hover_color="#4A4A4A",
                width = 70,
                height = 50
                )       
            btn2.grid(
                row = (i//3) +4 , 
                column= i % 3 , 
                padx = 1 , 
                pady = 1 , 
                sticky = "nsew"
                )
            self.btn2_list.append(btn2)


        list_bouton3 = [
            "C","Mod","⌫"
            ]
        self.btn3_list = []
        for i,nom in enumerate(list_bouton3):
            btn3 = ctk.CTkButton(
                self.calculatrice_frame,
                text=nom,
                text_color= "#40E0D0",
                font=("Cascadia Code",14),
                fg_color="transparent",
                hover_color=None,
                width = 10,
                height = 30
                )
            if i == 2 :
                btn3.grid(
                    row = 2 , 
                    column= i+1 , 
                    pady = 1 , 
                    padx = 1 , 
                    sticky = "nsew"
                    )
            else:
                btn3.grid(
                    row = 2 , 
                    column= i , 
                    pady = 1 , 
                    padx = 1 , 
                    sticky = "nsew"
                    )           
            self.btn3_list.append(btn3)
        
        self.btn3_list[0].configure(text_color="red")

        self.egal_btn = ctk.CTkButton(
            self.calculatrice_frame,
            text= "=",
            font=("Cascadia Code",14),
            text_color= "#40E0D0",
            fg_color=None,
            hover_color="#4A4A4A",
            width = 70,
            height= 50
            )
        self.egal_btn.grid(
            row = 7 ,
            column = 3,
            padx= 1 ,
            pady = 1 ,
            sticky = "nsew"
            )
        

    def set_entrer(self,value):
        self.entrer.configure(state="normal")
        self.entrer.delete(0,ctk.END)
        self.entrer.insert(0,value)
        self.entrer.configure(state="readonly")
        