class menu: #creating a dictionary that can later be accessed as the main file needs.
    def __init__(self,name,amount):
            self.name = name
            self.amount = amount
            self.price = 0
            self.total = 0
    
    def __Pricelist(self): #using the underscore infront of the function in order to lockdown the code in order so that nobody can change the value in the future.
        if self.name.lower() == "dry cured iberian ham":
            self.price = 177.8 #a set price that cannot be changed by anyone
        elif self.name.lower() == "wagyu steaks":
            self.price = 450
        elif self.name.lower() == "matsutake mushrooms":
            self.price = 272
        elif self.name.lower() == "Kopi Luwak Coffee":
            self.price = 306.5
        elif self.name.lower() == "moose cheese":
            self.price = 487.2
        elif self.name.lower() == "white truffles":
            self.price = 3600
        elif self.name.lower() == "blue fin tuna":
            self.price = 3603
        elif self.name.lower() == "le bonnotte potatoes":
            self.price = 270.81
        else:
            self.price = 0
    
    def total_price(self):
        self.__Pricelist() #to give the function the opportunity to the access the other function to get the price list
        self.total=self.price*self.amount #To get the total amount of the purchase
        return self.total #return it to the global lanscape

    def __str__(self):
        self.__Pricelist()
        return f"Name: {self.name}\n Amount: {self.amount}\n Price: {self.price}\n Total: {self.total}"

    def get_price(self):
        self.__Pricelist()
        return self.price
