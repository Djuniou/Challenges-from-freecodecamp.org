class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []
        self.balance = 0.0
        self.spent = 0.0
        
    def __str__ (self):
        lines = []
        s=''
        title = self.name.center(30).replace(" ","*")
        for i,entry in enumerate(self.ledger):
            for c,character in enumerate(entry['description']):
                if (c < 23):
                    s += (character) 
            lines.append(s)         
            s = ''  
            lines[i] = ('{:<23}{:>7.2f}'.format(lines[i], entry['amount']))         
        output = title
        for each_line in lines:
            output += "\n" + each_line    
        output += "\nTotal: "+'{:.2f}'.format(self.balance)    
        return output
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description}) 
        self.balance += amount
        
    def withdraw(self, amount, description=""):
        if (self.check_funds(amount)):
            self.ledger.append({"amount": -1*amount, "description": description})
            self.balance -= amount
            self.spent += amount
            return True
        else:
            return False
        
    def get_balance(self):
        return self.balance     
    
    def transfer(self,amount,t_name):
        if (amount > self.balance):
            return False
        else:
            self.withdraw(amount,"Transfer to "+str(t_name.name))   
            t_name.deposit(amount,"Transfer from "+str(self.name))
            return True
        
    def check_funds(self,amount):    
        if (amount > self.balance):
            return False
        else:
            return True

def create_spend_chart(categories):
    total = 0.0
    graph = ""
    percentage = []
    last_j = 1
    max_vlen = 0 # max len of the categories name
    max_hlen = 0 # max horizontal len of '-' line
    
    max_hlen = 3*(len(categories))+1
    
    title = "Percentage spent by category"   
    graph += title+"\n"
    for i,category in enumerate(categories):
        total += category.spent    
        if (len(categories[i].name)>max_vlen):
            max_vlen = len(categories[i].name)
    for category in categories:
        percentage.append((int(100*category.spent/total)//10)*10)
        
    #Printing percentages + graph points    
    for i in range(10,-1,-1): #11 lines in this loop
        if (i==10):
            graph += '{:>4}'.format(str(i*10)+"| ")
        else:
            graph += ' {:>4}'.format(str(i*10)+"| ")
        for j,category in enumerate(categories): # Category's index is the same as percentage's index
             if (((i*10)==percentage[j]) or ((i*10)<percentage[j])):
                 graph += "o"   
             else:        
                 graph += " "    
             graph += "  "         
        graph += "\n"
    graph += "    "    
    
    #Printing separator's line 
    for i in range(max_hlen): #'-' line
        graph += "-"
    
    #Printing lines with names
    for line_num in range(max_vlen): #line has the line index(a number) until the last one(last letter)
        graph += "\n     " 
        for j,category in enumerate(categories):    
            if (line_num >= len(category.name)):
                graph += " "
            else:     
                graph += (category.name[line_num]) 
            graph += "  "     
    return graph    
