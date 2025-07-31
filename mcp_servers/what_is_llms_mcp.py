from mcpdoc.main import create_server

doc_sources = [
    {"name": "WhatIsLLMs", "llms_txt": "https://llmstxt.org/llms.txt"}
]

server = create_server(doc_sources)
server.run(transport="stdio", port=5003)