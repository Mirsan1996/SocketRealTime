from threading import Thread

def client_0():
    import integers.suscriptorN_0
def client_1():
    import integers.suscriptorN_1
def client_2():
    import integers.suscriptorN_2
def client_3():
    import integers.suscriptorN_3
def client_4():
    import integers.suscriptorN_4
def client_5():
    import integers.suscriptorN_5
def client_6():
    import integers.suscriptorN_6
def client_7():
    import integers.suscriptorN_7
def client_8():
    import integers.suscriptorN_8
def client_9():
    import integers.suscriptorN_9
def client_10():
    import integers.suscriptorT_10
def client_11():
    import integers.suscriptorT_11
def client_12():
    import integers.suscriptorT_12
def client_13():
    import integers.suscriptorT_13
def client_14():
    import integers.suscriptorT_14
def client_15():
    import integers.suscriptorT_15
def client_16():
    import integers.suscriptorT_16
def client_17():
    import integers.suscriptorT_17
def client_18():
    import integers.suscriptorT_18
def client_19():
    import integers.suscriptorT_19

if __name__=='__main__':
    threads = []
    threads.append(Thread(target=client_0))
    threads.append(Thread(target=client_1))
    threads.append(Thread(target=client_2))
    threads.append(Thread(target=client_3))
    threads.append(Thread(target=client_4))
    threads.append(Thread(target=client_5))
    threads.append(Thread(target=client_6))
    threads.append(Thread(target=client_7))
    threads.append(Thread(target=client_8))
    threads.append(Thread(target=client_9))
    threads.append(Thread(target=client_10))
    threads.append(Thread(target=client_11))
    threads.append(Thread(target=client_12))
    threads.append(Thread(target=client_13))
    threads.append(Thread(target=client_14))
    threads.append(Thread(target=client_15))
    threads.append(Thread(target=client_16))
    threads.append(Thread(target=client_17))
    threads.append(Thread(target=client_18))
    threads.append(Thread(target=client_19))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
