# HeaderSpy

Welcome to the HeaderSpy, a powerful tool designed to extract and analyze email headers. This tool empowers you to effortlessly retrieve valuable information such as sender details, recipient information, timestamps, and routing data from email headers.

- Additionally, users can explore a comprehensive array of supplementary header fields, such as Message ID, Return Path, Received-SPF, and DKIM Signature. 

- This tool serves as an indispensable asset for forensic analysts, offering robust capabilities for scrutinizing email authenticity, comprehending intricate email routing, and extracting vital details about both the sender and recipient.

- The output is presented in a tabular format making it easy to read and analyze.
## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
   - [Install Dependencies](#installdependices)
- [Usage](#usage)
- [Commands](#commands)
- [Author](#author)


## Features

- **Header Extraction:** Quickly parse email headers from a given file, making it easy to examine the email's metadata.

- **Message Information:** Gain insights into critical email header fields like To, From, Subject, Date, and Delivered-To.

- **Additional Fields:** Explore an array of additional email header fields, including Message ID, Return Path, Reply-To, X-Headers, Received, MIME Version, Content Type, Received-SPF, DKIM Signature, Authentication Results, X-Mailer, and DMARC Results.

- **Custom Output:** Save the analyzed email header information to a file or display it directly in the console.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python:** The tool is built with Python, so you need to have Python installed on your system. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/)


## Installation

1. **Cloning:** Clone the repository to your local machine:

   ```shell
   git clone https://github.com/yourusername/HeaderSpy.git

2. **Change Directory:** Navigate to the project directory using the `cd` command:

   ```shell
   cd HeaderSpy
   ```

## Install Dependencies

3. **Install Dependencies:** The tool relies on external Python packages. You can install these dependencies using pip, a package manager for Python:

   ```shell
   pip install tabulate colorama
   ```
## Usage

**Commands:**

   ```shell
   python HeaderSpy.py -hf {file path or file name}
   ```

- You can use both the path of the email header file or Header file name.
- While using File name ,the email header file and the tool should be same in location.   

 ```shell 
  python HeaderSpy.py -hf header.txt 
   ```
   ```shell
   python HeaderSpy --header_file header.txt 
   ```
 - Both of the Commands, Analyzes the email header in the 'header.txt' file and displays the results on the console.


 ```shell
   python HeaderSpy.py -hf header.txt -O results.txt
   ```
 ```shell
    python HeaderSpy.py --header_file header.txt --output_file results.txt
   ```
   
- Both the Commands, Analyzes the email header in the 'header.txt' file and saves the analysis results in the 'results.txt' file.

## Author

This tool was developed by **Hariharan.T**

  Thank you for using HeaderSpy, and we hope it simplifies your email header analysis tasks. 


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
