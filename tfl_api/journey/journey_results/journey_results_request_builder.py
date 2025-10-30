from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_from_item_request_builder import WithFromItemRequestBuilder

class JourneyResultsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /Journey/JourneyResults
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new JourneyResultsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/Journey/JourneyResults", path_parameters)
    
    def by_from(self,from: str) -> WithFromItemRequestBuilder:
        """
        Gets an item from the tfl_api.Journey.JourneyResults.item collection
        param from: Origin of the journey. Can be WGS84 coordinates expressed as "lat,long", a UK postcode, a Naptan (StopPoint) id, an ICS StopId, or a free-text string (will cause disambiguation unless it exactly matches a point of interest name).
        Returns: WithFromItemRequestBuilder
        """
        if from is None:
            raise TypeError("from cannot be null.")
        from .item.with_from_item_request_builder import WithFromItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["from"] = from
        return WithFromItemRequestBuilder(self.request_adapter, url_tpl_params)
    

