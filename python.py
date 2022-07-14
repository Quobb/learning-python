weight= int(input("your weight "))
unit=input("(K)g or (L)bs")
if unit.upper() == "K":
      convert= weight / 0.45
      print ("your weight lBs" + str(convert))
else:
      convert=weight * 0.45
      print("weight in kgs: " + str(convert))