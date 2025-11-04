from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_severity_item_request_builder import WithSeverityItemRequestBuilder

class StatusRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /Status
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new StatusRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/Status", path_parameters)
    
    def by_severity(self,severity: int) -> WithSeverityItemRequestBuilder:
        """
        Gets an item from the tfl_api_line.Status.item collection
        param severity: Format - int32. The level of severity (eg: a number from 0 to 14)
        Returns: WithSeverityItemRequestBuilder
        """
        if severity is None:
            raise TypeError("severity cannot be null.")
        from .item.with_severity_item_request_builder import WithSeverityItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["severity"] = severity
        return WithSeverityItemRequestBuilder(self.request_adapter, url_tpl_params)
    

