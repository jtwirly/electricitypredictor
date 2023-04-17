# Load and preprocess the historical electricity price and consumption data

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import openai
import os

credential = DefaultAzureCredential()

secret_client = SecretClient(vault_url="https://keyvault1555.vault.azure.net/", credential=credential)
secret = secret_client.get_secret("openai")

openai.api_key = secret.value

#initialize OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

from azureml.core import Workspace, Dataset
import pandas as pd

# Load the dataset from the default datastore
default_ds = Workspace.from_config().get_default_datastore()
dataset = Dataset.Tabular.from_delimited_files(default_ds.path('ontario_electricity_demand/ontario_electricity_demand.csv'))

# Convert to Pandas dataframe
df = dataset.to_pandas_dataframe()

# Print the list of columns before setting the date as the index
print("Columns before setting date as index:", df.columns.tolist())

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

# Set date as index
df.set_index('date', inplace=True)

# Print the list of columns after setting the date as the index
print("Columns after setting date as index:", df.columns.tolist())

# Add additional features (e.g. weather, solar, and wind generation) if available

# Split the data into training and testing sets
train_data = df.loc['2003-01-01':'2018-12-31']
test_data = df.loc['2019-01-01':]

# Scale the data using MinMaxScaler
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
train_data_scaled = scaler.fit_transform(train_data)
test_data_scaled = scaler.transform(test_data)

print(df.columns)
print(df.columns.tolist())
