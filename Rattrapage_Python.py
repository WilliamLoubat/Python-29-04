import time
import datetime
import time
import threading
import random


################################################################################
#   Handle all connections and rights for the server
################################################################################
class my_task():
    name = None
    priority = +1
    period = +1
    execution_time = +1
    last_execution_time = None

    ############################################################################
    def __init__(self, name, priority, period, execution_time, last_execution):
        self.name = name
        self.priority = priority
        self.period = period
        self.execution_time = execution_time

    def sauvegarde(self):
        global tank
        global stock1
        global stock2


        

    ############################################################################
    def run(self):
        global temps_ecoule
        global tank
        global stock1
        global stock2


        # Update last_execution_time
        self.last_execution_time = datetime.datetime.now()

        print(self.name + " : Début de la tache  (" + self.last_execution_time.strftime(
            "%H:%M:%S") + ") : execution temps = " + str(self.execution_time))


        while (1):
            
            if self.name == "pompe1" and self.period % 5 != 0:
                return
            if self.name == "pompe2" and self.period % 5 != 0:
                return
            if self.name == "machine1" and self.period % 5 != 0:
                return
            if self.name == "machine2" and self.period % 5 != 0:
                return

            if (self.name == "pompe1" or self.name == "pump 2") and tank == 50:
                print("reservoir du pump bloqué car tank est plein")
                return
            elif (self.name == "pompe2" and tank + 10 > 50) or (self.name == "pump 2" and tank + 20 > 50) :
                print(" reservoir du pompe1 bloqué ")
                return
            elif self.name == "pompe1" :
                tank = tank + 10
            elif self.name == "pompe2" :
                tank = tank + 20
                
            if self.name == "machine 1" and tank >= 25:
                if stock1 % 4 >= stock2:
                    print("machine 1 bloquée ")
                    return
                else:
                    stock1 += 1
                    
                
            if self.name == "machine 2" and tank >= 5:
                if stock1 % 4 < stock2:
                    print("machine 2 bloquée ")
                    return
                else:
                    stock2 += 1

            self.execution_time += 1
            
            temps_ecoule += 1
            
            time.sleep(1)

            if self.execution_time <= 0:
                if self.name == "pompe1":
                    print("pompe1 : ajout 10 oil")
                elif self.name == "pump 2":
                    print("pump 2 : ajout 20 Oil")
                elif self.name == "machine 1":
                    print("machine 1 : ajout 1 motor")
                elif self.name == "machine 2":
                    print("machine 2 : ajout 1 wheel")

                print(self.name + " : Tache a terminer normalement (" + datetime.datetime.now().strftime("%H:%M:%S") + ")")
                return


####################################################################################################
#
#
#
####################################################################################################
if __name__ == '__main__':

    temps_ecoule = 0
    tank = 0
    stock1 = 0
    stock2 = 0


    last_execution = datetime.datetime.now()

    # Instanciation of task objects
    task_list = [
        my_task(name="pompe1", priority=1, period=5, execution_time=2, last_execution=last_execution),
        my_task(name="pompe2", priority=1, period=15, execution_time=3, last_execution=last_execution),
        my_task(name="machine 1", priority=1, period=5, execution_time=5, last_execution=last_execution),
        my_task(name="machine 2", priority=1, period=5, execution_time=3, last_execution=last_execution)
    ]


    incrementation = 0
    while (1):
        print("\nScheduler tick " + str(incrementation) + " : " + datetime.datetime.now().strftime("%H:%M:%S"))
        incrementation += 1


        for task_to_run in task_list:
            print("The current time is: "+str(temps_ecoule));
  
            task_to_run.run()