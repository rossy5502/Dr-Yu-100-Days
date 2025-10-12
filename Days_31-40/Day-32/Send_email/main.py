import random
from datetime import datetime
from pathlib import Path
from typing import List, Optional
import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage

now=datetime.now()
weekday=now.weekday()


# the following code is to send a quote of the day to an email


def read_quotes(file_path: str = "quotes.txt") -> List[str]:
    """
    Read quotes from a text file and return them as a list of strings.
    
    Args:
        file_path: Path to the quotes file. Defaults to 'quotes.txt'.
        
    Returns:
        List of quotes as strings.
        
    Raises:
        FileNotFoundError: If the quotes file doesn't exist.
        IOError: If there's an error reading the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # Remove any empty lines and strip whitespace
            quotes = [line.strip() for line in file]
            return [quote for quote in quotes if quote]
    except FileNotFoundError:
        raise FileNotFoundError(f"Quotes file not found at {file_path}")
    except IOError as e:
        raise IOError(f"Error reading quotes file: {e}")


def get_random_quote(quotes: List[str]) -> str:
    """Return a random quote from the provided list of quotes."""
    if not quotes:
        raise ValueError("No quotes available")
    return random.choice(quotes)

def send_email(quote_of_the_day):
    msg = MIMEText(quote_of_the_day)
    msg["Subject"] = "Hello from smtplib"
    msg["From"] = "you@example.com"
    msg["To"] = "someone@example.com"

    with smtplib.SMTP("localhost", 8025) as server:
        server.send_message(msg)

    print(f"SUCCESS :Email sent \n {quote_of_the_day}!")
def main() -> None:
    if weekday:
        """Main function to display a random quote."""
        try:
            quotes = read_quotes()
            quote = get_random_quote(quotes)
            send_email(quote)
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
    #for the stmp to work on local server run the below prompt first
    #py -m aiosmtpd -n -l localhost:8025


