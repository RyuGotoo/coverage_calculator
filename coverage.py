import random

NUM_SERVERS = 20
ACCESS_TIMES = 59

# calculate coverage of accessed servers many times
coverage_list = []
for _ in range(10000):
    # define server model
    class Server(object):
        def __init__(self):
            self.count = 0

        def access(self):
            self.count += 1
            return self.count

    # create server instances
    servers = []
    for _ in range(NUM_SERVERS):
        servers.append(Server())

    # access servers at random
    for _ in range(ACCESS_TIMES):
        rnd = random.randint(0, NUM_SERVERS-1)
        servers[rnd].access()

    # count accessed servers
    accessed_servers_num = 0
    for i in range(NUM_SERVERS):
        if servers[i].count > 0:
            accessed_servers_num += 1

    # calculate coverage of accessed servers
    coverage = accessed_servers_num / NUM_SERVERS

    # append the coverage
    coverage_list.append(coverage)

# output
avg_coverage = sum(coverage_list) / len(coverage_list)
print('access times:', ACCESS_TIMES)
print('number of servers:', NUM_SERVERS)
print('number of accessed servers:', round(NUM_SERVERS * avg_coverage, 1))
print('coverage:', round(avg_coverage * 100, 1), '%')
