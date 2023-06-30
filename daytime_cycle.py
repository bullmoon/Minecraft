import mcrcon, time

host = "10.20.30.99"
port = 25575
password = "minecraft"

# Create an instance of the MCRcon class with host and password arguments
rcon = mcrcon.MCRcon(host, password)

# Connect to the server
rcon.connect()

command = "time set day"

while True:
    # Send the command to the server
    response = rcon.command(command)

    # Print the response
    print(response)
    time.sleep(90)
    
# Disconnect from the server
rcon.disconnect()
