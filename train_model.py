import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib

print("⏳ 1. Loading Simulation Dataset...")
# We use this mini-dataset to guarantee the demo works fast
data = {
    'text': [
        "Win a $1000 cash prize now!", 
        "Meeting is at 3pm tomorrow", 
        "URGENT! Your account is compromised", 
        "Hey, can we grab lunch?", 
        "Free entry to the contest", 
        "Project review is on Monday",
        "Click here to claim your reward",
        "Please review the attached file"
    ],
    'label': ['spam', 'ham', 'spam', 'ham', 'spam', 'ham', 'spam', 'ham']
}
df = pd.DataFrame(data)
print(f"✅ Loaded {len(df)} training examples.")

print("⚙️ 2. Building Pipeline (Vectorization + Naive Bayes)...")
# This creates the mathematical model
model = make_pipeline(CountVectorizer(), MultinomialNB())

print("🧠 3. Training Model...")
model.fit(df['text'], df['label'])
print("✅ Model Trained Successfully.")

print("💾 4. Saving Model to 'spam_classifier.joblib'...")
# We save it so the server can use it later
joblib.dump(model, 'spam_classifier.joblib')
print("✅ Model Saved. Ready for Deployment.")