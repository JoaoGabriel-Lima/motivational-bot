from twilio.rest import Client 
 
account_sid = 'AC3de56d48aea93dcfe71a2ebce59f4612' 
auth_token = '8f815c337892201667a5704c78332108' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='🐒',      
                              to='whatsapp:+5521995709913' 
                          ) 
 
print(message.sid)