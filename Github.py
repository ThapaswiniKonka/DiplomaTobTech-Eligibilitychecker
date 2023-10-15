print("CHECKOUT THAT IF YOU ARE ELIGIBLE FOR B.TECH AFTER DIPLOMA OR NOT")
credits1=int(input("enter credits in 1st sem:"))
credits2=int(input("enter credits in 2nd sem:"))
credits3=int(input("enter credits in 3rd sem3:"))
credits4=int(input("enter credits in 4th sem4:"))
credits5=int(input("enter credits in 5th sem5:"))
sum=credits1+credits2+credits3+credits4+credits5
print("TOTAL CREDITS:", sum)
if sum>150:
        print("OOPS!!! YOU HAVE ENTERED WRONG VALUES")
elif sum>=130:
        print("CONGRATULATIONS!!!YOU ARE ELIGIBLE")
elif sum<=129:
          print("SORRY YOU NOT ELIGIBLE")
          print("BETTER LUCK NEXT TIME")
print("THANK YOU")
