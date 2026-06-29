import subprocess
import time

# Service name to monitor (example: 'nginx')
SERVICE_NAME = "nginx"

def is_service_running(service):
    try:
        # Check service status
        result = subprocess.run(
            ["systemctl", "is-active", service],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return result.stdout.strip() == "active"
    except Exception as e:
        print(f"❌ Error checking service: {e}")
        return False

def restart_service(service):
    try:
        subprocess.run(["sudo", "systemctl", "restart", service], check=True)
        print(f"🔄 Service '{service}' restarted successfully.")
    except Exception as e:
        print(f"❌ Error restarting service: {e}")

if __name__ == "__main__":
    print(f"Monitoring service: {SERVICE_NAME}")
    if not is_service_running(SERVICE_NAME):
        print(f"🚨 ALERT: Service '{SERVICE_NAME}' is down!")
        restart_service(SERVICE_NAME)
    else:
        print(f"✅ Service '{SERVICE_NAME}' is running normally.")
