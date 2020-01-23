import json
import re
input = open("inp.txt", "r")
inp = input.readlines()

d_pos = [i for i, x in enumerate(inp) if x[0:8] == "CRITICAL"]
cntr = 0
descriptions = []
services = []
report = {}
host = ""
ind = 0
try:
    while ind <= len(inp):
        if cntr == 0:
            host = inp[ind][:-1]
            cntr += 1
        elif cntr == 1:
            cntr += 1
        elif cntr == 2:
            services.append(inp[ind][:-1])
            cntr += 1
        elif cntr == 3:
            descriptions.append(inp[ind][:-1])
            cntr += 1
        else:
            if ind + 1 in d_pos:
                while ind + 1 in d_pos:
                    services.append(inp[ind][:-1])
                    ind += 1
                    descriptions.append(inp[ind][:-1])
                report[host] = [services, descriptions]
            else:
                report[host] = [services, descriptions]
                ind -= 1
            host = ""
            services = []
            descriptions = []
            cntr = 0
        ind += 1
except:
    pass

str = ""
f = open("out.txt", "w")
for host, arr in report.items():
    services = arr[0]
    descriptions = arr[1]
    for i in range(len(services)):
        temp = re.findall(r'\S+', descriptions[i])
        lastcheck = temp[1] + " " + temp[2]
        duration = temp[3] + " " + temp[4] + " " + temp[5] + " " + temp[6]
        status = " ".join(temp[8:])
        str = "NAGIOS {}, {}, {} (Last Check) {} (Duration) {}\n".format(host, services[i], lastcheck, duration, status)
        f.write(str)
f.close()
input.close()
