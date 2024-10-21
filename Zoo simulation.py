
"""
write python code for "deveop a simulation system for zoo. 
the system should manage different types of animals and their interactions in park.
basic Objaects : animal class for all types of animals . common attrubutes name, age,enerygy level. basic methods eat , sleep , make sounds .
subcalsses Herbivores and Carnivores will inherit from anial , with specific chat´ractistics and behaviours. 
visitor class for visitors in park with name and age.Create animals species like lion, giraffe, elephants with unque charachteristics and behaviour . 
interaction between animal like hunting , playing. .
Allow visitors to feed certain animal species to affect therie energy levels .
simultae a day in zoo where animals follow their natural routine and interact with visitors
"""

import random
import sys

class Animal():
    def __init__(self,species,name,age,energy_level):
        self.species=species
        self.name=name
        self.age=age
        self.energy_level=energy_level

    def energy(self):
        if self.energy_level <=10:
            print(f"'{self.name}' the {self.species} 's energy is low." )
           
        if self.energy_level >100:
            self.energy_level =100

    def eat(self):
        self.energy_level +=20
        self.energy()
        return (f"'{self.name}' the {self.species} is eating. Energy level: {self.energy_level} ")

    def sleep(self):
        self.energy_level +=50
        self.energy()
        return (f"{self.name} the {self.species} is sleeping and regaining energy ")

    def make_sound(self):
        self.energy_level -=5
        return(f"'{self.name}' the {self.species} is making sound.")




class Herbivores(Animal):
    def __init__(self,species,name,age,energy_level):
        super().__init__(species,name,age,energy_level)
    
    def make_sound(self):
       if self.species.lower()=='elephant':
           self.energy_level -=5
           return(f"'{self.name}' the {self.species} trumpets.")

       else:
           return super().make_sound()
       


    
class Carnivores(Animal):
    def __init__(self,species,name,age,energy_level):
        super().__init__(species,name,age,energy_level) 


    def make_sound(self):
       if self.species.lower()=='lion':
           self.energy_level -=5
       return(f"'{self.name}' the {self.species} roars.")
    
    def hunt(self,animal):
         self.animal=animal
         return (f"'{self.name}' the {self.species} is hunting '{self.animal.name}' the {self.animal.species} ")
        


class Visitor():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        #self.animal=animal
        

    def feed(self,animal):
        self.animal=animal
    #check if animal energy level is low then feed
        if self.animal.energy_level <= 40:
            print(f"{self.animal.name}'s Energy level is low ({self.animal.energy_level}) , visitor '{self.name}'is feeding {self.animal.name} ({self.animal.species})")
            self.animal.energy_level += 20
        else:
            return

    


