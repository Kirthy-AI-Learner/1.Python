class GroupFunctions():
    def listFunction():
        subfields = ['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        print("Sub-fields in AI are: ")
        for fields in subfields:
            print(fields)
    def OddEven():
        num = int(input("Enter the number: "))
        if(num%2==0):
            print(num," is Even number")
        else:
            print(num," is Odd number")
    def Eligible():
        Gender = input("Your Gender: ")
        Age = int(input("Your Age: "))
        if(Gender == 'Male' and Age >21):
            print("ELIGIBLE")
        elif(Gender == 'Female' and
             Age >18):
            print("ELIGIBLE")
        else:
            print('NOT ELIGIBLE')
    def percentage():
        subject1 = int(input("Subject1 = "))
        subject2 = int(input("Subject2 = "))
        subject3 = int(input("Subject3 = "))
        subject4 = int(input("Subject4 = "))
        subject5 = int(input("Subject5 = "))
        total = subject1+subject2+subject3+subject4+subject5
        percentage = total/5
        print('Total: ',total)
        print('Percentage: ',percentage)
    def triangle():
        Height = int(input("Height : "))
        Breadth = int(input("Breadth : "))
        print('Area formula: (Height*Breadth)/2')
        area=(Height*Breadth)/2
        print('Area of Triangle:',area)
        Height1 = int(input("Height1 : "))
        Height2 = int(input("Height2 : "))
        Breadth = int(input("Breadth : "))  
        print('Perimeter formula: Height1+Height2+Breadth')
        perimeter = Height1+Height2+Breadth
        print('Perimeter of Triangle: ',perimeter)
