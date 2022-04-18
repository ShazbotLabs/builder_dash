from typing import Dict, Any


def readme_rst(content_data: Dict[Any, Any]) -> str:
    content = f"""{content_data['name']}
{'=' * len(content_data['name'])}

{content_data['description']}
"""
    return content
