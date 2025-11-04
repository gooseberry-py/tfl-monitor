from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_end_date_item_request_builder import WithEndDateItemRequestBuilder

class ToRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /{ids-id}/Status/{startDate}/to
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ToRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/{ids%2Did}/Status/{startDate}/to", path_parameters)
    
    def by_end_date(self,end_date: str) -> WithEndDateItemRequestBuilder:
        """
        Gets an item from the tfl_api_line.item.Status.item.to.item collection
        param end_date: Format - date-time (as date-time in RFC3339). End date for the period that the disruption will fall within to be included in the results
        Returns: WithEndDateItemRequestBuilder
        """
        if end_date is None:
            raise TypeError("end_date cannot be null.")
        from .item.with_end_date_item_request_builder import WithEndDateItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["endDate"] = end_date
        return WithEndDateItemRequestBuilder(self.request_adapter, url_tpl_params)
    

