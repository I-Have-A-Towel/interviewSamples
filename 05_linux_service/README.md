
## Scenario
You’ve built a very simple Flask app in `Python` (api.py). On a `Linux Server`, you've set up and installed a `systemd` unit file (api.service) to manage the execution of the service (starting/stopping/environment variables, etc).
When the server starts up, `systemd` is configured to automatically start the service.

**Issue: When the server boots up, systemd appears to continuously re-start the service that is running your app.**

### Question

What avenues would you take to debug this situation?

### Required Knowledge:
- systemd
- python (minimal)