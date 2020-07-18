print("\n\n************Welcome to Political Compass************\n")
print("Answer the following statements according to the key given below\n")
print("Key:\n 1- Strongly agree\n 2- Agree\n 3- Neutral/unsure\n 4- Disagree\n 5- Strongly disagree \n")
print("Your closest poitical ideology will be produced eventually")
print("Answer honestly!","\n")

EM = 0
NW = 0
LA = 0
TP = 0

#E type:

E1=int(input("1. It is necessary for govt to intervene in economy to protect consumers \n"))

if (E1==1):
    EM+=2

elif(E1==2):
    EM+=1

elif(E1==3):
    pass

elif(E1==4):
    EM-=1

elif(E1==5):
    EM-=2

else:
    print("Invalid input! \n Input should be from 1 to 5")


E2=int(input("2. Taxing the rich is not bad \n"))

if (E2==1):
    EM+=2

elif(E2==2):
    EM+=1

elif(E2==3):
    pass

elif(E2==4):
    EM-=1

elif(E2==5):
    EM-=2

else:
    print("Invalid input! \n Input should be from 1 to 5")


E3=int(input("3. Inheritance of wealth is not bad \n"))

if (E3==1):
    EM-=2

elif(E3==2):
    EM-=1

elif(E3==3):
    pass

elif(E3==4):
    EM+=1

elif(E3==5):
    EM+=2

else:
    print("Invalid input! \n Input should be from 1 to 5")


E4=int(input("4. The rich getting better healthcare & education is not bad \n"))

if (E4==1):
    EM-=2

elif(E4==2):
    EM-=1

elif(E4==3):
    pass

elif(E4==4):
    EM+=1

elif(E4==5):
    EM+=2

else:
    print("Invalid input! \n Input should be from 1 to 5")

E5=int(input("5. Workers should own means of production \n"))

if (E5==1):
    EM+=2

elif(E5==2):
    EM+=1

elif(E5==3):
    pass

elif(E5==4):
    EM-=1

elif(E5==5):
    EM-=2

else:
    print("Invalid input! \n Input should be from 1 to 5")

E6=int(input("6. Opportunity should be deserved not reserved \n"))

if (E6==1):
    EM-=2

elif(E6==2):
    EM-=1

elif(E6==3):
    pass

elif(E6==4):
    EM+=1

elif(E6==5):
    EM+=2

else:
    print("Invalid input! \n Input should be from 1 to 5")




#Dtype:

D1=int(input("7. Tarrifs on international trade must be increased to encourage local products \n"))

if (D1==1):
    NW+=2

elif(D1==2):
    NW+=1

elif(D1==3):
    pass

elif(D1==4):
    NW-=1

elif(D1==5):
    NW-=2

else:
    print("Invalid input! \n Input should be from 1 to 5")

D2=int(input("8. United world govt would be better \n"))

if (D2==1):
    NW-=2

elif(D2==2):
    NW-=1

elif(D2==3):
    pass

elif(D2==4):
    NW+=1

elif(D2==5):
    NW+=2

else:
    print("Invalid input! \n Input should be from 1 to 5")

D3=int(input("9. Military spending must be reduced \n"))

if (D3==1):
    NW-=2

elif(D3==2):
    NW-=1

elif(D3==3):
    pass

elif(D3==4):
    NW+=1

elif(D3==5):
    NW+=2

else:
    print("Invalid input! \n Input should be from 1 to 5")

D4=int(input("10. My nation is great \n"))

if (D4==1):
    NW+=2

elif(D4==2):
    NW+=1

elif(D4==3):
    pass

elif(D4==4):
    NW-=1

elif(D4==5):
    NW-=2

else:
    print("Invalid input! \n Input should be from 1 to 5")



D5=int(input("11. Open borders for immigrants \n"))


if (D5==1):
    NW-=2

elif(D5==2):
    NW-=1

elif(D5==3):
    pass

elif(D5==4):
    NW+=1

elif(D5==5):
    NW+=2

else:
    print("Invalid input! \n Input should be from 1 to 5")

D6=int(input("12. We should always stand by our nation in international issues \n"))

if (D6==1):
    NW+=2

elif(D6==2):
    NW+=1

elif(D6==3):
    pass

elif(D6==4):
    NW-=1

elif(D6==5):
    NW-=2

else:
    print("Invalid input! \n Input should be from 1 to 5")

#C type:

C1=int(input("13. General populace makes poor decision \n"))

if (C1==1):
    LA-=2

elif(C1==2):
    LA-=1

elif(C1==3):
    pass

elif(C1==4):
    LA+=1

elif(C1==5):
    LA+=2

else:
    print("Invalid input! \n Input should be from 1 to 5")

C2=int(input("14. Govt surveillance is necessary \n"))

if (C2==1):
    LA-=2

elif(C2==2):
    LA-=1

elif(C2==3):
    pass

elif(C2==4):
    LA+=1

elif(C2==5):
    LA+=2

