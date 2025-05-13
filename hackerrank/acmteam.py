def acmTeam(topic):
    teams = list(itertools.combinations(topic, 2))
    subjects = []
    for team in teams:
        known = 0
        for topic in range(len(team[0])):
            if team[0][topic] == "1" or team[1][topic] == "1":
                known += 1
        subjects.append(known)
    return [max(subjects), subjects.count(max(subjects))]