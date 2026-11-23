import asyncio
import os
import re
import csv
from datetime import datetime
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    print("=========================================")
    print(" LinkedIn Follow-up Sender")
    print("=========================================")
    
    queue_path = os.path.join(os.path.dirname(__file__), "..", "followup_queue.md")
    if not os.path.exists(queue_path):
        print(f"[-] Could not find {queue_path}. Please run draft_followup.py first.")
        return
        
    with open(queue_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    pattern = r"- \[x\] \*\*(.*?)\*\*\s*\(Sent \d+ days ago\)\n\s+URL: `(.*?)`\n\s+Username: `(.*?)`\n\s+Inbox Context: .*?\n\s+Message:\n((?:\s+> .*?\n?)+)"
    matches = re.finditer(pattern, content)
    
    to_send = []
    for m in matches:
        name = m.group(1).strip()
        url = m.group(2).strip()
        username = m.group(3).strip()
        raw_message = m.group(4)
        
        message = re.sub(r"^\s+> ", "", raw_message, flags=re.MULTILINE).strip()
        to_send.append({"name": name, "url": url, "username": username, "message": message})
        
    if not to_send:
        print("[+] No approved follow-ups found in followup_queue.md (check for [x]).")
        return
        
    print(f"[+] Found {len(to_send)} approved follow-ups. Connecting to MCP Server...")
    
    server_params = StdioServerParameters(
        command="uvx",
        args=["mcp-server-linkedin@latest"]
    )
    
    log_path = os.path.join(os.path.dirname(__file__), "..", "followup_log.csv")
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("[+] Connected.")
            
            for person in to_send:
                print(f"[*] Sending follow-up to {person['name']}...")
                try:
                    # Note: We use send_message, not connect_with_person, because they are already a connection!
                    await session.call_tool("send_message", arguments={
                        "linkedin_username": person['username'],
                        "message": person['message'],
                        "confirm_send": True
                    })
                    print(f"    [OK] Sent.")
                    
                    # Log the successful follow-up
                    file_exists = os.path.isfile(log_path)
                    with open(log_path, mode='a', newline='', encoding='utf-8') as csvfile:
                        writer = csv.writer(csvfile)
                        if not file_exists:
                            writer.writerow(["Timestamp", "Name", "Username", "Message"])
                        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), person['name'], person['username'], person['message']])
                        
                except Exception as e:
                    print(f"    [FAIL] Could not send follow-up to {person['name']}: {e}")
                    
    print(f"\n[+] Finished. Sent follow-ups are logged in {os.path.abspath(log_path)}")

if __name__ == "__main__":
    asyncio.run(main())
