Debug = False
from collections import defaultdict

DB_order = defaultdict(dict)
DB_user = defaultdict(list)

def to_unix_ts(x):
#     TODO: from min to sec
    return x * 60

def is_late(X, Y, K, ordered_at, finished_at, arrived_at, started_at):
    # проверить что пассажир сел в течении бесплатного времени ожидания
    X, Y, K = list(map(to_unix_ts, [X, Y, K]))
    late = finished_at - ((X + Y + K) + ordered_at)
    if started_at < arrived_at + K and \
       0 < late:
        return True, late
    return False, 0

def solve(N, K):
    global DB_order
    global DB_user
    users = defaultdict(int)
    for user, orders in DB_user.items():
        for order_id in orders:
            if Debug:
                print(len(DB_order[order_id]))
            if len(DB_order[order_id]) < 6:
                continue
            X = DB_order[order_id]['X']
            Y = DB_order[order_id]['Y']
            ordered_at = DB_order[order_id]['ordered']
            finished_at = DB_order[order_id]['finished']
            arrived_at = DB_order[order_id]['arrived']
            started_at = DB_order[order_id]['started']
            t, late = is_late(X, Y, K, ordered_at, finished_at, arrived_at, started_at)
            if t:
                users[user] += late
    if not users:
        return '-'
    users = sorted(users.items(), reverse=True, key=lambda x: (x[1], x[0]))
    res = [x[0] for x in users[:N]]
    if res:
        s = f"{res[0]}"
        for i in res[1:]:
            s += f" {i}"
        return s
    else:
        return '-'




def common_command(field_name, l):
    global DB_order
    orderd_id, t = l
    DB_order[orderd_id][field_name] = int(t)

def read_command(s):
    global DB_order
    global DB_user

    l = s.split()
    command = l[0]
    if Debug:
        print(l)
    if command == 'ordered':
        order_id, user_id, ordered_at, X, Y = l[1:]
        DB_order[order_id]['ordered'] = int(ordered_at)
        DB_order[order_id]['X'] = int(X)
        DB_order[order_id]['Y'] = int(Y)
        DB_user[user_id].append(order_id)
    else:
        # started, finished, arrived
        common_command(command, l[1:])

if __name__ == "__main__":
    x = int(input())
    for i in range(x):
        DB_order = defaultdict(dict)
        DB_user = defaultdict(list)

        q = input()
        if Debug:
            print(q)
        s, N, K = list(map(int, q.split()))
        l = []
        for j in range(s):
            read_command(input())
        print(solve(N, K))
