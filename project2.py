morning_person = 0
afternoon_person = 0
night_person = 0

answer1 = input (" do you prefer A breakfast, B lunch, or C dinner")
if answer1 == "A" or answer1 == "a" or answer1 == (" a") or answer1 == " A": 
    morning_person += 5
elif answer1 == "B" or answer1 == "b" or answer1 == " B" or answer1 == " b":
    afternoon_person += 4
elif answer1 == "C" or answer1 == "c" or answer1 == " c" or answer1 == " C":
    night_person += 3

print ("")

answer2 = input ("when do you usually wake up? A before 11 pm, B in between 11 - 12 pm, or C in between 1-2 pm")
if answer2 == "A" or answer2 == "a" or answer2 == " a" or answer2 == " A":
    morning_person += 5
elif answer2 == "b" or answer2 == "B" or answer2 == " B" or answer2 == " b":
    afternoon_person += 4
elif answer2 == "c" or answer2 == "C" or answer2 == " c" or answer2 == " C":
    night_person += 3

print ("")

answer3 = input ("when do you feel the most motivated? A morning, B afternoon, C night")
if answer3 == "a" or answer3 == "A" or answer3 == " a" or answer3 == " A":
    morning_person += 5
elif answer3 == "b" or answer3 == "B" or answer3 == " B" or answer3 == " b":
    afternoon_person += 4
elif answer3 == "c" or answer3 == "C" or answer3 == " C" or answer3 == " c":
    night_person += 3

print ("")

answer4 = input ("Do you think of yourself as a A morning person, B afternoon person, C or night person?")
if answer4 == "A" or answer4 == "a" or answer4 == " a" or answer4 == " A":
    morning_person += 5
elif answer4 == "B" or answer4 == "b" or answer4 == " b" or answer4 == "  B":
    afternoon_person += 4 
elif answer4 == "c" or answer4 == "C" or answer4 == " c" or answer4 == " C":
    night_person += 3

print ("")

print ("if you started a new fitness class between 7 and 8 am how well would you perform?")
answer5 = input (" A bad, B ok, C very well ")
if answer5 == "a" or answer5 == "A" or answer5 == " a" or answer5 == " A":
    night_person += 3
elif answer5 == "B" or answer5 == "b" or answer5 == " B" or answer5 == " b":
    afternoon_person += 4
elif answer5 == "C" or answer5 == "c" or answer5 == " c" or answer5 == " C":
    morning_person += 5 

print ("")

if night_person > morning_person and night_person >= afternoon_person:
    print ("you are a night owl")
if morning_person > afternoon_person and morning_person > night_person:
    print ("you are a morning person")
if afternoon_person > morning_person and afternoon_person > night_person:
    print ("you are a afternoon person")