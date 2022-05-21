##extra 
hello="whatever"
print("hello")

##Enter your name
name=input("What is your name? " )
print("My name is " + name + "!")
print("Hello " + name + "!")


##Enter your age
age = input("What is your age? " )
print("I am " + age + " years old")


###Inquire abut  the weather
rain = 0
while(rain !='y' or rain !='n'):
    rain = input('Rain? y/n')
    break

if rain == 'y':
    print("Get an umbrella.")
    umbrella =input('Umbrella? y/n')

    if umbrella=='y':
     print("You can go.")

    else:
        print("Wait Inside.")
        
else:
    print("You can go.")
