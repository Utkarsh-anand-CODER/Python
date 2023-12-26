import subprocess

# Name of the requirements file
requirements_file = 'requirements.txt'

# Get the list of installed packages
installed_packages = subprocess.check_output(['pip', 'freeze']).decode('utf-8').split('\n')

# Writing installed packages to the requirements file
with open(requirements_file, 'w') as file:
    for package in installed_packages:
        if package:
            file.write(f'{package}\n')

print(f'Requirements written to {requirements_file}')
