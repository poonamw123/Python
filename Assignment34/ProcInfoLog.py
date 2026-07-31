import sys
import os
import smtplib
from email.message import EmailMessage
import Marvellous

#-----------------------------------------------------------
# Function Name : SendMail
# Description : Send log file through mail
#-----------------------------------------------------------

def SendMail(FileName, ReceiverMail):

    SenderMail = "poonam2208wategaonkar@gmail.com"
    Password = "tsscktbxsxsdliup"

    try:

        Msg = EmailMessage()

        Msg["Subject"] = "Marvellous Process Log"
        Msg["From"] = SenderMail
        Msg["To"] = ReceiverMail

        Msg.set_content("Please find attached Process Log File.")

        with open(FileName,"rb") as fobj:

            FileData = fobj.read()

        Msg.add_attachment(FileData,
                           maintype="application",
                           subtype="octet-stream",
                           filename=os.path.basename(FileName))

        Server = smtplib.SMTP_SSL("smtp.gmail.com",465)

        Server.login(SenderMail,Password)

        Server.send_message(Msg)

        Server.quit()

        print("Mail sent successfully")

    except Exception as E:

        print("Unable to send mail :",E)

#-----------------------------------------------------------
# Function Name : main
#-----------------------------------------------------------

def main():

    if(len(sys.argv) == 2):

        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):

            print("This automation script creates process log.")

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):

            print("Usage :")
            print("python ProcInfoLog.py DirectoryName")
            print("python ProcInfoLog.py DirectoryName EmailID")

        else:

            Directory = sys.argv[1]

            ProcessList = Marvellous.GetAllProcesses()

            FileName = Marvellous.CreateLogFile(Directory,
                                                ProcessList)

            print("Log file created successfully")

    elif(len(sys.argv) == 3):

        Directory = sys.argv[1]

        ReceiverMail = sys.argv[2]

        ProcessList = Marvellous.GetAllProcesses()

        FileName = Marvellous.CreateLogFile(Directory,
                                            ProcessList)

        SendMail(FileName,ReceiverMail)

    else:

        print("Invalid number of arguments")
        print("Use --h for help")
        print("Use --u for usage")

#-----------------------------------------------------------

if __name__ == "__main__":
    main()
