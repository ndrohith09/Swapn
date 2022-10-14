from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware 
import uvicorn 
import boto3
import joblib 
 
app = FastAPI() 

origins = [
    "http://localhost",
    "http://localhost:3000",
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World Summarize"} 

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):       
    print(file)
    # convert to byte array 
    file_bytes = await file.read()
    imageBytes = bytearray(file_bytes)

    textract = boto3.client('textract' , region_name = 'us-east-1') 
 
    response = textract.detect_document_text(
    Document={
            'Bytes': imageBytes,
        'S3Object': { 
            'Bucket': 'comprehend-09',
            'Name': file.filename
        }
    }) 

    text = ""
    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            print ('\033[94m' +  item["Text"] + '\033[0m')
            text = text + " " + item["Text"]

    # Amazon Comprehend client
    comprehend = boto3.client('comprehendmedical')
    rxnorm = comprehend.infer_rx_norm(Text = text) 
    tablets = []
    #get tablets
    for entity in rxnorm["Entities"]:
        print("- {}".format(entity["Text"]))
        print ("   Type: {}".format(entity["Type"]))
        print ("   Category: {}".format(entity["Category"])) 
        if(entity["Category"] == "MEDICATION"):
                    tablets.append(entity["Text"])

    #get age
    entities =  comprehend.detect_entities(Text=text)  
    age = 0 
    for entity in entities["Entities"]: 
        if entity['Type'] == "AGE" :  
            age = int(entity["Text"])    

    #make model predictions 
    model = joblib.load('model.h5')
    prediction = model.predict([age, tablets])
    print(prediction) 

    side_effects = {'cough': 1, 'drug ineffective': 2, 'nasopharyngitis': 3, 'product use issue': 4, 'device issue': 5, 'colorectal cancer': 6, 'headache': 7, 'decreased appetite': 8, 'pyrexia': 9, 'nausea': 10, 'pain in extremity': 11, 'alopecia': 12, 'fatigue': 13, 'diarrhoea': 14, 'incorrect dose administered': 15, 'injection site pain': 16, 'wrong technique in product usage process': 17, 'prostate cancer': 18, 'dizziness': 19, 'product use in unapproved indication': 20, 'injection site haemorrhage': 21, 'back pain': 22, 'insomnia': 23, 'asthenia': 24, 'abdominal discomfort': 25, 'hypertension': 26, 'off label use': 27, 'rash': 28, 'pain': 29, 'malaise': 30, 'arthralgia': 31, 'cerebrovascular accident': 32, 'product dose omission issue': 33, 'drug dependence': 34, 'death': 35, 'abdominal pain upper': 36, 'constipation': 37, 'hospitalisation': 38, 'covid-19': 39, 'condition aggravated': 40, 'pruritus': 41, 'vomiting': 42, 'therapy interrupted': 43, 'dyspnoea': 44, 'anxiety': 45, 'weight increased': 46, 'inappropriate schedule of product administration': 47, 'feeling abnormal': 48, 'emotional distress': 49, 'illness': 50, 'fall': 51, 'urinary tract infection': 52, 'pneumonia': 53, 'visual impairment': 54, 'bladder cancer': 55, 'gait disturbance': 56, 'renal cancer': 57, 'weight decreased': 58, 'peripheral swelling': 59, 'no adverse event': 60, 'others': 61}
    side_effects = {v: k for k, v in side_effects.items()} 
    print(side_effects[prediction[0]]) 
    return {"message": side_effects[prediction[0]]} 


@app.post("/test")
async def test(url: str ):
    return {"message": "Hello World Summarize" + url}   

 
if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
