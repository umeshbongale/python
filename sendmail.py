"""The first step is to create an SMTP object, each object is used for connection 
with one server."""

import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)

#Next, log in to the server
server.login("bongale.umesh", "")

#Send the mail
msg = "Hello!" 
# The /n separates the message from the headers
server.sendmail("bongale.umesh@gmail.com", "umeshbongale@gmail.com", msg)