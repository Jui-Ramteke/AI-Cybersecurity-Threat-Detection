import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os

# Import the preprocessing function we just built!
from src.preprocess import preprocess_data 

def train_and_evaluate():
    print("\n[1/3] Fetching preprocessed data...")
    X_train_scaled, X_test_scaled, y_train, y_test = preprocess_data()
    
    print("\n[2/3] Training AI Model (Random Forest)... This might take a few seconds.")
    # Initialize 100 "decision trees" to act as our security team
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train_scaled, y_train)
    
    print("\n[3/3] Testing the AI Model on unseen data...")
    y_pred = rf_model.predict(X_test_scaled)
    
    print("\n" + "="*35)
    print("      MODEL EVALUATION RESULTS")
    print("="*35)
    print(classification_report(y_test, y_pred))
    
    # Create a visual Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6,4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=['Normal', 'Attack'], 
                yticklabels=['Normal', 'Attack'])
    
    plt.title('Threat Detection Confusion Matrix')
    plt.ylabel('Actual Network Traffic')
    plt.xlabel('What the AI Predicted')
    
    # Save the graph and the model
    os.makedirs('outputs', exist_ok=True)
    plt.savefig('outputs/confusion_matrix.png', bbox_inches='tight')
    print("\n✅ Visual Confusion Matrix saved to outputs/confusion_matrix.png")
    
    joblib.dump(rf_model, 'models/rf_model.pkl')
    print("✅ Trained AI Model successfully saved to models/rf_model.pkl\n")

if __name__ == "__main__":
    train_and_evaluate()