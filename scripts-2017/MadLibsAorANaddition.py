#A visit to the dentist
def aVisitToTheDentist():
    a = str.lower(input("PLURAL NOUN: "))
    b = input("PERSON IN ROOM (LAST NAME): ")
    c = str.lower(input("ADJECTIVE: "))
    d = str.lower(input("NOUN: "))
    e = str.lower(input("PART OF THE BODY: "))
    f = str.lower(input("PART OF THE BODY: "))
    g = str.lower(input("PART OF THE BODY: "))
    h = str.lower(input("PLURAL PART OF THE BODY: "))
    i = str.lower(input("NOUN: "))
    j = str.lower(input("NOUN: "))
    k = str.lower(input("EXCLAMATION: "))
    l = str.lower(input("NOUN: "))
    m = str.lower(input("NOUN: "))
    n = str.lower(input("PART OF THE BODY: "))
    o = str.lower(input("VERB: "))
    p = str.lower(input("NOUN: "))
    q = str.lower(input("ADJECTIVE: "))
    r = str.lower(input("NOUN: "))
    aoran0=aOrAn(c)
    aoran1= aOrAn(j)
    aoran2= aOrAn(l)
    print("DONE")
    ready = "no"
    while ready != "yes":
        ready = input("Are you ready? yes/no: ")
        ready = str.lower(ready)
    print("TITLE: A VISIT TO THE DENTIST")
    print(" ")
    print("A one-act play to be performed by two " + a + " in this room.")
    print("PATIENT: Thank you so very much for seeing me, Dr. "+b+", on such "+aoran0+c+" notice.")
    print("DENTIST: What is your problem, young "+d+"?")
    print("PATIENT: I have a pain in my upper "+e+", which is giving me a severe "+f+"-ache.")
    print("DENTIST: Let me take a look. Open your "+g+" wide. Good. Now I'm going to tap your "+h+" with my "+i+".")

    print("PATIENT: Shouldn't you give me "+aoran1+j+" killer?")
    print("DENTIST: It's not necessary yet, "+k+"! I think I see "+aoran2+l+" in your upper "+m+".")
    print("PATIENT: Are you going to pull my "+n+" out?")
    print("DENTIST: No. I'm going to "+o+" your tooth and put it in a temporary "+p+".")
    print("PATIENT: When do I come back for the "+q+" filling?")
    print("DENTIST: A day after I cash your "+r+".")
    print("THE END")
    return
#Amusement Parks
def amusementParks():
    a = str.lower(input("NOUN: "))
    b = str.lower(input("ARTICLE OF CLOTHING: "))
    c = str.lower(input("ADJECTIVE: "))
    d = str.lower(input("ADJECTIVE: "))
    e = str.lower(input("NOUN: "))
    f = str.lower(input("PLURAL NOUN: "))
    g = str.lower(input("NOUN: "))
    h = str.lower(input("ADJECTIVE: "))
    i = str.lower(input("TYPE OF FOOD: "))
    j = str.lower(input("TYPE OF LIQUID: "))
    k = str.lower(input("PART OF THE BODY: "))
    l = str.lower(input("PLURAL NOUN: "))
    m = str.lower(input("PLURAL NOUN: "))
    n = str.lower(input("ANIMAL: "))
    o = str.lower(input("NOUN: "))
    print("DONE")
    aoran1 = aOrAn(d)
    aoran2 = aOrAn(e)
    str1="An amusement park is always fun to visit on a hot summer "
    str2=". When you get there, you can wear your "
    str3=" and go for a swim. And there are lots of "
    str4=" things to eat. You can start off with "
    str5="-dog on "
    str6=" with mustard, relish, and "
    str7=" on it. Then you can have a buttered ear of "
    str8=" with a nice "
    str9=" slice of "
    str10=" and a big bottle of cold "
    str11=". When you are full, it's time to go on the roller coaster, which should settle your "
    str12=". Other amusement park rides are the bumper cars, which have little "
    str13=" that you drive and run into other "
    str14=", and the merry-go-round, where you can sit on a big "
    str15=" and try to grab the gold "
    str16=" as you ride past it."
    ready = "no"
    while ready != "yes":
        ready = input("Are you ready? yes/no: ")
        ready = str.lower(ready)
    print("TITLE: AMUSEMENT PARKS")
    print(" ")
    print(str1+a+str2+b+str3+c+str4+aoran1+d+str5+aoran2+e+str6+f+str7+g+str8+h+str9+i+str10+j+str11+k+str12+l+str13+m+str14+n+str15+o+str16)
    print("THE END")
    return
