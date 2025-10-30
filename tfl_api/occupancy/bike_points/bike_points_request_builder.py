from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_ids_item_request_builder import WithIdsItemRequestBuilder

class BikePointsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /Occupancy/BikePoints
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new BikePointsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/Occupancy/BikePoints", path_parameters)
    
    def by_ids(self,ids: str) -> WithIdsItemRequestBuilder:
        """
        Gets an item from the tfl_api.Occupancy.BikePoints.item collection
        param ids: Unique identifier of the item
        Returns: WithIdsItemRequestBuilder
        """
        if ids is None:
            raise TypeError("ids cannot be null.")
        from .item.with_ids_item_request_builder import WithIdsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["ids"] = ids
        return WithIdsItemRequestBuilder(self.request_adapter, url_tpl_params)
    

