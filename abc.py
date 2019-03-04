import sys
import random

def randomName():
    f=open("names.txt")
    t = f.read()
    names = t.split('\n')
    f.close()
    random.shuffle(names)
    return str(names[0])

def randomNP():
    f = open("newspapers.txt")
    t = f.read()
    names = t.split('\n')
    f.close()
    random.shuffle(names)
    newspaper=names[0]
    listNP=["It is being reported by " +newspaper+" that, ", "New article in " +newspaper+ " reports that, "]
    random.shuffle(listNP)
    return str(listNP[0])

countries=[]

CountryOfficial=["Prime Minister", "President", "Secretary of State", "Defense Minister"]
astro=0

def randomCO():
    random.shuffle(CountryOfficial)
    return str(CountryOfficial[0])

Relative=["Mother", "Father", "Parents", "Brother", "Sister"]

def expressMarvelC(p1, p2, country):
    s1="\n'You've done the country proud' "+p2+", said "+p1+" of "+country+".\n"
    s2="'Thank You "+p1+", feels great coming from someone as respectable as you.', said"+p2+" of "+country+".\n"
    s3="'Hope you continue to inspire us "+p2+"', said "+p1+" of "+country+"."
    return s1+s2+s3

def expressAnger(p1, p2, c1, c2):
    s1 = "\n'We are fed up of' " + c2 + ", said " + p1 + " of " + c1 + ".\n"

    s2x = ["'They are to blame.'\n", "'They started it.\n''", "'We, aren't to blame.\n'", "'We, didn't start it.\n'"]
    random.shuffle(s2x)
    s2=s2x[0]

    s3 = "\n" + p2 +" of "+c2 +" responded with his own escalating remark,"

    s4="\n'It is no secret that they feel we aren't equipped to fight this off.'"
    s5="\n'We will will respond fiercely when challenged!'"

    return "\n"+s1+s2+s3+s4+s5

def expressGratitude(p1, p2, c1, c2):
    s1="\n'We are thankful to "+c1+" for their investment!'"
    s2="\n'They have been extremely helpful to us!', said " + p2 + " of " + c2 + ".\n"
    s3=p1+" echoed similar tones on the occasion of the joint meeting and responded,"


    p=['partnership', 'joint-venture', 'Memorandum of understanding']
    random.shuffle(p)
    

    s4="\n'I am pleased to inform you all here today that we have entered a "




def main(outlook):

    global countries

    file = open("novel.txt", 'w+')

    def Astro():
        random.shuffle(countries)
        country1=countries[0][0]
        country2=countries[1][0]

        global astro
        astro=astro+1

        celestial = ["Planet", "Star", "Galaxy"]
        random.shuffle(celestial)
        celestialbody=str(celestial[0])+str(astro)

        person1=randomCO()
        person2=randomName()

        s1=randomNP()

        s2x=["an astronomical discovery has been made by " +country1+".", country1+ " has made has made an Astronomical Discovery."]
        random.shuffle(s2x)
        s2=s2x[0]

        s3x=[" "+celestialbody +"was discovered in " +country1+ " by " +randomName()+".", " "+randomName()+" has discovered "+celestialbody+" in "+country1+"."]
        random.shuffle(s3x)
        s3=s3x[0]

        s4=expressMarvelC(person1, person2, country1)

        s5=country2+" has congratulated "+country1+" on their space success."

        s = "\n"+s1+s2+s3+s4+s5
        return s

    def Economic():
        s = "This is an Economic Investment! \n"
        return s

    def Discovery():
        s = "This is an Health,AI,Energy Discovery! \n"
        return s

    def War():
        random.shuffle(countries)
        A=countries[0][0]
        B=countries[1][0]


        s = "This is a War between " + str(A) + " and " + str(B) +"!" +"\n"
        return s

    def Dol():
        s = "This marks death of legend! \n"
        return s

    def Scam():
        s = "This is a Scam! \n"
        return s

    def Wr():
        s = "This is marks a world Record! \n"
        return s

    def RichieRich():
        s = "This marks new Richest Person in World! \n"
        return s

    def Np():
        s = "This marks a Nobel Prize win! \n"
        return s

    def Chapter(x, eventList):
        C = "Chapter: " + str(x) + ",Year: " + str(2020 + x - 1) + "\n"
        file.write(C)

        for event in eventList:
            if event == "Astro":
                s = Astro()
                file.write(s)
            elif event == "Economic":
                s = Economic()
                file.write(s)
            elif event == "Discovery":
                s = Discovery()
                file.write(s)
            elif event == "War":
                s = War()
                file.write(s)
            elif event == "Dol":
                s = Dol()
                file.write(s)
            elif event == "Scam":
                s = Scam()
                file.write(s)
            elif event == "Wr":
                s = Wr()
                file.write(s)
            elif event == "RichieRich":
                s = RichieRich()
                file.write(s)
            elif event == "Np":
                s = Np()
                file.write(s)
        return


    def switch(s):
        k=0

        #pick incoming Country
        countriesFile= open('countries.txt')
        text = countriesFile.read()
        listofCs= text.split('\n')
        random.shuffle(listofCs)
        newCountry=listofCs[0]

        #assign incoming rating
        newCountryRating=35

        while(k<7):
            if(countries[k][0]==s):
                countries[k][0]=newCountry
                countries[k][1]=newCountryRating
            k=k+1

        return

    def plrc():
        index=0
        k=0
        minRating=100
        while(k<7):
            if(countries[k][1]<minRating):
                index=k
                minRating=countries[k][1]
            k=k+1

        return str(countries[index][0])


    eList=["Astro", "Economic", "Discovery", "War", "Dol", "Scam", "Wr", "RichieRich", "Np"]
    pList=["Astro", "Economic", "Discovery"]
    nList=["War", "Dol", "Scam"]
    zList=["Wr", "RichieRich", "Np"]



    for chapterNumber in range(1,51):
        print(chapterNumber)

        #add postive/negative event and zero event.
        if(chapterNumber%2):
            if(outlook==1):
                random.shuffle(pList)
                eList.append(pList[0])
            elif(outlook==-1):
                random.shuffle(nList)
                eList.append(nList[0])
            random.shuffle(zList)
            eList.append(zList[0])

        #pick 9 random events from eventList
        random.shuffle(eList)
        CheList=eList[0:9]

        Chapter(chapterNumber, CheList)
        if(chapterNumber%5==0):
            CTBR=plrc()
            switch(CTBR)

    file.close()

    return


if __name__ == "__main__":
    o = int(sys.argv[1])

    countries.append(["United States", 100])
    countries.append(["China", 70])
    countries.append(["India", 60])
    countries.append(["Germany", 45])
    countries.append(["UK", 40])
    countries.append(["Pakistan", 37])
    countries.append(["France", 40])

    main(o)
