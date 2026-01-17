from datasets import load_dataset
from transformers import T5Tokenizer, AutoModelForSeq2SeqLM, TrainingArguments, Trainer, DataCollatorForSeq2Seq

model_name = "csebuetnlp/banglat5"
dataset = load_dataset("json", data_files="data/bangla_instructions.json")

tokenizer = T5Tokenizer.from_pretrained(model_name, legacy=True)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def preprocess(example):
    # Extract from nested "inputs"
    inputs_dict = example.get("inputs", {})
    instruction = inputs_dict.get("instruction", "")
    input_text = inputs_dict.get("input", "")
    output_text = inputs_dict.get("output", "")

    # Build prompt
    if input_text:
        prompt = instruction + " " + input_text
    else:
        prompt = instruction

    # Tokenize with text + text_target
    model_inputs = tokenizer(prompt, truncation=True, padding="max_length", max_length=128)
    labels = tokenizer(text_target=output_text, truncation=True, padding="max_length", max_length=128)

    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

tokenized = dataset["train"].map(preprocess)

args = TrainingArguments(
    output_dir="model/fine_tuned_model",
    per_device_train_batch_size=4,
    num_train_epochs=3,
    logging_dir="logs/",
    save_steps=500
)

trainer = Trainer(
    model=model,
    args=args,
    train_dataset=tokenized,
    tokenizer=tokenizer,
    data_collator=DataCollatorForSeq2Seq(tokenizer, model=model)
)

trainer.train()
