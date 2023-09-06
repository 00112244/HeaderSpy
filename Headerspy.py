import argparse
from tabulate import tabulate
from colorama import Fore, Style

# Function to print text inside a highlighted box
def print_highlighted_text(text):
    box_width = 80
    print("+" + "-" * (box_width - 2) + "+")
    for line in text.splitlines():
        print("|" + line.center(box_width - 2) + "|")
    print("+" + "-" * (box_width - 2) + "+")

# Function to parse email headers from a file
def parse_header(header_file):
    header_data = {}

    with open(header_file, 'r') as file:
        lines = file.readlines()

        current_field = None
        current_value = ''

        for line in lines:
            if ':' in line:
                if current_field:
                    header_data[current_field] = current_value.strip()

                current_field, current_value = line.split(':', 1)
                current_field = current_field.strip()
                current_value = current_value.strip()
            elif current_field:
                current_value += ' ' + line.strip()

        if current_field:
            header_data[current_field] = current_value.strip()

    return header_data

# Function to display email header information
def display_header_info(header_data):
    output = ''

    # Display message information
    output += f"{Fore.RED}Message Information:\n"
    output += "---------------------\n"
    output += Style.RESET_ALL

    # Commonly recognized email header fields
    fields = ['To', 'From', 'Subject', 'Date', 'Delivered-To']

    table_data = []
    for field in fields:
        if field in header_data:
            table_data.append([field, header_data[field]])

    output += tabulate(table_data, headers=[f"{Fore.BLUE}Field", f"{Fore.BLUE}Value"], tablefmt="fancy_grid")
    output += f"\n{Style.RESET_ALL}"

    # Display additional fields
    output += f"{Fore.RED}\nAdditional Fields:\n"
    output += "------------------\n"
    output += Style.RESET_ALL

    # Additional useful fields
    additional_fields = {
        'Message-ID': 'Message ID',
        'Return-Path': 'Return Path',
        'Reply-To': 'Reply-To',
        'X-Headers': 'X-Headers',
        'Received': 'Received',
        'MIME-Version': 'MIME Version',
        'Content-Type': 'Content Type',
        'Received-SPF': 'Received-SPF',
        'DKIM-Signature': 'DKIM Signature',
        'Authentication-Results': 'Authentication Results',
        'X-Mailer': 'X-Mailer',
        'DMARC-Results': 'DMARC Results'
    }

    table_data = []
    for field, label in additional_fields.items():
        if field in header_data:
            table_data.append([label, header_data[field]])

    output += tabulate(table_data, headers=[f"{Fore.BLUE}Field", f"{Fore.BLUE}Value"], tablefmt="fancy_grid")
    output += f"\n{Style.RESET_ALL}"

    return output   

if __name__ == "__main__":
    # Print a welcome message and tool information inside a highlighted box
    welcome_message = """
    Welcome to Email Header Analyzer Tool!
    This tool is designed to extract and analyze email headers.
     It can help you extract sender, recipient, timestamps, \n and  routing data from email headers.
    """
    print_highlighted_text(welcome_message)

    print("                                    A tool for email header Analysis")
    print("                                           By: Hariharan (00112244)\n")

    # Define command-line arguments and options
    parser = argparse.ArgumentParser(description='HeaderSpy', prog='HeaderSpy.py')
    parser.add_argument('-hf', '--header_file', type=str, help='Path to the email header file')
    parser.add_argument('-O', '--output_file', type=str, help='Path to the output file')
    args = parser.parse_args()

    # Parse email header file and display information
    if args.header_file:
        header_data = parse_header(args.header_file)
        output = display_header_info(header_data)

        # Save the output to a file or print it to the console
        if args.output_file:
            with open('analysis_results.txt', 'w', encoding='utf-8') as file:
                file.write(output)
        else:
            print(output)
    else:
        # Display the tool's help message if no header file is provided
        parser.print_help()
