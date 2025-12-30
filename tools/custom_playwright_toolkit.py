from typing import TYPE_CHECKING, List, Optional, Type
from langchain_core.tools import BaseTool
from langchain_community.agent_toolkits.base import BaseToolkit
from langchain_community.tools.playwright.base import BaseBrowserTool, lazy_import_playwright_browsers

if TYPE_CHECKING:
    from playwright.async_api import Browser as AsyncBrowser
    from playwright.sync_api import Browser as SyncBrowser

from langchain_community.tools.playwright.click import ClickTool
from langchain_community.tools.playwright.current_page import CurrentWebPageTool
from langchain_community.tools.playwright.extract_text import ExtractTextTool
from langchain_community.tools.playwright.get_elements import GetElementsTool
from langchain_community.tools.playwright.navigate import NavigateTool
from langchain_community.tools.playwright.navigate_back import NavigateBackTool
from langchain_community.tools.playwright.extract_hyperlinks import ExtractHyperlinksTool

from fill import FillTool

class PlayWrightBrowserToolkit(BaseToolkit):
    sync_browser: Optional["SyncBrowser"] = None
    async_browser: Optional["AsyncBrowser"] = None

    def get_tools(self) -> List[BaseTool]:
        tool_classes: List[Type[BaseBrowserTool]] = [
            NavigateTool,
            NavigateBackTool,
            ClickTool,
            ExtractTextTool,
            ExtractHyperlinksTool,
            GetElementsTool,
            CurrentWebPageTool,
            FillTool,
        ]

        return [
            cls.from_browser(sync_browser=self.sync_browser, async_browser=self.async_browser)
            for cls in tool_classes
        ]

    @classmethod
    def from_browser(cls, sync_browser=None, async_browser=None):
        lazy_import_playwright_browsers()
        return cls(sync_browser=sync_browser, async_browser=async_browser)
