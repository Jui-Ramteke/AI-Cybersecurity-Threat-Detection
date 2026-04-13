import pandas as pd
import numpy as np
import os

def generate_network_data(num_samples=5000):
    np.random.seed(42)
    
    # Normal Traffic
    normal_data = {
        'duration': np.random.uniform(0.1, 5.0, int(num_samples * 0.8)),
        'src_bytes': np.random.normal(500, 100, int(num_samples * 0.8)),
        'dst_bytes': np.random.normal(2000, 500, int(num_samples * 0.8)),
        'failed_logins': np.zeros(int(num_samples * 0.8)),
        'label': ['normal'] * int(num_samples * 0.8)
    }
    
    # Attack Traffic (DoS, Brute Force anomalies)
    attack_data = {
        'duration': np.random.uniform(10.0, 50.0, int(num_samples * 0.2)),
        'src_bytes': np.random.normal(10000, 5000, int(num_samples * 0.2)), # High payload
        'dst_bytes': np.random.normal(50, 10, int(num_samples * 0.2)),
        'failed_logins': np.random.randint(5, 50, int(num_samples * 0.2)), # Brute force indicator
        'label': ['attack'] * int(num_samples * 0.2)
    }
    
    df_normal = pd.DataFrame(normal_data)
    df_attack = pd.DataFrame(attack_data)
    
    df = pd.concat([df_normal, df_attack]).sample(frac=1).reset_index(drop=True)
    
    # Ensure data dir exists
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/network_traffic.csv', index=False)
    print("✅ Simulated dataset generated at data/network_traffic.csv")
    return df

if __name__ == "__main__":
    generate_network_data()