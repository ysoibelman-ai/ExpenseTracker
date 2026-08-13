import os
from dotenv import load_dotenv
load_dotenv()
data_file = os.getenv("DATA_FILE", "NONE")
currency = os.getenv("CURRENCY", "SHEKEL")
monthly_budget= os.getenv("MONTHLY_BUDGET","MINIMUM")