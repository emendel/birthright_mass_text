from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
fh = open("interest_list.csv", "r")
list_list = []
while True:
    line = fh.readline()
    list1 = line.split(',')
#    list1.append(list1)
    list_list.append(list1)
    if not line:
        break

print len(list_list)
numbers = {}
emails = {}
for x in list_list:
#    print x
    if len(x) > 5:
        if x[7] == "" and x[9] == "":
            #print 'empty'
            number = x[3]
            formatted_number = number.replace("-","") 
            if len(formatted_number) == 10:
                numbers[x[0]] = '+1' + formatted_number
            else:
                emails[x[0]] = x[2]

print (numbers)
print len(numbers)

print emails
print len(emails)

for x in numbers:
    print numbers[x]

#account_sid = 'ACd0ddb2932641e3f7759d4341b6b87fd0'
#auth_token = '753c0b06bda73ae82cc79ea04e197b1c'
#client = Client(account_sid, auth_token)
#
#message = client.messages.create(
#                              from_='+19478887081',
#                              body='Test',
#                              to='+12488021094'
#                          )
#
print(message.sid)
