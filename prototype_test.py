from Schedule_Manager_Class import Schedule_Manager

value = 0

def calc():
    global value
    value += 1
    print("calc value = %d" % value)
    if value == 5:
        scheduler.kill_scheduler("1")

if __name__ == '__main__':

    scheduler = Schedule_Manager()

    scheduler.start_scheduler(calc, 'interval', "1", 1)


