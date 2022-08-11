# Robot Control Panel

### This is a website that controls the movement of the robot and saves the movements in a database.

## UI
![img.png](img.png)

### When pressed on a button
![img_1.png](img_1.png)

### The Database
![img_2.png](img_2.png)


## The Algorithm For Connecting a Web page to The Sensors:
* build the circuit.
* open the  Arduino  IDE include the wifi library.
* specify your network credentials so that the esp32 can establish a connection with your router
* specify the robot states f(forward), s(stop), b(backward), r(right),and l(left).
* In the setup connection start the internet connection after a successful connection print the IP address using wifi.localIP.
* In the loop listen for any request http://127.0.0.1:5000/save_move?move=f ( after ? is the state of the robot ).
* allow the use to move according to the value specified in the request.
* upload the code to the circuit.
* open the serial monitor copy the ESP IP address. Use it to access the web server.

# Rana(2022)