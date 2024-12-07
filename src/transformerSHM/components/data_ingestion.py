import os 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config


