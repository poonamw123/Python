import sys
import os
import hashlib
import time
import smtplib
import re
from email.message import EmailMessage



def CalculateCheckSum(FileName):
    fobj = open(FileName, "rb")
    
    hobj = hashlib.md5()
    
    Buffer = fobj.read(1024)
    
    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)
    
    fobj.close()
    
    return hobj.hexdigest()

def FindDuplicate(DirectoryName):
    
    Ret = os.path.exists(DirectoryName)
    
    if Ret == False:
        print("Path is invalid")
        return
    
    Ret = os.path.isdir(DirectoryName)
    
    Duplicate = {}
    
    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(FolderName, fname)
            
            Checksum = CalculateCheckSum(fname)
            
            if Checksum in Duplicate:
                Duplicate[Checksum].append(fname)
            else:
                Duplicate[Checksum] = [fname]
    
    TotalFiles = 0
    
    for value in Duplicate.values():
        TotalFiles = TotalFiles + len(value)
        
    DuplicateFiles = 0
    Result = list(filter(lambda x : len(x) > 1, Duplicate.values()))
    
    for value in Result:
        DuplicateFiles = DuplicateFiles + len(value)
    
    
    return Duplicate, TotalFiles, DuplicateFiles
                
def DeleteDuplicate(DirectoryName):
    Duplicate, TotalFiles, DuplicateFiles = FindDuplicate(DirectoryName)
    
    Result = list(filter(lambda x : len(x) > 1, Duplicate.values()))
    
    Count = 0
    TotalDeleted = 0
    DeletedFiles = []
      
    for value in Result:
        Count = 0
        for subvalue in value:
            Count = Count + 1
            if(Count > 1):
                os.remove(subvalue)
                DeletedFiles.append(subvalue)
                TotalDeleted = TotalDeleted + 1
        Count = 0
    
    print("Total deleted files : ", TotalDeleted)
    return TotalDeleted, DuplicateFiles, TotalDeleted, DeletedFiles

