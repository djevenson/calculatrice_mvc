#controler (connection model<-->view)

class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        for btn2 in self.view.btn2_list :
            btn2.configure(command=lambda b=btn2: 
                           self.on_click(b.cget("text")))
        
        for btn1 in self.view.btn1_list :
            btn1.configure(command=lambda b=btn1: 
                           self.on_click(b.cget("text")))
            
        for btn0 in self.view.btn0_list :
            btn0.configure(command=lambda b=btn0: 
                           self.on_click(b.cget("text")))
        
        expo = self.view.btn3_list[2]
        expo.configure(command = lambda b=expo:
                       self.on_click(b.cget("text")))
        #self.view.btn3_list[2].configure(command=lambda b=btn3_list[2] :self.on_click(b.cget("text")))
            
        self.view.btn3_list[3].configure(command=self.delete)
        
        self.view.btn3_list[0].configure(command=self.clear)

        self.view.egal_btn.configure(command=self.calculate)

        self.view.btn3_list[1].configure(command = self.modulo)
    
    def calculate(self):
        value = self.model.calculate()
        self.view.set_entrer(value)

    def on_click(self,char):
        value=self.model.add(char)
        self.view.set_entrer(value)

    def delete(self):
        value = self.model.delete()
        self.view.set_entrer(value)

    def clear(self):
        value=self.model.clear()
        self.view.set_entrer(value)

    def modulo (self) :
        
        value = self.model.modulo()  
        self.view.set_entrer(value)  

    