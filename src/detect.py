import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt
import os

def run_threat_detection():
    print("\n[INITIATING LIVE SOC ALERT SYSTEM...]")
    
    # 1. Load the "live" data we generated
    df = pd.read_csv('data/network_traffic.csv')
    
    # 2. Load the Scaler we saved earlier to normalize this new data
    scaler = joblib.load('models/scaler.pkl')
    features = df.drop('label', axis=1) # Drop the label, the AI must guess!
    features_scaled = scaler.transform(features)
    
    print("Scanning network traffic for zero-day anomalies...")
    
    # 3. Initialize the Unsupervised AI (Isolation Forest)
    # contamination=0.2 means we expect roughly 20% of the traffic to be malicious
    iso_forest = IsolationForest(contamination=0.2, random_state=42)
    
    # The AI scores each row. -1 means anomaly (threat), 1 means normal
    df['anomaly_score'] = iso_forest.fit_predict(features_scaled)
    
    # Map those numbers to readable SOC alerts
    df['status'] = df['anomaly_score'].map({-1: '🚨 THREAT DETECTED', 1: '✅ Clear'})
    
    # Filter and count the threats
    threats = df[df['status'] == '🚨 THREAT DETECTED']
    print(f"\nCRITICAL: {len(threats)} anomalies detected in recent traffic!\n")
    
    # 4. Create a Visual Threat Map for the SOC Dashboard
    plt.figure(figsize=(10,6))
    
    # Plot normal traffic in blue, and threats in red
    scatter = plt.scatter(df['src_bytes'], df['duration'], 
                          c=df['anomaly_score'], cmap='coolwarm', alpha=0.7)
    
    plt.title('Live Threat Detection: Zero-Day Anomalies Identified')
    plt.xlabel('Source Bytes Sent (Payload Size)')
    plt.ylabel('Connection Duration (Seconds)')
    
    # Save the graph
    os.makedirs('outputs', exist_ok=True)
    plt.savefig('outputs/threat_scatter.png', bbox_inches='tight')
    print("✅ Visual Threat Map saved to outputs/threat_scatter.png\n")

if __name__ == "__main__":
    run_threat_detection()