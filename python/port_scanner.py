
import argparse
import platform
import subprocess
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

LINUX_SCRIPT = BASE_DIR / "linux" / "check_port.sh"
WINDOWS_SCRIPT = BASE_DIR / "windows" / "check_port.ps1"


def check_port(port, host, system):

    if system == "Windows":

        powershell = shutil.which("powershell") or shutil.which("pwsh")

        if not powershell:
            print("ERROR: PowerShell not found")
            return None

        command = [
            powershell,
            "-NoProfile",
            "-ExecutionPolicy", "Bypass",
            "-File", str(WINDOWS_SCRIPT),
            "-Port", str(port),
            "-HostName", host
        ]

    else:

        command = [
            "bash",
            str(LINUX_SCRIPT),
            str(port),
            host
        ]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=6
        )

        print(result.stdout.strip())

        if result.returncode == 0:
            return True

        elif result.returncode == 1:
            return False

        else:
            print(result.stderr.strip())
            return None

    except subprocess.TimeoutExpired:
        print(f"ERROR: Timeout on port {port}")
        return None

    except Exception as error:
        print(f"ERROR: {error}")
        return None


def main():

    parser = argparse.ArgumentParser(
        description="TCP Port Scanner"
    )

    parser.add_argument(
        "ports",
        nargs="+",
        type=int,
        help="Ports to check"
    )

    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="Target host"
    )

    args = parser.parse_args()

    system = platform.system()

    print(f"\nOperating system: {system}")
    print(f"Target host: {args.host}")
    print("-" * 40)

    if system not in ["Windows", "Linux"]:
        print("Unsupported operating system")
        return

    opened = 0
    closed = 0
    errors = 0

    for port in args.ports:

        if port < 1 or port > 65535:
            print(f"ERROR: Invalid port {port}")
            errors += 1
            continue

        result = check_port(port, args.host, system)

        if result is True:
            opened += 1
        elif result is False:
            closed += 1
        else:
            errors += 1

    print("-" * 40)
    print("SUMMARY")
    print(f"Open ports: {opened}")
    print(f"Closed ports: {closed}")
    print(f"Errors: {errors}")


if __name__ == "__main__":
    main()
