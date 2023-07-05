## 6/28/2023
### Creating Pull Requests (PR's)



## 6/27/2023
### Creating a RDS PostgreSQL Database on the AWS Free Tier
Reference: https://www.youtube.com/watch?v=I_fTQTsz2nQ

#### Initial Setup Instructions
- In search bar, search for RDS, and select the button to Create a Database.
- Choose standard create option. Select Postgresql engine type.
- Select Free Tier under Templates section.

Settings Section
- Update DB instance name: media-backlog-api
- Update master username: postgres
- Set master password: Under_Trees

Instance Configuration
- Utilize: db.t3.micro

Storage
- General Purpose SSD (gp2)
- Allocated Storage: 20 GB
- Disable Storage Autoscaling

Connectivity
- Default VPC, and Subnet Groups: Default
- Public Access: Yes
- Security Group
  - Choose Existing VPC
  - Maintain "default" security group
  - No preference necessary for Availability Zone (AZ)
  - Database port: 5432

Database Authentication: Password authentication

Initial Database Name: media-backlog-api
- Disable automated backups
- Enable encryption
- Performance Insights: Enabled

Monitoring: Disable
Maintenance and Others: Default



## 6/23/2023
### Working with Postgresql
Reference: 
- https://www.codementor.io/@engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb
- https://www.commandprompt.com/education/different-methods-to-create-a-table-in-postgresql/




### Creating Login
Log into SQL Server
- psql postgres

Creating Users (After logging in)
- CREATE ROLE username WITH LOGIN PASSWORD 'quoted password' [OPTIONS]

Creating a Password
- \password postgres
- Next enter password and confirm it.

Creating a Role with a password
- CREATE ROLE pedro WITH LOGIN PASSWORD 'Starter pack';

### Creating and Managing Databases
- CREATE DATABASE databasename;

List DB's
- \l

Choose DB
- \c databasename

Create a Table
- CREATE TABLE table_name(
  id int PRIMARY KEY,
  name VARCHAR(30));

Show All Tables in Database
- \d: List all tables in Database
- \d tablename: Shows table entry structure and types.
- SELECT * FROM table; Shows all entries inside a table.


## 6/22/2023
Task: Stand up AWS Instance: https://medium.com/techfront/step-by-step-visual-guide-on-deploying-a-flask-application-on-aws-ec2-8e3e8b82c4f7 
- Change directory to the folder where the key pair is located
- Secure the key pairs by running the following script: chmod 400 vs-flask-1.cer
- Run the following scripts to connect to the EC2 server: ssh -i "vs-flask-1.cer" ubuntu@ec2-3-145-72-178.us-east-2.compute.amazonaws.com
  - Where "vs-flask-1.cer" is the key pair name in quotations. ubuntu@ec2-3-145-72-178.us-east-2.compute.amazonaws.com is the cloud location of the server instance.

### If dependencies haven't been installed yet:
1. Install Python Virtualenv
  - sudo apt-get update
  - sudo apt-get install python3-venv

### Activate virtual environment
Create directory
- mkdir media-backlog-api
- cd media-backlog-api

Create new virtual environment
- python3 -m venv venv

Activate the virtual environment
- source venv/bin/activate

Install Flask
- pip install Flask
- pip install flask_sqlalchemy
- sudo apt install libpq-dev (Facilitates psycopg2 install on Ubuntu)
- pip install psycopg2-binary. This is a drop-in replacement to psycopg2 that eliminates the need for building from source.

### Create basic Flask API
- sudo nano app.py
  - Paste app.py script in file.
  - Paste the following after sqlalchemy library import.
    - from sqlalchemy.ext.declarative import declarative_base
  - Define Base and paste Videogame Class after app config section.
    - Base = declarative_base()
  - Select Ctrl + O. Save file by selecting Enter.
  - Exit nano by selecting Ctrl + X
  - Verify that the file is as it should be by pasting the following: cat app.py
  - 
- python app.py (Test whether the app is running)

## Run Gunicorn WSGI server to connect Flask Application
Install Gunicorn 
- pip install gunicorn

Run Gunicorn
- gunicorn -b 0.0.0.0:8000 app:app
- Exit using: Ctl + C




vpc: 
Subnet: Slide of IP addresses to work on

Network ACL
- Establishes rules for network traffic. Attached at subnet level.
Security group. Attached at level of EC2 instance
- All things that I want to accept. 

