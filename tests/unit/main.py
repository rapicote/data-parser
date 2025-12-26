# main.py
import argparse
import logging
from data_parser.config import Config
from data_parser.data_loader import DataLoader
from data_parser.parsing_engine import ParsingEngine

def main():
    parser = argparse.ArgumentParser(description='Data Parser')
    parser.add_argument('--config', type=str, help='Path to the configuration file')
    parser.add_argument('--log-level', type=str, choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], help='Logging level')
    
    args = parser.parse_args()
    
    logging.basicConfig(level=getattr(logging, args.log_level.upper()))
    
    config = Config(args.config)
    
    data_loader = DataLoader(config)
    data_loader.load_data()
    
    parsing_engine = ParsingEngine(config, data_loader.parsed_data)
    parsing_engine.parse_data()
    
if __name__ == '__main__':
    main()