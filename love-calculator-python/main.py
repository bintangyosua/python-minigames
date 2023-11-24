# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names = name1.lower() + name2.lower()

total_T = names.count('t')
total_R = names.count('r')
total_U = names.count('u')
total_E = names.count('e')

total_true = str(total_T + total_R + total_U + total_E)

total_L = names.count('l')
total_O = names.count('o')
total_V = names.count('v')
total_E = names.count('e')

total_love = str(total_L + total_O + total_V + total_E)

value = total_true + total_love
value_int = int(value)

if (value_int < 10 or value_int > 90):
    print(f"Your score is {value}, you go together like coke and mentos.")
elif(value_int >= 40 and value_int <= 60):
    print(f"Your score is {value}, you are alright together.")
else:
    print(f"Your score is {value}.")