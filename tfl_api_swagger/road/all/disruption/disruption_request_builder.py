from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_disruption_ids_item_request_builder import WithDisruptionIdsItemRequestBuilder

class DisruptionRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /Road/all/Disruption
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DisruptionRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/Road/all/Disruption", path_parameters)
    
    def by_disruption_ids(self,disruption_ids: str) -> WithDisruptionIdsItemRequestBuilder:
        """
        Gets an item from the tfl_api.Road.all.Disruption.item collection
        param disruption_ids: Comma-separated list of disruption identifiers to filter by.
        Returns: WithDisruptionIdsItemRequestBuilder
        """
        if disruption_ids is None:
            raise TypeError("disruption_ids cannot be null.")
        from .item.with_disruption_ids_item_request_builder import WithDisruptionIdsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["disruptionIds"] = disruption_ids
        return WithDisruptionIdsItemRequestBuilder(self.request_adapter, url_tpl_params)
    

