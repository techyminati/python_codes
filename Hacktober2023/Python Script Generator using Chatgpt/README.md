# Python Script Generator

A Python script that interacts with the OpenAI API to generate Python code based on a given prompt.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [API Key](#api-key)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Python Script Generator is a command-line tool that utilizes the OpenAI API to generate Python code snippets based on a provided prompt. It simplifies the process of creating Python scripts for various tasks.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x
- Requests library
- buy openai Subscription and after use its API

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/python-script-generator.git
   ``````

2. Navigate to the project directory:
 
    ```bash
   cd python-script-generator
   ``````

## Usage

To generate a Python script, use the following command:

   ```bash
   python generate_script.py "Your prompt here" "output.py"
   ``````
   
## API Key

To use the OpenAI API, you need to first buy openai subscription and after that set your OpenAI API key as an environment variable. Follow these steps to obtain and set up your API key:

1. Sign up for an OpenAI account, buy openai subscription and create an API key on the OpenAI website.

2. Set your API key as an environment variable:

   ```bash
   $env:OPENAI_API_KEY="your-api-key"
   ``````

## Example

Here's an example of generating a Python script:

   ```bash
   $env:OPENAI_API_KEY="your-api-key"
   ``````
   ```bash
   generate_script.py "Create a function that calculates the factorial of a number" "factorial.py"
   ``````

Generated factorial.py:

 ```python
   def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

   ``````

