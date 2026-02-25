#controler (connection model<-->view)

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
            
        self.view.win_view.bind(
            "<Key>",
            self.key_press
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
    
    def key_press(self, event ):

        key = event.char

        # Chiffres
        if key.isdigit():
            self.on_click(key)

        # Opérateurs
        elif key in "+-":
            self.on_click(key)

        elif key == "*":
            self.on_click("×")

        elif key == "/":
            self.on_click("÷")

        elif key == "^":
            self.on_click("^")

        elif key == ".":
            self.on_click(".")

        # Parenthèses
        elif key in "()":
            self.parenthese()

        elif key in "=":
            self.calculate()

        # Racine (touche r)
        elif key.lower() == "r":
            self.racine()

        # Entrée = calcul
        elif event.keysym == "Return" :
            self.calculate()

        # Backspace
        elif event.keysym == "BackSpace":
            self.delete()

        # Suppr (clear)
        elif event.keysym == "Delete":
            self.clear()


    def calculate(self):
        value = self.model.calculate()
        self.view.set_entrer(value)


    def on_click(self,char):
        value = self.model.add(char)
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
        pass
        value = self.model.parenthese()
        self.view.set_entrer(value)

    def racine (self) :
        pass
        value = self.model.racine()
        self.view.set_entrer(value)


        


    