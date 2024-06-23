# Error Log Monitoring

## Description

This project is a Python-based solution for monitoring error logs and computing the mean severity of logs based on their types and timestamps.


## Problem Statement
### Properties

#### Timestamp 
- A 64-bit integer representing the time of the error occurrence.

#### Log Type 
- A string (max length of 100 characters) describing the error category.

#### Log Severity 
- A floating-point value indicating the error's severity.

Each log entry is formatted as: TIMESTAMP;LOG_TYPE;SEVERITY

Example: 1715744138011;INTERNAL_SERVER_ERROR;23.72


### Operations
#### 
1. Submit a new log entry.
2. Compute the mean severity by log type.
3. Compute the mean severity before a specific timestamp.
4. Compute the mean severity after a specific timestamp.
5. Compute the mean severity for a specific log type before a specific timestamp.
6. Compute the mean severity for a specific log type after a specific timestamp.



## Sample Input

```
1 1715744138011;INTERNAL_SERVER_ERROR;23.72
1 1715744138012;INTERNAL_SERVER_ERROR;10.17
2 INTERNAL_SERVER_ERROR
1 1715744138012;BAD_REQUEST;15.22
1 1715744138013;INTERNAL_SERVER_ERROR;23.72
3 BEFORE 1715744138011
3 AFTER 1715744138010
2 BAD_REQUEST
4 BEFORE INTERNAL_SERVER_ERROR 1715744138011
4 AFTER INTERNAL_SERVER_ERROR 1715744138010
```


## Sample Output

```
No output
No output
Mean: 16.945000
No output
No output
Mean: 0.0
Mean: 18.207500
Mean: 15.220000
Mean: 0.0
Mean: 19.203333
```


### Assumptions

1. Timestamps are given in ascending order.
2. The log type can be any UTF-8 string up to 100 characters, with at most 5 different log types.
3. Severity is a positive non-zero floating-point number.


<br/>


## Setup Instructions

### Prerequisites

- Python 3.9 (for local execution)
- Docker (for containerized execution)

### For Running Locally

1. **Clone the repository**

   ```
   git clone https://github.com/Pratyay008/Curieo.ai.git
   ```

2. **Change the directory**

   ```
   cd Curieo.ai
   ```

3. **Delete the output files**

   Delete the five output files. Then check with each and every command which will  generate different output files.

4. **For running the code**   



- With Sample Input given previously: 

   ```
   python3 main.py "$(cat input.txt)" > output.txt
   ```
- With Very Large input: 

   ```
   python3 main.py "$(cat input1.txt)" > output1.txt
   ```
- With Empty input: 

   ```
   python3 main.py "$(cat input2.txt)" > output2.txt
   ```
- With Wrong input: 

   ```
   python3 main.py "$(cat input3.txt)" > output3.txt
   ```
- With Only one row input: 

   ```
   python3 main.py "$(cat input4.txt)" > output4.txt
   ```



5. **Checking the output**  
   The results will be written to `output.txt`, `output1.txt`, `output2.txt`, `output3.txt`, and `output4.txt` files in the project directory. Open these files to view the results of our queries.

<br/>

### Running with Docker Container

1. **Building locally**

   ```
   docker build . -t log-monitor
   ```

2. **Running locally**

   ```
   docker run -it log-monitor "$(cat input.txt)" > output.txt
   ```

3. **Publishing docker image to dockerhub**

   ```
   docker build -t pratyay008/log_monitor .
   ```

   ```
   docker login
   ```

   ```
   docker push -a pratyay008/log_monitor
   ```

4. **You need to run**

   ```
   docker run -it pratyay008/log_monitor "$(cat input.txt)"
   ```

5. **Already pushed, if you want to pull**

   ```
   docker pull pratyay008/log_monitor:tagname
   ```
