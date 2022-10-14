## Abstract
Predicting a drug's adverse side effects is crucial because they could significantly affect a patient. When a treatment goes beyond treating the intended disease, it results in side effects. The effect can be mild or severe and even fatal. A medicine, surgery, or other type of intervention, such as complementary and alternative therapies, may be used as the treatment. An essential way to guarantee patients can benefit from the significant advantages offered by long-term treatment is to inform patients about the possibility that these adverse events could occur and give instructions prior to treatment to prevent adverse medication reactions.FDA dataste

## Inspiration
Numerous individuals taking daily prescriptions have these adverse side effects as a result of the new medication, dosage, etc. These side effects will have different levels of harmful implications on the patient's body. Although a doctor can anticipate a patient's adverse effects based on an examination of individuals but this is not always possible. What about the other possible side effects which the doctor is not aware of?
 Swapn's goal is to help medical professionals predict the negative side effects of the drugs they give to patients.It can be accomplished with the use of artificial intelligence.
 
## Problem Statement 
Adverse effects of medications are most likely to happen when a person first uses the drug, when they stop using it, or when the dosage changes.What if we could anticipate their adverse side effects based on their current medical prescription which can help them to prevent the side effects?  

## Solution
We can help the doctor choose a prescribed drug that has fewer or no negative side effects by predicting the adverse side effects of the drug based on its aspects . On uploading the prescription as document the doctor will be able to get the possible adverse side affects of the each particular drug prescribed by him. If a new medication needs to be prescribed, the doctor can do so based on the anticipated side effects and more . This can be achieved by using AWS Comprehend Medical , AWS Textract and Neural Networks. 

## Novelty 
Some drugs can have negative effects in people. Predicting the side effects of these medications beforehand will help prevent serious consequences of any kind. 

## FlowChart 

FlowChart of application
![architecture](https://user-images.githubusercontent.com/73429989/195945636-e0668f02-82f9-4461-8463-92b859854f02.png)

FlowChart of Model
![deep-learning-model](https://user-images.githubusercontent.com/73429989/195945804-ad6ec4e1-7657-4475-b802-403aacb0ada9.png)   

##How we build it :

1. AWS  EC2 instance
A wide range of instance types designed for various use cases are available with Amazon EC2. You have the freedom to select the ideal combination of resources for your applications thanks to the flexibility provided by instance types, which include various combinations of CPU, memory, storage, and networking capacity. To scale your resources to the demands of your target workload, each instance type offers one or more instance sizes. The fastapi application was deployed on amazon EC2 instance which helps to handle request response.

2. AWS Textract :
Adding document text recognition and analysis to your applications is simple using Amazon Textract. It assists in the detection of typed and handwritten text in a variety of documents, such as tax forms, financial reports, and medical records. Using the Amazon Textract Document Analysis API, you can extract text, forms, and tables from documents with structured data. We can also use the AnalyzeExpense API to process invoices and receipts. We have control over how text is organised as an input for NLP applications with Amazon Textract. Text can be extracted as lines and words. Here, the uploaded a document for processing by AWS Textract, which will then extract the text for processing by AWS Comprehend.  
 
3. AWS Comprehend Medical
A HIPAA-compliant natural language processing (NLP) service called Amazon Comprehend Medical use machine learning that has been specifically taught to comprehend and extract health information from medical literature, such as prescriptions, procedures, or diagnoses. The extracted text will be processed using AWS Comprehend Medical based on InferRxNorm function which helps to extract all Generic and brand names of drug . The extract drug information form the AWS service will be used to make side effects predictions. 

4. Predictions
To anticipate the negative effects, a deep learning model will be developed. To train this model, we will use the FDA-provided drug dataset. The model will be trained using the dataset and then be saved for later use. The pre-trained moel will be utilised to make predictions via transfer learning. 

5. SageMaker Studio
Amazon SageMaker JumpStart helps you quickly and easily get started with machine learning. The solutions are fully customizable and supports one-click deployment and fine-tuning of more than 150 popular open source models such as natural language processing, object detection, and image classification models.To train the model and work with its preprocessing we came up with sage makers 

Open FDA Dataset :  https://open.fda.gov/data/downloads/
Model Dataset : https://drive.google.com/file/d/1er1Ml5x1wAQ1VvYwBkaN7bLKDmKT9I25/view?usp=sharing 


## Web Application 
- Frontend -> React JS & Chakra UI
- Backend -> Fast API 
- Deep Learning Model -> Pytorch  , AWS
- Hosting -> AWS 

## Challenges we ran into  
-We had issues with API integrationg with React JS which was later rectified . 
-The user interface integration of our deep learning model was
challenging.
-Working with a deep learning model was a difficult portion of the
project.
-It was interesting to work on with some AWS Services.

## Accomplishments we are proud of : 
- We were successful in developing a remarkable approach that can helps to predict the adverse side effects of a drug . 
- Using AWS Comprehend as well as AWS Textract to process the document was an astetic part
- Was able to develope a deep learning model using FDA drug dataset.
- It was amazing to think of creating a web application and using this
concept.

## What we Learnt : 
- We came across many useful AWS services such as EC2 , Comprehend Medical , Textract and many more .
- Deep learning model training required a significant amount of time and
computation power.
- It was difficult to integrate our deep learning model with the user
interface.
- Improving the model's accuracy was an aesthetic taste.
- We gained experience using FastApi and gained knowledge of several
deep learning models.

## Whats next 
- Suggesting medications which has less  or no complications.
- Giving personalized feeback for each person 
- By incorporating regional languages the document can be processed in native languages . 
- Improving models accuracy for better performance of the application.
- The application can also be extended to Drug Discovery Analysis .
