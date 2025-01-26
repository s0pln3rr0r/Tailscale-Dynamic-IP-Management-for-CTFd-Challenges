import requests
import re
import time

def get_devices(api_key, tailnet):
    url = f"https://api.tailscale.com/api/v2/tailnet/{tailnet}/devices"
    print(f"Fetching devices from: {url}")
    response = requests.get(url, auth=(api_key, ''))
    if response.status_code == 200:
        print("Devices successfully retrieved!")
        return response.json().get('devices', [])
    else:
        print(f"Error fetching devices. Status code: {response.status_code}")
        print(f"Response: {response.text}")
        return []

def update_device_ip(api_key, device_id, new_ip):
    url = f"https://api.tailscale.com/api/v2/device/{device_id}/ip"
    payload = {"ipv4": new_ip}
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    print(f"Updating device {device_id} to new IP: {new_ip}")
    
    retries = 3
    for attempt in range(retries):
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            print(f"Successfully updated device {device_id} to IP {new_ip}")
            return
        elif response.status_code == 500:
            print(f"Server error (500) on attempt {attempt+1}, retrying...")
            time.sleep(2)  
        else:
            print(f"Error updating device {device_id}. Status code: {response.status_code}")
            print(f"Response: {response.text}")
            return

def format_ip(team_number, machine_number):
    return f"100.110.{team_number}.{machine_number}"

def main():
    api_key = input("Enter your Tailscale API key: ").strip()
    tailnet = input("Enter your Tailscale organization name: ").strip()

    print("Fetching devices...")
    devices = get_devices(api_key, tailnet)

    for device in devices:
        tags = device.get('tags', [])
        print(f"Processing device {device.get('id', 'unknown')} with tags: {tags}")
        if len(tags) == 2:
            team_match = next((tag for tag in tags if re.match(r'tag:team-\d+', tag)), None)
            machine_match = next((tag for tag in tags if re.match(r'tag:machine-\d+', tag)), None)

            if team_match and machine_match:
                team_number = int(re.search(r'\d+', team_match).group())
                machine_number = int(re.search(r'\d+', machine_match).group())
                
                new_ip = format_ip(team_number, machine_number)
                device_id = device.get('id')

                if device_id:
                    update_device_ip(api_key, device_id, new_ip)
            else:
                print(f"Skipping device {device.get('id', 'unknown')}: Tags do not match.")
        else:
            print(f"Skipping device {device.get('id', 'unknown')}: Does not have exactly 2 tags.")

if __name__ == "__main__":
    main()
