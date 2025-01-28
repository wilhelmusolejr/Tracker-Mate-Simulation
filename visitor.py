import requests
import json
from datetime import datetime
import platform
import sys
import os

from machine import get_machine_id


def get_visitor_info():
    # Get location data
    response = requests.get("https://ipinfo.io?token=e8c7c222ea978f")
    location_data = response.json()
    
    # Get device info
    device_info = {
        "browser": sys.version,  # Python version instead of browser user-agent
        "platform": platform.system(),
        "screen_width": os.get_terminal_size().columns if sys.stdout.isatty() else "Unknown",
        "screen_height": os.get_terminal_size().lines if sys.stdout.isatty() else "Unknown",
    }
    
    # Visitor info
    visitor_info = {
        **device_info,
        "country": location_data.get("country", "Unknown"),
        "city": location_data.get("city", "Unknown"),
        "region": location_data.get("region", "Unknown"),
        "ip": location_data.get("ip", "Unknown"),
    }
    
    return format_visitor_info(visitor_info)

def format_visitor_info(info):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    formatted_info = f"""
{date}
--------------------------
💻  Platform : {info['platform']}
------
🌍  Country : {info['country']}
🏙️   City : {info['city']}
🌏  Region : {info['region']}
📍  IP Address : {info['ip']}
---------------------------
"""
    return formatted_info

if __name__ == "__main__":
    print(get_visitor_info())

