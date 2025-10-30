from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_from_stop_point_item_request_builder import WithFromStopPointItemRequestBuilder

class TimetableRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /Line/{ids-id}/Timetable
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TimetableRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/Line/{ids%2Did}/Timetable", path_parameters)
    
    def by_from_stop_point_id(self,from_stop_point_id: str) -> WithFromStopPointItemRequestBuilder:
        """
        Gets an item from the tfl_api.Line.item.Timetable.item collection
        param from_stop_point_id: The originating station's stop point id (station naptan code e.g. 940GZZLUASL, you can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name)
        Returns: WithFromStopPointItemRequestBuilder
        """
        if from_stop_point_id is None:
            raise TypeError("from_stop_point_id cannot be null.")
        from .item.with_from_stop_point_item_request_builder import WithFromStopPointItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["fromStopPointId"] = from_stop_point_id
        return WithFromStopPointItemRequestBuilder(self.request_adapter, url_tpl_params)
    

