side_1=int(input("enter the first side of the triangle="))
side_2=int(input("enter the second side of the triangle="))
side_3=int(input("enter the third side of the triangle="))
if (side_1+side_2>side_3)or(side_2+side_3>side_1)or(side_3+side_1>side_2):
    print("yes")
else:
    print("false")
