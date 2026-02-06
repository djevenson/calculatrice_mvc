class CalculatorModel:
    def __init__(self):
        self.value=""   

    def add(self,fish):
        if self.value =="" and fish in "+-*/**":
            return self.value
        
        elif len(self.value)>=1 and self.value[-1] in "+-*/**" and fish in "+-*/**":
            return self.value
        
        elif len(self.value)>=1 and self.value[-1]=="0" and fish.isdigit():
            self.value = self.value[:-1] + fish
            return self.value

        elif self.value == "0" :
            if fish.isdigit():
                return fish
            else :
                self.value += fish
                return self.value


        self.value +=fish
        return self.value
    
    def delete(self):
        self.value = self.value[:-1]
        return self.value
    
    def clear(self):
        self.value=""
        return self.value
    
    def calculate(self):
        if len(self.value)>=1 and self.value[-1] in "+-*/**":
            return self.value
        
        elif self.value == "":
            return self.value
        
        try:
            self.value=str(eval(self.value))

        except ZeroDivisionError:
            return "Tanw kreten 😂"
            
        except:
            self.self.value="Error"
        return self.value
