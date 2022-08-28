


#brand_dictionary={'Moderna':1,'Pfizer':2,'Astra-Zeneca':3, 'Sputnik':4, 'Janssen':5, 'CoronaVac':6, 'None':7}
import random
class vcard:
    
    def __init__(self):
        self.brands=[1,2,3,4,5,6,7]
        self.key=[]
   
        
        
        
    def keyList(self):
        self.key=[random.choices(self.brands,k=4)]
        
                        
    def guess(self,a,b,c,d):
        feedback1=[]
        if a==self.key[0][0]:
            feedback1.append('Y')
        elif a in self.key[0]:
            feedback1.append('O')
        else:
            feedback1.append('N')
                        
        if b==self.key[0][1]:
            feedback1.append('Y')
        elif b in self.key[0]:
            feedback1.append('O')
        else:
            feedback1.append('N')
                        
        if c==self.key[0][2]:
            feedback1.append('Y')
        elif c in self.key[0]:
            feedback1.append('O')
        else:
            feedback1.append('N')
                        
        if d==self.key[0][3]:
            feedback1.append('Y')
        elif d in self.key[0]:
            feedback1.append('O')
        else:
            feedback1.append('N')
                        
                        
        return feedback1
                        
                        
     
#     def play ():
#         return   
            
                        
                        
            
        
                        








