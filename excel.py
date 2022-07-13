# Import pandas
import pandas as pd

# Load the xlsx file
excel_data = pd.read_excel("static/files/Template.xlsx")
# Read the values of the file in the dataframe
data = pd.DataFrame(excel_data, columns=['os', 'ag', 'type', 'key', 'tg', 'af'])
# Print the content

print("The content of the file is:\n", data['os'][0])