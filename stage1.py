import json
import os



def saveDelimiter(labels):
    wordTokens = labels.copy()
    newTokens = []
    for itr in wordTokens:
        if(itr == "and"):
            newTokens.append("savedDelimiter")
        else:
            newTokens.append(itr)
    return newTokens.copy()

def cleanUp(tagged):
    newTagged = []
    with open(os.path.abspath('corpus.json')) as jFile:
        jsonDict = json.load(jFile)
    for listElement in tagged:
        if (jsonDict.get('elements')).get(listElement) != None :
            newTagged.append({"element":listElement})
        elif (jsonDict['attributes']).get(listElement) != None:
            newTagged.append({"attribute":listElement})
        elif (jsonDict['value']).get(listElement) != None:
              newTagged.append({"value":listElement})
             
    return newTagged
        


def finalProccess(key, finalDict):
    attribList = finalDict[key]['attribute']
    valueList = finalDict[key]['value'] 
    temp = []
    temp2 = []
    print("Latest attrib and value list -> ",attribList,valueList)
    while attribList[-1] != "savedDelimiter":
        temp.append(attribList.pop())
        temp2.append(valueList.pop())
    
    #print(temp)
    #print(temp2)
    return temp.copy(), temp2.copy()


def getTagSet(tagged):
    
    print("tagged original  -> ",tagged)
    tagged = cleanUp(tagged)
    #
    finalDict = {}
    valuesList = []
    attribList = []
    elementList = []
    with open(os.path.abspath('corpus.json')) as jFile:
        jsonDict = json.load(jFile)

    key = 0
    
    readytoBreak = 100
    for listElement in tagged:
        
        #print(listElement)

        if  listElement.get('attribute') != None:
            attribList.append(listElement.get('attribute'))
            readytoBreak += 1
        if  listElement.get('value') != None:
            valuesList.append(listElement.get('value'))
            readytoBreak -= 1


        if listElement.get('element') != None:
            if len(attribList) > 0 and len(valuesList) > 0 :
                finalDict[key] = {
                "element": elementList.copy(),
                "attribute": attribList.copy(),
                "value": valuesList.copy()
                }
                key += 1
                elementList.clear()
                attribList.clear()
                valuesList.clear()
                readytoBreak = 0 
            
            ele  = listElement.get('element')
            elementList.append(ele)
            print("Element -> ",ele)
            print("key -> ",key)
            print("len attrib list -> ",len(attribList))
            print("len value list -> ",len(valuesList))

            


        
  



    if len(elementList) > 0 and len(attribList) == 0 and len(valuesList) == 0:
        attribList,valuesList  = finalProccess(key-1, finalDict)
        finalDict[key] = {
        "element": elementList.copy(),
        "attribute": attribList.copy(),
        "value": valuesList.copy()
        }
        elementList.clear()
        attribList.clear()
        valuesList.clear()
    else:
        finalDict[key] = {
        "element": elementList.copy(),
        "attribute": attribList.copy(),
        "value": valuesList.copy()
        }
        elementList.clear()
        attribList.clear()
        valuesList.clear()
    


    #print("->>>>>>>>>>>>>>> Elements  ",elementList)
    #print("->>>>>>>>>>>>>>> Attributes  ",attribList)
    print("\n___________________________________________________________________________________________________________")
    print("FINAL DICT -> ")
    for key,value in finalDict.items():
        print(key," -> ",value)
    print("___________________________________________________________________________________________________________\n")
    
    return finalDict

    


    #print(data)

 


















#getTagSet("a")