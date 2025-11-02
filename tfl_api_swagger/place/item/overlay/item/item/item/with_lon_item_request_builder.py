from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_width_item_request_builder import WithWidthItemRequestBuilder

class WithLonItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /Place/{-id}/overlay/{z}/{Lat}/{Lon}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithLonItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/Place/{%2Did}/overlay/{z}/{Lat}/{Lon}", path_parameters)
    
    def by_width(self,width: int) -> WithWidthItemRequestBuilder:
        """
        Gets an item from the tfl_api.Place.item.overlay.item.item.item.item collection
        param width: The width of the requested overlay.
        Returns: WithWidthItemRequestBuilder
        """
        if width is None:
            raise TypeError("width cannot be null.")
        from .item.with_width_item_request_builder import WithWidthItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["width"] = width
        return WithWidthItemRequestBuilder(self.request_adapter, url_tpl_params)
    

