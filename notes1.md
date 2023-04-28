## 4/26/2023
Feature branch: New branch off main would be called videogame branch. 

# Moving through branches
git checkout -b <branchname>
git checkout master

.gitignore very literal
- Wildcard selector: *.___
- Regex (to learn)
- Configuring a local gitignore.


## Storing in database (UUID)
- Need unique ID for any new entries.
- 

Models
- Tool: Goes into DB and generates python equivalent to generate database.

## Class
Higher type that encapsulates multiple types. Meta object to hold other things.
class Car:
  int horsepower
  string color
  string engine
  
  def whatsmycolor(): # Only works if you have an instance of a car.
    return self.color
  


sf.Car.new()
sf.horsepower = 10000
sf.color = "red"
sf.engine = " v8"

sf.whatsmycolor()

python constructor: 

member is part of a class
member function (method) on a class specifically.

def getReleaseData(self) # Requires you to pass on "self" 
print self.releaseDate()

def __init__(self, name, platform):
  self.gameName = name
  self.gamePlatform = platform

def getName(self):
  print(self.gameName)

requestJson = request.get_json()
tetris = VideoGame('Hatris', "NES")
tetris.getName()

Homework: 
1. Create video game class
2. Make sure local main is connected to main
3. Create video game class. Whenever POST w/ JSON that has the videogame data. Create an instance of the video game class and print to terminal.
[Tip: UUID will not be provided. Use server to generate UUID and put it in class. If the person doesn't return all info, return an error. If return everything, return success.] 




## 4/6/2023

## Compiler that takes GO code that changes the code 
package main

func main() {

}

python has an interpreter that reads your code.

for int i = 0; i < 10; i = i +5 {
    
}

## Notes on HTTP requests
Wire transmits light from one point to the other. Receivers and senders communicate what the signals mean.
Letter contents need to be legible between the sendor and reader.

HTTP request, address systems. Send this letter to this recipient.
Structure: Verb, URL, headers, meta-data. Returner will send something that's a similar structure as well. 
Anything that's wrong about it, you'll get an error.
- Section for Data: Send or receive. GET will send the request. There's no letter. There's just an envelope
 being sent for more data.
  When server sees that they send an HTML page. HTML is sent in body of response. Data section.

POST request: Accepted communication, POST request send file to do something with the data.
- Request is sent to server with data. Filling out data that you want to send to the server.
HTTP request from client to server.

FLASK request
Top of file, from flask import request. Data type that takes HTTP request wrap and puts it into a Python 
type to be used with Python.
Can be used to get header, and other components.

Frames are data packets. 

return is the return to the client

attributes are not functions. They're a class.
methods are functions that are specific to requests.

curl -X POST URL -H "Content-Type: application/json" -d '{foo:bar}'
  man curl
mime types: application/json tells that the type of data is json.

request.data - attribute of request.