#main program section
class Zoo:
    def __init__(self): 
        self.animallist = [] 
        self.carni=[]
        self.herbi=[]
        self.visitorlist=[]

 # get all animal instances  and add them to list to further process
    def add_animal(self,animal): 
        self.animal=animal
        self.animallist.append(self.animal)
        if isinstance(self.animal,Carnivores):
            self.carni.append(self.animal)
        if isinstance(self.animal,Herbivores):
            self.herbi.append(self.animal)



    # get all visitor instances fromand add them to list to further process
    def add_visitor(self,visitor): 
        self.visitor=visitor
        self.visitorlist.append(self.visitor)
        #print (self.visitor.name)

    #count of animal present per species
    def species_count(self,animal):
        self.animal=animal
        s_count =0
        
        for a in self.animallist:
            if a.species==self.animal.species:
                s_count +=1
        return s_count
    
    #do not repeat ramdom animal generation during playtime
    def no_repeat(self,a1,a2):
        self.a1=a1
        self.a2=a2
        if self.a1.name==self.a2.name:
            self.a2=random.choice(self.animallist)
            self.no_repeat(self.a1,self.a2)
            return a2
                
        else:
            return a2
 
    def day(self):
        print("\n Welcome at Zoo ! Day begins\n")

        print("Mornig time : Animals Making sounds:\n")
        for a in self.animallist:
            print(a.make_sound())
        
        print("\nAnimals having their meal:\n")
        for a in self.animallist:
             print(a.eat())


        #play time, choose any 2 random animals and define if playing or hunting
        print("\n Out time : \n")


        a1=random.choice(self.animallist)
        a2=random.choice(self.animallist)
        #print ("a1 , a2 ",a1.name , a2.name)

        if a1.name==a2.name:
           a2=self.no_repeat(a1,a2)
           #a2=random.choice(self.animallist)


        herbi_out_count=self.herbi.count(a1) + self.herbi.count(a2)
        #carniisout=self.carni.count(a1) + self.carni.count(a2)


        if herbi_out_count ==2:
        
            print(f"'{a1.name} 'the {a1.species} and '{a2.name}' the {a2.species} are out and playing")
            a1.energy_level -=40
            a2.energy_level -=40


        elif herbi_out_count ==1: 
            print(f"'{a1.name}' the {a1.species} and '{a2.name}' the {a2.species} are out")

          #check if animals in this herbivores species are more than one  then allow hunt
            species=[]
            species=[h.species for h in self.herbi if h==a1 ]
            # for h in self.herbi:
            #     if h==a1 :
            #        species= h.species
            #        break
            #print("species",h.species , type(h.species))
            #print("species" ,species)
            if species==[]:
                carniout=a1
                herbiout=a2
            else:
                carniout=a2
                herbiout=a1
                

            for c in self.carni:
                if c==carniout:
                    count=self.species_count(herbiout)

                    if count>1:
                        print(c.hunt(herbiout))
                    else:
                        print(f"'{herbiout.name}' the {herbiout.species} escapped from '{c.name}' the {c.species}")
                        a2.energy_level -=40
                    break

                    
        else:
            print(f"'{a1.name}' the {a1.species} and '{a2.name}' the {a2.species} are out and playing")
            a1.energy_level -=40
            a2.energy_level -=40

        print("\n")
        for a in self.animallist:
            if a.energy_level<=50:
                visitorany = random.choice(self.visitorlist)
                visitorany.feed(a)
        
        #evening time animals go to sleep
        print("\nEvening time : \n ")
        for a in self.animallist:
          print(a.sleep())



zoo=Zoo()


carnivores1=Carnivores('Lion','Simba',4,10)
carnivores2=Carnivores('Lion','Bambi',5,20)
carnivores3=Carnivores('Lion','Mufasa',10,60)

herbivores1=Herbivores('Elephant','Happy',10,30)
herbivores2=Herbivores('Elephant','Jumbo',10,30)
herbivores3=Herbivores('Elephant','Larry',10,30)
herbivores4=Herbivores('Giraffe','Gracy',10,50)
# herbivores5=Herbivores('Giraffe','Gorge',8,60)
# herbivores6=Herbivores('Giraffe','Games',18,80)


#call function to create list of all animals to process
zoo.add_animal(carnivores1)
zoo.add_animal(carnivores2)
zoo.add_animal(carnivores3)

zoo.add_animal(herbivores1)
zoo.add_animal(herbivores2)
zoo.add_animal(herbivores3)
zoo.add_animal(herbivores4)
# zoo.add_animal(herbivores5)
# zoo.add_animal(herbivores6)




#call function to create list of all visitors to process
visitor1=Visitor('Anna',20)
visitor2=Visitor('Bob',40)
visitor3=Visitor('Mark',35)
visitor4=Visitor('Sara',10)
visitor5=Visitor('Sam',15)
  
zoo.add_visitor(visitor1)
zoo.add_visitor(visitor2)
zoo.add_visitor(visitor3)
zoo.add_visitor(visitor4)
zoo.add_visitor(visitor5)

zoo.day()

#print(carnivores1.make_sound())
      