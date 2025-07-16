# Traffic Analyzer

A Python tool for analyzing web server logs to detect suspicious traffic patterns, such as bots, crawlers, and excessive requests.

## Features

- Parses web server logs in the Common Log Format
- Detects suspicious IPs based on request volume, status codes, and user-agent heuristics
- Generates summary reports of traffic statistics
- Visualizes top IPs and requested URLs
- Outputs a list of suspicious IPs

## Requirements

See `requirements.txt` for dependencies.

## Usage

1. Place your log file (e.g., `sample-log.log`) in the project directory.
2. Run the analyzer:

   ```bash
   python traffic_analyzer.py
```markdown
# Traffic Analyzer

A Python tool for analyzing web server logs to detect suspicious traffic patterns, such as bots, crawlers, and excessive requests.

## Features

- Parses web server logs in the Common Log Format
- Detects suspicious IPs based on request volume, status codes, and user-agent heuristics
- Generates summary reports of traffic statistics
- Visualizes top IPs and requested URLs
- Outputs a list of suspicious IPs

## Requirements

See `requirements.txt` for dependencies.

## Usage

1. Place your log file (e.g., `sample-log.log`) in the project directory.
2. Run the analyzer:

   ```bash
   python traffic_analyzer.py
   ```

3. View the generated report in the terminal.
4. Check `traffic_analysis.png` for visualizations.
5. Suspicious IPs are saved to `suspicious_ips.txt`.

## Output

- **traffic_analysis.png**: Bar charts of top IPs and URLs
- **suspicious_ips.txt**: List of detected suspicious IP addresses
