import os
import sys
import random
import smtplib

def OTP_verifying(count):
    sender=smtplib.SMTP("smtp.gmail.com",587)
    sender.starttls()
    sender.login("__sender_gmailID___","__16_Digit__code___")
    receiver_emailid=str(input("Enter your Email ID :"))
    OTP=""
    for i in range(6):
        rn=random.randint(0,10)
        OTP+=str(rn)
    sender.sendmail("__sender_gmailID___",receiver_emailid,OTP)
    Verifing_otp=str(input("Enter the OTP sent to your mail :"))
    if Verifing_otp==OTP:
        print("OTP Verification Successful")
        sys.exit()
    else:
        print("Wrong OTP entered . Verification Unsuccessful")
        choice=int(input("Enter 0 to exit and 1 to resend the OTP :"))
        if choice==0:
            print("Quitting...!")
            sys.exit()
        else:
            count+=1
            return count

print("Welcome to the OTP Verification portal")
(count,choice)=(0,0)
while count<3:
    count=OTP_verifying(count)
if count==3:
    print("Entered Wrong OTP several Times")
    print("Present OTP verification is temporarly Closed. please try after some time")
        
