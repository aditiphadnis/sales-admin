from typing import Optional, Type
from pydantic import BaseModel, Field
from langchain_community.tools.playwright.base import BaseBrowserTool
from langchain_community.tools.playwright.utils import (
    aget_current_page,
    get_current_page,
)

class FillToolInput(BaseModel):
    """Input to a fill tool"""
    selector: str = Field(..., description="CSS selector to fill")
    value: str = Field(..., description="Text to enter")

class FillTool(BaseBrowserTool):
    name = "fill_element"
    description = "Fill a text input identified by CSS selector."

    args_schema: Type[BaseModel] = FillToolInput

    def _run(self, selector: str, value: str, **kwargs) -> str:
        page = get_current_page(self.sync_browser)
        page.fill(selector, value)
        return f"Filled {selector}"

    async def _arun(self, selector: str, value: str, **kwargs) -> str:
        page = await aget_current_page(self.async_browser)
        await page.fill(selector, value)
        return f"Filled {selector}"
