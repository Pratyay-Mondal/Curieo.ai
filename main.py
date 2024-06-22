import sys
from statistics import mean
from collections import defaultdict



class LogMonitor:

    def __init__(self):
        self.logs = []
        self.type_severity_map = defaultdict(list)
    
    def add_log(self, timestamp, log_type, severity):
        self.logs.append((timestamp, log_type, severity))
        self.type_severity_map[log_type].append((timestamp, severity))
    
    def mean_severity_by_type(self, log_type):
        if log_type not in self.type_severity_map or not self.type_severity_map[log_type]:
            return "Mean: 0.0"
        return f"Mean: {mean(severity for _, severity in self.type_severity_map[log_type]):.6f}"
    
    def mean_severity_before(self, timestamp):
        filtered_severities = [severity for ts, _, severity in self.logs if ts < timestamp]
        if not filtered_severities:
            return "Mean: 0.0"
        return f"Mean: {mean(filtered_severities):.6f}"
    
    def mean_severity_after(self, timestamp):
        filtered_severities = [severity for ts, _, severity in self.logs if ts > timestamp]
        if not filtered_severities:
            return "Mean: 0.0"
        return f"Mean: {mean(filtered_severities):.6f}"
    
    def mean_severity_type_before(self, log_type, timestamp):
        if log_type not in self.type_severity_map or not self.type_severity_map[log_type]:
            return "Mean: 0.0"
        filtered_severities = [severity for ts, severity in self.type_severity_map[log_type] if ts < timestamp]
        if not filtered_severities:
            return "Mean: 0.0"
        return f"Mean: {mean(filtered_severities):.6f}"
    
    def mean_severity_type_after(self, log_type, timestamp):
        if log_type not in self.type_severity_map or not self.type_severity_map[log_type]:
            return "Mean: 0.0"
        filtered_severities = [severity for ts, severity in self.type_severity_map[log_type] if ts > timestamp]
        if not filtered_severities:
            return "Mean: 0.0"
        return f"Mean: {mean(filtered_severities):.6f}"





def main():
    log_monitor = LogMonitor()
    
    with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
        for line in infile:
            parts = line.strip().split()
            command = parts[0]

            if command == '1':
                timestamp, log_type, severity = parts[1].split(';')
                log_monitor.add_log(int(timestamp), log_type, float(severity))
            elif command == '2':
                log_type = parts[1]
                result = log_monitor.mean_severity_by_type(log_type)
                outfile.write(result + '\n')
            elif command == '3':
                sub_command = parts[1]
                timestamp = int(parts[2])
                if sub_command == 'BEFORE':
                    result = log_monitor.mean_severity_before(timestamp)
                elif sub_command == 'AFTER':
                    result = log_monitor.mean_severity_after(timestamp)
                outfile.write(result + '\n')
            elif command == '4':
                sub_command = parts[1]
                log_type = parts[2]
                timestamp = int(parts[3])
                if sub_command == 'BEFORE':
                    result = log_monitor.mean_severity_type_before(log_type, timestamp)
                elif sub_command == 'AFTER':
                    result = log_monitor.mean_severity_type_after(log_type, timestamp)
                outfile.write(result + '\n')



if __name__ == '__main__':
    main()
