from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_query_item_request_builder import WithQueryItemRequestBuilder

class SearchRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /Search
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SearchRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/Search", path_parameters)
    
    def by_query(self,query: str) -> WithQueryItemRequestBuilder:
        """
        Gets an item from the tfl_api_line.Search.item collection
        param query: Search term e.g victoria
        Returns: WithQueryItemRequestBuilder
        """
        if query is None:
            raise TypeError("query cannot be null.")
        from .item.with_query_item_request_builder import WithQueryItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["query"] = query
        return WithQueryItemRequestBuilder(self.request_adapter, url_tpl_params)
    

