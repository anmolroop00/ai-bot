import speech_recognition as sr
from keras.models import load_model
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import joblib
import os
#import cv2
import numpy as np

model = joblib.load('SalaryModel.pk1')
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening..')
            talk("Yes boss")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
            else:
                talk('Please try again')
                take_command()
    except Exception as e:
        talk('Sorry I cant get it, plese try again')
        pass
    return command
def run():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('its currently ' + time)
    elif 'salary' or 'payment' in command:
        with sr.Microphone() as source:
            talk('Please tell me years')
            voice2 = listener.listen(source)
            command2 = listener.recognize_google(voice2)
            print(command2)
            y = float(command2)
            print(y)
            sal = model.predict([[y]])[0]
            strsal = str(sal)
            print(strsal)
            talk("Estimated Salary is " + strsal)
    elif 'search' or 'tell me about' in command:
        result = command.replace('tell me about', '')
        print(result)
        info = wikipedia.summary(result, 4)
        talk('according to wikipedia')
        talk(info)    
run()


'''
elif 'who am i' in command:
        classifier = load_model('myface.h5')
        monkey_breeds_dict = {"[0]": "anmol", 
                            "[1]": "covid"
                            }
        monkey_breeds_dict_n = {"anmol": "anmol", 
                      "normal": "covid"}
        cap = cv2.VideoCapture(0)
        def draw_test(name, pred, im):
            monkey = monkey_breeds_dict[str(pred)]
            BLACK = [0,0,0]
            expanded_image = cv2.copyMakeBorder(im, 80, 0, 0, 100 ,cv2.BORDER_CONSTANT,value=BLACK)
            cv2.putText(expanded_image, monkey, (20, 60) , cv2.FONT_HERSHEY_SIMPLEX,1, (0,0,255), 2)
            cv2.imshow(name, expanded_image)  
            while True:
                status, photo = cv2.read()
                cv2.imshow('vid',photo)
                
            
            # Get Prediction
            res = np.argmax(classifier.predict(input_im, 1, verbose = 0), axis=1)
            
            # Show image with predicted class
            draw_test("Prediction", res, input_original) 
            cv2.waitKey(0)
            cv2.destroyAllWindows()
def getRandomImage(path):
            """function loads a random images from a random folder in our test path """
            folders = list(filter(lambda x: os.path.isdir(os.path.join(path, x)), os.listdir(path)))
            random_directory = np.random.randint(0,len(folders))
            path_class = folders[random_directory]
            print("Class - " + monkey_breeds_dict_n[str(path_class)])
            file_path = path + path_class
            file_names = [f for f in listdir(file_path) if isfile(join(file_path, f))]
            random_file_index = np.random.randint(0,len(file_names))
            image_name = file_names[random_file_index]
            return cv2.imread(file_path+"/"+image_name)
        for i in range(0,15):
            input_im = getRandomImage("anmol/validation/")
            input_original = input_im.copy()
            input_original = cv2.resize(input_original, None, fx=0.5, fy=0.5, interpolation = cv2.INTER_LINEAR)
            
            input_im = cv2.resize(input_im, (64, 64), interpolation = cv2.INTER_LINEAR)
            input_im = input_im / 255.
            input_im = input_im.reshape(1,64,64,3) 
'''