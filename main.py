

from statistics import mean
from collections import defaultdict
import sys


class LogMonitor:

    def __init__(self):
        self.logs = []
        self.type_severity_map = defaultdict(list)
    
    def add_log(self, timestamp, log_type, severity):
        self.logs.append((timestamp, severity))
        self.type_severity_map[log_type].append((timestamp, severity))
        return f"No output"
    
    def mean_severity_by_type(self, log_type):
        if not self.type_severity_map[log_type]:
            return "Mean: 0.0"
        return f"Mean: {mean(severity for _, severity in self.type_severity_map[log_type]):.6f}"
    
    def mean_severity_before(self, timestamp):
        return self.mean_before(self.logs, timestamp=timestamp)
    
    def mean_severity_after(self, timestamp):
        return self.mean_after(self.logs, timestamp=timestamp)
    
    def mean_severity_type_before(self, log_type, timestamp):
        return self.mean_before(self.type_severity_map[log_type], timestamp=timestamp)
    
    def mean_severity_type_after(self, log_type, timestamp):
        return self.mean_after(self.type_severity_map[log_type], timestamp=timestamp)
    
    def mean_after(self, logs, timestamp):
        filtered_severities = [severity for ts, severity in logs if ts > timestamp]
        if not filtered_severities:
            return "Mean: 0.0"
        return f"Mean: {mean(filtered_severities):.6f}"

    def mean_before(self, logs, timestamp):
        filtered_severities = [severity for ts, severity in logs if ts < timestamp]
        if not filtered_severities:
            return "Mean: 0.0"
        return f"Mean: {mean(filtered_severities):.6f}"



def main():
    log_monitor = LogMonitor()
    input = sys.argv[1]
    cmds = input.split("\n")
    output = []

    for cmd in cmds:
        parts = cmd.strip().split()
        command = parts[0]

        if command == '1':
            timestamp, log_type, severity = parts[1].split(';')
            result = log_monitor.add_log(int(timestamp), log_type, float(severity))
            output.append(result)

        elif command == '2':
            log_type = parts[1]
            result = log_monitor.mean_severity_by_type(log_type)
            output.append(result)

        elif command == '3':
            sub_command = parts[1]
            timestamp = int(parts[2])
            if sub_command == 'BEFORE':
                result = log_monitor.mean_severity_before(timestamp)
            elif sub_command == 'AFTER':
                result = log_monitor.mean_severity_after(timestamp)
            output.append(result)

        elif command == '4':
            sub_command = parts[1]
            log_type = parts[2]
            timestamp = int(parts[3])
            if sub_command == 'BEFORE':
                result = log_monitor.mean_severity_type_before(log_type, timestamp)
            elif sub_command == 'AFTER':
                result = log_monitor.mean_severity_type_after(log_type, timestamp)
            output.append(result)

    print("\n".join(output))

if __name__ == '__main__':
    main()
