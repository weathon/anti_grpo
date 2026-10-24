import wandb
print("finishing", wandb.run.name if wandb.run else None)
wandb.finish()
print("wandb finished")
