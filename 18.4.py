def ItemProcess(AddItem, InString):
    RetFlag  = False
    if AddItem = "Yes":
        RetFlag = AddToList(InString)
    else:
        RemoveFromList(InString)
    return RetFlag
