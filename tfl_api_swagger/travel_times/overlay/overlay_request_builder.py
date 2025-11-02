from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_z_item_request_builder import WithZItemRequestBuilder

class OverlayRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /TravelTimes/overlay
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new OverlayRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/TravelTimes/overlay", path_parameters)
    
    def by_z(self,z: int) -> WithZItemRequestBuilder:
        """
        Gets an item from the tfl_api.TravelTimes.overlay.item collection
        param z: The zoom level.
        Returns: WithZItemRequestBuilder
        """
        if z is None:
            raise TypeError("z cannot be null.")
        from .item.with_z_item_request_builder import WithZItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["z"] = z
        return WithZItemRequestBuilder(self.request_adapter, url_tpl_params)
    

