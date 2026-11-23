import asyncio
import os
import re
import csv
from datetime import datetime
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    print("=========================================")
    print(" LinkedIn Outbound Sender")
    print("=========================================")
    
    queue_path = os.path.join(os.path.dirname(__file__), "..", "outbound_queue.md")
    if not os.path.exists(queue_path):
        print(f"[-] Could not find {queue_path}. Please run draft_outbound.py first.")
        return
        
    with open(queue_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    pattern = r"- \[x\] \*\*(.*?)\*\*\n\s+URL: `(.*?)`\n\s+Message:\n((?:\s+> .*?\n)+)"
    matches = re.finditer(pattern, content)
    
    to_send = []
    for m in matches:
        name = m.group(1).strip()
        url = m.group(2).strip()
        raw_message = m.group(3)
        
        message = re.sub(r"^\s+> ", "", raw_message, flags=re.MULTILINE).strip()
        to_send.append({"name": name, "url": url, "message": message})
        
    if not to_send:
        print("[+] No approved connections found in outbound_queue.md (check for [x]).")
        return
        
    print(f"[+] Found {len(to_send)} approved connections. Connecting to MCP Server...")
    
    server_params = StdioServerParameters(
        command="uvx",
        args=["mcp-server-linkedin@latest"]
    )
    
    log_path = os.path.join(os.path.dirname(__file__), "..", "sent_log.csv")
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("[+] Connected.")
            
            for person in to_send:
                print(f"[*] Sending connection request to {person['name']}...")
                try:
                    username = person['url'].strip('/').split('/')[-1]
                    result = await session.call_tool("connect_with_person", arguments={
                        "linkedin_username": username,
                        "note": person['message']
                    })
                    
                    if getattr(result, "isError", False):
                        print(f"    [FAIL] MCP Server error: {result.content}")
                        continue
                        
                    print(f"    [OK] Sent.")
                    
                    # Log the successful send
                    file_exists = os.path.isfile(log_path)
                    with open(log_path, mode='a', newline='', encoding='utf-8') as csvfile:
                        writer = csv.writer(csvfile)
                        if not file_exists:
                            writer.writerow(["Timestamp", "Name", "URL", "Message"])
                        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), person['name'], person['url'], person['message']])
                        
                except Exception as e:
                    print(f"    [FAIL] Could not send to {person['name']}: {e}")
                    
    print(f"\n[+] Finished. Sent connections are logged in {os.path.abspath(log_path)}")
    print("Please remember to mark them as [SENT] in the markdown file if you wish to keep it as a backup.")

if __name__ == "__main__":
    asyncio.run(main())
