class CalculatorModel:
    def __init__(self):
        self.value=""   

    def add(self,fish):
        self.value +=fish
        return self.value
    
    def clear(self):
        self.value=""
        return self.value
    
    def calculate(self):
        try:
            self.value=str(eval(self.value))
            
        except:
            self.self.value="Error"
        return self.value
