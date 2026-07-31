import sys
import Marvellous

#-----------------------------------------------------------
# Function Name : DisplayAllProcesses
# Description : Displays information of all running processes
#-----------------------------------------------------------

def DisplayAllProcesses():

    ProcessList = Marvellous.GetAllProcesses()

    if(len(ProcessList) == 0):
        print("No running process found")
        return

    Border = "-" * 80

    print(Border)
    print("Running Process Information")
    print(Border)
    print("{:<10}{:<35}{}".format("PID","Process Name","Username"))
    print(Border)

    for Process in ProcessList:

        print("{:<10}{:<35}{}".format(
            Process["pid"],
            Process["name"],
            Process["username"]
        ))

    print(Border)

#-----------------------------------------------------------
# Function Name : DisplaySpecificProcess
# Description : Displays information of specified process
#-----------------------------------------------------------

def DisplaySpecificProcess(ProcessName):

    ProcessList = Marvellous.GetProcessByName(ProcessName)

    if(len(ProcessList) == 0):

        print("Process not found")
        return

    Border = "-" * 80

    print(Border)
    print("Process Information")
    print(Border)

    for Process in ProcessList:

        print("PID :",Process["pid"])
        print("Name :",Process["name"])
        print("Username :",Process["username"])
        print(Border)

#-----------------------------------------------------------
# Function Name : main
# Description : Entry point
#-----------------------------------------------------------

def main():

    if(len(sys.argv) == 1):

        DisplayAllProcesses()

    elif(len(sys.argv) == 2):

        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):

            print("This automation script displays running process information.")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):

            print("Usage :")
            print("python ProcInfo.py")
            print("python ProcInfo.py ProcessName")

        else:

            DisplaySpecificProcess(sys.argv[1])

    else:

        print("Invalid number of arguments")
        print("Use --h for help")
        print("Use --u for usage")

#-----------------------------------------------------------

if __name__ == "__main__":
    main()