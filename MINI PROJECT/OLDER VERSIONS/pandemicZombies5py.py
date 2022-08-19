


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
        feedback=[]
        win=['Y' ,'Y' ,'Y' ,'Y']
        
        if self.count<3:
            
            if a==self.key[0][0]:
                feedback.append('Y')
            elif a in self.key[0]:
                feedback.append('O')
            else:
                feedback.append('N')

            if b==self.key[0][1]:
                feedback.append('Y')
            elif b in self.key[0]:
                feedback.append('O')
            else:
                feedback.append('N')

            if c==self.key[0][2]:
                feedback.append('Y')
            elif c in self.key[0]:
                feedback.append('O')
            else:
                feedback.append('N')

            if d==self.key[0][3]:
                feedback.append('Y')
            elif d in self.key[0]:
                feedback.append('O')
            else:
                feedback.append('N')

            if feedback==win:
                self.count=self.count+1
                return f'You have found the profile, go and save the world!'
            else:
                self.count=self.count+1
                return f'Not quite, here are some hints: {feedback}'
            
            
            
            
        if self.count==3:
            
            if a==self.key[0][0]:
                feedback.append('Y')
            elif a in self.key[0]:
                feedback.append('O')
            else:
                feedback.append('N')

            if b==self.key[0][1]:
                feedback.append('Y')
            elif b in self.key[0]:
                feedback.append('O')
            else:
                feedback.append('N')

            if c==self.key[0][2]:
                feedback.append('Y')
            elif c in self.key[0]:
                feedback.append('O')
            else:
                feedback.append('N')

            if d==self.key[0][3]:
                feedback.append('Y')
            elif d in self.key[0]:
                feedback.append('O')
            else:
                feedback.append('N')

            if feedback==win:
                self.count=self.count+1
                return f'You have found the profile, go and save the world!'
            else:
                self.count=self.count+1
                return f'The next pandemic has hit. Everyone will die now and you are to blame!'
   
        else:
            return f'The next pandemic has hit. Everyone will die now and you are to blame!'

                        
            
            
    def play (self):
        
        if self.count<4:
            x = list(map(int, input("Enter your vaccination code here: ").split(',')))
            a=x[0]
            b=x[1]
            c=x[2]
            d=x[3]
            return self.guess(a,b,c,d)
        else:
            return f'The next pandemic has hit. Everyone will die now and you are to blame!'
  
            
                        
                        
            
        
                        








