import requests

a=input("한글을 입력하세요")

# This function will pass your text to the machine learning model
# and return the top result with the highest confidence
def classify(text):
    key = "25b7fef0-b571-11ec-98c5-896493b5101b0b3dd0cd-c638-4eb5-9cb5-38347a3de3c2"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text })

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()


# CHANGE THIS to something you want your machine learning model to classify
demo = classify(a)

 
label = demo["class_name"]
confidence = demo["confidence"]


# CHANGE THIS to do something different with the result
print ("result: '%s' with %d%% confidence" % (label, confidence))