import random

'''
totalS = int(input("How many students are there? "))

for i in range(totalS):
    s = input("Student name and info eg. name, 0/1, 0/1: ")
'''

# students
# list of tuples for house prefects [name, citizenship, christian]

excos = [
    ("Jin Kawaso", 0, 0, 0),  # if Singaporean = 1, if Christian = 1, if boy = 0
    ("Abigail Kastono Ahadi", 1, 1, 1),
    ("Natalie Chew Jiaxian", 1, 1, 1),
    ("Yoona Son (Iris)", 0, 0, 1),
    ("Samuel Agra Sianipar", 1, 1, 0),
    ("Elizabeth Chia Kay Yan", 1, 1, 1)
]

schoolPre = [
    ("Ko Bomin (Bonnie)", 1, 0),  # if Singaporean = 1, if Christian = 1
    ("Yang Nayoung", 1, 1),
    ("Lucas Leong Joe-Yii", 1, 1),
    ("Le Quoc Thai", 0, 0),
    ("Wu Yanyu (Rita)", 1, 1),
    ("Jesslyn Goh", 1, 1),
    ("Erica Molenberg", 1, 0),
    ("Jesslyne Yau", 1, 1),
    ("Cheng Xirui", 0, 0),
    ("Lee Chaehyeon", 1, 1),
    ("Cheng Yingfei (Selina)", 0, 0),
]

housePre = [
    ("Skyler", 1, 0),
    ("Le Han", 1, 1),  # if Singaporean = 1, if Christian = 1
    ("Shreya", 1, 1),
    ("Jiayi", 0, 0),
    ("Donohue", 1, 1)
]

# dictionary of duties
duties = {
    "EXCO's Supervision": "",
    "Foyer": "",
    "Skirt Escort": "",
    "PA Supervisor": "",
    "Prayer": "",
    "Pledge": "",
    "Back gate": "",
    "Flag Raising": "",
}

Fri_duties = {
    "Chapel Stage": "",
    "Chapel Escort": "",
    "Tie Selling": "",
}

Wed_duties = {
    "Assembly Stage": "",
    "Assembly Escort": "",
}

totalS = len(excos) + len(housePre) + len(schoolPre)
# print(totalS)

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


def allocation(exc, sp, hp):

    # iterating through days
    for d in days:

        # iterating through regular duties
        for i in duties:
            # getting random integer to choose student from the lists
            ran_e = random.randint(0, len(exc) - 1)
            ran_h = random.randint(0, len(hp) - 1)

            # checking for the unique duties that have conditions to them eg. require students from different lists
            if i == "EXCO's Supervision":
                # calling the function to get the 2 names from the exc list
                duties[i] = rand_s(exc, 2)

            elif i == "PA Supervisor":
                duties[i] = rand_s(sp, 1)

            elif i == "Skirt Escort" and exc[ran_e][3] == 0:
                rand_s_conditional(exc, 3, 1, i)

            elif i == "Back gate":
                duties[i] = rand_s(sp, 2) + ", " + rand_s(hp, 2)

            elif i == "Prayer" and hp[ran_h][2] == 0:
                rand_s_conditional(hp, 2, 1, i)

            elif i == "Pledge" and hp[ran_h][1] == 0:
                rand_s_conditional(hp, 1, 1, i)

            else:
                # first person is school prefect, second two are house prefects
                duties[i] = rand_s(sp, 1) + ", " + rand_s(hp, 2)

        # formatting the terminal output
        print(d)
        print(duties)

        # iterating through Wednesday Duties
        if d == "Wednesday":
            for i in Wed_duties:
                Wed_duties[i] = rand_s(exc, 2)
            print(Wed_duties)

        # iterating through Friday Duties
        if d == "Friday":
            for i in Fri_duties:
                if i == "Tie Selling":
                    Fri_duties[i] = rand_s(exc, 1)
                else:
                    Fri_duties[i] = rand_s(exc, 2)
            print(Fri_duties)
        print()

        # terminal table print attempt
        '''print("                                 " + d, end="")
    print()
    for i in duties:
        print(i)'''


def rand_s(db, n):  # getting random person n number of times from db
    s = ""

    temp = -1  # number that cannot equal to a iteration of db (used to mitigate repeats)

    for i in range(n):
        ran = random.randint(0, len(db) - 1)
        # print(ran)
        if not temp == ran:  # attempt to reduce repeats
            s += db[ran][0]
            temp = ran
        elif ran == temp == 0:
            s += db[ran + 1][0]
        else:
            s += db[ran // 2][0]

        if not i - n + 1 == 0:
            s += ", "

    return s


def rand_s_conditional(db, iter_num, correct_num, duty):  # getting random person but with conditions
    ran = 0
    while ran < len(db) - 1:
        ran += 1
        if db[ran][iter_num] == correct_num:
            duties[duty] = db[ran][0]


allocation(excos, schoolPre, housePre)


