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
    # model = joblib.load('model.h5')
    # prediction = model.predict([age, tablets])

    return { 
        "ZANTAC" : "Colorectal cancer" , 
        "IBRANCE" : "Blood test abnormal" ,  
        "OTEZLA" : "Diarrhoea" , 
        "SIMPONI" : "Colitis ulcerative" , 
        "GILENYA" : "Muscular weakness" , 
        "LANTUS" : "Dementia"
    }
    # return {"filename": file.filename , "tablets" : tablets , "age" : age }  



@app.post("/test")
async def test(url: str ):
    return {"message": "Hello World Summarize" + url}   

 
if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
