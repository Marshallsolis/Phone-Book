    

#----------------------------------------------------------------------------------------------------------------------------------
class Contact:
    def __init__(self,number='') -> None:
        
        self._number=number
        self.__socialType=None
        self.__socialID=None
    
    @property
    def number(self):
        return self._number
    
    @number.setter
    def number(self,value):
        if (len(value) != 11):
            print("11 digits required!")

        else:
            print("Number succesfully added.")
            self._number=value
            

    @property
    def socialID(self):
        
        return self.__socialID
    
    @socialID.setter
    def socialID(self,value):
        if len(value)==0:
            self.__socialID=''
        else:
            self.__socialID=value
    

    @property
    def socialType(self):
        return self.__socialType
    
    @socialType.setter
    def socialType(self,value):
        if value=='':
            self.__socialType=''
        else:
            self.__socialType=value

        

            

    
    def __str__(self) -> str:

        
        return f"Number:{self.number}\nsocial:\n{self.socialType}:\t{self.socialID}"
    


#----------------------------------------------------------------------------------------------------------------------------------
class Address:
    def __init__(self,city,street,alley,building_number) -> None:
        self.city=city
        self.street=street
        self.alley=alley
        self.BN=building_number
  
            

   
    def __str__(self) -> str:
        return f"\nCity:{self.city}\tStreet:{self.street}\nAlley:{self.alley}\tBuilding Number:{self.BN}\n"
    

#-----------------------------------------------------------------------------------------------------------------------------------
class Human:
    def __init__(self,id,firstname,lastname,age,nickname,category,contact) -> None:
        self.id=id
        self.fname=firstname
        self.lname=lastname
        self.age=age
        self.nickname=nickname
        self.category=category
        self.address = None
        self.contact=Contact(contact)
        

    def __str__(self) -> str:
        return f"ID:{self.id} Firstname:{self.fname}\tLastname:{self.lname}\nAge:{self.age}\tNickname:{self.nickname}\tRelationship:{self.category}\nAddress:{self.address}\nContact Information:\n{self.contact}"

