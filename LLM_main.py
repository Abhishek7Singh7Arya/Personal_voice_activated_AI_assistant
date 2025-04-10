import requests,json
import ollama
import speech_recognition 
import pyttsx3

# Initialize TTS Engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

    # print(listen())
def askme(prompt,conversation):
    
    # while (prompt:=input('>: ')) !='exit':
    conversation.append({"role":"user","content":prompt})

    data={
        "model":"deepseek-r1",
        "messages":conversation,
        "stream":False
        }
    url = "http://localhost:11434/api/chat"# write your own LLM url here
    response = requests.post(url,json=data)
    response_json=json.loads(response.text)

    answer = response_json["message"]["content"]
    conversation.append({"role":"assistant","content":answer})
    print(answer)
    speak(answer)



recognizer = speech_recognition.Recognizer()


if __name__=="__main__":
    # response=ask_ai("write a java hello world code!")
    # print(response)
    conversation=[]
    while True:
        try:
            print("Speech Recognization Ready!")
            with speech_recognition.Microphone() as mic:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(mic,duration=0.2)
                print("1")
                audio = recognizer.listen(mic)
                print("1")
                prompt = recognizer.recognize_google(audio)
                prompt = prompt.lower()
                # prompt="write a program for hello world in java"
                print(f"I Recognized {prompt}")
                conversation.append({"role":"user","content":prompt})
                response =askme(prompt,conversation=conversation)
                print(response)

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            continue