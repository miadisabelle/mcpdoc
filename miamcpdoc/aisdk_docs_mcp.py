from mcpdoc.main import create_server

doc_sources = [
    {"name": "VercelAISDK", "llms_txt": "https://ai-sdk.dev/llms.txt"}
]

server = create_server(doc_sources)
server.run(transport="stdio")