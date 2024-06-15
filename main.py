import pyttsx3

robo = pyttsx3.init()
print("welcome to RoboSpeaker 1.1 created by keshav...")
while True:
    user_input = input("Enter what do you want to say : ")
    if user_input =="0":
        break
    else:
        print(user_input)
        robo.say(user_input)
        robo.runAndWait()

