from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_direction_item_request_builder import WithDirectionItemRequestBuilder

class SequenceRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /Line/{ids-id}/Route/Sequence
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new SequenceRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/Line/{ids%2Did}/Route/Sequence", path_parameters)
    
    def by_direction(self,direction: str) -> WithDirectionItemRequestBuilder:
        """
        Gets an item from the tfl_api.Line.item.Route.Sequence.item collection
        param direction: The direction of travel. Can be inbound or outbound.
        Returns: WithDirectionItemRequestBuilder
        """
        if direction is None:
            raise TypeError("direction cannot be null.")
        from .item.with_direction_item_request_builder import WithDirectionItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["direction"] = direction
        return WithDirectionItemRequestBuilder(self.request_adapter, url_tpl_params)
    

