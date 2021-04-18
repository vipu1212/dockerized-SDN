import simple_swtch
import requests as http

if __name__ == "__main__":
    res = http.get('https://04iz2wo404.execute-api.ap-south-1.amazonaws.com/demo/')
    controller_ip = res.json().get('ip')
    print(f'Controller IP: {controller_ip}')
    simple_swtch.start(controller_ip)
    