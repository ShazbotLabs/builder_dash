def readme_rst(content_data: dict) -> str:
    content = f"""{content_data['name']}
{'=' * len(content_data['name'])}

{content_data['description']}
"""
    return content
