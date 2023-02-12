import sys
import json

if len(sys.argv) == 1:
    print("Please provide the file to change")
    sys.exit(1)

package_file = sys.argv[1]

with open(package_file, 'r') as file:
    package_json = json.load(file)
    
package_json['scripts']['newpage'] = "cd scripts && python3 create_page.py"

with open(package_file, 'w') as file:
    json.dump(package_json, file, indent=4)

    