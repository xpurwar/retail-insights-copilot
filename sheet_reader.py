import pandas as pd
#  An implementation of the Microsoft paper pip SpreadsheetLLM
from sheetwise import SpreadsheetLLM

# Initialize the framework
sllm = SpreadsheetLLM()

# Load your spreadsheet
df = pd.read_excel("/Users/ananyapurwar/Coder_Boi/retail-insights-copilot/Data/sample_-_superstore.xls")

# Compress and encode for LLM use
llm_ready_text = sllm.compress_and_encode_for_llm(df)

# Copy and paste this text directly into ChatGPT/Claude
print(llm_ready_text)