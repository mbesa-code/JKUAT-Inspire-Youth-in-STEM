enter_score = int(input("Enter the score: "))
if 90 <= score <= 100:
    print("grade A")
elif 80 <= score <= 89:
    print("grade B")
elif 70 <= score <= 79:
    print("grade C")
elif 60 <= score <= 69:
    print("grade D")
elif 50 <= score <= 59:
    print("grade E")
elif 0 <= score <= 49:
    print("grade F")
else:
    print("grade X") 

