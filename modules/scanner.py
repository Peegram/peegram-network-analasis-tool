import socket
from concurrent.futures import ThreadPoolExecutor

def verify_socket(target, port):
    try:
        # Construct raw IPv4 TCP Stream Socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.0)
        
        # Connect execution
        execution_result = sock.connect_ex((target, port))
        if execution_result == 0:
            try:
                service = socket.getservbyport(port, 'tcp')
            except Exception:
                service = "Unknown Protocol"
            print(f"  [✓] Port {port:<5} | STATUS: OPEN | SERVICE: {service}")
        sock.close()
    except Exception:
        pass

def run_scanner(target):
    print(f"[*] Dispatching multi-threaded active probe matrix against: {target}")
    print("[*] Thread pool workers initialized. Auditing structural ports 1-1024...")
    print("-" * 65)
    
    # Thread pool orchestration allocation
    with ThreadPoolExecutor(max_workers=150) as executor:
        for port in range(1, 1025):
            executor.submit(verify_socket, target, port)
            
    print("-" * 65)
    print("[*] Active probe cycle complete.")
