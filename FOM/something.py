def BoatSurvive(max):
    boat=[]
    people=[1,2,1,3,2,1,3]
    people.sort()
    print(people)
    end=len(people)
    while people != []:
        c=1
        for i in range(c,end):
            if people[0]+people[i]==max:
                boat.append([people[0],people[i]])
                people.remove(people[0])
                people.remove(people[i])
            else:
                def chain():
                    try:
                        new=people[0]+people[c]
                        if new+people[i]==max:
                            boat.append([people[0]+people[c],people[i]])
                            people.remove(people[0])
                            people.remove(people[c])
                            people.remove(people[i])
                        else:
                            chain()
                    except:
                        print("Bye bye")
                chain()
    return(boat)

print(BoatSurvive(3))