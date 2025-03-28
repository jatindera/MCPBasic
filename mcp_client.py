from mcp import ClientSession
from mcp.client.sse import sse_client


async def run():
    async with sse_client(url="http://localhost:8000/sse") as streams:
        async with ClientSession(*streams) as session:
            await session.initialize()

            # List available tools
            tools = await session.list_tools()
            # print(tools)
            resources_static = await session.list_resources()
            print("*" * 50)
            print("List of Static Resources:")
            print(resources_static)
            print("*" * 50)
            resources_dynamic = await session.list_resource_templates()
            print("List of Dynamic Resources:")
            print(resources_dynamic)
            print("*" * 50)
            prompts_list = await session.list_prompts()
            print("List of prompts:")
            print(prompts_list)
            print("*" * 50)

            # Call a tool
            result = await session.call_tool("add", arguments={"a": 45, "b": 25})
            # print(result)
            print(result.content[0].text)

            result = await session.read_resource("resource://static_data")
            staticText = result.contents[0].text
            print(staticText)

            name = "Jatinder"
            result = await session.read_resource(f"greeting://{name}")
            greeting = result.contents[0].text
            print(greeting)

            result = await session.get_prompt(
                "review_code", arguments={"code": 'print("Hello World")'}
            )
            print("Prompt", result)


            result = await session.get_prompt(
                "debug_error", arguments={"error": 'NumberFormatException: 1 is a string'}
            )
            print("Prompt", result)


if __name__ == "__main__":
    import asyncio

    asyncio.run(run())
