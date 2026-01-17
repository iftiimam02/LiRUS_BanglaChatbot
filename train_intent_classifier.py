import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments

# Path to pre-trained Bangla BERT
MODEL_NAME = "sagorsarker/bangla-bert-base"
MODEL_PATH = "./bangla_intent_model"

# Load dataset
df = pd.read_csv("intent_dataset.csv")

# Map intents to indices
intent_labels = sorted(df['intent'].unique())
label2id = {label: i for i, label in enumerate(intent_labels)}
id2label = {i: label for label, i in label2id.items()}
df['label'] = df['intent'].map(label2id)

# Tokenizer & model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_NAME,
    num_labels=len(intent_labels)
)

# Tokenize dataset
encodings = tokenizer(list(df['text']), truncation=True, padding=True)
labels = list(df['label'])

class IntentDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels
    def __len__(self):
        return len(self.labels)
    def __getitem__(self, idx):
        return {key: torch.tensor(val[idx]) for key, val in self.encodings.items()} | {'labels': torch.tensor(self.labels[idx])}

dataset = IntentDataset(encodings, labels)

# Training arguments
args = TrainingArguments(
    output_dir=MODEL_PATH,
    num_train_epochs=5,
    per_device_train_batch_size=4,
    save_strategy="epoch",
    logging_dir="./logs",
    logging_steps=5,
    report_to="none"
)

# Trainer
trainer = Trainer(
    model=model,
    args=args,
    train_dataset=dataset
)

# Train
trainer.train()

# Save tokenizer & model
tokenizer.save_pretrained(MODEL_PATH)
model.save_pretrained(MODEL_PATH)
print(f"✅ Model trained and saved in {MODEL_PATH}")
