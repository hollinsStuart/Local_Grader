import subprocess

result = subprocess.run(["ls", "-l"], capture_output=True)

print(result.stdout)
