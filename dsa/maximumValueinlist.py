# class Maxi:
#     pass

        
    
#     def maximum_number(self,people):
#         limit = 0

#         for person in people:
#             if people[person] > limit:

#                 limit = people[person]
#         print(limit)
# maxi  = Maxi()
# maxi.maximum_number([12,3,4,56,7])
# class Person:
#   pass
  
  
#   def hello(name):
#     print(name)
          
# person = Person()
# person.hello("gyelsthen")


# class Person:
#     name=""
#     Age=0

#     def __init__(self,person,age):
#         self.name = person
#         self.Age = age

#     def setName(self):
#         print(self.name)
#     def setAge(self):
#         print(self.Age)
# personName = Person("gyelt",24)
# personName.setName()
# personName.setAg

class Maxi:
    # boat_capacity = 2
    # print(boat_capacity)
    def __init__(self) -> None:
        pass

    def maximum_number(self,person):

        limit = 0
        boat_capacity =2
        output =0
        if len(person)==boat_capacity:
            for i in range(len(person)):
                for j in range(len(person)):
                    if person[i]!=person[j]:
                        limit = person[i]+person[j]
                       
                        if person[i]+person[j]==limit:
                            output+=1
                            print(output)
        else:
        #    setting limit condition
            for i in range(len(person)):
                if person[i] > limit:
                    limit = person[i]
            # checking the limit is equal to less than the item in a list
            for j in range(len(person)):
                if person[j] <= limit:
                    output+=1
            maxi = 0
            for l in range(len(person)):
                maxi +=person[l]
                if maxi <= limit:
                    output+=1
               
            print(output)
                            
                                
                                


        

        

maxi = Maxi()

maxi.maximum_number([3,2,2,1])
