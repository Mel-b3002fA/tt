from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments

# Load pre-trained model and tokenizer
model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Prepare dataset and tokenizer (you can fine-tune it on your data)
# Example of training setup
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=4,
    num_train_epochs=3,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,  # your dataset here
    eval_dataset=eval_dataset,  # your evaluation data here
)

trainer.train()
