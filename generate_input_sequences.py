# Define a function that generates input sequences for the GPT-3 model based on the preprocessed data. This function should take as input a single historical data point, such as the electricity price and consumption for a specific hour, and generate an input sequence that includes relevant contextual information and a prompt asking the model to predict the price and consumption for the next hour.

def generate_input_sequence(data_point):
    # Extract relevant features from the data point
    hour = data_point["hour"]
    demand = data_point["hourly_demand"]
    price = data_point["hourly_average_price"]
    
    # Format the features as a string and add relevant contextual information
    #context = f"Current hour: {hour}\nCurrent demand: {demand} kWh\nCurrent price: {price} cents/kWh\n\nPredict the price and demand for the next hour."
    
    # Return the input sequence as a dictionary with the context and prompt
    #return {"context": context, "prompt": "Predict the price and demand for the next hour."}

    ##context = f"Current hour: {hour}\nCurrent demand: {demand} kWh\nCurrent price: {price} cents/kWh\n\n"
    ##prompt = "Please provide the predicted price and demand for the next hour in the format: 'Price: X.XX cents/kWh, Demand: YYYYY.YY kWh'"
    
    ##return {"context": context, "prompt": prompt}

    context = f"Hour: {hour}. Demand: {demand} kWh. Price: {price} cents/kWh. "
    prompt = "Based on this information, predict the electricity price in cents/kWh and demand in kWh for the next hour."
    
    return {"context": context, "prompt": prompt}
