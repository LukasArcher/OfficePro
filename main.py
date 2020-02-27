from queue import Queue
from user_messages import UserInterface
from exepcions import EmptyQueue, InvalidCommand

queues = {
    'A': Queue(),
    'B': Queue(),
    'C': Queue()
}

secret_password = "SECRET"
vip_password = "VIP"
user_interface = UserInterface()


if __name__ == '__main__':
    while True:
        choose = user_interface.choice().split()
        try:
            if choose[0] in queues.keys() and len(choose) == 1:
                num = queues[choose[0]].add_user()
                user_interface.new_user(choose[0], num)
                user_interface.clear()
            elif choose[0] == secret_password and len(choose) == 1:
                secret_l = user_interface.secret_choice()
                if secret_l in queues.keys():
                    try:
                        num = queues[secret_l].remove_user()
                    except EmptyQueue:
                        num = None
                    user_interface.next_user(secret_l, num)
                    user_interface.clear()
                else:
                    raise InvalidCommand("Invalid command!")
            elif choose[0] == vip_password and len(choose) == 2:
                vip_l = choose[1]
                if vip_l in queues.keys():
                    num = queues[vip_l].add_vip()
                    user_interface.next_user(vip_l, num)
                    user_interface.clear()
                else:
                    raise InvalidCommand("Invalid command!")
            else:
                raise InvalidCommand("Invalid command!")
        except InvalidCommand:
            print("I don't understand that command...")
            user_interface.clear()

