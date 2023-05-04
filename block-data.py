import sys
from bitcoinrpc.authproxy import AuthServiceProxy

def get_block_data(block_hash, rpc_connection):
    block = rpc_connection.getblock(block_hash)

    data = {
        "Height": block["height"],
        "Version": block["version"],
        "Size": block["size"],
        "Confirmations": block["confirmations"],
        "Time": block["time"]
    }

    return data, block["previousblockhash"]

def print_block_data(data):
    print(f"{data['Height']:<7} {data['Version']:<10} {data['Size']:<7} {data['Confirmations']:<15} {data['Time']:<10}")




def print_column_headers():
    print("Height  Version    Size    Confirmations   Time")
    print("------  ---------- -----   --------------  ---------")



def main():
    if len(sys.argv) < 2:
        print("Usage: python get_previous_blocks.py <block_hash>")
        return

    block_hash = sys.argv[1]
    block_hash = sys.argv[1]
    # Example for Deutsche eMark
    rpc_user = "eMark.rpc"
    rpc_password = "ThouShaltNotRevealThinePassword"
    rpc_host = "127.0.0.1"
    rpc_port = "4444"

    rpc_connection = AuthServiceProxy(f"http://{rpc_user}:{rpc_password}@{rpc_host}:{rpc_port}")

        
    try:
        i = 0
        while True:
            if i % 25 == 0:
                print_column_headers()
    
            block_data, previous_block_hash = get_block_data(block_hash, rpc_connection)
            print_block_data(block_data)
            block_hash = previous_block_hash
    
            i += 1
    
            if i % 25 == 0:
                user_input = input("Enter to continue next previous 25 or 'q' to quit: ")
                if user_input.lower() == 'q':
                    break
    except KeyboardInterrupt:
        print("\nProgram interrupted by Ctrl-C")

if __name__ == "__main__":
    main()

