import sys
import random

#returns a random name
def randomName():
    f=open("names.txt")
    t = f.read()
    names = t.split('\n')
    f.close()
    random.shuffle(names)
    return str(names[0])

#returns a random Newspaper article header and footer
def randomNP(p1):
    f = open("newspapers.txt")
    t = f.read()
    names = t.split('\n')
    f.close()
    random.shuffle(names)
    newspaper=names[0]
    NPStart=["It is being reported by " +newspaper+" that, ", "New article in " +newspaper+ " reports that, ",
            "In an interview published by "+newspaper+" it was reported that, "]
    random.shuffle(NPStart)
    NPEnd = "\nThe primary reporter of this news is "+str(p1)+" of the publishing house "+newspaper+"."

    return (str(NPStart[0]),NPEnd)

def rNP():
    f = open("newspapers.txt")
    t = f.read()
    names = t.split('\n')
    f.close()
    random.shuffle(names)
    newspaper=names[0]

    return str(newspaper)



countries=[]

CountryOfficial=["Prime Minister", "President", "Secretary of State", "Defense Minister"]
astro=0


quarter = ["First", "Second", "Third", "Fourth"]


day = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

#returns a random Country Official Name
def randomCO():
    random.shuffle(CountryOfficial)
    return str(CountryOfficial[0])

Relative=["Mother", "Father", "Parents", "Brother", "Sister"]


def expressMarvel(p1, p2, country):
    s1="\n'You've done the country proud, "+p1+"', said "+p2+" of "+country+".\n"
    s2="'Thank You "+p2+", feels great coming from someone as respectable as you.', said "+p1+" of "+country+".\n"
    s3="'Hope you continue to inspire us "+p1+"', said "+p2+" of "+country+"."
    return s1+s2+s3

def expressAnger(p1, p2, c1, c2, c3):
    s1 = "\n'We are fed up of' " + c2 + ", said " + p1 + " of " + c1 + ".\n"

    s2x = ["'They are to blame.'\n", "'They started it.\n''", "'We, aren't to blame.\n'", "'We, didn't start it.\n'"]
    random.shuffle(s2x)
    s2=s2x[0]

    s3 = "\n" + p2 +" of "+c2 +" responded with his own escalating remark,"

    s4="\n'It is no secret that they feel we aren't equipped to fight this off.'"
    s5="\n'We will will respond fiercely when challenged!'"
    s6="\n"+c3+" has asked both "+c1+" and "+c2+" to de-escalate tensions and avoid any action that may result in " \
                                                "eventual disastrous consequences"

    return "\n"+s1+s2+s3+s4+s5+s6

def expressGratitude(p1, p2, c1, c2):
    s1="'We are thankful to "+c1+" for their investment!'"
    s2="\n'They have been extremely helpful to us!', said " + p2 + " of " + c2 + ".\n"
    s3=p1+" echoed similar tones on the occasion of the meeting and responded,"


    p=['partnership', 'joint-venture', 'Memorandum of understanding']
    random.shuffle(p)
    s4="\n'I am pleased to inform you all here today that we have entered a "+p[0]+" with "+p2

    return "\n"+s1+s2+s3+s4

def scamConv(p1, p2, c1):

    scam=["Coal Scam", "Multi-level marketing scam", "Defense Budget Scam"]
    random.shuffle(scam)
    scamx=scam[0]

    s1="\nOfficial "+p1+" was in a press conference today and answered questions about the "+scamx+"."
    s2="\n'We are investigating reports that a "+scamx+" has been uncovered to have take place in "+c1+".'"
    s3="\n"+p2+", the opossition party leader has asked the government to install an independent body into the investigation."
    s4="\n'An independent body is necessary to ensure that corruption does not change the outcome of the" \
       " investigation.', said "+p2+" of "+c1+"."

    return s1+s2+s3+s4



