This is a Python-based cloud deployment recommendation platform that helps users choose the most suitable cloud architecture based on workload characteristics such as traffic pattern, latency sensitivity, request volume, and budget. The project includes an interactive Streamlit dashboard, a command-line deployment advisor, and a Machine Learning-powered spam detection API deployed using Google Cloud Functions.


Requirements

The following software must be installed on the system:

- Python 3.10 or above
- pip

Python Libraries:

- streamlit
- pandas
- numpy
- plotly
- scikit-learn
- joblib
- functions-framework
- fuzzywuzzy
- streamlit-option-menu
- requests

Installation

Clone the repository:

bash
git clone https://github.com/YOUR_USERNAME/Smart-Cloud-Deployment-Advisor.git


Move into the project directory:

bash
cd Smart-Cloud-Deployment-Advisor


Install the required Python packages:

bash
pip install -r requirements.txt


If the requirements file is unavailable, install manually:

bash
pip install streamlit pandas numpy plotly scikit-learn joblib functions-framework fuzzywuzzy streamlit-option-menu requests



Running the Application

1. Train the Machine Learning Model (Optional)

bash
python train_model.py


This generates the trained model file:


spam_classifier.joblib


2. Run the Streamlit Dashboard

bash
streamlit run frontend_pro.py

The dashboard will open in your browser.

3. Run the Command Line Deployment Advisor

bash
python deploy_advisor.py


Answer the questions regarding:

- Traffic Pattern
- Latency Sensitivity
- Project Budget

The advisor will recommend the most suitable cloud deployment strategy.

4. Deploy the Backend API

Run the Google Cloud Function locally:

bash
functions-framework --target predict


The API will expose an endpoint that accepts POST requests for spam prediction.

Usage

The platform consists of multiple modules:

Architecture Simulator

Compare Serverless and Virtual Machine deployment models based on:

- Traffic Pattern
- Monthly Requests
- Estimated Cost
- Scalability

Live Threat Scanner

Enter a message to classify it as:

- Spam
- Safe (Ham)

using a trained Naive Bayes Machine Learning model.

AI Architect

Ask cloud computing questions related to:

- Serverless Computing
- Virtual Machines
- Cloud Cost Optimization
- Cold Starts
- Scaling Strategies
- AWS, Azure, and Google Cloud

Cloud Market Feed

Displays simulated cloud pricing information for:

- AWS Lambda
- Google Cloud Functions
- Azure Functions

to help compare deployment costs.

Predictive Scaling

Visualizes projected traffic and demonstrates proactive cloud resource scaling using simulated workload patterns.

Decision Logic

The deployment recommendation is based on the following parameters:

- Traffic Pattern
- Latency Sensitivity
- Budget
- Monthly Request Volume

Recommendation Rules

Serverless (Google Cloud Functions)

Recommended when:

- Traffic is bursty
- Budget is limited
- Pay-per-use pricing is beneficial
- Automatic scaling is required


Dedicated Virtual Machine

Recommended when:

- Traffic is steady
- High request volume
- Predictable workloads
- Consistent low latency is required

Hybrid Deployment

Recommended when:

- Workload characteristics are mixed
- Balance between scalability and cost is required

Machine Learning Model

Algorithm Used:

- Multinomial Naive Bayes

Feature Extraction:

- CountVectorizer

Training Dataset:

- Sample email dataset containing spam and legitimate messages.

Prediction Output:

- Spam
- Ham

Technologies Used

Programming Language

- Python

Frameworks

- Streamlit
- Google Functions Framework

Machine Learning

- Scikit-Learn
- Naive Bayes
- CountVectorizer

Visualization

- Plotly
- Pandas
- NumPy

Cloud Concepts

- Serverless Computing
- Google Cloud Functions
- AWS Lambda
- Azure Functions
- Virtual Machines
- Cost Optimization
- Predictive Scaling


Team:

Karthick Balaji R
SrihariVasagar S
Dakshin Sidarth M S

Bachelor of Engineering (Computer Science)

Cloud Computing | Machine Learning | Distributed Systems