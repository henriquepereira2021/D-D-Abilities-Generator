from random import randrange
statA1 = int(randrange(1,7))
statA2 = int(randrange(1,7))
statA3 = int(randrange(1,7))
statA4 = int(randrange(1,7))

statAA1 = statA2 + statA3 + statA4
statAA2 = statA1 + statA3 + statA4
statAA3 = statA1 + statA2 + statA4
statAA4 = statA1 + statA2 + statA3

if statA1 <= statA2 and statA1 <= statA3 and statA1 <= statA4:
    statA = int(statAA1)
if statA2 <= statA1 and statA2 <= statA3 and statA2 <= statA4:
    statA = int(statAA2)
if statA3 <= statA1 and statA3 <= statA2 and statA3 <= statA4:
    statA = int(statAA3)
if statA4 <= statA1 and statA4 <= statA2 and statA4 <= statA3:
    statA = int(statAA4)

statAmod = round((statA - 10.5)/2)

if statAmod >= 0:
    statAmodsign = "+"
else:
    statAmodsign = ""


statB1 = int(randrange(1,7))
statB2 = int(randrange(1,7))
statB3 = int(randrange(1,7))
statB4 = int(randrange(1,7))

statBB1 = statB2 + statB3 + statB4
statBB2 = statB1 + statB3 + statB4
statBB3 = statB1 + statB2 + statB4
statBB4 = statB1 + statB2 + statB3

if statB1 <= statB2 and statB1 <= statB3 and statB1 <= statB4:
    statB = int(statBB1)
if statB2 <= statB1 and statB2 <= statB3 and statB2 <= statB4:
    statB = int(statBB2)
if statB3 <= statB1 and statB3 <= statB2 and statB3 <= statB4:
    statB = int(statBB3)
if statB4 <= statB1 and statB4 <= statB2 and statB4 <= statB3:
    statB = int(statBB4)

statBmod = round((statB - 10.5)/2)

if statBmod >= 0:
    statBmodsign = "+"
else:
    statBmodsign = ""

statC1 = int(randrange(1,7))
statC2 = int(randrange(1,7))
statC3 = int(randrange(1,7))
statC4 = int(randrange(1,7))

statCC1 = statC2 + statC3 + statC4
statCC2 = statC1 + statC3 + statC4
statCC3 = statC1 + statC2 + statC4
statCC4 = statC1 + statC2 + statC3

if statC1 <= statC2 and statC1 <= statC3 and statC1 <= statC4:
    statC = int(statCC1)
if statC2 <= statC1 and statC2 <= statC3 and statC2 <= statC4:
    statC = int(statCC2)
if statC3 <= statC1 and statC3 <= statC2 and statC3 <= statC4:
    statC = int(statCC3)
if statC4 <= statC1 and statC4 <= statC2 and statC4 <= statC3:
    statC = int(statCC4)

statCmod = round((statC - 10.5)/2)

if statCmod >= 0:
    statCmodsign = "+"
else:
    statCmodsign = ""

statD1 = int(randrange(1,7))
statD2 = int(randrange(1,7))
statD3 = int(randrange(1,7))
statD4 = int(randrange(1,7))

statDD1 = statD2 + statD3 + statD4
statDD2 = statD1 + statD3 + statD4
statDD3 = statD1 + statD2 + statD4
statDD4 = statD1 + statD2 + statD3

if statD1 <= statD2 and statD1 <= statD3 and statD1 <= statD4:
    statD = int(statDD1)
if statD2 <= statD1 and statD2 <= statD3 and statD2 <= statD4:
    statD = int(statDD2)
if statD3 <= statD1 and statD3 <= statD2 and statD3 <= statD4:
    statD = int(statDD3)
if statD4 <= statD1 and statD4 <= statD2 and statD4 <= statD3:
    statD = int(statDD4)

statDmod = round((statD - 10.5)/2)

if statDmod >= 0:
    statDmodsign = "+"
else:
    statDmodsign = ""

