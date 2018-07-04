try:
    a = 9
    #b = a/0                             #Zero division error
    f = open("abc.txt")                 #File not found
    for line in f:
        print(line)

# except FileNotFoundError:
#     print("File not find")
#
# except ZeroDivisionError:
#     print("Divided by zero you moron")

# except (FileNotFoundError, ZeroDivisionError):        #combined excetion
#      print("error caught")

# except Exception as e:                      #accepts all kinds of exception
#     print("Error : ",e)

except FileNotFoundError as e:
    print(e.filename)
    
# We added it here just for fun
