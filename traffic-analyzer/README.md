# Traffic Analyzer
A Python script for analyzing web server logs to detect suspicious traffic patterns.

## Features
- Analyzes web server logs for request counts by IP address.
- Detects suspicious IPs based on request volume and status codes.
- Generates a report of traffic analysis.
- Visualizes the top IPs and requested URLs.

## Requirements
- Python 3.x
- pandas
- matplotlib

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd traffic-analyzer
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage
Run the script with a log file:
```
python traffic_analyzer.py
```

## Output
The script will generate a report in the console and save suspicious IPs to `suspicious_ips.txt`. A visualization will be saved as `traffic_analysis.png`.