users = {}

with open('DATA/passwd') as passwd_in:
    for raw_line in passwd_in:
        line = raw_line.strip()
        computer_name, password, inbound_port, outbound_port, user, home_dir, shell = line.split(':')
        if shell == "":
            shell = "NONE"
        #print(computer_name, password, inbound_port, outbound_port, user, home_dir, shell)

        if shell in users:
            users[shell] += 1
        else:
            users[shell] = 1

for shell, count in users.items():
    print("{:5d} {}".format(count, shell))
