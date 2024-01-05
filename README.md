
# Site Reliability Engineering - Exercise

The utility monitors the availability of HTTP API endpoints per domain.

# Getting Started

## Overview
This program automates the health checking of HTTP API endpoints:
- **Endpoint Configuration**: It begins by reading a YAML configuration file that lists the API endpoints, following the structure outlined in `sample.yaml`.
- **Parsing**: The YAML file is parsed to extract endpoint information.
- **Health Checks**: Each endpoint is checked for availability. An endpoint is considered *healthy* if it responds with a `2xx` status code within a latency threshold of `500ms`.
- **Availability Metric**: The script calculates the availability percentage for each domain using the formula: `100 * (number of HTTP requests that had an outcome of UP / number of HTTP requests)`

### What is in the files?

FETCH-EXERCISE

    ├── app.log                 # descriptive logs of program flow
    ├── argparser.py            # Configuration for reading console input - file path
    ├── caller.py               # Responsible for making an API call and tracking the response
    ├── checkhealth.py          # Initiates API calls and calculates availability per domain
    ├── endpoint.py             # Defines Schema for endpoints like in `sample.yaml`
    ├── logger.py               # Configuration for logging to `app.log`
    ├── main.py                 # Main (entry point)
    ├── reader.py               # Reads file path and reads contents as text lines
    └── README.md               # You are reading it right now :)
    └── requirements.txt        # Contains Python config packages - for installation
    └── response.py             # Defines schema for response (code, latency, outcome)
    └── sample.yaml             # Sample input file
    └── utils.py                # Helper functions
    └── yamlparser.py           # Extracts endpoints from contents of a sample file

## Installation

### Prerequisites

Before you begin, ensure you have met the following requirements:

**Python**: the scripts are written in Python. If you do not have Python installed on your system, it can be downloaded from the [official Python website](https://www.python.org/downloads/). This project is compatible with Python 3.x. To verify that Python is installed correctly, open your terminal and run:

```bash
python --version
```

In case you do not have `pip`, install it through [tutorial](https://pip.pypa.io/en/stable/installation/)

Next, clone this repository and install the requirements by running:

```bash
git clone https://github.com/MohamedAliHabib/fetch-exercise.git
cd fetch-exercise
pip install -r requirements.txt
```

## Usage

Run `main.py` and pass the input file path as an argument. Checks are run periodically every 15s until interrupted by the user by pressing `ctrl+c`

```bash
python main.py PATH
```

To see an example, run:
```bash
python main.py ./sample.yaml
```

The script will log the calculated availability to terminal every 15 seconds for each domain as follows:
```bash
fetch.com has 33% availability percentage
www.fetchrewards.com has 100% availability percentage
```

Information and error logs of the workflow will logged in `app.log`


# Thank you

Thanks for taking the time to stop by :)<br/>

Enjoy some Bach in the meantime:
[Spotify: Sonata for Violin Solo No. 1 in G Minor, BWV 1001: 1. Adagio - Hilary Hahn](https://open.spotify.com/track/2lh5pqyvcUnXpsGRzhm737?si=f4fa748f750b4976)
