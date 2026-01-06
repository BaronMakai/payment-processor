import logging
import os
import json

def load_config(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Configuration file '{filename}' not found")
    with open(filename, 'r') as file:
        return json.load(file)

def setup_logging(level=logging.INFO, filename=None):
    logging.basicConfig(level=level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    if filename:
        logging.getLogger().addHandler(logging.FileHandler(filename))