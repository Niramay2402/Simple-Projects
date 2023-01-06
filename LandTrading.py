
print("Land Trading Application")

#MVC
# overloading in python

class LandTrading:
    
    
    def __init__(self, landOwnerId = 0, landOwnerName="", acresOfLand = 0, amount=0):
        self.landOwnerId = landOwnerId
        self.landOwnerName = landOwnerName
        self.acresOfLand = acresOfLand
        self.amount = amount
        
   
    def get_landOwnerId(self):
        return self.landOwnerId
           
    def set_landOwnerId(self,Id):
         self.landOwnerId = Id
         
    def get_landOwnerName(self):
        return self.landOwnerName
        
    def set_landOwnerName(self, name):
        self.landOwnerName = name
        
    def get_acresOfLand(self):
        return self.acresOfLand
        
    def set_acresOfLand(self,acres):
        self.acresOfLand = acres
         
    def get_amount(self):
        return self.amount
        
    def set_amount(self,Amt):
        self.amount = Amt
    

# driver code

Me = LandTrading()

print("Owner 1")
Me.set_landOwnerId(int(input("Owner Id For 1 Owner:")))
Me.set_landOwnerName(input("Owner name:"))
Me.set_acresOfLand(int(input("How much Acres of Land u have:")))
Me.set_amount(int(input("Amount in Bank:")))




print(Me.set_landOwnerId)