def main(outlook):

    global countries

    file = open("novel.txt", 'w+')

    def Astro():
        random.shuffle(countries)
        country1=countries[0][0]
        country2=countries[1][0]

        #increment country1's rating
        countries[0][1]=countries[0][1]+5

        global astro
        astro=astro+1

        celestial = ["Planet", "Star", "Galaxy"]
        random.shuffle(celestial)
        celestialbody=str(celestial[0])+str(astro)

        person1=randomName()
        person2=randomCO()
        person4 = randomName()

        (start,end)=randomNP(person4)

        s2x=["an astronomical discovery has been made by " +country1+".", country1+ " has made has made an Astronomical Discovery."]
        random.shuffle(s2x)
        s2=s2x[0]

        s3x=[" "+celestialbody +" was discovered in " +country1+ " by " +randomName()+".", " "+randomName()+" has discovered "+celestialbody+" in "+country1+"."]
        random.shuffle(s3x)
        s3=s3x[0]

        s4=expressMarvel(person1, person2, country1)

        s5="\n "+country2+" has congratulated "+country1+" on their space success."

        person3=randomCO()
        s6="\n'We support "+country1+" in their pursuit of astronomical endeavors!', said "+person3+" of "+country2+"."

        s = "\n"+start+s2+s3+s4+s5+s6+end
        return s

    def Economic():

        random.shuffle(countries)
        country1 = countries[0][0]
        country2 = countries[1][0]

        # increment country1's and country2's rating
        countries[0][1] = countries[0][1] + 2
        countries[1][1] = countries[0][1] + 6

        global quarter
        random.shuffle(quarter)
        quarter1 = quarter[0]

        random.shuffle(day)
        day1 = day[0]

        s1 = country1 + " economy cooled as G.D.P. grew at 2.6% Rate in " + quarter1 + " Quarter."

        s2 = " "+country1 + " stocks closed lower " + day1 + \
             ", erasing early gains as investors continued to track trade negotiations between the "\
             + country1 + " and " + country2 + " as the two nations appear to inch closer to a pact."

        person1=randomCO()
        person2=randomCO()
        person3=randomName()

        s3=expressGratitude(person1, person2, country2, country1)

        (start, end) = randomNP(person3)

        return "\n"+start+s1+s2+s3+end

    def Discovery():
        random.shuffle(countries)
        country = countries[0][0]
        person = randomCO()

        # increment country1's rating
        countries[0][1] = countries[0][1] + 5

        article1 = "The scienntific community reports that an element of higher atomic weight than " +\
        "uranium has been discovered in " + country + " by Dr." + person + ". The element has been " +\
        "assigned the atomic number 93 and its atomic weight has been found to be 240 from an analysis of " +\
        "the silver salt, Ag(93)O4. The new element would be a congener of manganese and of rhenium, which " +\
        "was discovered in 1925. It should thus form an acid analogous to HReO4 and also salts similar to the " +\
        "permanganates and perrhenates. Dr. " + person + " has suggested the name 'Bohemium' for the new element, " +\
        "which he considers is probably the parent element of protactinium"

        article2 = "Researchers reported on Thursday that in debris flying out from the collisions of protons at the CERN " +\
        "particle physics laboratory in " + country + ". The discovery fits with the Standard Model, the prevailing " +\
        "understanding of how the smallest bits of the universe behave, and does not seem to point to new physics. " +\
        "'The existence of these particles has been predicted by the Standard Model,' said " + person + ", a " +\
        "physicist at the University of " + country + " who led the research. 'Their properties have also been predicted.'" +\
        "Dr. " + person + " presented the findings on Thursday at a European Physical Society conference in Venice, and a paper " +\
        "describing them has been submitted to the journal Physical Review Letters."

        articles = [article1, article2]
        random.shuffle(articles)
        person3=randomName()
        (start, end) = randomNP(person3)

        return start+articles[0]+end

    def War():
        random.shuffle(countries)
        A=countries[0][0]
        B=countries[1][0]
        C=countries[2][0]

        #decrement A's and B's rating
        r1=(countries[0][1])/5
        r2=(countries[1][1])/5

        countries[0][1]=countries[0][1]-r1
        countries[1][1]=countries[1][1]-r2

        person1=randomCO()
        person2=randomCO()

        s1= "A war has broken out between "+A+" and "+B+". "

        s2 = expressAnger(person1, person2, A, B, C)

        person3 = randomName()
        (start, end) = randomNP(person3)

        return start+s1+s2+end

    def Dol():
        random.shuffle(countries)
        country = countries[0][0]

        #decrement country1's rating
        countries[0][1]=countries[0][1]-5

        person = randomCO()

        article1 = "The national newspapers of "+country+" reported that today " + person + " was found dead in his home in " + country +\
        ", with fresh injection marks in both arms and a fatal wound to the head from the 20-gauge shotgun found between his knees. " +\
        person + "’s suicide brought an end to a life marked by far more suffering than is generally associated with rock superstardom. " +\
        "But rock superstardom never did sit well with + " + person + ", a committed social outsider who was reluctantly dubbed the " +\
        "spokesman of his generation. “Success to him seemed like, I think, a brick wall,” said friend Greg Sage, a musical hero of " +\
        "Cobain’s from the local punk rock scene of the 1980s. “There was nowhere else to go but down.”"

        person3 = randomName()
        (start, end) = randomNP(person3)
        return start+article1+end

    def Scam():
        random.shuffle(countries)
        A = countries[0][0]
        person1 = randomCO()
        person2 = randomName()

        #decrement A's rating
        countries[0][1]=countries[0][1]-6

        s1="\n A scam was uncovered in "+A+" in a fiery battle between the government and the opposition."
        s2="\n Excepts from the session in the upper house session show the internal turbulence within "+A+"."
        s3=scamConv(person1, person2, A)

        person3 = randomName()
        (start, end) = randomNP(person3)
        return "\n"+start+s1+s2+s3+end

    def Wr():
        random.shuffle(countries)

        country1 = countries[0][0]
        country2 = countries[1][0]

        global indvSports, teamSports

        indvSports = ["Swimming", "100 meter sprint", "Archery", "shooting", "Boxing", "Wrestling", "Shot Put",
                      "Discuss Throw","200 meter race","200 meter relay","400 meter relay", "Weightlifting",
                      "Tabletennis", "Badminton", "Lawn Tennis", "Kayaking", "Cycling", "Marathon", "Racquet Ball",
                      "Golf", "Skiing", "Carrom", "Chess"]

        teamSports = ["Hockey", "Soccer", "Volleyball", "Beach Volleyball", "Cricket", "BasketBall", "HandBall",
                      "Baseball", "Softball", "IceHockey", "Kabaddi", "Polo"]

        random.shuffle(indvSports)
        random.shuffle(teamSports)

        person1 = randomCO()
        person2 = randomName()

        position = ["first", "second"]
        random.shuffle(position)
        pos1 = position[0]

        if pos1 == "first":
            pos2 = "second"
            text = "by defeating with a lead of "
        else:
            pos2 = "first"
            text = "by a difference of "

        points = ["4", "6", "8", "23", "32", "12", "2", "1", "22", "56", "32", "53", "25", "13", "14"
                  , "16", "17", "19", "9", "21", "27", "28", "29", "36", "34"]
        random.shuffle(points)

        eventx = ["commonwealth", "olympics", "winter olympics", "world cup", "Asia cup", "American league"]
        random.shuffle(eventx)

        s1 = eventx[0] + " saw a number of players nail down their places in record history, chief among them " +\
              countries[2][0] + " player " + randomName() + ", who retained his " + indvSports[0] + \
              " title by defeating " + countries[3][0] + " player " + randomName() + " meanwhile, " + \
                countries[4][0] + "’s " + randomName() + " maintained remarkable unbeaten record at the " + \
             eventx[0] + ", winning the " + indvSports[0] +" title in a row after her previous wins."

        s2 = " " + indvSports[1] + " match was held in " + countries[5][0] + " between " + person1 + "and" + person2 +\
              " " + person2 + " secured the " + pos1 + " position " + text + " " + points[0] + \
             " points with its opponent."

        event1 = eventx[1]
        event2 = eventx[2]
        event3 = eventx[3]
        random.shuffle(day)
        s5 = "The " + event1 + " Qualifiers wrapped up in style this past " + day[0] + ", highlighted by several standout performances from across the continent. " + event2 + " hosts " + country1 + " were at the forefront of a slew of brilliant performances. Caption " + randomName() + " successfully recorded back to back brilliant performances throughout the " + event1 + " event."

        s3 = expressMarvel(person2, person1, country1)

        s4 = country2 + " has congratulated " + country1 + " on winning the " + teamSports[0] + " " + \
             event3 + " title."

        px=randomName()
        (start,end)=randomNP(px)

        s = "\n"+ start + s1 + s2 + s3 + s4 + s5 + end

        return s

    def RichieRich():
        random.shuffle(countries)
        country1 = countries[0][0]
        country2 = countries[1][0]

        person1=randomName()
        person2=randomName()
        person3=randomCO()

        s1=person1 + " now holds the post of world’s richest person."+" Their country of residence is "+country1+". "
        s2=person2 + " now holds the post of world’s second richest person."+" Their country of residence is "+country2+". "
        s3=expressMarvel(person1, person3, country1)

        px = randomName()
        (start, end) = randomNP(px)

        return "\n"+start+s1+s2+s3+end

    def Np():
        random.shuffle(countries)
        country = countries[0][0]
        person = randomCO()
        newsPaperName1 = rNP()
        h1 = "---------------Welcome to " + newsPaperName1 + "---------------\n\n"
        newsPaperName2 = rNP()

        topics = ["physics", "chemistry", "literature", "peace", "medicine"]
        random.shuffle(topics)

        topic = topics[0]

        article1 = "The " + newsPaperName2 + " newspapers reported that " + person + ", a professor at the " +\
        country + " Institute of Technology, was awarded the Nobel Prize in " + topic + " on Tuesday " +\
        "for work tremendous work in the respective field"

        return article1

    def Chapter(x, eventList):
        C = "\n\nChapter: " + str(x) + ",Year: " + str(2020 + x - 1) + "\n"
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
