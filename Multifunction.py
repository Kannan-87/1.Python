class multifun():
    
    def Subfields():
      lists = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
      print("Sub-fields in AI are:")
      for subfield in lists:
        print(subfield)
      return lists
    
    def OddEven():
      num = int (input("Enter a number: "))
      if ((num%2)==1):
        print (num, " is Odd number")
        type = num, " is Odd number"
      else:
        print(num, " is Even number")
        type = num, " is Even number"
      return type

    def Eligibility():
      gender = input("Your Gender : ")
      age = int(input("Your Age : "))
      if(gender=="Male"):
        if(age>20):
          print("ELIGIBLE")
          eligibility = "ELIGIBLE"
        else:
          print("NOT ELIGIBLE")
          eligibility = "NOT ELIGIBLE"
      else:
        if(age>19):
             print("ELIGIBLE")
             eligibility = "ELIGIBLE"
        else:
          print("NOT ELIGIBLE")
          eligibility = "NOT ELIGIBLE"
      return eligibility

    def Percentage(Subject1, Subject2, Subject3, Subject4, Subject5):
        print("Subject1= ",Subject1)
        print("Subject2= ",Subject2)
        print("Subject3= ",Subject3)
        print("Subject4= ",Subject4)
        print("Subject5= ",Subject5)
        Total = Subject1 + Subject2 + Subject3 + Subject4 + Subject5
        print("Total :", Total)
        Percentage = Total/5
        print("Percentage : ", Percentage)
        return Percentage
    
    def triangle():
      Height = int(input("Height: "))
      Breadth = int(input("Breadth: "))
      Area= (Height*Breadth)/2
      print("Area of Triangle: ", Area)
      return Area

    def triangle2():
       Height1 = int(input("Height1: "))
       Height2 = int(input("Height2: "))
       Breadth = int(input("Breadth: "))
       Perimeter= Height1+Height2+Breadth
       print("Perimeter of Triangle: ", Perimeter)
       return Perimeter

