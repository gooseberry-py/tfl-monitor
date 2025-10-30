from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_line_item_request_builder import WithLineItemRequestBuilder

class CrowdingRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /StopPoint/{ids-id}/Crowding
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CrowdingRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/StopPoint/{ids%2Did}/Crowding", path_parameters)
    
    def by_line(self,line: str) -> WithLineItemRequestBuilder:
        """
        Gets an item from the tfl_api.StopPoint.item.Crowding.item collection
        param line: A particular line e.g. victoria, circle, northern etc.
        Returns: WithLineItemRequestBuilder
        """
        if line is None:
            raise TypeError("line cannot be null.")
        from .item.with_line_item_request_builder import WithLineItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["line"] = line
        return WithLineItemRequestBuilder(self.request_adapter, url_tpl_params)
    

