# Soldier

import random

class Soldier:
    
    def __init__(self, health, strength):
        #super().__init__(health, strenght) 
        self.health=health
        self.strength=strength
        
        
    def attack(self):
        return self.strength
    
    
    def receive_damage(self, damage):
        self.health= self.health - damage
        
    
    
    pass

# Viking


class Viking(Soldier):
    
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name=name
#Soldier.__init__(self, health, strength)        
#super().__init__(health, strenght)       
# This is anpther method to inherit propertirs from parent but didn't work
      
    def receive_damage(self, damage):
        self.health= self.health - damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'

        
        
    def battle_cry(self):
        return f'Odin Owns You All!'
        
    pass

#Saxon

class Saxon(Soldier):
    
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def receive_damage(self, damage):
        self.health= self.health - damage
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return f'A Saxon has died in combat'
        
        
    pass

#war

class War:
    
    def __init__(self):
        self.viking_army=[]
        self.saxon_army=[]
    
    def add_viking(self,vik):
        self.viking_army.append(vik)
    
    def add_saxon(self,sax):
        self.saxon_army.append(sax)
    
    def viking_attack(self):
        S= random.choice(self.saxon_army)
        V= random.choice(self.viking_army).strength
        outcome= S.receive_damage(V)
        if S.health <= 0:
            self.saxon_army.remove(S)
        return outcome
        
    def saxon_attack(self):
        S= random.choice(self.saxon_army).strength
        V= random.choice(self.viking_army)
        outcome= V.receive_damage(S)
        if V.health <= 0:
            self.viking_army.remove(V)
        return outcome

                
        
    def show_status(self):
        if len(self.saxon_army)==0:
            return ('Vikings have won the war of the century!')
        elif len(self.viking_army)==0:
            return ('Saxons have fought for their lives and survive another day...')
        else:
            return ('Vikings and Saxons are still in the thick of battle.')

    pass








     
        
    

    