import asyncio
import os
import csv
from datetime import datetime
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    print("=========================================")
    print(" LinkedIn Follow-up Drafter")
    print("=========================================")
    
    log_path = os.path.join(os.path.dirname(__file__), "..", "sent_log.csv")
    if not os.path.exists(log_path):
        print(f"[-] No sent_log.csv found. You need to send initial messages first.")
        return
        
    candidates = []
    # Read the log and find candidates
    with open(log_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                sent_date = datetime.strptime(row["Timestamp"], "%Y-%m-%d %H:%M:%S")
                days_ago = (datetime.now() - sent_date).days
                if days_ago >= 3:
                    # We have a candidate!
                    url = row["URL"]
                    username = url.strip('/').split('/')[-1]
                    name = row["Name"]
                    candidates.append({
                        "name": name,
                        "username": username,
                        "url": url,
                        "days_ago": days_ago
                    })
            except Exception as e:
                pass
                
    if not candidates:
        print("[+] No connections found that were sent 3+ days ago.")
        return
        
    print(f"[+] Found {len(candidates)} candidates for follow-up. Checking their inbox status...")
    
    server_params = StdioServerParameters(
        command="uvx",
        args=["mcp-server-linkedin@latest"]
    )
    
    outbound_queue = []
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("[+] Connected to MCP Server.")
            
            for c in candidates:
                print(f"[*] Checking conversation with {c['name']} ({c['username']})...")
                try:
                    # Check conversation
                    result = await session.call_tool("get_conversation", arguments={"linkedin_username": c['username']})
                    # If this succeeds, it means they accepted and a conversation exists!
                    convo_data = result.content[0].text
                    
                    # We don't parse it deeply, just provide the context to the user.
                    first_name = c['name'].split(" ")[0] if " " in c['name'] else c['name']
                    message = f"Hi {first_name} - bumping this to the top of your inbox. Are you open to a quick chat about engineering/AI roles at your team?"
                    
                    outbound_queue.append({
                        "name": c['name'],
                        "username": c['username'],
                        "url": c['url'],
                        "days_ago": c['days_ago'],
                        "message": message,
                        "context": convo_data[:500] + ("..." if len(convo_data) > 500 else "")
                    })
                    print(f"    [OK] Conversation found. Added to follow-up queue.")
                    
                except Exception as e:
                    # Probably no conversation means they haven't accepted yet
                    print(f"    [SKIP] Could not find conversation (likely pending or error): {e}")
                    
    if not outbound_queue:
        print("[+] None of the candidates have accepted the connection yet (or conversations not found).")
        return
        
    queue_path = os.path.join(os.path.dirname(__file__), "..", "followup_queue.md")
    with open(queue_path, "w", encoding="utf-8") as f:
        f.write("# LinkedIn Follow-up Approval Queue\n\n")
        f.write("Check the box `[x]` for the follow-ups you want to send. Then run `send_followup.py`.\n")
        f.write("Review the [Inbox Context] to ensure they haven't already replied to you!\n\n")
        
        for item in outbound_queue:
            f.write(f"- [ ] **{item['name']}** (Sent {item['days_ago']} days ago)\n")
            f.write(f"      URL: `{item['url']}`\n")
            f.write(f"      Username: `{item['username']}`\n")
            f.write(f"      Inbox Context: {repr(item['context'])}\n")
            f.write(f"      Message:\n")
            f.write(f"      > {item['message']}\n\n")
            
    print(f"\n[+] Drafted {len(outbound_queue)} follow-ups to {os.path.abspath(queue_path)}")

if __name__ == "__main__":
    asyncio.run(main())
