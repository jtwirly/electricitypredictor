import openai
import os

# Set up OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Get user input
temperature = input("Enter the current temperature (in °F): ")
solar_power = input("Enter the solar power generation (in %): ")

# Generate input sequence based on user input
input_sequence = f"The current temperature is {temperature}°F and solar power generation is at {solar_power}%, what will be the predicted electricity prices and consumption for the next hour?"

# Generate output sequence from GPT-3 model
def generate_response(prompt, max_tokens=1024, temperature=0.7):
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=input_sequence,
      max_tokens=max_tokens,
      n=1,
      stop=None,
      temperature=0.7
    )
    return response["choices"][0]["text"]

try:
    prompt = input_sequence
    response = generate_response(prompt, max_tokens=100)
    print(response)
except Exception as e:
    print(f"Error: {e}")
    print("I'm sorry, there was an error processing your request.")

# Extract predicted price and demand from output sequence
##predicted_price = float(response["choices"][0]["text"].split(": ")[1].split(" ")[0])
##predicted_demand = float(response["choices"][0]["text"].split(": ")[2].split(" ")[0])

# Print the predicted price and demand
##print(f"Predicted price: {predicted_price:.2f} cents/kWh")
##print(f"Predicted demand: {predicted_demand:.2f} kWh")