To Do:
1. Update security groups with new port range and source
2. GET/UUID to get one record back, POST, DELETE
3. Make web application able to run on server.
4. Run on server with database.




## 6/13/2023
Understand how the app actually works. 

Addressing a Specific Service
- Every laptop has an IP address. 127001 is reserved for the device
- Port number: Different process or program can be run on different ports. 
  - Review Port number conventions. Registered port numbers.
  - SSH: Secure Shell run on port 22. Can block port 22
- IP Address: Building to be sent to. Port is part of the building. 

Domain Name Service (DNS): Protocol that ID's what IP address connects to a specific server.

AWS Explained
- Data centers are meant to serve websites in a way that's publicly addressable via websites.
Elastic Compute (EC2)
  - Instance: CPU will be used.
  - All code will eventually be run on that server
- Internal IP Address within router is received
  - Whatever is controlling the router will address each individual device.
  - Private networks can be created that physically sit in office.
  Intranet - Internal internet.
- Private IP address is required to spin up server.

Virtual private cloud
- Allowing devices to take to one another.

CIDR: Classless Interdomain Routing - 10.0.0.0/16
- 4 decimal numbers: IPV4
 - 4 Different bytes of 8-bit each. 4 numbers are a address.
- CIDR: 255 x 255 x 255 x 255 available addresses. Devices are all supposed to be within a range, I want them included in my range. Include them in my router. 

Subnet: Explained

Route table Explained
- Rules for how to route traffic.


VPC: Subnets are created that route things differently.

Identity and Access Management (IAM):

Load Balancer: Created in VPC that has IP Address. Special server that's setup by AWS. 
- Configured in network. When this port is accessed, bring them to another network.

T2.micro (AWS Free Tier)
- Spin up instance using free tier.
- Get a flask response over the internet.
- Curl it over the internet.
- Key Pair creation and SSH login: Physical SSH key that has a private and public key. 



## 6/9/2023 to 6/12/2023
Task: Create UUID type in postgresql database
- While in your database run the following code:
  - CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
  - Where IF NOT EXISTS avoids the re-installing of the module.
- Run the following code to create your table with UUID4
  - CREATE TABLE videogames(
      videogame_id uuid DEFAULT uuid_generate_v4(),
      videogame_title VARCHAR(30) NOT NULL,
      videogame_platform VARCHAR(30) NOT NULL,
      videogame_releasedate DATE,
      videogame_publisher VARCHAR(30)
      );
- Alter table to drop default of UUID.
  - ALTER TABLE public.videogames ALTER COLUMN videogame_id DROP DEFAULT;

### Generate new models.py file with flask-sqlacodegen
- Run the following script
  - sqlacodegen postgresql:///media_backlog_api --table TABLENAME --outfile /Users/MT/Desktop/Dev-Ops Work/media-backlog-api-1/models.py


## 5/31/2023
Close branch
Update 

git branch -D video-game-database-creation (Branch Deletion)
git pull upstream main
git push origin main

### Start new branch
git checkout -b video-game-flask-sql-sql (New branch)
git cherry-pick

## Commit to database


# Long Term Roadmap
1. Implement VideoGame POST, GET, PATCH, DELETE
  - Update DB with UUID type
  - Build JSON after db.session.commit()
  - Implement release date and publisher for POST
2. Refactor Flask App for PRD.
3. Create AWS Cloud resources for app.
4. Get app running in PRD.



## 5/25/2023
SQLAlchemy: Library that's used to interact with different db packets.
- ORM: Object relational mapper. Has ability to create multiple different backends that translates to the right SQL format.

Flask-sqlcodegen
Uniform Resource Location: Location to find a website.
Uniform Resource Identifier (URI): 
- mysql can be the protocol

Create one entry
Create models.py with flask-sqlacodegen

config.py file


## 5/17/2023
Constructor
Builds object and store them into a variable.
Line 35: Dictonary 

Make a Class jsonified. 

What's the best way to represent data to the client after they post information.

Create a separate dictionary 

## Database Creation and SQLAlchemy Setup
- Install postgres (using web download page) and flask-sqlalchemy (pip install)
- Once Postgres is installed and running, create postgres database by running the following in the terminal:
  - psql -U postgres
  - CREATE DATABASE database_name; (e.g. media_backlog_api)
  - Expected entry output: CREATE DATABASE. Explanation: Confirms successful database creation
- Install alembic, Flask-Script and Flask-Migrate using "pip install" to manage database migrations and update database's schema.


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

