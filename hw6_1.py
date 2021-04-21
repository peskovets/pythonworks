from time import sleep

class Trafficlight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        n = 0
        while n != 3:
                print(self.__color[n])
                if n == 0:
                    sleep(7)
                elif n == 1:
                    sleep(2)
                elif n == 2:
                    sleep(6)
                n +=1

a = Trafficlight()
a.running()





