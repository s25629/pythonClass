# This is a sample Python script.
import smtplib from email.mime.text import MIMEText
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

studenci=[]


def send_email(subject,body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(sender, password)
    smtp_server.sendmail(sender, recipients, msg.as_string())
    smtp_server.quit()
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def giveGrade(pkt):
    print("dodawanie ocen")
    if pkt<=50:
        return "2"
    elif pkt<=60:
        return "3"
    elif pkt<=70:
        return "3+"
    elif pkt<=80:
        return "4"
    elif pkt<=90:
        return "4+"
    elif pkt<=100:
        return "5"

def _cheackMail(mail):
    for stu in studenci:
        if mail is stu["mail"]:
            return True

    return False

def _usunStudent(mail):
    if _cheackMail(mail):
        studenci.pop({"mail":mail})

def dodaj():
    mail=input("podaj mail")
    if _cheackMail(mail):
        imie = input("podaj imie studenta")
        nazwisko = input("podaj nazwisko")
        pkt = input("podaj ilosc pktów")
        grade = giveGrade(pkt)
        status="GRADE"
        student={"mail":mail,"imie":imie,"nazwisko":nazwisko,"pkt":pkt,"ocena":grade,"status":status}
        studenci.append(student)
    else:print("powtarzajacy sie mail")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    plik=open("students.txt")
    linie=plik.read().split("\n")
    index=0
    for i in linie:
        wartosci=i.split(",")
        if len(wartosci)==4:
            wartosci.append(" ")
            wartosci.append(" ")

        student={"mail":wartosci[0],"imie":wartosci[1],"nazwisko":wartosci[2],"pkt":wartosci[3],"ocena":wartosci[4],"status":wartosci[5]}
        if student["status"]!="GRADE" or student["status"]!="MAILED":
            student["ocena"]=giveGrade(student["pkt"])
            student["status"]="GRADE"
        studenci.append(student)

#   wysyłanie
    send_email()








# See PyCharm help at https://www.jetbrains.com/help/pycharm/
