
## Scenario
You’ve built a simple docker image that runs an API in python using Flask. You’ve put it on a Linux server and created a service unit file so it will be started on boot and re-started on failure with the appropriate mounts and environment variables. Issue: when the server boots up, the service appears to just keep re-starting. 

### Question

What avenues would you take to debug this situation?

### Required Knowledge:
- systemd
- docker
- python (minimal)

### Potential answers:
- Check status systemctl
- Check logs using journalctl
- Stop the service using systemctl
- Make sure API runs properly locally
- Try starting the docker container manually to see if anything goes wrong
- Check unit file to see if the settings are correct:
  - environment variables or file(s)
  - mounted volumes
  - Unit settings (Before/After)
