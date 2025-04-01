class agent:
    
    def __init__(self,name,age):
        print("Welcome to the game")
        self.name = name
        self.age = age
        self.health = 100
        self.alive = True
         
    def curr_health(self):
        print('Current health of',self.name , 'is',self.health)
        
    def punched(self):
         self.health -=10
         
    def shooted(self):
        self.health -= 50 
        
    def is_alive(self):
        if self.health==0:
            self.alive = False 
            
    def info(self):
        print('Name   :', self.name)
        print('Age    :', self.age)
        print('Health   :',self.health)  
        print('Alive : ', self.alive)  
        
    
p1 = agent("Sid",22)
p1.curr_health()
p1.punched()
p1.shooted()
p1.info()
print("-"*30)

p2 = agent("Somesh",25)
p2.curr_health()
p2.shooted()
p2.shooted()
p2.info()
print("-"*50)