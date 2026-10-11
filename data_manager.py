import json

# Path to your data file
DATA_FILE = "bank_data.json"

# ------------------------------
# Load Data Function
# ------------------------------
def load_data():
    """Load data from JSON file or create default if missing."""
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        # Default structure if file does not exist
        return {
            "managers": {"admin": {"password": "admin123"}},
            "staff": {},
            "customers": {}
        }

# ------------------------------
# Save Data Function
# ------------------------------
def save_data(data):
    """Save data to the JSON file."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
