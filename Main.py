from controller.Controller import Controller
from colorama import init, Fore
import requests


class Main:

    @staticmethod
    def main():
        init()

        banner = '''
        _____ _____         _____            
       |_   _|  __ \\       / ____|           
         | | | |__) |_____| |  __  ___  ___  
         | | |  ___/______| | |_ |/ _ \\/ _ \\ 
        _| |_| |          | |__| |  __/ (_) |
       |_____|_|           \\_____|\\___|\\___/ 
       ---------------------------------------
        Created by : Homeless
        Version : 1.0.0
       ---------------------------------------
        '''
        print(Fore.RED + banner)
        ctrl = Controller()

        try:

            while True:
                try:
                    print(Fore.GREEN + "[1] INGRESAR API-KEY MAXMIND.")
                    print(Fore.GREEN + "[2] CONSULTAR IP.")
                    print(Fore.GREEN + "[3] SALIR", end='\n\n')

                    option = int(input("INGRESAR OPCION > "))

                    if option == 1:
                        ctrl.add_api_key()
                        continue

                    elif option == 2:
                        try:
                            ctrl.query_ip()
                            continue
                        except ValueError as ex:
                            print(Fore.RED + "[X] " + ex.__str__(), end= "\n\n")
                    elif option == 3:
                        ctrl.exit_program()
                        continue
                    else:
                        print(Fore.RED + "[X] Opcion no valida", end="\n\n")
                except ValueError:
                    print(Fore.RED + "[X] Opcion no valida", end="\n\n")
                    continue
                except requests.HTTPError as ex:
                    print(Fore.RED + "[X] API-KEY Maxmind: " + ex.__str__(), end="\n\n")
                    continue
        except KeyboardInterrupt:
            exit(0)


if __name__ == '__main__':
  Main.main()
