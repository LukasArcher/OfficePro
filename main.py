from queue import Queue
from user_message import *

queues = {
    'A': Queue(),
    'B': Queue(),
    'C': Queue()
}

secret_password = "SECRET"
vip_password = "VIP"


if __name__ == '__main__':
    while True:
        choose = choice().split()
        if choose[0] in queues.keys():
            num = queues[choose[0]].add_user()
            new_user(choose[0], num)
            clear()
        elif choose[0] == secret_password:
            secret_l = secret_choice()
            if secret_l in queues.keys():
                num = queues[secret_l].remove_user()
                next_user(secret_l, num)
                clear()
            else:
                print(error())
                clear()
        elif choose[0] == vip_password:
            vip_l = choose[1]
            if vip_l in queues.keys():
                num = queues[vip_l].add_vip()
                next_user(vip_l, num)
                clear()
            else:
                print(error())
                clear()
        else:
            print(error())
            clear()

