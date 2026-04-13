import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib
import os

def preprocess_data():
    print("Loading raw network traffic data...")
    df = pd.read_csv('data/network_traffic.csv')
    
    # Convert labels to binary (0 = normal, 1 = attack)
    df['label'] = df['label'].map({'normal': 0, 'attack': 1})
    
    # Separate features (X) from the target label (y)
    X = df.drop('label', axis=1)
    y = df['label']
    
    # Split the data: 80% to train the AI, 20% to test the AI
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale the features so all numbers are treated equally by the AI
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Save the scaler tool into our models folder so we can use it later on live data
    os.makedirs('models', exist_ok=True)
    joblib.dump(scaler, 'models/scaler.pkl')
    
    print("✅ Data preprocessed and Scaler saved to models/scaler.pkl")
    return X_train_scaled, X_test_scaled, y_train, y_test

if __name__ == "__main__":
    preprocess_data()