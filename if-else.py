
pizza order program
size=input("what size pizza you want s/m/l")
bill=0
if size=="S" or size=="s":
    bill +=100
    print("price for small size pizza is 100 rs")
elif size=="M" or size=="m":
    bill +=200
    print("price for medium size pizza is 200rs")
else:
    bill +=300
    print("price for large size pizza is 300rs")
add_pepperoni=input("do you wnat to add pepperoni y/n")
if add_pepperoni=="Y" or add_pepperoni=="y":
        bill+=30
        print("price for pepperoni is 30 rs")
else:
        print("price is o rs")

extra_cheese=input("do you want extra cheese y/n")
if extra_cheese=="Y" or extra_cheese=="y":
    bill+=20
    print("price for extra cheese is 20 rs")
else:
     print("price is 0")



#Love Claculator
name1=input("enter a his/her name")
name2=input("enter a his/her name")
combined_string=name1+name2
lower_case_string=combined_string.lower()
t=lower_case_string.count("t")
r=lower_case_string.count("r")
u=lower_case_string.count("u")
e=lower_case_string.count("e")
true=t+r+u+e
l=lower_case_string.count("l")
o=lower_case_string.count("o")
v=lower_case_string.count("v")
e=lower_case_string.count("e")
love=l+o+v+e
love_score=int(str(true)+str(love))
if love_score< 10 or love_score>90:
     print(f"your score is {love_score} you go together like coke and mentos")
elif love_score>=40 and love_score<=50:
     print(f"your score is {love_score} you are alright together")
else:
     print(f"your score is {love_score}")