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
        choose = choice()
        if choose in queues.keys():
            num = queues[choose].add_user()
            new_user(choose, num)
            clear()
        elif choose == secret_password:
            secret_l = secret_choice()
            if secret_l in queues.keys():
                num = queues[secret_l].remove_user()
                next_user(secret_l, num)
                clear()
            else:
                print(error())
                clear()
        elif choose == vip_password:
            vip_l = vip_choice()
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

