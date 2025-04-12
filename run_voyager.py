from voyager import Voyager
import os
import time

# Use mc_port instead of azure_login
# Default Minecraft port is 25565, but you can change it if needed
mc_port = 60650

# Checkpoint directory where all learning data will be saved
ckpt_dir = "ckpt"

# Create checkpoint directory if it doesn't exist
os.makedirs(ckpt_dir, exist_ok=True)

# Intelligently determine if this is the first run
action_dir = os.path.join(ckpt_dir, "action")
os.makedirs(action_dir, exist_ok=True)
chest_memory_path = os.path.join(action_dir, "chest_memory.json")

# Check if necessary checkpoint files exist
resume_learning = os.path.exists(chest_memory_path)
if resume_learning:
    print(f"Checkpoint files found in {ckpt_dir}. Will resume from checkpoint.")
else:
    print(f"No checkpoint files found in {ckpt_dir}. Starting fresh.")

# Print current time and configuration information
print("\n" + "="*50)
print(f"Start time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Minecraft port: {mc_port}")
print(f"Checkpoint directory: {ckpt_dir}")
print(f"Using model: {os.environ.get('ACTION_AGENT_MODEL', 'gpt-4o-2024-08-06')}")
print("="*50 + "\n")

# Initialize Voyager with resume=True to continue from the last checkpoint
print("Initializing Voyager...")
voyager = Voyager(
    mc_port=mc_port,
    resume=resume_learning,  # Automatically determined based on checkpoint files
    ckpt_dir=ckpt_dir,  # Specify checkpoint directory
    # OpenAI API Key will be loaded from the .env file
)

# Print initialization complete information
print("\n" + "="*50)
print("Voyager initialized successfully!")
print("Now, please follow these steps:")
print("1. Select 'Singleplayer' and create a new world")
print("2. Set game mode to 'Creative' and difficulty to 'Peaceful'")
print("3. After the world is created, press Esc key and click 'Open to LAN'")
print("4. Select 'Allow cheats: ON' and click 'Start LAN World'")
print("Voyager will join the game world soon...")
print("="*50 + "\n")

try:
    print("Starting learning process...")
    print("Tip: You can press Ctrl+C at any time to interrupt learning. Next time you run, it will automatically continue from the checkpoint")
    print("\n" + "="*50)
    print("LEARNING LOG START")
    print("="*50 + "\n")
    
    # Start lifelong learning
    voyager.learn()
    
    print("\n" + "="*50)
    print("Learning process completed!")
    print("="*50 + "\n")
    
except KeyboardInterrupt:
    print("\n" + "="*50)
    print("Learning process interrupted by user")
    print(f"All progress has been saved to the {ckpt_dir} directory")
    print("Next time you run, it will automatically continue from this point")
    print("="*50 + "\n")
except Exception as e:
    print("\n" + "="*50)
    print(f"An error occurred: {str(e)}")
    print(f"All progress has been saved to the {ckpt_dir} directory")
    print("Next time you run, it will automatically continue from the last checkpoint")
    print("="*50 + "\n")
    raise
