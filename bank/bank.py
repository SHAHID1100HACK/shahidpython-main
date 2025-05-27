greet=input("Greeting:").strip().capitalize()
# if greet=="Hello":
#     print("$0")
if greet[0:5]=="Hello":
    print("$0")
elif "H" in greet:
    print("$20")
else:
    print("$100")