def CreateDirectory(FolderName):
    Ret = False
    Ret = os.path.exists(FolderName)
    
    if(Ret == True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to proceed as directory name is already used by file")
            return None
        
        else:
            print("Directory already exists")
            
    else:
        os.mkdir(FolderName)
        print("Directory created successfully")
        
    return FolderName

def CreateLogFile(FolderName):
    Folder = CreateDirectory(FolderName)
    
    if(Folder == None):
        return None
    
    Timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(Folder, "DuplicateRemovalLog_%s.log" %Timestamp)
    
    return FileName

def WriteLog(LogFileName,
             DirectoryName,
             TotalFiles,
             DuplicateFiles,
             TotalDeleted,
             DeletedFiles):

    Border = "-" * 60

    fobj = open(LogFileName,"w")

    fobj.write(Border+"\n")
    fobj.write(" Marvellous Infosystems\n")
    fobj.write(" Duplicate File Removal Log\n")
    fobj.write(Border+"\n\n")

    fobj.write("Date & Time : ")
    fobj.write(time.ctime())
    fobj.write("\n")

    fobj.write("Directory Scanned : ")
    fobj.write(DirectoryName)
    fobj.write("\n")

    fobj.write("Total Files Scanned : ")
    fobj.write(str(TotalFiles))
    fobj.write("\n")

    fobj.write("Duplicate Files Found : ")
    fobj.write(str(DuplicateFiles))
    fobj.write("\n")

    fobj.write("Duplicate Files Deleted : ")
    fobj.write(str(TotalDeleted))
    fobj.write("\n\n")

    fobj.write(Border)
    fobj.write("\nDeleted Files\n")
    fobj.write(Border)
    fobj.write("\n")

    if(len(DeletedFiles) == 0):

        fobj.write("No Duplicate Files Found\n")

    else:

        for FileName in DeletedFiles:

            fobj.write(FileName)
            fobj.write("\n")

    fobj.write(Border)

    fobj.close()

    print("Log File Created Successfully")
    
    
def SendMail(LogFileName, ReceiverMail):
    Pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    if(re.match(Pattern,ReceiverMail) == None):

        print("Invalid Email Address")

        return
    
    try:
        SenderMail = "poonam2208wategaonkar@gmail.com"
        SenderPassword = "tsscktbxsxsdliup"
        
        Message = EmailMessage()
        
        Message["From"] = SenderMail
        Message["To"] = ReceiverMail
        Message["Subject"] = "Duplicate File Removal Log"
        
        Body = """
Hello,

Please find attached the Duplicate File Removal Log File.

This mail is generated automatically

Thanks & Regards,
Poonam Wategaonkar
"""
        Message.set_content(Body)
        fobj = open(LogFileName, "rb")
        FileData = fobj.read()
        FileName = os.path.basename(LogFileName)
        Message.add_attachment(FileData,
                               maintype = "application",
                               subtype = "octet-stream",
                               filename = FileName)
        fobj.close()
        
        SMPTServer = smtplib.SMTP("smtp.gmail.com", 587)
        
        SMPTServer.starttls()
        SMPTServer.login(SenderMail, SenderPassword)
        SMPTServer.send_message(Message)
        SMPTServer.quit()
        print("Mail sent successfully")
        
    except Exception as obj:
        print("Unable to send mail")
        print(obj)
        

def StartProcess(DirectoryName,EmailID):

    FolderName = "Marvellous"

    StartTime = time.time()

    LogFileName = CreateLogFile(FolderName)

    if(LogFileName == None):

        print("Unable to create Log File")

        return

    print("Searching Duplicate Files...")

    TotalFiles,DuplicateFiles,TotalDeleted,DeletedFiles = DeleteDuplicate(DirectoryName)

    WriteLog(LogFileName,
             DirectoryName,
             TotalFiles,
             DuplicateFiles,
             TotalDeleted,
             DeletedFiles)

    SendMail(LogFileName,EmailID)

    EndTime = time.time()

    print("-"*60)
    print("Execution Time :",EndTime - StartTime,"Seconds")
    print("-"*60)
    

def main():

    Border = "-" * 60

    print(Border)
    print(" Marvellous Duplicate File Removal")
    print(Border)

    if(len(sys.argv) == 2):

        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):

            print("Help")
            print()

            print("This application is used to remove duplicate files")
            print("It creates log file")
            print("Stores log inside Marvellous directory")
            print("Sends Log File through Email")
            print("Runs periodically")

            return

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):

            print("Usage")
            print()

            print("python",sys.argv[0],"Directory TimeInterval Email")

            print()

            print("Example")

            print("python",sys.argv[0],"D:\\Demo 60 abc@gmail.com")

            return

        else:

            print("Invalid Option")

            print("Use --h for Help")

            print("Use --u for Usage")

            return

    elif(len(sys.argv) == 4):

        DirectoryName = sys.argv[1]

        TimeInterval = sys.argv[2]

        EmailID = sys.argv[3]

        if(os.path.exists(DirectoryName) == False):

            print("Directory does not exist")

            return

        if(os.path.isdir(DirectoryName) == False):

            print("Invalid Directory")

            return

        if(TimeInterval.isdigit() == False):

            print("Time Interval should be numeric")

            return

        if(int(TimeInterval) <= 0):

            print("Time Interval should be greater than zero")

            return

        try:

            while(True):

                print(Border)

                print("Automation Started")

                print(Border)

                StartProcess(DirectoryName,
                             EmailID)

                print("Waiting for next execution...")

                time.sleep(int(TimeInterval) * 60)

        except KeyboardInterrupt:

            print("Automation Stopped Successfully")

        except Exception as obj:

            print("Error :",obj)

    else:

        print("Invalid Number Of Command Line Arguments")

        print("Use --h for Help")

        print("Use --u for Usage")
            
    
    

if __name__ == "__main__":
    main()
    