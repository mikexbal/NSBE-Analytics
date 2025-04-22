import pandas as pd

#Types of functions:
#Get member who comes to most events - Attendance DONE
#Get most common major -
#Get Breakdown of school years
#Total amount of members - Roster DONE
#Total amount of eboard members - Roster DONE
#Calculate points w spreadsheet and point breakdown (Attendance)
#Grab email from members - Roster

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

get_most_active_member('../data/NSBEAttendance_2025.csv')








