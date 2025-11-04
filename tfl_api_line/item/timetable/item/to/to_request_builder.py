from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_to_stop_point_item_request_builder import WithToStopPointItemRequestBuilder

class ToRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /{ids-id}/Timetable/{fromStopPointId}/to
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ToRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/{ids%2Did}/Timetable/{fromStopPointId}/to", path_parameters)
    
    def by_to_stop_point_id(self,to_stop_point_id: str) -> WithToStopPointItemRequestBuilder:
        """
        Gets an item from the tfl_api_line.item.Timetable.item.to.item collection
        param to_stop_point_id: The destination stations's Naptan code
        Returns: WithToStopPointItemRequestBuilder
        """
        if to_stop_point_id is None:
            raise TypeError("to_stop_point_id cannot be null.")
        from .item.with_to_stop_point_item_request_builder import WithToStopPointItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["toStopPointId"] = to_stop_point_id
        return WithToStopPointItemRequestBuilder(self.request_adapter, url_tpl_params)
    

