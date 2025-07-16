import re
from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plt

def analyze_logs(log_file):
    """Analyze web server logs for suspicious traffic patterns"""
    
    # Regex pattern for common log format
    log_pattern = r'(\d+\.\d+\.\d+\.\d+).*\[(.*?)\].*\"(.*?)\".*(\d{3})'
    
    ip_counts = defaultdict(int)
    status_counts = defaultdict(int)
    request_counts = defaultdict(int)
    suspicious_ips = set()
    user_agents = defaultdict(int)
    
    with open(log_file) as f:
        for line in f:
            try:
                match = re.match(log_pattern, line)
                if match:
                    ip, timestamp, request, status = match.groups()
                    ip_counts[ip] += 1
                    status_counts[status] += 1
                    request_counts[request.split()[1]] += 1
                    
                    # Extract User-Agent if available
                    ua_match = re.search(r'\"(.*?)\"$', line)
                    if ua_match:
                        user_agent = ua_match.group(1)
                        user_agents[user_agent] += 1
                    
                    # Bot detection heuristics
                    if ip_counts[ip] > 1000:  # Excessive requests
                        suspicious_ips.add(ip)
                    if status == '404' and ip_counts[ip] > 100:  # Many 404s
                        suspicious_ips.add(ip)
                    if 'bot' in line.lower() or 'crawl' in line.lower():  # Common bot UAs
                        suspicious_ips.add(ip)
            except:
                continue
    
    # Generate reports
    print("\n=== Traffic Analysis Report ===")
    print(f"Total unique IPs: {len(ip_counts)}")
    print(f"Total requests analyzed: {sum(ip_counts.values())}")
    print(f"Suspicious IPs detected: {len(suspicious_ips)}")
    
    print("\nTop 10 IPs by request volume:")
    for ip, count in sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"{ip}: {count} requests ({'SUSPICIOUS' if ip in suspicious_ips else 'normal'})")
    
    print("\nTop 10 requested URLs:")
    for url, count in sorted(request_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"{url}: {count} requests")
    
    print("\nStatus code distribution:")
    for code, count in sorted(status_counts.items()):
        print(f"HTTP {code}: {count} responses")
    
    # Visualization
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    pd.Series(dict(sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)[:20])).plot(kind='bar')
    plt.title('Top 20 IPs by Request Volume')
    plt.ylabel('Requests')
    plt.xticks(rotation=45)
    
    plt.subplot(1, 2, 2)
    pd.Series(dict(sorted(request_counts.items(), key=lambda x: x[1], reverse=True)[:10])).plot(kind='bar')
    plt.title('Top 10 Requested URLs')
    plt.ylabel('Requests')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.savefig('traffic_analysis.png')
    print("\nVisualization saved as traffic_analysis.png")
    
    return suspicious_ips

if __name__ == "__main__":
    print("Analyzing sample-log.log...")
    suspicious = analyze_logs('sample-log.log')
    
    with open('suspicious_ips.txt', 'w') as f:
        f.write("\n".join(suspicious))
    print("\nSuspicious IPs saved to suspicious_ips.txt")