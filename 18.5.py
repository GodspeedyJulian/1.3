ScoreDate=input("input score date")
Filehandler=open("scoreDetails.txt","a")
MembershipNumber=input("input the membership number")
while MembershipNumber !="":
    Score=input("Input the score")
    while int(Score)<50 or int(Score)>99:
        Score = input("input the Score")
    Filedata = MembershipNumber + ScoreDate + Score
    Filehandler.append = Filedata
    Membershipnumber=input("input the membership number")
closefile()
