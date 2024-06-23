# Error Log Monitoring

## Description

This project is a Python-based solution for monitoring error logs and computing the mean severity of logs based on their types and timestamps.

## Setup Instructions

### Prerequisites

- Docker
- Python 3.9+

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

   Delete the four output files to check whether the code is generating four new output files.

4. **For running the code**

   ```
    python3 main.py "$(cat input1.txt)" > output1.txt

    python3 main.py "$(cat input2.txt)" > output2.txt

    python3 main.py "$(cat input3.txt)" > output3.txt

    python3 main.py "$(cat input4.txt)" > output4.txt
   ```

5. **Checking the output**  
   The results will be written to `output1.txt`, `output2.txt`, `output3.txt`, and `output4.txt` files in the project directory. Open these files to view the results of our queries.

## Docker Container

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
