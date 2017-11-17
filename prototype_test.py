from Schedule_Manager_Class import Schedule_Manager

value = 0

def calc():
    global value
    value += 1
    print("calc value = %d" % value)

if __name__ == '__main__':

    scheduler = Schedule_Manager()

    scheduler.start_scheduler(calc, 'interval', "1", 5)

    if value == 5:
        scheduler.kill_scheduler("1")


