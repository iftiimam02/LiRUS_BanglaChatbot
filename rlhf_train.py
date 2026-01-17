# rlhf_train.py
from trl import PPOTrainer, PPOConfig
from transformers import AutoTokenizer, AutoModelForCausalLM

config = PPOConfig(model_name="Mahadih534/HydraIndicLM")
tokenizer = AutoTokenizer.from_pretrained(config.model_name)
model = AutoModelForCausalLM.from_pretrained(config.model_name)

ppo_trainer = PPOTrainer(config, model=model, tokenizer=tokenizer)

query = "তুমি কে?"
response = "আমি লিরাস, একটি সহায়ক রোবট।"
reward = 1.0

ppo_trainer.step([query], [response], [reward])