else:
    print("Invalid input! \n Input should be from 1 to 5")

C3=int(input("15. Peoples decision must be final, even if it is wrong \n"))

if (C3==1):
    LA+=2

elif(C3==2):
    LA+=1

elif(C3==3):
    pass

elif(C3==4):
    LA-=1

elif(C3==5):
    LA-=2

else:
    print("Invalid input! \n Input should be from 1 to 5")

C4=int(input("16. Strong leadership is better \n"))

if (C4==1):
    LA-=2

elif(C4==2):
    LA-=1

elif(C4==3):
    pass

elif(C4==4):
    LA+=1

elif(C4==5):
    LA+=2

else:
    print("Invalid input! \n Input should be from 1 to 5")

C5=int(input("17. Drugs should be legalised \n"))

if (C5==1):
    LA+=2

elif(C5==2):
    LA+=1

elif(C5==3):
    pass

elif(C5==4):
    LA-=1

elif(C5==5):
    LA-=2

else:
    print("Invalid input! \n Input should be from 1 to 5")

C6=int(input("18. Free press & right to protest are fundamental rights \n"))

if (C6==1):
    LA+=2

elif(C6==2):
    LA+=1

elif(C6==3):
    pass

elif(C6==4):
    LA-=1

elif(C6==5):
    LA-=2

else:
    print("Invalid input! \n Input should be from 1 to 5")

#S type:


S1=int(input("19. Children should be teached religious & traditional values \n"))

if (S1==1):
    TP+=2

elif(S1==2):
    TP+=1

elif(S1==3):
    pass

elif(S1==4):
    TP-=1

elif(S1==5):
    TP-=2

else:
    print("Invalid input! \n Input should be from 1 to 5")

S2=int(input("20. Traditions & culture are meaningless \n"))

if (S2==1):
    TP-=2

elif(S2==2):
    TP-=1

elif(S2==3):
    pass

elif(S2==4):
    TP+=1

elif(S2==5):
    TP+=2

else:
    print("Invalid input! \n Input should be from 1 to 5")

S3=int(input("21. Religion should play a role in govt \n"))

if (S3==1):
    TP+=2

elif(S3==2):
    TP+=1

elif(S3==3):
    pass

elif(S3==4):
    TP-=1

elif(S3==5):
    TP-=2

else:
    print("Invalid input! \n Input should be from 1 to 5")

S4=int(input("22. Churches/temples should be taxed the same way as other institutions \n"))

if (S4==1):
    TP-=2

elif(S4==2):
    TP-=1

elif(S4==3):
    pass

elif(S4==4):
    TP+=1

elif(S4==5):
    TP+=2

else:
    print("Invalid input! \n Input should be from 1 to 5")

S5=int(input("23. Same sex marriage & sex outside marriage should be legal \n"))

if (S5==1):
    TP-=2

elif(S5==2):
    TP-=1

elif(S5==3):
    pass

elif(S5==4):
    TP+=1

elif(S5==5):
    TP+=2

else:
    print("Invalid input! \n Input should be from 1 to 5")


S6=int(input("24. Traditional past was better than scientific present \n"))

if (S6==1):
    TP+=2

elif(S6==2):
    TP+=1

elif(S6==3):
    pass

elif(S6==4):
    TP-=1

elif(S6==5):
    TP-=2

else:
    print("Invalid input! \n Input should be from 1 to 5")

print("RESULTS! \n")

print("Economically, you are ",end="")

if (EM >= -12 and EM < -6):
    print("an Elitist \n")

elif (EM >= -6 and EM < 0 ):
    print("a Capitaist \n")

elif (EM > 0 and EM <= 6):
    print("an Egalitarian \n")

elif (EM >6 and EM <= 12):
    print("a Socialist\n")
else:
    print("a Centrist \n")

print("\n")

print("Diplomatically, you are ",end="")

if (NW >= -12 and NW < -6):
    print("an Authoritarian \n")

elif (NW >= -6 and NW < 0):
    print("a Humanist\n")

elif (NW > 0 and NW <= 6):
    print("a Patriot \n")

elif (NW > 6 and NW <= 12):
    print("a Nationalist\n")

else:
    print("a Centrist \n")

print("\n")

print("Civically, you are ", end="")

if (LA >= -12 and LA < -6):
    print("a Fascist \n")

elif (LA >= -6 and LA < 0):
    print("an Authoritarian \n")

elif (LA > 0 and LA <= 6):
    print("a Liberal \n")

elif (LA > 6 and LA <= 12):
    print("an Anarchist \n")

else:
    print("a Centrist \n")

print("\n")

print("Socially, you are ", end="")

if (TP >= -12 and TP < -6):
    print("a Modernist \n")

elif (TP >= -6 and TP < 0):
    print("a Secularist \n")

elif (TP > 0 and TP <= 6):
    print("a Conservative")

elif (TP > 6 and TP <= 12):
    print("a Traditionalist")

else:
    print("a Centrist \n")

































