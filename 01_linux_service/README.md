
## Scenario
You have a simple docker image that runs an API in python using Flask. You’ve put it on a Linux server and created a service unit file so it will be started on boot and re-started on failure with the appropriate mounts and environment variables. 

**Issue: When the server boots up, the service appears to just keep re-starting.**

### Question

What avenues would you take to debug this situation?

### Required Knowledge:
- systemd
- docker
- python (minimal)