# sos
stack overflow security scanning

## approach
Research Approach
We will be focusing on discovering patterns with vulnerabilities found in StackOverflow. As not
only an open-source forum and aid for almost every developer worldwide, we wish to investigate
the integrity and security strength of community feedback. We suspect there may be higher
probabilities of vulnerable code within certain topics, such as with coding languages like PHP or
C++. Though there are many classifications of a security vulnerability, we will focus on using
static analysis in code snippets.
Through a brief inspection of our available datasets (Google BigQuery), our first stage will be to
determine the assigned tags based on the question asked. As the dataset is missing
labels/tags, we will be using StackOverflow’s application and API to retrieve the tags. This will
help us categorize the answers to discover patterns if certain topics are more prone to
vulnerabilities.
We will be setting up a database and running custom scripts to make requests to
StackOverflow’s servers. We currently estimate that given 19 million unique questions and a
rate of 30 requests per second, the labeling process would take about 7.3 days. Most likely we
will also implement some distributed systems (or cloud service) to help speed up that process.
The second stage will be to scan the answers using semgrep, a static application security
testing (SAST) tool. Even though a StackOverflow answer may consist of a description with a
small code snippet, we hypothesize that developers may not understand the full concept of an
answer and will likely copy-paste the snippet into their code. semgrep also comes with its own
registry, providing parameters to detect security vulnerabilities.
Given that semgrep is written in OCaml, we estimate the scanning process will not take as much
time compared to stage one. The main question we will determine is how to set up the scanning
as well as categorize possible severities of detections. False positives may also be an issue as
well.
