import logging
from pathlib import Path
import sys
import platform
import time
import getpass

# Setting up logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Dynamically determine desktop path based on the OS
def get_desktop_path():
    if platform.system() == 'Windows':
        return Path.home() / 'Desktop'
    elif platform.system() == 'Darwin':
        return Path.home() / 'Desktop'
    else:
        return Path.home() / 'Desktop'

# Color definitions
COLOR_RED = '\033[31m'
COLOR_GREEN = '\033[32m'
COLOR_BLUE = '\033[34m'
COLOR_RESET = '\033[0m'

# Ensure requirements are met
required_python_version = (3, 6)
if sys.version_info < required_python_version:
    logger.error('Python 3.6 or newer is required.')
    sys.exit(1)

# Keylogger with daemon threads
class Keylogger:
    def __init__(self):
        self.running = True

    def start(self):
        while self.running:
            # Simulated key logging logic
            time.sleep(1)

    def stop(self):
        self.running = False
        logger.info('Keylogger stopped.')

keylogger = Keylogger()

# User input with retry mechanism
max_retries = 3
for attempt in range(max_retries):
    try:
        user_input = input('Please enter a command: ')
        logger.info(f'User input received: {user_input}')
        break  # Exit loop on valid input
    except Exception as e:
        logger.error(f'Error: {e}. Attempt {attempt + 1} of {max_retries}.')
        if attempt < max_retries - 1:
            continue  # Retry input
        else:
            logger.error('Max retries exceeded.')
            sys.exit(1)

# Start keylogger thread
keylogger_thread = threading.Thread(target=keylogger.start)
keylogger_thread.daemon = True
keylogger_thread.start()