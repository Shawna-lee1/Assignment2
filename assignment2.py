class Assignment2:
    
    # Constructor: Initializes the year instance variable.
    # Accepts one parameter: year (type int).
    def __init__(self, year):
        self.year = year
        
    # Method: Calculate and print the age based on the supplied currentYear argument.
    def tellAge(self,currentYear):
        age = currentYear - self.year
        print("Your age is", age)

    # Method: Calculate and return a list of 10-year anniversaries.
    def listAnniversaries(self):
        today = 2022
        anniversaries = []
        for i in range(1, 11):
            anniversary_year = self.year + i * 10
            if anniversary_year <= today:
                anniversaries.append(i * 10)
        return anniversaries
    
    # Method: Modify the year as per the given specification and return the result as a string.
    def modifyYear(self, n):
        res = str(self.year)[:2] * n # Repeating the first two characters of the year n times
        t = self.year * n # Multiplying year by n 
        res = res + str(t)[::2] # Extracting odd index digits and combining the string
        return res
    
    # Static method: Checks if a string meets certain requirements.
    @staticmethod
    def checkGoodString(string):
        if len(string) < 9:
            return False
        if not string[0].islower():
            return False
        count_digits = sum(1 for char in string if char.isdigit())
        if count_digits != 1:
            return False
        return True

   
    # Static method: Attempts to create a TCP connection to a host and port.
    @staticmethod
    def connectTcp(host, port):
        try:
            # Create a TCP socket and attempt to connect.
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            return True  # If the connection was successful.
        except Exception as e:
            return False  # If an error occurred during connection.

#testing to see if code would output "your age is xxxx"
a = Assignment2(2000)
a.tellAge(2022)

#testing to see if code would output a list of 10 year anniversaries assuming it is 2022 [10,20]
ret = a.listAnniversaries()
print(ret)

# output [10,20,30]
a = Assignment2(1991)
ret = a.listAnniversaries()
print(ret)

#testing the String Manipulation method output: 171717181818
a = Assignment2(2000)
ret = a.modifyYear(5)
print(ret)

#testing checkGoodString method

ret = Assignment2.checkGoodString("f1obar0more")
print(ret)

ret = Assignment2.checkGoodString("foobar0more")
print(ret)

#testing connectTcp method
retval = Assignment2.connectTcp("www.google.com", 80)
if retval:
    print("Connection established correctly")
else:
    print("Some error")






