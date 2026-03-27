# 🛡️ My Local AI Speed Test Dashboard

Hey! I built this to answer: **"Can small AI models run on my regular laptop instead of expensive cloud services?"**

## 📊 What I Found (My Laptop Numbers)

| AI Model | Answer Speed | Extra RAM | Best For |
|----------|--------------|-----------|----------|
| `llama3.2` (smallest) | **5.4 seconds** ⭐ | Almost nothing | Fast chats |
| `gemma3` (medium) | 6.6 seconds | Almost nothing | Good balance |
| `qwen2` (largest) | 12.2 seconds | Almost nothing | Long answers |

**Real test**: gemma3 answered live in **8.9 seconds** (totally normal!)

## 🚀 How Anyone Can Run It (2 Minutes)

```bash
git clone https://github.com/nehamanore09/Local-SLM-Benchmark.git
cd Local-SLM-Benchmark
pip install -r requirements.txt
streamlit run app.py
```

**Boom!** Opens cool dashboard at `localhost:8501` 🎉

## 💡 Why I Built This

**Problem**: Companies pay ₹800-5000/month to OpenAI + send customer data to USA  
**My Fix**: Run AI completely offline on normal laptops:
- ✅ **₹0 cost** 
- ✅ **Private** (data never leaves your laptop)
- ✅ **Fast enough** (5.4s answers)
- ✅ **No internet needed**

## 🎯 Real Jobs That Need This
- 🏥 Hospitals → Patient chatbots (private data)
- 🏦 Banks → Document review (financial secrets safe)
- 🛒 Stores → Product help (customer data private)
- 📚 Schools → Student helpers (works offline)

## Quick Stats:
- ✅ 5.4s fastest response (llama3.2)
- ✅ 0MB extra RAM usage
- ✅ 3 models compared
- ✅ Production-ready dashboard
- ✅ Zero cloud costs
