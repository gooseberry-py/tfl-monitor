from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_pin_lon_item_request_builder import WithPinLonItemRequestBuilder

class WithPinLatItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /TravelTimes/compareOverlay/{z}/mapcenter/{mapCenterLat}/{mapCenterLon}/pinlocation/{pinLat}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithPinLatItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/TravelTimes/compareOverlay/{z}/mapcenter/{mapCenterLat}/{mapCenterLon}/pinlocation/{pinLat}", path_parameters)
    
    def by_pin_lon(self,pin_lon: float) -> WithPinLonItemRequestBuilder:
        """
        Gets an item from the tfl_api.TravelTimes.compareOverlay.item.mapcenter.item.item.pinlocation.item.item collection
        param pin_lon: The longitude of the pin.
        Returns: WithPinLonItemRequestBuilder
        """
        if pin_lon is None:
            raise TypeError("pin_lon cannot be null.")
        from .item.with_pin_lon_item_request_builder import WithPinLonItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["pinLon"] = pin_lon
        return WithPinLonItemRequestBuilder(self.request_adapter, url_tpl_params)
    

