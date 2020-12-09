/*basic print and concatanation*/

print('purple!')
print('and pink toes!')

toeColour = input('What colour would you like your toes? ')
print(toeColour + ' toes please')

giMoney = input('How much money have you spent in Genshin Impact? ')
print(giMoney ,400, ':(')

favFood = input("What is pootie's favourite food? ")
print(favFood + " jk it's me")

shopping_list = ['apples', 'oranges', 'pears', 'condoms']

example = [675.6, 'we like toes', 453, True]

gamesForMeAndPootie = ['wow', 'league', 'genshin impact']

print(shopping_list[2])
print(example[1])
print(gamesForMeAndPootie[2])

/*if elif else*/

food = input("What's your favourite food? ")

if food == '':
    print ('Answer me bruh')
else:
    print ('Cool!')

food = input('Please state your favourite food: ')
if food == '':
    print('Answer me bruh??')
elif food == 'bueno' or 'rocher' or 'fingers':
    print('Same here bud!')
else:
    print("That explains why you're fat smh.")

/*if elif else*/

acnh = input("Who is your favourite ACNH character? ")
if acnh == '':
    print('Uhh yikes, rude much')
else:
    print("Well uhhHh that's a. Choice :D")

/*if elif if with formulas ad conversion*/

feet = float(input("What is your height in meters? "))
feetFormula = feet ** 0.3048

print('Your height in meters: ', feetFormula)

meters = float(input('What about your height in feet? '))
metersFormula = meters ** 3.2808

print('Your height in feet: ', metersFormula)

question = input('Would you like your height in meters or feet? ')
if question == 'feet':
    print('Your height in feet: ', feetFormula)
elif question == 'meters':
    print('Your height in meters: ', metersFormula)
else:
    print('Answer me you dipshit!')

/*if elif else*/

question = input('Would you like your height in meters or feet? ')

if question == 'feet':
    heightF = float(input('What is your height in meters? '))
    f2M = heightF ** 3.281
    print(f2M,'feet')

elif question == 'meters':
    heightM = float(input('What is your height in feet? '))
    m2F = heightM / 3.281
    print(m2F, 'meters')

else:
    print('Answer me you dipshit!')
