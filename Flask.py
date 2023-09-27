from flask import Flask, render_template, request
import pandas as pd
import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        portfolio_value = float(request.form["portfolio_value"])

        # Generate or update your DataFrame based on user input
        # For demonstration purposes, creating a sample DataFrame
        data = {'Ticker': ['AAPL', 'MSFT'], 'Stock Price': [150, 300]}
        final_dataframe = pd.DataFrame(data)

        # Calculate the number of shares to buy based on user input
        position_size = portfolio_value / len(final_dataframe.index)
        final_dataframe["Number of Stocks to Buy"] = final_dataframe["Stock Price"].apply(lambda stock_price: math.floor(position_size / stock_price))

        return render_template("index.html", data=final_dataframe)
    return render_template("index.html", data=None)

if __name__ == "__main__":
    app.run(debug=True)
