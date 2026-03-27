import ollama
import time
import psutil
import pandas as pd
import numpy as np

# Your exact 3 models (from JSON above)
models = ['llama3.2:latest', 'gemma3:4b', 'qwen2:7b']
prompt = "Explain RAG in AI (50 words max)"  # Fixed for fair comparison
results = []

print("🏃 Starting benchmark...")

for model in models:
    print(f"\n⏱️  Testing {model}...")
    latencies = []
    memories = []
    
    for i in range(10):  # 10 runs per model
        start_time = time.time()
        start_mem = psutil.Process().memory_info().rss / (1024**2)  # MB
        
        response = ollama.chat(model=model, messages=[{'role': 'user', 'content': prompt}])
        
        latency = (time.time() - start_time) * 1000  # ms
        memory_used = psutil.Process().memory_info().rss / (1024**2) - start_mem
        
        latencies.append(latency)
        memories.append(memory_used)
        print(f"  Run {i+1}: {latency:.0f}ms, {memory_used:.0f}MB")
    
    results.append({
        'model': model,
        'avg_latency_ms': np.mean(latencies),
        'std_latency': np.std(latencies),
        'avg_memory_mb': np.mean(memories),
        'total_tokens': len(response['message']['content'])
    })

# SAVE YOUR INTERVIEW CSV
df = pd.DataFrame(results)
df.to_csv('benchmark_results.csv', index=False)
print("\n RESULTS SAVED TO benchmark_results.csv")
print(df.round(2))