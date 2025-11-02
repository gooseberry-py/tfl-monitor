from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_lon_item_request_builder import WithLonItemRequestBuilder

class WithLatItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /Place/{-id}/At/{Lat}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithLatItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/Place/{%2Did}/At/{Lat}", path_parameters)
    
    def by_lon(self,lon: str) -> WithLonItemRequestBuilder:
        """
        Gets an item from the tfl_api.Place.item.At.item.item collection
        param lon: Unique identifier of the item
        Returns: WithLonItemRequestBuilder
        """
        if lon is None:
            raise TypeError("lon cannot be null.")
        from .item.with_lon_item_request_builder import WithLonItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["Lon"] = lon
        return WithLonItemRequestBuilder(self.request_adapter, url_tpl_params)
    

