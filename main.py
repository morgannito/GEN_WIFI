data = {}
with open('compte_wifi_2.txt', 'r') as f_in:
    data2 = ""
    user=""
    password=""

    for line in f_in:

        line = line.split()
        if (line[0] == "Username"):
            user = line[2]
            # print(line[2])
        if (line[0] == "Password"):
            password = line[2]
            # print(line[2])
        if (user):
            if(password):
                print(user + "," + password)
                user = ""
                password = ""

