import yfinance as yf

def display_menu():
    print("\nStock Portfolio Tracker")
    print("1. Add stock to portfolio")
    print("2. Remove stock from portfolio")
    print("3. View portfolio performance")
    print("4. Exit")

def get_stock_price(ticker):
    try:
        stock = yf.Ticker(ticker)
        price = stock.history(period="1d")['Close'].iloc[-1]
        return price
    except IndexError:
        print(f"Error fetching data for {ticker}: No price data found. Is the ticker correct?")
        return None
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

def add_stock(portfolio):
    ticker = input("Enter stock ticker: ").upper()
    if not ticker.isalpha():
        print("Invalid ticker. Please enter a valid stock ticker (e.g., AAPL, TSLA).")
        return

    try:
        shares = float(input("Enter number of shares: "))
        if shares <= 0:
            print("Number of shares must be greater than zero.")
            return
    except ValueError:
        print("Invalid input. Please enter a numeric value for the number of shares.")
        return

    price = get_stock_price(ticker)
    if price:
        portfolio[ticker] = {
            "shares": shares,
            "price": price
        }
        print(f"Added {shares} shares of {ticker} at ${price:.2f} per share.")

def remove_stock(portfolio):
    ticker = input("Enter stock ticker to remove: ").upper()
    if ticker in portfolio:
        del portfolio[ticker]
        print(f"Removed {ticker} from portfolio.")
    else:
        print("Stock not found in portfolio.")

def view_portfolio(portfolio):
    if not portfolio:
        print("Portfolio is empty.")
        return

    print("\nYour Portfolio:")
    total_value = 0

    for ticker, data in portfolio.items():
        price = get_stock_price(ticker)
        if price:
            current_value = price * data["shares"]
            total_value += current_value
            print(f"{ticker}: {data['shares']} shares @ ${price:.2f} per share = ${current_value:.2f}")
        else:
            print(f"{ticker}: Error fetching current price.")

    print(f"\nTotal Portfolio Value: ${total_value:.2f}")

def main():
    portfolio = {}

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_stock(portfolio)
        elif choice == "2":
            remove_stock(portfolio)
        elif choice == "3":
            view_portfolio(portfolio)
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
