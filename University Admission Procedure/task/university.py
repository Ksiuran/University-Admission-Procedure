
def popdep(app, apps, dep, count, maxapp, name, loc):
    if len(dep) == maxapp:
        return
    else:
        i = len(dep)
        count = count + i
        it = 0
        if count >= maxapp:
            while i < maxapp:
                if app[it][loc] == name:
                    # I really tried to avoid ifs in this part but I have to for implementing the special score
                    ifblock(app, apps, dep, name, it)
                    i += 1
                else:
                    it += 1
        else:
            while i < count:
                if app[it][loc] == name:
                    ifblock(app, apps, dep, name, it)
                    i += 1
                else:
                    it += 1
            return


def ifblock(app, apps, dep, name, it):
    if name == "Biotech":
        if app[it][12] > apps[it][6]:
            dep.append([app[it][0], app[it][1], app[it][12]])
            apps.remove(app[it])
            app.remove(app[it])
        elif app[it][12] == apps[it][6]:
            if app[it][0] < apps[it][0]:
                dep.append([app[it][0], app[it][1], app[it][12]])
                apps.remove(app[it])
                app.remove(app[it])
            elif app[it][0] == apps[it][0]:
                if app[it][1] < apps[it][1]:
                    dep.append([app[it][0], app[it][1], app[it][12]])
                    apps.remove(app[it])
                    app.remove(app[it])
                else:
                    dep.append([apps[it][0], apps[it][1], apps[it][6]])
                    app.remove(apps[it])
                    apps.remove(apps[it])
            else:
                dep.append([apps[it][0], apps[it][1], apps[it][6]])
                app.remove(apps[it])
                apps.remove(apps[it])
        else:
            dep.append([apps[it][0], apps[it][1], apps[it][6]])
            app.remove(apps[it])
            apps.remove(apps[it])
    elif name == "Chemistry":
        if app[it][3] > apps[it][6]:
            dep.append([app[it][0], app[it][1], app[it][3]])
            apps.remove(app[it])
            app.remove(app[it])
        elif app[it][3] == apps[it][6]:
            if app[it][0] < apps[it][0]:
                dep.append([app[it][0], app[it][1], app[it][3]])
                apps.remove(app[it])
                app.remove(app[it])
            elif app[it][0] == apps[it][0]:
                if app[it][1] < apps[it][1]:
                    dep.append([app[it][0], app[it][1], app[it][3]])
                    apps.remove(app[it])
                    app.remove(app[it])
                else:
                    dep.append([apps[it][0], apps[it][1], apps[it][6]])
                    app.remove(apps[it])
                    apps.remove(apps[it])
            else:
                dep.append([apps[it][0], apps[it][1], apps[it][6]])
                app.remove(apps[it])
                apps.remove(apps[it])
        else:
            dep.append([apps[it][0], apps[it][1], apps[it][6]])
            app.remove(apps[it])
            apps.remove(apps[it])
    elif name == "Engineering":
        if app[it][11] > apps[it][6]:
            dep.append([app[it][0], app[it][1], app[it][11]])
            apps.remove(app[it])
            app.remove(app[it])
        elif app[it][11] == apps[it][6]:
            if app[it][0] < apps[it][0]:
                dep.append([app[it][0], app[it][1], app[it][11]])
                apps.remove(app[it])
                app.remove(app[it])
            elif app[it][0] == apps[it][0]:
                if app[it][1] < apps[it][1]:
                    dep.append([app[it][0], app[it][1], app[it][11]])
                    apps.remove(app[it])
                    app.remove(app[it])
                else:
                    dep.append([apps[it][0], apps[it][1], apps[it][6]])
                    app.remove(apps[it])
                    apps.remove(apps[it])
            else:
                dep.append([apps[it][0], apps[it][1], apps[it][6]])
                app.remove(apps[it])
                apps.remove(apps[it])
        else:
            dep.append([apps[it][0], apps[it][1], apps[it][6]])
            app.remove(apps[it])
            apps.remove(apps[it])
    elif name == "Physics":
        if app[it][10] > apps[it][6]:
            dep.append([app[it][0], app[it][1], app[it][10]])
            apps.remove(app[it])
            app.remove(app[it])
        # picks based on name if scores are the same
        elif app[it][10] == apps[it][6]:
            if app[it][0] < apps[it][0]:
                dep.append([app[it][0], app[it][1], app[it][10]])
                apps.remove(app[it])
                app.remove(app[it])
            elif app[it][0] == apps[it][0]:
                if app[it][1] < apps[it][1]:
                    dep.append([app[it][0], app[it][1], app[it][10]])
                    apps.remove(app[it])
                    app.remove(app[it])
                else:
                    dep.append([apps[it][0], apps[it][1], apps[it][6]])
                    app.remove(apps[it])
                    apps.remove(apps[it])
            else:
                dep.append([apps[it][0], apps[it][1], apps[it][6]])
                app.remove(apps[it])
                apps.remove(apps[it])
        else:
            dep.append([apps[it][0], apps[it][1], apps[it][6]])
            app.remove(apps[it])
            apps.remove(apps[it])
    else:
        if app[it][4] > apps[it][6]:
            dep.append([app[it][0], app[it][1], app[it][4]])
            apps.remove(app[it])
            app.remove(app[it])
            # picks based on name if scores are the same
        elif app[it][4] == apps[it][6]:
            if app[it][0] < apps[it][0]:
                dep.append([app[it][0], app[it][1], app[it][4]])
                apps.remove(app[it])
                app.remove(app[it])
            elif app[it][0] == apps[it][0]:
                if app[it][1] < apps[it][1]:
                    dep.append([app[it][0], app[it][1], app[it][4]])
                    apps.remove(app[it])
                    app.remove(app[it])
                else:
                    dep.append([apps[it][0], apps[it][1], apps[it][6]])
                    app.remove(apps[it])
                    apps.remove(apps[it])
            else:
                dep.append([apps[it][0], apps[it][1], apps[it][6]])
                app.remove(apps[it])
                apps.remove(apps[it])
        else:
            dep.append([apps[it][0], apps[it][1], apps[it][6]])
            app.remove(apps[it])
            apps.remove(apps[it])
    return


