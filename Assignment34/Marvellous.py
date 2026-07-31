import psutil
import os
import time

#-----------------------------------------------------------
# Function Name : GetAllProcesses
# Description : Returns list of all running processes
#-----------------------------------------------------------

def GetAllProcesses():

    ProcessList = []

    for proc in psutil.process_iter():

        try:
            Info = proc.as_dict(attrs = ['pid','name','username'])
            ProcessList.append(Info)

        except (psutil.NoSuchProcess,
                psutil.AccessDenied):
            pass

    return ProcessList

#-----------------------------------------------------------
# Function Name : GetProcessByName
# Description : Returns information of specific process
#-----------------------------------------------------------

def GetProcessByName(ProcessName):

    ProcessList = []

    for proc in psutil.process_iter():

        try:
            Info = proc.as_dict(attrs = ['pid','name','username'])

            if Info['name'] != None:

                if Info['name'].lower() == ProcessName.lower():

                    ProcessList.append(Info)

        except (psutil.NoSuchProcess,
                psutil.AccessDenied):
            pass

    return ProcessList

#-----------------------------------------------------------
# Function Name : CreateDirectory
# Description : Creates directory if it does not exist
#-----------------------------------------------------------

def CreateDirectory(DirName):

    if os.path.exists(DirName) == False:

        os.mkdir(DirName)

#-----------------------------------------------------------
# Function Name : CreateLogFile
# Description : Creates log file in specified directory
#-----------------------------------------------------------

def CreateLogFile(DirName, ProcessList):

    CreateDirectory(DirName)

    TimeStamp = time.ctime()

    TimeStamp = TimeStamp.replace(" ","_")
    TimeStamp = TimeStamp.replace(":","_")

    FileName = os.path.join(DirName,
                            "Marvellous" + TimeStamp + ".log")

    Border = "-" * 80

    try:

        fobj = open(FileName,"w")

        fobj.write(Border+"\n")
        fobj.write("Marvellous Infosystems Process Log\n")
        fobj.write("Log Generated at : "+time.ctime()+"\n")
        fobj.write(Border+"\n")

        fobj.write("{:<10}{:<35}{}\n".format(
            "PID",
            "Process Name",
            "Username"))

        fobj.write(Border+"\n")

        for Process in ProcessList:

            fobj.write("{:<10}{:<35}{}\n".format(
                Process["pid"],
                Process["name"],
                Process["username"]))

        fobj.write(Border)

        fobj.close()

    except Exception as E:

        print("Unable to create log file :",E)

    return FileName