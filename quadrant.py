horizontal_axis = input()
vertical_axis = input()
if int(horizontal_axis) > 0 and int(vertical_axis) > 0:
    print("1")
elif int(horizontal_axis) < 0 and int(vertical_axis) > 0:
    print ("2")
elif int(horizontal_axis) < 0 and int(vertical_axis) < 0:
    print("3")
else:
    print("4")
