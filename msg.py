import smtplib
from email.MIMEBase import MIMEBase
from email import encoders
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import getpass
import fbchat
import tweepy
import sys
from twilio import TwilioRestException
from twilio.rest import TwilioRestClient
print """ .......................................................
				WELCOME  
....................................................... """

print "Enter your email details"
your_adr = raw_input("Your email id \n")
pass_adr = getpass.getpass()


print "Enter your Facebook details"
your_id = str(raw_input("Enter username \n"))
pass_fb = getpass.getpass()

print "Enter SMS details"

ACCOUNT_SID = raw_input("Your account id\n")
AUTH_TOKEN = raw_input("Your authentication token\n")
fromNum = raw_input("Your number\n")

print "Enter Twitter account details"

ACCESS_TOKEN = raw_input("Your access_token\n");
ACCESS_SECRET = getpass.getpass("Your access token secret\n");
CONSUMER_KEY = raw_input("Your consumer key\n");
CONSUMER_SECRET = getpass.getpass("YOur consumer secret");

exit_input = raw_input("To exit type EXIT, else press any key\n")

while(exit_input != 'EXIT' and exit_input != 'exit'):
	print "Email - [1]   FB - [2]  SMS - [3]  Twitter - [4]"
	number = int(raw_input("Select any one above\n"))
	if(number == 1):
		rec_adr = raw_input("Enter receiver's email\n")
		msg= MIMEMultipart()
		subj=raw_input("Subject:")
		msg['From']=your_adr
		msg['To']=rec_adr
		msg['Subject']=subj
			
		print "Enter body of email"
		body=sys.stdin.read();
		
		msg.attach(MIMEText(body,'plain'))
		
		inp = raw_input("Do you want to attach any file? y/n")
		if(inp == 'y'):
			strings = raw_input("Enter file address\n")
			if(strings != ''):
				attachment = open(strings,'rb')
				part = MIMEBase('application','octet-stream')
				part.set_payload((attachment).read())
				encoders.encode_base64(part)
				part.add_header('Content-Disposition',"attachment; filename = %s" % strings)
				msg.attach(part)

		server = smtplib.SMTP('smtp.gmail.com',587)
		server.starttls()
		server.login(your_adr,pass_adr)
		text = msg.as_string()
		server.sendmail(your_adr,rec_adr,text)
		server.quit()


	elif(number == 2):
		client = fbchat.Client(your_id,pass_fb)
		print "Type your friend's name: "
		fname = raw_input("Enter friend's name :\n")
		friends = client.getUsers(fname)

		friend = friends[0]
		message = raw_input("Message to send: \n")
		sent = client.send(friend.uid,message)
			
		if sent:
			print("Message sent successfully :) ")
		else:
			print("Message sending failed")

	elif(number == 3):
		client = TwilioRestClient(ACCOUNT_SID,AUTH_TOKEN)

		ToNum = raw_input("Enter the number you want to send SMS \n");
		bodytext = raw_input("Enter text you want to enter\n")
		try:
			client.messages.create( to = '+91'+ToNum, from_ = '+' + fromNum, body = bodytext)
		except TwilioRestException as e:
			if(e.code == 21212):
				fromNum = raw_input("Enter your correct no")
			elif(e.code == 21608):
				print"Verify the no "
			elif(e.code == 20003):
				ACCOUNT_SID = raw_input("Enter correct acc SID")
				AUTH_TOKEN = raw_input("Enter correct acc token")
			else:
				print "Error occured.. Try again!"
	elif(number == 4):
		auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET);
		auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET);
		print "Enter your tweet\n";
		tweet=sys.stdin.read();
		status = tweepy.API(auth).update_status(status=tweet);
			
	exit_input = raw_input("To exit type EXIT, else press any key\n")

print("THank you for using MultiMessenger! :) ");












