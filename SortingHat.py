                          
                           # SORTING HAT PROGRAM #
                                                         #HARRY POTTER FAN  CLUB         #BY Jay26
 #HERE ITS A PROGRAM FOR ALL the harry potter FANS ID:: Jay26 ;;Jatinpandya 
 #its a dev.version of cpoyrighted code by python
 #this program req. a input of your name and thrn it will define the details as like:: house you belong and roommate and your resemblence 
#code starts
#Enter your name
import random
#No 2 trending in python
n=input("")
print(n + " Welcome to Hogwarts")
print("^     ^     ^")
print("|     |     |")
print("-------------")
print("*           *")
print("*    ..     *")
print("*  :    :   *")
print("*  :    :   *")
print("-------------")
print("Time for the sorting ceremony")
print("     *      ")
print("    ***     ")
print("   *****    ")
print("  *******   ")
print("===========")

h=random.randint(10,100)
if(h%3==0):
   print("Hmm Your house is Gryffindor")
elif(h%2==0):
   print("Hmm Your house is Hufflepuff")
elif(h%5==0):
   print("Hmm Your house is Tidda")
else:
   print("Hmm Your house is Slytherin")
   
c=["Harry Potter","Ronny Weasely","Hermione Granger","Remus Lupin","Sirius Black","Albus Dumbledore","Fred Weasely","Nymphadora Tonks","Percy Weasely","Severus Snape","Tom Riddle","Draco Malfoy","Luna Lovegood","Neville Longbottom","Peter Pattigrew","Dobby","Rubeus Hagrid"]
ch=["brave","a loyal friend","brilliant","dedicated","a righteous person","an inspiration","jocular","daring","disciplined","loyal","power hungry","a misunderstood person","innocent","humble","cunning","cute","good-at-heart"]
print("*********************************")
no=random.randint(0,16)
nm=c[no]
chh=ch[no]
print("You are like " + nm)
print("You are  " + chh)
anim=["doe","unicorn","dog","hippogriff","whale","owl","rat","cat"]
print("*********************************")
print("Your animagus is a " + anim[random.randint(0,7)])

print("*********************************")
s=["Charms","Transfiguration","Potions","Magical History","Defence Against Dark Arts","Care for Magical creatures","Ancient Runes","Herbology"]
subj=s[random.randint(0,7)]
print("Your favourite subject here would be " + subj)
print("**************************************")
th=["Professor Snape","Professor Mcgonagall","Professor Slughorn","Professor Binns","Professor Sprout","Professor Lupin","Madame Pomfrey"]
print("You would be a favourite of " +th[random.randint(0,6)])
print("**************************************")
print("""A harry potter code by Jay 26""")

