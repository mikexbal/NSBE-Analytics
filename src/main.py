import pandas as pd

#Types of functions:
#Get member who comes to most events - Attendance DONE
#Get most common major -
#Get Breakdown of school years
#Total amount of members - Roster DONE
#Total amount of eboard members - Roster DONE
#Calculate points w spreadsheet and point breakdown (Attendance)
#Grab email from members - Roster

#All csv files should be placed into the data folder
#To use filename in function follow this format: "../data/[filename].csv"


def print_members(filename):
    df = pd.read_csv(filename)
    print(df.to_string())

def get_total_member_count(filename):
    df = pd.read_csv(filename)
    members = df[['Name', 'Member/Eboard', ]]
    distinct_members = members.drop_duplicates()
    total_members = len(distinct_members)
    eboard_count = df['Member/Eboard'].value_counts().get('E-Board', "Can't be found")
    member_count = df['Member/Eboard'].value_counts().get('Member', "Can't be found")

    print(f"Total Members: {total_members}\n"
          f"Total E-Board Members: {eboard_count}\n"
          f"Total Regular Members: {member_count}")

def get_most_active_member(filename):
    df = pd.read_csv(filename)
    members = df['Name']
    most_active_member = members.value_counts().index[0]
    attendance_count = members.value_counts()[most_active_member]

    print(f"The most active member is {most_active_member}, with {attendance_count} entires!")

def get_member_emails(filename, name):
    df = pd.read_csv(filename)
    member = df[df['Name'] == name][['Name', 'Email']]
    print(member)

def get_academic_years(filename):
    df = pd.read_csv(filename)
    freshman_count = df['Year'].value_counts().get('Freshman', "Can't be found")
    sophmore_count = df['Year'].value_counts().get('Sophmore', "Can't be found")
    junior_count = df['Year'].value_counts().get('Junior', "Can't be found")
    senior_count = df['Year'].value_counts().get('Senior', "Can't be found")
    grad_count = df['Year'].value_counts().get('Grad Student', "Can't be found")
   
    print(f'''
    Frehsman = {freshman_count}
    Sophmore = {sophmore_count}
    Junior = {junior_count}
    Senior = {senior_count}
    Grad Student = {grad_count}''')

def get_academic__major_count(filename):
    df = pd.read_csv(filename)
    #Majors = Arch, Biomed, Biophy, Civil, Comp, Con, Cyber, Elec, Eng, Env, Indu, Info, Man, Mech, MechTech, Neuro, Undecl
    major_counts = df['Major/Minor'].str.lower().str.strip().value_counts()

    print(major_counts)

    #clean_majors = majors.str.strip().str.title()
    #print(clean_majors)
   
    
get_academic__major_count("../data/NSBEMajors_24-25.csv")











