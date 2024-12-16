from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/get_data/pid/{pid}")
async def get_data(pid: int):
    # Define the curl command as a string
    cookie = "wordpress_77b7898063b2a498589395a22b16287c=rupesh224%7C1734103254%7C3gmxmJ3LCZOYjYIpW5wwGZ6hRPkFm9qsJEXUV8E0XRN%7C0981a0990bc91aa1e5ff779c09e4e486146254376d3daf3a57c3888343f7c5e7; PHPSESSID=gfpmcnefpkhkp3t3blj14pa57u; wordpress_logged_in_77b7898063b2a498589395a22b16287c=hamrokotha1%7C1734536889%7CL0w43S91WyeTOMZ1bm6dcCt7Kp9HnV8G0zkVM3cCa2G%7C9ecded39196a15554c800ca68f72071800d5184eb093536184673eb020964e52; wfwaf-authcookie-7390d758a99f62df17e443d0b10ea9b9=12661%7Cother%7Cread%7C1709578cdbd02d8083d7126e36862047781bf437e418d6f0eda0a7d883513925"
    

    curl_command = f"""
curl 'http://www.4kotha.com/wp-admin/admin-ajax.php' \
    -H 'Accept: application/json, text/javascript, */*; q=0.01'\
    -H 'Accept-Language: en-GB,en;q=0.9,en-US;q=0.8,ja;q=0.7,ne;q=0.6'\
    -H 'Connection: keep-alive'   -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8'\
    -H 'Cookie: {cookie}'\
    -H 'DNT: 1'   -H 'Origin: http://www.4kotha.com' \
    -H 'Referer: http://www.4kotha.com/user-dashboard/'\
    -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'\
    -H 'X-Requested-With: XMLHttpRequest'\
    --data-raw 'slug=apartment&pid={pid}&action=mmtre_get_property_type_details_input_form_fe&mmtre_nonce=49802cb373'\
    --insecure | grep -oP '98\d+'
"""
    # Run the curl command using subprocess
    response = subprocess.run(curl_command, shell=True, capture_output=True, text=True)

    # Extract numbers starting with '98' followed by digits using regex
    matches = re.findall(r'98\d+', response.stdout)

    # Return the result as a JSON response
    return {"matches": matches}

