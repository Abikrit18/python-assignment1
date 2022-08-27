#Name: Abikrit Gautam               
#Program Description: This program simulates a website that takes the input from the user. It calculates the 
#                      subtotal and total price with tax as mathematical function are used.
#                      Additionally, this program uses concatenation, slices, input function etc.


print("""
+---------------------------------------------+
|     Welcome to Abikrit's Bedsheet store!!   |
+---------------------------------------------+
|   All of our bedsheet is $5.50 per cartoon. |
|                                             |
|   We carry all of the bedsheet you          |
|   may need. Tell us about the bedsheet you  |
|   are looking for, and we'll prepare it.    |
|                                             |
|   Bring the code given at checkout to       |
|   pick up your order.                       |
+---------------------------------------------+
""")
print()
print("               ================             ")
print("---------------|CHOOSE A COLOR|---------------")
print("               ================             ")
print()
name=input("Enter Bedsheet color (uppercase letters only):")

print()
print("               ================             ")
print("---------------|  SET AMOUNT  |---------------")
print("               ================             ")
print()
cartoons=input("Enter number of cartoon per sheet:")
sheets=input("Enter number of sheet:")

print()
print("               ================             ")
print("---------------|   CHECK OUT   |---------------")
print("               ================             ")
print()

print("===================")
print("      Receipt     ")
print("===================")
print(" - ",name.upper())
print(" - ",cartoons," cartoon(s)")
print(" - ",sheets," sheet(s)")
print("===================")
subtotal=(5.5*int(cartoons)*int(sheets))
print(" Subtotal: ",subtotal)
tax=round(subtotal*0.11,2)
print(" Tax:      ", tax)
total=subtotal+tax
print(" Total:    ",total)
print("===================")
print()
print("YOUR CODE: ",name[0:2].upper()+name[-1].upper()+"-"+cartoons+"-"+sheets)
print()
print("------------------------------------------------")
print()
print("              Please come again!                ")
print()
print("------------------------------------------------")

