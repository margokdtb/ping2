import ping3
import concurrent.futures
from tqdm import tqdm

print("\n\n  ")

def ping_host(host):
    try:
        response_time = ping3.ping(host, timeout=2)  # Set timeout to 2 seconds
        if response_time is None:
            response_time = 999  # Use a high value to represent unreachable hosts
    except Exception as e:
        response_time = 999  # Use a high value to represent hosts with ping error
    return (host, response_time)

def main():
    with open("hasil5_sni.txt", "r") as file:
        host_list = file.read().splitlines()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = []
        for host in host_list:
            results.append(executor.submit(ping_host, host))

        with tqdm(total=len(results), desc="Pinging hosts") as pbar:
            sorted_results = []
            for future in concurrent.futures.as_completed(results):
                sorted_results.append(future.result())
                pbar.update(1)

        sorted_results = sorted(sorted_results, key=lambda x: x[1])

        with open("hasil5_sni_ping.txt", "w") as output_file:
            for result in sorted_results:
                host, response_time = result
                output_file.write(f"{host} : {response_time:.2f} s\n")
                print(f"{host} -  Time: {response_time:.2f} s")

if __name__ == "__main__":
    main()
   
print("\n\nHasil telah disimpan di file hasil5_sni_ping.txt \n")