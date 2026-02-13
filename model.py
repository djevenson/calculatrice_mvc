import math

class CalculatorModel:
    def __init__(self):
        self.value="0"   

    def add(self,fish):
        if self.value =="" and fish in "+-*/**":
            return self.value
        
        elif len(self.value)>=1 and self.value[-1] in "+-*/**" and fish in "+-*/**":
            return self.value
        
        elif len(self.value)>=1 and self.value[-1]=="0" and fish.isdigit():
            self.value = self.value[:-1] + fish
            return self.value

        elif self.value == "0":
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
    
#autoriser tout les fonction de la biblioteque mathematique sauf celle avec "__" au debut
    

    def converssion_signe(self,value):
        expr = value.replace ("×" , "*")
        expr = expr.replace ("÷" , "/")
        expr = expr.replace ("√" , "math.sqrt")
        expr = expr.replace ("^" , "**")
        return expr

    def calculate(self):
         
        fonction_acceptable = {k: getattr(math,k) for k in dir(math) if not k.startswith("__")}


        self.value = self.converssion_signe(self.value)
        if len(self.value)>=1 and self.value[-1] in "+-*/**":
            return self.value
        
        elif self.value == "":
            return self.value
        
        try:
            self.value=str(eval(self.value,{"__builtins__":None},fonction_acceptable))

        except ZeroDivisionError:
            return "Tanw kreten 😂"
            
        except:
            self.self.value="Error"
        return self.value
    

    def modulo (self) :
        if "+-÷√×^()" in self.value:
            self.value = self.value
            return self.value

        elif int(self.value) % 2 == 0 :
            self.value = "Paire"
            return self.value
        
        elif int(self.value) % 2 == 1 :
            self.value = "Impaire"
            return self.value
        """else :
            self.value = self.value
            return self.value"""