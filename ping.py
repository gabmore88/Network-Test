import subprocess

def ping_host(ip):
    """
    Checks if a host is online using a single ICMP ping.

    Parameters:
        ip (str): IP address of the device to ping.

    Returns:
        str: 'Online' if the host responds, 'Offline' otherwise.
    """

    # Execute a single ping to the target IP
    result = subprocess.run(
        ["ping", "-n", "1", ip],
        capture_output=True,
        text=True
    )

    # Determine status based on TTL in response
    if "TTL=" in result.stdout:
        return "Online"
    else:
        return "Offline"
