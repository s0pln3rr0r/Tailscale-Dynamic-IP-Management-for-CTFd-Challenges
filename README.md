
# Tailscale Dynamic IP Management for CTFd Challenges

## Overview

This Python script, created as part of the **BFCPT Blog Series - Part 4**, automates the process of assigning dynamic IP addresses to Boot2Root machines in a **Capture The Flag (CTF)** competition hosted on **CTFd** using **Tailscale**. The script updates the Tailscale devices' IPs based on team and machine numbers, making it easier to manage the IP assignments for your CTF challenges.

## Features

- Fetches devices from the Tailscale API.
- Updates the device IP addresses based on the team and machine numbers.
- Uses **Tailscale API** to automate IP assignments for Boot2Root machines.
- Integrates with **CTFd** to create dynamic IPs like `100.130.xx.yy` for each team and machine.

## Prerequisites

Before using this script, you need to have the following:

- **Tailscale Account & API Access**: Make sure you have API access to your Tailscale network.
- **Docker**: CTFd should be set up using Docker on your server.
- **Python 3**: This script requires Python 3.x.
- **Requests Library**: Install the `requests` library for making API calls.

```bash
pip install requests
```

## Setup Instructions

1. **Clone this repository**:
   ```bash
   git clone https://github.com/s0pln3rr0r/Tailscale-Dynamic-IP-Management-for-CTFd-Challenges.git
   cd Tailscale-Dynamic-IP-Management-for-CTFd-Challenges
   ```

2. **Configure the Script**:
   - Open the `main.py` file.
   - Provide your **Tailscale API key** and **tailnet** name in the script.

3. **Run the Script**:
   - Execute the script by running:
   ```bash
   python main.py
   ```

4. **Follow the on-screen prompts** to input your **Tailscale API key** and **tailnet** name.

## How It Works

This script fetches all devices from the Tailscale network and checks for specific tags (e.g., `tag:team-1`, `tag:machine-3`). Based on these tags, it dynamically constructs the IP address in the format `100.130.xx.yy` where `xx` represents the team number and `yy` represents the machine number. It then updates the device IP in Tailscale using the API.

## CTFd Integration

Once the devices have their IPs updated, you can use these IPs in your CTFd challenges. For example:

```
To connect to the machine, replace `xx` with your team number in the IP `100.130.xx.03`. For example: Machine IP for `team-2` would be `100.130.02.03`.
```

## Troubleshooting

- **Tailscale API Access**: If you encounter any authentication issues, double-check your Tailscale API key and ensure it has the necessary permissions.
- **Device Tagging**: Ensure that your devices have the correct tags (`tag:team-<team_number>` and `tag:machine-<machine_number>`).
- **Permission Issues**: Ensure you have appropriate permissions to modify device IPs in your Tailscale network.

## Contributing

Feel free to fork this repository and submit pull requests for improvements, bug fixes, or feature requests. If you encounter issues or have any suggestions, please open an issue.

## Contact

For any questions, feel free to contact me via [s0pln3rr0r@proton.me](mailto:s0pln3rr0r@proton.me).
