def print_results(results):
    for host in results:
        print(f"\n[+] {host['ip']}")
        for port in host['open_ports']:
            print(f"   - {port}/tcp")