statE1 = int(randrange(1,7))
statE2 = int(randrange(1,7))
statE3 = int(randrange(1,7))
statE4 = int(randrange(1,7))

statEE1 = statE2 + statE3 + statE4
statEE2 = statE1 + statE3 + statE4
statEE3 = statE1 + statE2 + statE4
statEE4 = statE1 + statE2 + statE3

if statE1 <= statE2 and statE1 <= statE3 and statE1 <= statE4:
    statE = int(statEE1)
if statE2 <= statE1 and statE2 <= statE3 and statE2 <= statE4:
    statE = int(statEE2)
if statE3 <= statE1 and statE3 <= statE2 and statE3 <= statE4:
    statE = int(statEE3)
if statE4 <= statE1 and statE4 <= statE2 and statE4 <= statE3:
    statE = int(statEE4)

statEmod = round((statE - 10.5)/2)

if statEmod >= 0:
    statEmodsign = "+"
else:
    statEmodsign = ""

statF1 = int(randrange(1,7))
statF2 = int(randrange(1,7))
statF3 = int(randrange(1,7))
statF4 = int(randrange(1,7))

statFF1 = statF2 + statF3 + statF4
statFF2 = statF1 + statF3 + statF4
statFF3 = statF1 + statF2 + statF4
statFF4 = statF1 + statF2 + statF3

if statF1 <= statF2 and statF1 <= statF3 and statF1 <= statF4:
    statF = int(statFF1)
if statF2 <= statF1 and statF2 <= statF3 and statF2 <= statF4:
    statF = int(statFF2)
if statF3 <= statF1 and statF3 <= statF2 and statF3 <= statF4:
    statF = int(statFF3)
if statF4 <= statF1 and statF4 <= statF2 and statF4 <= statF3:
    statF = int(statFF4)

statFmod = round((statF - 10.5)/2)

if statFmod >= 0:
    statFmodsign = "+"
else:
    statFmodsign = ""

statssum = int(statA + statB + statC + statD + statE + statF)

print()
print("Your stats are: ", statA, "(", statAmodsign, statAmod, "),", statB, "(", statBmodsign, statBmod, "), ", statC, "(", statCmodsign, statCmod, "), ", statD, "(", statDmodsign, statDmod, "), ", statE, "(", statEmodsign, statEmod, "), ", statF, "(", statFmodsign, statFmod, ")")
print()


if statssum <= 60:
    print("Yeesh. Good luck out there.")

if statssum > 60 and statssum <= 72:
    print("That's a bit too low. But difficulty builds character.")

if statssum > 72 and statssum <= 82:
    print("That's well suited for an adventurer.")

if statssum > 82:
    print("Oh ! Please, don't hurt me ! Take everything I have !")

print()

if statA < 14 and statB < 14 and statC < 14 and statD < 14 and statE < 14 and statF < 14:
    print("YOUR STATS ARE TOO LOW. YOU ARE ALLOWED TO ROLL FOR THEM AGAIN.")

print("Now you need to arrange your stats between your abilities.")
STR = int(input("Type your strenght value: "))
DEX = int(input("Type your dexterity value: "))
CON = int(input("Type your constitution value: "))
INT = int(input("Type your intelligence value: "))
WIS = int(input("Type your wisdom value: "))
CHA = int(input("Type your charisma value: "))
print()
absum = STR + DEX + CON + INT + WIS + CHA

while absum != statssum:
    print("You typed your stats wrong. Please try it again.")
    STR = int(input("Type your strenght value: "))
    DEX = int(input("Type your dexterity value: "))
    CON = int(input("Type your constitution value: "))
    INT = int(input("Type your intelligence value: "))
    WIS = int(input("Type your wisdom value: "))
    CHA = int(input("Type your charisma value: "))
    absum = STR + DEX + CON + INT + WIS + CHA
else:
    print("Your stats are arranged like this:")
    print("STR: ", STR)
    print("DEX: ", DEX)
    print("CON: ", CON)
    print("INT: ", INT)
    print("WIS: ", WIS)
    print("CHA: ", CHA)