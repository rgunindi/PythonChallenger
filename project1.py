# N
# project_code1,start_date,end_date,budget
# project_code2,start_date,end_date,budget 

# DD/MM/YYYY

# 10
# project_code1,10/01/2022,20/02/2023,1300
# project_code2,10/02/2022,20/03/2023,1300


# Total budget: 2600
# project_code1,10/01/2022,20/02/2023,1300,Team_1
# project_code2,10/02/2022,20/03/2023,1300,Team_2
nTeamNumber=int(input())
inputVeri=" "
projectList=[]
while inputVeri!="":
    inputVeri=input()
    if inputVeri!="":
        projectList.append(inputVeri)
teamCount=len(projectList)
seperatedDataList=[]
for i in projectList:
    seperatedData=i.split(',')
    seperatedDataList.append(seperatedData)
    # print(seperatedData)
dateList=[]
for i in seperatedDataList:
    seperatedDataList.sort(i[1])

print(seperatedDataList)
print(nTeamNumber)