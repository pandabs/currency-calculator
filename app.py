from flask import Flask, render_template, request

app = Flask(__name__)

# Currency exchange rates
exchange_rates = {
    'euro': 0.01417,
    'gbp': 0.0100,
    'aud': 0.02140,
    'cad': 0.02027
}

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        amount_inr = request.form.get('amountInr')
        currency = request.form.get('currency')

        if currency in exchange_rates and amount_inr:
            amount_inr = float(amount_inr)
            # Calculate the equivalent amount in the selected currency
            equivalent_amount = amount_inr * exchange_rates[currency]
            result = f"You need {equivalent_amount:.2f} {currency.upper()} to get {amount_inr} INR."
        else:
            result = "Invalid currency name or amount."

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
