dataBase = []

def getGroupIndexInDatabase(dataBase, group):           #loops through dataBase to check if contains grp name and returns the index
    for i in range(len(dataBase)):                      #return -1 if grp not found on dataBase
        if dataBase[i].get(group) != None:
            return i
    return -1

def inputRecord(dataBase, group, studentId, score):             #input studentId and score into respective group on database
    groupIndex = getGroupIndexInDatabase(dataBase, group)       #get grp index on dataBase
    if (groupIndex == -1):                                      #if grp doesn't exist, create new grp and append id & score
        dataBase.append({group :[{'studentId': studentId, 'score': score}]})
    else:
        groupList = dataBase[groupIndex].get(group)             #if group exist, append id & score to existing group list
        groupList.append({'studentId': studentId, 'score': score})

inputRecord(dataBase, 'grp1', 1, 100)
inputRecord(dataBase, 'grp1', 2, 90)
inputRecord(dataBase, 'grp2', 1, 80)
print(dataBase)