#Commencement Speech
def commencementSpeech():
    a = str(input("YEAR: "))
    b = str.lower(input("ADJECTIVE: "))
    c = str(input("NUMBER: "))
    d = str(input("NUMBER BELOW 51: "))
    e = str(input("NUMBER BELOW 296: "))
    f = str.lower(input("ADJECTIVE: "))
    g = (input("PERSON (FIRST AND LAST NAME): "))
    h = str(input("YEAR: "))
    i = (input("PERSON IN ROOM (FIRST AND LAST NAME): "))
    j = (input("CELEBRITY (FIRST AND LAST NAME): "))
    k = str.lower(input("VERB: "))
    l = str.lower(input("NOUN: "))
    m = str.lower(input("ADVERB: "))
    n = str.lower(input("OCCUPATION: "))
    o = str.lower(input("OCCUPATION: "))
    p = str.lower(input("NOUN: "))
    aoranb = aOrAn(b)
    aoranf = aOrAn(f)
    aorann = aOrAn(n)
    aoranp = aOrAn(p)
    print("DONE")
    ready = "no"
    while ready != "yes":
        ready = input("Are you ready? yes/no: ")
        ready = str.lower(ready)
    print("TITLE: COMMENCEMENT SPEECH")
    print(" ")
    print("We've gathered here today to celebrate the Class of "+a+", "+aoranb+b+" group of "+c+" students hailing from "+d+" states and "+e+" countries to create "+aoranf+f+" community like nowhere else. Since "+g+" founded the school in "+h+", it's produced students like "+i+" and "+j+", people who understand what our motto means when it tells us to "+k+" the "+l+" "+m+". We know you will do the same, because even if you go on to be "+aorann+n+" or "+o+", you all share one thing in common: "+aoranp+p+" from this fine institution.")
    print("THE END")
    return
def aOrAn(letter):
    if (str.lower(letter[0])== "a") or (str.lower(letter[0])== "e") or(str.lower(letter[0])== "i") or(str.lower(letter[0])== "o") or(str.lower(letter[0])== "u"):
        return "an "
    else:
        return "a "
def main():
    import random
    madLibs = ['a visit to the dentist', 'amusement parks', 'commencement speech']
    madLibsOriginal = ['a visit to the dentist', 'amusement parks', 'commencement speech']
    again = "yes"
    while again == "yes":
        print("These are the MadLibs in this program:")
        for i in madLibsOriginal:
            print(i.title())
        print(" ")
        choice = input("Enter the name of the MadLib you want to play, or enter literally anything else to play a random MadLib: ")
        choice = str.lower(choice)
        if choice in madLibsOriginal:
            if choice == "a visit to the dentist":
                       aVisitToTheDentist()
                       if "a visit to the dentist" in madLibs:
                           madLibs.remove("a visit to the dentist")
            elif choice == "amusement parks":
                       amusementParks()
                       if "amusement parks" in madLibs:
                           madLibs.remove("amusement parks")
            elif choice == "commencement speech":
                       commencementSpeech()
                       if "commencement speech" in madLibs:
                           madLibs.remove("commencement speech")
        elif choice not in madLibsOriginal: #if choice is random
            if len(madLibs) == 0:
                print("You have played all the MadLibs.")
                choice2 = input("Do you want to reset the pool of MadLibs? yes/no: ")
                if str.lower(choice2) == "yes":
                       madLibs = ['a visit to the dentist', 'amusement parks']
                else:
                    break
            else:
                choice = random.choice(madLibs)   
                if choice == "a visit to the dentist":
                               aVisitToTheDentist()
                               madLibs.remove("a visit to the dentist")
                elif choice == "amusement parks":
                               amusementParks()
                               madLibs.remove("amusement parks")
                elif choice == "commencement speech":
                       commencementSpeech()
                       if "commencement speech" in madLibs:
                           madLibs.remove("commencement speech")
            again = input("Do you want to play again? yes/no: ")
            again = str.lower(again)
main()
