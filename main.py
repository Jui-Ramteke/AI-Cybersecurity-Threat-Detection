import time
from src.dataset_sim import generate_network_data
from src.preprocess import preprocess_data
from src.train_model import train_and_evaluate
from src.detect import run_threat_detection

def run_pipeline():
    print("="*50)
    print(" 🛡️ AI-POWERED CYBERSECURITY THREAT DETECTION 🛡️")
    print("="*50)
    time.sleep(1)
    
    print("\n[PHASE 1] Generating Simulated Network Traffic...")
    generate_network_data()
    time.sleep(1)
    
    print("\n[PHASE 2] Preprocessing and Scaling Data...")
    X_train_scaled, X_test_scaled, y_train, y_test = preprocess_data()
    time.sleep(1)
    
    print("\n[PHASE 3] Training Supervised Model (Random Forest)...")
    train_and_evaluate()
    time.sleep(1)
    
    print("\n[PHASE 4] Running Live Unsupervised Threat Detection...")
    run_threat_detection()
    
    print("\n" + "="*50)
    print(" ✅ PIPELINE EXECUTION COMPLETE. ALL SYSTEMS SECURE.")
    print("="*50)

if __name__ == "__main__":
    run_pipeline()