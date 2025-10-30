from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_year_item_request_builder import WithYearItemRequestBuilder

class AccidentStatsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /AccidentStats
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new AccidentStatsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/AccidentStats", path_parameters)
    
    def by_year(self,year: int) -> WithYearItemRequestBuilder:
        """
        Gets an item from the tfl_api.AccidentStats.item collection
        param year: The year for which to filter the accidents on.
        Returns: WithYearItemRequestBuilder
        """
        if year is None:
            raise TypeError("year cannot be null.")
        from .item.with_year_item_request_builder import WithYearItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["year"] = year
        return WithYearItemRequestBuilder(self.request_adapter, url_tpl_params)
    

