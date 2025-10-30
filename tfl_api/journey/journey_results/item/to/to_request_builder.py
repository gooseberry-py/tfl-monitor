from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_to_item_request_builder import WithToItemRequestBuilder

class ToRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /Journey/JourneyResults/{from}/to
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ToRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/Journey/JourneyResults/{from}/to", path_parameters)
    
    def by_to(self,to: str) -> WithToItemRequestBuilder:
        """
        Gets an item from the tfl_api.Journey.JourneyResults.item.to.item collection
        param to: Destination of the journey. Can be WGS84 coordinates expressed as "lat,long", a UK postcode, a Naptan (StopPoint) id, an ICS StopId, or a free-text string (will cause disambiguation unless it exactly matches a point of interest name).
        Returns: WithToItemRequestBuilder
        """
        if to is None:
            raise TypeError("to cannot be null.")
        from .item.with_to_item_request_builder import WithToItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["to"] = to
        return WithToItemRequestBuilder(self.request_adapter, url_tpl_params)
    

