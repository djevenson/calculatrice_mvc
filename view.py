#pour ajouter la fenetre
import customtkinter as ctk
class CalculatorView:
    def __init__(self,win_view):     
        self.win_view=win_view
        self.win_view.title("MVC Calculatrice CSI")
        
        self.entrer = ctk.CTkEntry(
            win_view,
            font=("Arial",18,"bold"),
            justify = "right",
            width = 300,
            height= 50 ,
            border_width= 0,
            fg_color="transparent"
            )
        self.entrer.grid(row =0, columnspan = 4 , sticky = "nsew" )


        list_bouton = [
            "(",")","√",
            ]
        
        self.btn0_list = []
        for i,nom in enumerate(list_bouton):
            btn0 = ctk.CTkButton(
                win_view,
                text=nom,
                fg_color="#E43414",
                hover_color="#24D1BA",
                width = 70,
                height = 50
                )
            btn0.grid(row = 2 , column = i , pady = 1 , padx = 1 , sticky = "nsew")
            self.btn0_list.append(btn0)

        
        list_bouton1 = [
            "×","÷","+","-","."
            ]
        
        self.btn1_list = []
        for i,nom in enumerate(list_bouton1):
            btn1 = ctk.CTkButton(
                win_view,
                text=nom,
                font=("Arial",18,"bold"),
                fg_color="#E43414",
                hover_color="#24D1BA",
                width = 70,
                height = 50
                )
            if i == 4 :
                btn1.grid( row = i +2 , column = 0 , padx = 1 , pady = 1 , sticky = "nsew")
            else :
                btn1.grid( row = i +2, column= 3 , pady = 2 , padx = 2 , sticky = "nsew")
            self.btn1_list.append(btn1)


        list_bouton2 = [
            "9","8","7",
            "6","5","4",
            "3","2","1",
            "0"
            ]
        self.btn2_list = []
        for i , nom in enumerate(list_bouton2) :
            btn2 = ctk.CTkButton(
                win_view,
                text=nom,
                font=("Arial",18,"bold"),
                fg_color="#571212",
                hover_color="#24D1BA",
                width = 70,
                height = 50
                )
            if i == 9 :
                btn2.grid(row = (i//3) +3 , column = (i % 3) +1 , pady= 1 , padx = 1 , sticky = "nsew")
            else :
                btn2.grid(row = (i//3) +3 , column= i % 3 , padx = 1 , pady = 1 , sticky = "nsew")
            self.btn2_list.append(btn2)


        list_bouton3 = [
            "AC","Mod","^","Del"
            ]
        self.btn3_list = []
        for i,nom in enumerate(list_bouton3):
            btn3 = ctk.CTkButton(
                win_view,
                text=nom,
                font=("Arial",18),
                fg_color="#571212",
                hover_color="#24D1BA",
                width = 70,
                height = 50
                )
            btn3.grid(row = 1 , column= i , pady = 1 , padx = 1 , sticky = "nsew")
            self.btn3_list.append(btn3)
        
        self.egal_btn = ctk.CTkButton(
            win_view,
            text= "=",
            font=("Arial",18,"bold"),
            fg_color= "#d61b1b",
            hover_color= "#24D1BA",
            width = 142,
            height= 50
            )
        self.egal_btn.grid(
            row = 6 ,
            column = 2,
            columnspan = 3 ,
            padx= 1 ,
            pady = 1 ,
            sticky = "nsew"
            )
        

    def set_entrer(self,value):
        self.entrer.delete(0,ctk.END)
        self.entrer.insert(0,value)
