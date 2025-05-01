class validator:


    def __init__(self):

        self.name = ""
        self.email = ""

    def validname(self, name):

        return name != "" and not name.isdigit()

    def validmail(self):
       
       
        while True:
            email = input("enter your email: ")
            if "@" in email and "." in email:
                return email
            else:
                print("enter a valid email")

    def collectdata(self):

        name = input("enter your name")

        
        if self.validname(name):
            self.name = name

            self.email = self.validmail()

            print("name:", self.name)
            print("email:", self.email)
        else:
            print("invalid")