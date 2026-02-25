import math

class CalculatorModel:  #classe qui gere les donnees et la logique de l'application
    def __init__(self): #initialisation de la classe
        self.value=""   

    def add(self,fish): #ajouter le caractère clique au entry
        
        if self.value =="" and fish in "+÷×^": #si le entry est vide et que l'utilisateur clique sur un opérateur, ne rien faire
            self.value = ""
            return self.value
        
        elif fish.isalpha():
            return self.value

        elif self.value == "" and fish == ".": #si le entry est vide et que l'utilisateur clique sur le point, ajouter "0." au entry
            self.value += "0."
            return self.value

        elif len(self.value)>=1 and self.value[-1] in "+-×÷^." and fish in "+-×÷^.": #si le dernier caractère du entry est un opérateur et que l'utilisateur clique sur un opérateur, remplacer le dernier caractère par le nouveau
            return self.value
        
        
        elif len(self.value)>=1 and self.value[-1]==")" and fish.isdigit():
            self.value += "×" + fish
            return self.value
    
        elif self.value == "0": #si le entry contient "0" et que l'utilisateur clique sur un chiffre, remplacer "0" par le nouveau chiffre
            if fish.isdigit():
                return fish
            else :
                self.value += fish
                return self.value
        else:
            self.value +=fish
            return self.value
    
    def parenthese (self): 
        n_par_ouvertes = self.value.count("(")
        n_par_fermees = self.value.count(")")

        if n_par_ouvertes == n_par_fermees : #si le nombre de parenthese ouvertes est égal au nombre de parenthese fermées, ajouter une parenthese ouvrante
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
    
#autoriser tout les fonction de la biblioteque mathematique sauf celle avec "__" au debut
    

    def converssion_signe(self,value):
        key = value.replace ("×" , "*")
        key = key.replace ("÷" , "/")
        key = key.replace ("√" , "sqrt")
        key = key.replace ("^" , "**")
        return key

    def calculate(self):
         
        fonction_acceptable = {k: getattr(math,k) for k in dir(math) if not k.startswith("__")}

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
            self.value=str(eval(self.value,{"__builtins__":None},fonction_acceptable))
            if "." in self.value:
                resultat = str(round(float(self.value),5))
                return resultat
            else:
                return self.value
        

        except Exception as e :
            self.value="Error"
            return self.value
        
    

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
            