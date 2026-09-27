ball=int(input("Ballni kiriting: "))

if ball<0 or ball>100:
    print("Bunday ball mavjud emas!")
elif ball>=0 and ball<=59:
    print("F")
elif ball>=60 and ball<=69:
    print("D")
elif ball>=70 and ball<=79:
    print("C")
elif ball>=80 and ball<=89:
    print("B")
elif ball>=90 and ball<=100:
    print("A")