def printdep(dep, name):
    with open(f"{name}.txt.", "w") as f:
        for i in dep:
            print(i[0], i[1], i[2], file=f)

    return


maxa = int(input())
# populate applicants from file
applicants = list()
with open("applicants.txt", "r") as f:
    for line in f:
        line = line.strip()
        applicants.append(line.split(" "))

# create department lists
Biotech = list()
Chemistry = list()
Engineering = list()
Mathematics = list()
Physics = list()

# make the gpa a float
for n in applicants:
    n[2] = float(n[2])
    n[3] = float(n[3])
    n[4] = float(n[4])
    n[5] = float(n[5])
    n[6] = float(n[6])

# create a copy of the current list, for later
applis = applicants.copy()

# create the extra mean scores
for n in range(len(applicants)):
    # score for phys
    applicants[n].append(((applicants[n][4] + applicants[n][2]) / 2))
    # score for engi
    applicants[n].append(((applicants[n][5] + applicants[n][4]) / 2))
    # score for bio
    applicants[n].append(((applicants[n][3] + applicants[n][2]) / 2))

z = 7
while z != 10:
    # get the count of people with each dep as their prio
    priolist = [sublist[z] for sublist in applicants]
    bioc = priolist.count("Biotech")
    chemc = priolist.count("Chemistry")
    engc = priolist.count("Engineering")
    mathc = priolist.count("Mathematics")
    physc = priolist.count("Physics")

    # sort the forked list by dep, special score descending, fname, and lname
    applis = sorted(applis, key=lambda x: (x[z], -x[6], x[0], x[1]))
    # build departments based off prio
    # sort by department, score, descending, fname, lname. for bio
    applicants = sorted(applicants, key=lambda x: (x[z], -x[12], x[0], x[1]))
    popdep(applicants, applis, Biotech, bioc, maxa, "Biotech", z)
    # sort by department, score, descending, fname, lname. for chem
    applicants = sorted(applicants, key=lambda x: (x[z], -x[3], x[0], x[1]))
    popdep(applicants, applis, Chemistry, chemc, maxa, "Chemistry", z)
    # sort by department, score, descending, fname, lname. for Engineering
    applicants = sorted(applicants, key=lambda x: (x[z], -x[11], x[0], x[1]))
    popdep(applicants, applis, Engineering, engc, maxa, "Engineering", z)
    # sort by department, score, descending, fname, lname. for Math
    applicants = sorted(applicants, key=lambda x: (x[z], -x[4], x[0], x[1]))
    popdep(applicants, applis, Mathematics, mathc, maxa, "Mathematics", z)
    # sort by department, score, descending, fname, lname. for Phys
    applicants = sorted(applicants, key=lambda x: (x[z], -x[10], x[0], x[1]))
    popdep(applicants, applis, Physics, physc, maxa, "Physics", z)

    z += 1

# resort just in case
Biotech = sorted(Biotech, key=lambda x: (-x[2], x[0], x[1]))
Chemistry = sorted(Chemistry, key=lambda x: (-x[2], x[0], x[1]))
Engineering = sorted(Engineering, key=lambda x: (-x[2], x[0], x[1]))
Mathematics = sorted(Mathematics, key=lambda x: (-x[2], x[0], x[1]))
Physics = sorted(Physics, key=lambda x: (-x[2], x[0], x[1]))

# write files
printdep(Biotech, "Biotech")
printdep(Chemistry, "Chemistry")
printdep(Engineering, "Engineering")
printdep(Mathematics, "Mathematics")
printdep(Physics, "Physics")
