import subprocess
import os

adb_path = '/Users/eminaslantepe/Library/Android/sdk/platform-tools/adb'  # on terminal run 'which adb' to get the path

def get_apk_paths(package_name):
    try:
        result = subprocess.run([adb_path, 'shell', 'pm', 'path', package_name], capture_output=True, text=True)
        apk_paths = []
        for line in result.stdout.splitlines():
            if 'package:' in line:
                apk_path = line.replace('package:', '').strip()
                apk_paths.append(apk_path)
        return apk_paths
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

def pull_apks(package_name, destination_folder):
    apk_paths = get_apk_paths(package_name)

    if apk_paths:
        print(f"APK paths found: {apk_paths}")
        try:
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            destination_folder = os.path.join(desktop_path, package_name)
            os.makedirs(destination_folder, exist_ok=True)  # Klasör yoksa oluştur

            for apk_path in apk_paths:
                apk_name = apk_path.split('/')[-1]
                pull_command = [adb_path, 'pull', apk_path, f"{destination_folder}/{apk_name}"]
                subprocess.run(pull_command, check=True)
                print(f"APK successfully pulled: {apk_name}")

            print(f"All APKs successfully pulled to {destination_folder}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to pull APKs: {e}")
    else:
        print("APK paths not found.")

if __name__ == "__main__":
    package_name = input("Enter the package name: ")
    pull_apks(package_name, "~/Desktop")

#