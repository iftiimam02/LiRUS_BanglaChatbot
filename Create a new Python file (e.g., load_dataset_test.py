from datasets import load_dataset

# ✅ Load Alpaca-Bangla dataset from HuggingFace
dataset = load_dataset("nihalbaig/alpaca-bangla")

# ✅ Print a sample
print(dataset["train"][0])

