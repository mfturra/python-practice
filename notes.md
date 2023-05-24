## 5/17/2022
Constructor
Builds object and store them into a variable.
Line 35: Dictonary 

Make a Class jsonified. 

What's the best way to represent data to the client after they post information.

Create a separate dictionary 




# 5/11/2023
Own Time Research
1. What does it mean to serialize data?

### How to kill active port
ps aux | grep -i flask | awk '{print $2}' | while read line
do pkill -9 $line
done




git diff HEAD HEAD~1
Show me the difference. HEAD and HEAD-1 are different commit hashes.

REST API
- Server responds in JSON

201 Success and creation 

Build JSON out and return fields. 
Flask return http status code
- return Response("{'a':'b'}", status=201, mimetype='applcation)
- Mimetype/Content-Type: The type of data being sent.

Return 201 success output
Return 400 error request
Return 500 internal server error

Be as specific as possible to make sure that 



# 5/4/2023
## Things to Review
1. Walk through how HTTP protocols work with headers and body messages. Provide us with examples of how it's used and how to use curl to interact with the terminal while using it. Why do we use the terminal to interact with the client? How is that easier?
2. How would I use the from_json function to load json data?

Response and Requesrt Router are the inputs.
- What is a response writer?
Address
HTTP handler

### Header (Meta data about request)
GET: Verb being called | Path
Host: HTTP version being used.
Accept: */* 
Content-Length: Characters for body of message
Content-Type: application/json
User-Agent: What sent the request? (Ex: curl/7.82.0)
Body: Content that's being sent to the server. (Please do something about this)

HTTP Response Codes (mdn web docs): Request API Return code conventions

evaluating dictionary key
- Key value store: 
Method: Function that's specific to a type
- Example: if __ in ___ dict.keys() or value()
- Update: If the person adds data that wasn't supposed to be added

## 4/26/2023
Feature branch: New branch off main would be called videogame branch. 

# Moving through branches
git checkout -b <branchname>
git checkout master

.gitignore very literal
- Wildcard selector: *.___
- Regex (to learn)
- Configuring a local gitignore.

git branch: Provides user with name of current branch

# Git pull
git pull
- Combination: git fetch and git merge
- git fetch downloads content from the specified remote repository.
- git merge, merges the remote content refs and heads into a new local merge commit. 
- Event Summary: A branch is created to add or fix a feature that's disconnected from the main branch. When creating a new pull request, a new commit is created that merges the commits from the branch with those of the master. 

git pull --rebase
- Event summary: When a remote commit is behind the local commits, the rebase copies the remote commits to the local origin/main commit history.



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
