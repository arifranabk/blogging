import logging
import colorama
from colorama import Fore, Style

def setup_logger():
    colorama.init(autoreset=True)
    
    logger = logging.getLogger('SEO_Toolkit')
    logger.setLevel(logging.INFO)
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    formatter = logging.Formatter(f'{Fore.CYAN}%(asctime)s{Style.RESET_ALL} - %(levelname)s - %(message)s', datefmt='%H:%M:%S')
    console_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)
    return logger
