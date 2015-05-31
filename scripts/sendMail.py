#! /usr/bin/python

# Comment the following 3 lines if you are uploading the script to your
# tropo account
import sys
sys.path.append('../lib')
from tropoEmul import *

import smtplib
from email.mime.text import MIMEText 

def sendMail(caseNumber):

    # Credentials (for your email/gmail account)
    username = 'username'
    password = 'password'

    fromName = 'Username <username@gmail.com>'
    toName = 'Recipient <nobody@example.com>'
    
    msg = MIMEText('Hello GVE Escalation Team,\nPlease escalate case number ' 
    + str(caseNumber) + 
    ' since we just got a call from the requester.\n\nThanks!');
    
    msg['Subject'] = 'GVE Case Escalation Case #' + str(caseNumber)
    msg['From'] = fromName
    msg['To'] = toName
    
    # The actual mail send
    # adapt to your mail providers' server addresses
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username, password)
    server.sendmail(fromName, [toName], msg.as_string())
    server.quit()
  
    # Remove the following 2 lines before using your script on tropo  
    print 'Message has been successfully sent to ' + repr(msg['To']) + '.'
    print msg.as_string()

###
# Program starts here
###

ask('Hello, please enter your case number you want to escalate.', {
    'choices':'[7 DIGITS]',
    'terminator':'#',
    'timeout':5.0,
    'mode':'dtmf',
    'onChoice': lambda event : sendMail(result.value),
    'onBadChoice': lambda event : say('Please enter a valid case number which consists of 7 digits.')
})


