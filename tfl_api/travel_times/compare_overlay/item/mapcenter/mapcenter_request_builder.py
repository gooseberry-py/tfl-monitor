from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_map_center_lat_item_request_builder import WithMapCenterLatItemRequestBuilder

class MapcenterRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /TravelTimes/compareOverlay/{z}/mapcenter
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MapcenterRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/TravelTimes/compareOverlay/{z}/mapcenter", path_parameters)
    
    def by_map_center_lat(self,map_center_lat: float) -> WithMapCenterLatItemRequestBuilder:
        """
        Gets an item from the tfl_api.TravelTimes.compareOverlay.item.mapcenter.item collection
        param map_center_lat: The map center latitude.
        Returns: WithMapCenterLatItemRequestBuilder
        """
        if map_center_lat is None:
            raise TypeError("map_center_lat cannot be null.")
        from .item.with_map_center_lat_item_request_builder import WithMapCenterLatItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["mapCenterLat"] = map_center_lat
        return WithMapCenterLatItemRequestBuilder(self.request_adapter, url_tpl_params)
    

