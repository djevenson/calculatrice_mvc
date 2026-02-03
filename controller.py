#controler (connection model<-->view)

class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        for btn in self.view.buttons:
            btn.config(command=lambda b=btn:
                       self.on_click(b["text"]))
        
        self.view.clear_btn.config(command=self.clear)

        self.view.egal_btn.config(command=self.calculate)
    
    def calculate(self):
        value = self.model.calculate()
        self.view.set_entry(value)

    def on_click(self,char):
        value=self.model.add(char)
        self.view.set_entry(value)

    def clear(self):
        value=self.model.clear()
        self.view.set_entry(value)

        

    