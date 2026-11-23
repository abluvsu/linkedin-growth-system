import asyncio
import json
import os
import re
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    print("=========================================")
    print(" LinkedIn Outbound Drafter")
    print("=========================================")
    
    server_params = StdioServerParameters(
        command="uvx",
        args=["mcp-server-linkedin@latest"]
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("[+] Connected to LinkedIn MCP Server.")
            
            print("[+] Searching for target profiles (VP Engineering)...")
            try:
                result = await session.call_tool("search_people", arguments={"keywords": "VP Engineering"})
                data = json.loads(result.content[0].text)
                
                # The MCP server returns scraped references
                references = data.get("references", {}).get("search_results", [])
                
                # Filter out mutual connections which might be returned
                people = [p for p in references if p.get("kind") == "person"]
                
                # Deduplicate by URL
                seen = set()
                unique_people = []
                for p in people:
                    if p["url"] not in seen:
                        seen.add(p["url"])
                        unique_people.append(p)
                
                print(f"[+] Found {len(unique_people)} unique profiles. Processing the first 10...")
                
                outbound_queue = []
                for person in unique_people[:10]:
                    name = person.get("text", "Unknown")
                    url = person.get("url", "")
                    
                    first_name = name.split(" ")[0] if " " in name else name
                    
                    message = f"Hi {first_name},\n\nI saw your company has been growing. I have been building production AI systems at ICICI Prudential for 4+ years, including a predictive model that cut a 7-day manual process to 15 minutes under full regulatory compliance. If your team is hiring for AI or engineering roles, I would love to connect."
                    
                    outbound_queue.append({
                        "name": name,
                        "url": url,
                        "message": message
                    })
                
                queue_path = os.path.join(os.path.dirname(__file__), "..", "outbound_queue.md")
                with open(queue_path, "w", encoding="utf-8") as f:
                    f.write("# LinkedIn Outbound Approval Queue\n\n")
                    f.write("Check the box `[x]` for the messages you want to send. Then run `send_outbound.py`.\n\n")
                    
                    for item in outbound_queue:
                        f.write(f"- [ ] **{item['name']}**\n")
                        f.write(f"      URL: `{item['url']}`\n")
                        f.write(f"      Message:\n")
                        f.write(f"      > {item['message'].replace(chr(10), chr(10) + '      > ')}\n\n")
                
                print(f"[+] Successfully drafted messages to {os.path.abspath(queue_path)}")
                
            except Exception as e:
                print("[-] Error during execution:")
                print(e)

if __name__ == "__main__":
    asyncio.run(main())
