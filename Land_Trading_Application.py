
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
        
    def sellingTo(self,landQty,pricePerAcre,LandBuyer):
        
        self.amount = self.amount + (landQty*pricePerAcre)
        LandBuyer.amount = LandBuyer.amount - (landQty*pricePerAcre)
        self.acresOfLand = self.acresOfLand - landQty
        LandBuyer.acresOfLand = LandBuyer.acresOfLand  +landQty
        
    

# driver code

print("Owner 1")
owner_id = int(input("Owner Id For 1 Owner:"))
owner_name = input("Owner name:")
owner_acresOfland = int(input("How much Acres of Land u have:"))
owner_amt = int(input("Amount in Bank:"))

Owner1 = LandTrading(owner_id,owner_name,owner_acresOfland,owner_amt)


Owner2 = LandTrading()

print("Owner 2")
Owner2.set_landOwnerId(int(input("Owner Id For 2 Owner:")))
Owner2.set_landOwnerName(input("Owner name:"))
Owner2.set_acresOfLand(int(input("How much Acres of Land u have:")))
Owner2.set_amount(int(input("Amount in Bank:")))

print("*****************************")

LandSell=int(input(("How wants to sell the Land: ")))
Qty=int(input(("what amount of land u want to sell: ")))
pricePerAcre= int(input(("Price per acre of the Land: ")))

print("")
print("Before Transaction")
print("*****************************")

print("Owner1")
print("Land Avialble:", Owner1.acresOfLand)
print("Amount Avialble", Owner1.amount)
print("")
print("Owner2")
print("Land Avialble:",Owner2.get_acresOfLand())
print("Amount Avialble",Owner2.get_amount())


if(LandSell == 1):
    Owner1.sellingTo(Qty,pricePerAcre,Owner2)
    
else:
    Owner2.sellingTo(Qty,pricePerAcre,Owner1)
    

print("After the Transaction")
print("")
print("*****************************")

print("Owner1")
print("Land Avialable:", Owner1.acresOfLand)
print("Amount Avialable", Owner1.amount)
print("")
print("Owner2")
print("Land Avialable:",Owner2.get_acresOfLand())
print("Amount Avialable",Owner2.get_amount())
