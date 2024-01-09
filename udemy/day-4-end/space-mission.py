print('''
                         .-.
                        ( (
                         `-'






                    .   ,- I'm going to the Moon Mãe!
                   .'.
                   |o|
                  .'o'.
                  |.-.|
                  '   '
                   ( )
                    )
                   ( )

               ____
          .-'""p 8o""`-.
       .-'8888P'Y.`Y[ ' `-.
     ,']88888b.J8oo_      '`.
   ,' ,88888888888["        Y`.
  /   8888888888P            Y8\
 /    Y8888888P'             ]88\
:     `Y88'   P              `888:
:       Y8.oP '- >            Y88:
|          `Yb  __             `'|
:            `'d8888bo.          :
:             d88888888ooo.      ;
 \            Y88888888888P     /
  \            `Y88888888P     /
   `.            d88888P'    ,'
     `.          888PP'    ,'
       `-.      d8P'    ,-'  
          `-.,,_'__,,.-'
''')
print("Welcome to Turra's Space Adventure.")
print(
    "Your mission is to find the right sequence of choices that'll get you in space! Choose wisely!"
)

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
# Preliminary Greeting
print(
    "\nYou take your seat in the rocketship when, on the left, a console automatically generates the following prompt:"
)
first_name = input("\nWhat is your first name? ").capitalize()
last_name = input("What is  your last name: ").capitalize()
welcome = print(
    f"Welcome Cadet {first_name} {last_name}. Best of luck to you on your quest to get to space!\n"
)

print("\n[In the middle of your console there is a large red button. During your travels, worst case scenario, type RED into your console and you'll get ejected out of your seat.]\n")

## Story Time
# First Decisive Event
button_choice = input(f"Cadet {last_name}, there are two buttons on your right hand side with no labels, which do you select? Blue or Green: ").lower()

if button_choice == "green":
  print("A voice in your helmet says that you're ready for takeoff. Launching in 3, 2, 1...You close your eyes and the force of the rocketship propels your body deeper into your seat. Moments later you've traveled past the stratosphere and you're 50km from earth!\n")
  
  # Second Decisive Event
  print("You start to fly through the air and alarms start to blare all around you. Your read from your console:\n")
  toggle_choice = input("There are two toggle options on your left that'll subdue the mechanical failure: Do you choose the Left or Right? ")
  
  if toggle_choice == "left":
    print("Slowly alarms start to dim. Then you hear another BOOM and your rocketship starts to travel even faster through the air! Moments later your 70km from earth's surface!")
  elif toggle_choice == "red":
    print("The ceiling of your capsule explodes open. Immediately you feel your body get jerked through the ceiling from an explosion from your seat. Moments later a parachute opens up and you safely land on the ground. You'll have to try another day. Thank you for your service.")
  else:
    print("The alarms around you start to get louder. Moments later the console starts to flash red and presents the following message:\n")

    # Sub-event
    flight_choice = input(f"Cadet {last_name}, there are fire's starting around the external part of your capsule. You must either use the flight stick to spin the rocketship and extinguish the flames or press the red button. Which do you choose? flight stick or red button: ")

    #
    if (flight_choice == "flight stick") or (flight_choice == "flightstick") or (flight_choice == "stick"):
      print("Your rocketship starts a barrel roll and the flames are put out just in time as your rocketship propels into the thermosphere! All the sudden you look around you, you see the Aurora Burealis. Moments later you make it into space! Congratulations! Enjoy your ascent to the space station. You'll be here a while ;)")
    else:
      print("The ceiling of your capsule explodes open. Immediately you feel your body get jerked through the ceiling from an explosion from your seat. Moments later a parachute opens up and you safely land on the ground. You'll have to try another day. Thank you for your service.")

elif button_choice == "red":
  print("The ceiling of your capsule explodes open. Immediately you feel your body get jerked through the ceiling from an explosion from your seat. Moments later a parachute opens up and you safely land on the ground. You'll have to try another day. Thank you for your service.")
else:
  print("You hear a large rumbling take place around you with a sudden crank in the mechanical system. The engine just stalled out. You'll have to leave the rocketship and try another day. Thank you for your service.")