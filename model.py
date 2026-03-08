import math

class CalculatorModel:  
    def __init__(self): 
        self.value=""
        self.true_value =self.value
        self.history_list = []   



    def add(self,fish): 
        
        if self.value =="" and fish in "+÷×^": 
            return self.value
        
        elif fish.isalpha():
            return self.value

        elif self.value == "" and fish == ".": 
            self.value += "0."
            return self.value

        elif len(self.value)>=1 and self.value[-1] in "+-×÷^." and fish in "+-×÷^.": 
            return self.value
            
        elif len(self.value)>=1 and self.value[-1]==")" and fish.isdigit():
            self.value += "×" + fish
            return self.value
    
        elif self.value == "0": 
            if fish.isdigit():
                return fish
            else :
                self.value += fish
                return self.value
        else:
            self.value +=fish
            return self.value
    
    def plus_moins(self):
        if self.value == "":
            self.value += "-"
            return self.value
        elif self.value[0] == "-":
            self.value = self.value[1:]
            return self.value
        else:
            self.value = "-" + self.value
            return self.value

    def parenthese (self): 
        n_par_ouvertes = self.value.count("(")
        n_par_fermees = self.value.count(")")

        if n_par_ouvertes == n_par_fermees : 
            if len(self.value)>=1 and self.value[-1] in "0123456789)":
                self.value += "×("
                return self.value           
            else:
                self.value += "("
                return self.value              

        elif len(self.value)>=1 and self.value[-1] in "+÷×^(":
            self.value += "("
            return self.value
         
        elif n_par_ouvertes > n_par_fermees :
            self.value += ")"
            return self.value
        
        elif n_par_ouvertes < n_par_fermees :
            self.value += "("
            return self.value       
        
        elif self.value == "" :
            self.value += "("
            return self.value



    def remplacer (self,fish):
        self.value = fish
        return self.value



    def racine (self) :
        if self.value == "":
            self.value += "√("
            return self.value
        elif self.value[-1] in "+÷×^(":
            self.value += "√("
            return self.value
        
        elif self.value == "-":
            self.value += "√("
            return self.value   
        
        else :
            self.value += "×√("
            return self.value



    def delete(self):
        if self.value =="Error" or self.value == "Paire" or self.value == "Impaire":
            self.value=""
            return self.value
        self.value = self.value[:-1]
        return self.value
    


    def clear(self):
        self.value=""
        return self.value
    


    def converssion_signe(self,value):
        key = value.replace ("×" , "*")
        key = key.replace ("÷" , "/")
        key = key.replace ("√" , "math.sqrt")
        key = key.replace ("^" , "**")
        return key
    


    def calculate(self):

        true_value = self.value
        self.value = self.converssion_signe(self.value)

        if len(self.value)>=1 and self.value[-1] in "×÷^√-+":
            return self.value

        elif self.value.count("(") != self.value.count(")") :
            return self.value
            
        elif self.value == "Paire" or self.value == "Impaire" :
            self.value = ""
            return self.value
        elif self.value == "":
            return self.value
        
        try:
            resultat = str(eval(self.value))
            
            self.history_list.append(f"{true_value} = {resultat}")
            self.value = resultat
            return self.value    
            
        except Exception as e :
            self.value="Error"
            return self.value
    


    def get_history(self):
        return self.history_list



    def modulo (self) :
        try:
            if int(self.value) % 2 == 0 :
                self.value = "Paire"
                return self.value
            
            elif int(self.value) % 2 == 1 :
                self.value = "Impaire"
                return self.value
            elif self.value == "" :
                self.value = self.value
                return self.value
        
        except Exception:
            self.value = "Error"
            return self.value
            