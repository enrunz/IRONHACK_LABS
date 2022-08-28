


#brand_dictionary={'Moderna':1,'Pfizer':2,'Astra-Zeneca':3, 'Sputnik':4, 'Janssen':5, 'CoronaVac':6, 'None':7}
import random
class vcard:
    
    def __init__(self):
        self.brands=[1,2,3,4,5,6,7]
        self.key=[]
        self.count=0
   
        
        
        
    def keyList(self):
        self.key=[random.choices(self.brands,k=4)]
        
                        
    def guess(self,a,b,c,d):
        feedback1=[]
        win=['Y' ,'Y' ,'Y' ,'Y']
        
        if self.count<3:
            
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

            if feedback1==win:
                self.count=self.count+1
                return f'You have found the profile, go and save the world!{self.count}'
            else:
                self.count=self.count+1
                return f'Not quite, here are some hints: {feedback1}{self.count}'
            
            
            
            
        if self.count==3:
            
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

            if feedback1==win:
                self.count=self.count+1
                return f'You have found the profile, go and save the world!{self.count}'
            else:
                self.count=self.count+1
                return f'The next pandemic has hit. Everyone will die now and you are to blame!'
   
        else:
            return f'The next pandemic has hit. Everyone will die now and you are to blame!'

                        
     
#     def play ():
#         return   
            
                        
                        
            
        
                        








