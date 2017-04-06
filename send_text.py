from twilio.rest import Client

# Your Account SID from twilio.com/console
#account_sid = "AC5b090aa799d85cde150b69de7fd0a53c"
account_sid = "AC83e3d8cbb8187654043b9b713cb422ea"
# Your Auth Token from twilio.com/console
auth_token  = "aecde4da36f1e5db3d703b6e57b2d2fc"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16505495122",
    from_="+19196944449",
    body="Hello from Python!")

print(message.sid)