#---------------------------------------------------------------------------------------------------------------------------------
class PhoneBook:

    records=[]
    
    
    def add(self):
        id=len(PhoneBook.records)+1
        fname=input("Please enter your first name: ")
        lname=input("Please enter your last name: ")
        age=input("How old are you? ")
        nickname=input("what are you usually called by your friend? ")
        print("Category:\n1)Family\n2)Friend\n3)Colleague\n4)Other ")
        a=input("Select a number from the category list above: ")
        if a=="1":
            category="Family"
        elif a=="2":
            category="Friend"
        elif a=="3":
            category="Colleague"
        elif a=="4":
            category="Other"
        else:
            category=''

        
        contact=input("Please enter your contact number: ")

        obj=Human(id,fname,lname,age,nickname,category,contact)

        q=input("Want to add an address?(y/n)")
        if q=="y":
            city=input("Enter your Hometown name: ")
            street=input("Enter your street name: ")
            alley=input("Enter your alley name: ")
            BN=input("Enter your building number: ")
            obj.address=Address(city,street,alley,BN)
        else:
            obj.address=Address("","","","")
        
        
        q=input("Want to add a Social Address?(y/n) ")
        if q=="y":
            print("1)G-mail\t2)Telegram\t3)Instagram")
            q=input("What type of Social Address you want to add?")
            if q=="1":
                obj.contact.socialType="Gmail"
            if q=="2":
                obj.contact.socialType="Telegram"
            if q=="3":
                obj.contact.socialType="Instagram"
            id=input("Enter your Social ID: ")
            obj.contact.socialID=id
        else:
            obj.contact.socialID=''
        self.records.append(obj)
        print("Contact Saved")

    
    def update(self,name):
        for item in self.records:
            if name==item.fname:
                index=item.id
                print(self.records[index-1])
                print("1)Firstname: ")
                print("2)Lastname: ")
                print("3)Age: ")
                print("4)Nickname: ")
                print("5)Category: ")
                print("6)Contact:")
                print("7)Address:")
                print("Enter 0 to Exit")
                b=input("Enter the field number you want to change: ")
                while b!="0":
                    if b=="1":
                        new_fname=input("Enter new firstname: ")
                        if new_fname=='':
                            self.fname = self.fname
                        else:
                            PhoneBook.records[index-1].fname = new_fname
                        break
                    elif b=="2":
                        new_lname=input("Enter new lastname: ")
                        if new_lname=='':
                            self.lname=self.lname
                        else:
                            self.lname=new_lname
                        break
                    elif b=="3":
                        new_age=input("Enter new age: ")
                        if new_age=='':
                            PhoneBook.records[index-1].age=PhoneBook.records[index-1].age
                        else:
                            PhoneBook.records[index-1].age=new_age
                        break
                    elif b=="4":
                        new_nickname=input("Enter new nickname: ")
                        if new_nickname=='':
                            PhoneBook.records[index-1].nickname=PhoneBook.records[index-1].nickname
                        else:
                            PhoneBook.records[index-1].nickname=new_nickname
                        break
                    elif b=="5":
                        print("Category:\n1)Family\n2)Friend\n3)Colleague\n4)Other ")
                        q=input("Select a number from the category list above: ")
                        if new_category!='':
                            if new_category=="1":
                                new_category="Family"
                            elif new_category=="2":
                                new_category="Friend"
                            elif new_category=="3":
                                new_category="Colleague"
                            elif new_category=="4":
                                new_category="Other"

                            PhoneBook.records[index-1].category=new_category
                            break
                        else:
                            PhoneBook.records[index-1].category=PhoneBook.records[index-1].category
                            break
                    elif b=="6":
                        print("1)Number\t2)Social Address")
                        a=input("Which one you want to change?(Enter Digit) ")
                        if a=="1":
                            new_number=input("Enter new number: ")
                            if new_number=='':
                                PhoneBook.records[index-1].contact.number=PhoneBook.records[index-1].contact.number
                            else:
                                PhoneBook.records[index-1].contact.number=new_number
                            break
                        elif a=="2":
                            print("1)G-mail\t2)Telegram\t3)Instagram")
                            q=input("What type of Social Address you want to add?")
                            if q=="1":
                                new_socialtype="Gmail"
                            if q=="2":
                                new_socialtype="Telegram"
                            if q=="3":
                                new_socialtype="Instagram"
                            else:
                                new_socialtype=''
                            PhoneBook.records[index-1].contact.socialType=new_socialtype

                            new_socialID=input(f"Enter your new {new_socialtype} ID: ")
                            if new_socialtype=='':
                                PhoneBook.records[index-1].contact.socialID=PhoneBook.records[index-1].contact.socialID
                            else:
                                PhoneBook.records[index-1].contact.socialID=new_socialID
                            break
                    elif b=="7":
                        print("1)City\t2)Street\n3)Alley\t4)Building Number ")
                        a=input("Which Part do you wnat to edit?(Enter Digit) ")
                        if a=="1":
                            new_city=input("Enter new City name: ")
                            if new_city=='':
                                PhoneBook.records[index-1].address.city=PhoneBook.records[index-1].address.city
                            else:
                                PhoneBook.records[index-1].address.city=new_city
                            break
                        if a=="2":
                            new_street=input("Enter new Street name: ")
                            if new_street=='':
                                PhoneBook.records[index-1].address.street=PhoneBook.records[index-1].address.street
                            else:
                                PhoneBook.records[index-1].address=new_street
                            break
                        if a=="3":
                            new_alley=input("Enter new alley name: ")
                            if new_alley=='':
                                PhoneBook.records[index-1].address.alley=PhoneBook.records[index-1].address.alley
                            else:
                                PhoneBook.records[index-1].address.alley=new_alley
                            break
                        if a=="4":
                            new_BN=input("Enter new Building Number: ")
                            if new_BN=='':
                                PhoneBook.records[index-1].address.BN=PhoneBook.records[index-1].address.BN
                            else:
                                PhoneBook.records[index-1].address.BN=new_BN
                            break
            else:
                print("Cant find a contact with this name!")

    
    def show(self):
        if len(self.records)== 0:
            print("no contact")
        else:
            for r in self.records:
                print(r)
                print("-"*40)

    
    def delete(self,name):
        if len(self.records)!=0:
            for r in self.records:
                if name ==r.fname:
                    index = r.id
                    del self.records[index-1]
                    break
                else:
                    print(f"There is no contact as {name}")
                    break
        else:
            print("There is no contact")




                        

                







                

            


        


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# print(PhoneBook.records)
def main_menu():
    print("-" * 40)
    print("| ", "1 ) Add a new contact")
    print("| ", "2 ) show contacts")
    print("| ", "3 ) edit contact")
    print("| ", "4 ) delete contact")
    print("| ", "* ) Exit")
    print("-" * 40)

phonebook=PhoneBook()
current=0
while current != '*':
    main_menu()
    current=input()
    if current=='1':
        print("\033[1mCreate a new Contact:\033[0m")
        phonebook.add()
    elif current=='2':
        print("\033[1mShow all Contacts:\033[0m")
        phonebook.show()
    elif current=='3':
        print("\033[1mUpdate Existing Contacts:\033[0m")
        name=input("Enter the firstname of the contact you want to edit: ")
        phonebook.update(name)
    elif current=='4':
        print("\033[1mDelete Contacts\033[0m")
        name=input("Enter the firstname of the contact you want to delete: ")
        phonebook.delete(name)
        print("Deleted Successfuly")
    



        

