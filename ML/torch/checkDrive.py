import torch
print("Checking if GPU is available...")
if torch.cuda.is_available():
    print("GPU is available.")
    print(f"Number of GPUs available: {torch.cuda.device_count()}")
    print(f"Current GPU device: {torch.cuda.current_device()}")
    print(f"GPU Name: {torch.cuda.get_device_name(torch.cuda.current_device())}")
    print(f"CUDA Version: {torch.version.cuda}")
else:
    print("GPU is not available. Please check your CUDA installation or hardware configuration.")