import simple_swtch
import requests as http

if __name__ == "__main__":
    
    # Fetch Controller IP address
    res = http.get('https://04iz2wo404.execute-api.ap-south-1.amazonaws.com/demo/')
    controller_ips = res.json().get('ips')

    print(f'Controllers Available: {controller_ips}')

    controller_ip = controller_ips[-1]

    print(f'Using: {controller_ip}')
    
    # Starting mininet
    simple_swtch.start(controller_ip)
    