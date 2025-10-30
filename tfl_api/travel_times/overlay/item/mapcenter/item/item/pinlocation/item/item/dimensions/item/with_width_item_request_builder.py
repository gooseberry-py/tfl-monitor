from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_height_item_request_builder import WithHeightItemRequestBuilder

class WithWidthItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /TravelTimes/overlay/{z}/mapcenter/{mapCenterLat}/{mapCenterLon}/pinlocation/{pinLat}/{pinLon}/dimensions/{width}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithWidthItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/TravelTimes/overlay/{z}/mapcenter/{mapCenterLat}/{mapCenterLon}/pinlocation/{pinLat}/{pinLon}/dimensions/{width}", path_parameters)
    
    def by_height(self,height: int) -> WithHeightItemRequestBuilder:
        """
        Gets an item from the tfl_api.TravelTimes.overlay.item.mapcenter.item.item.pinlocation.item.item.dimensions.item.item collection
        param height: The height of the requested overlay.
        Returns: WithHeightItemRequestBuilder
        """
        if height is None:
            raise TypeError("height cannot be null.")
        from .item.with_height_item_request_builder import WithHeightItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["height"] = height
        return WithHeightItemRequestBuilder(self.request_adapter, url_tpl_params)
    

