from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_page_item_request_builder import WithPageItemRequestBuilder

class PageRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /StopPoint/Type/{types}/page
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PageRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/StopPoint/Type/{types}/page", path_parameters)
    
    def by_page(self,page: int) -> WithPageItemRequestBuilder:
        """
        Gets an item from the tfl_api.StopPoint.Type.item.page.item collection
        param page: Unique identifier of the item
        Returns: WithPageItemRequestBuilder
        """
        if page is None:
            raise TypeError("page cannot be null.")
        from .item.with_page_item_request_builder import WithPageItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["page"] = page
        return WithPageItemRequestBuilder(self.request_adapter, url_tpl_params)
    

