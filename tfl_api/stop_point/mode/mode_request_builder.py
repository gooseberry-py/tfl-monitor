from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_modes_item_request_builder import WithModesItemRequestBuilder

class ModeRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /StopPoint/Mode
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ModeRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/StopPoint/Mode", path_parameters)
    
    def by_modes(self,modes: str) -> WithModesItemRequestBuilder:
        """
        Gets an item from the tfl_api.StopPoint.Mode.item collection
        param modes: A comma-seperated list of modes e.g. tube,dlr
        Returns: WithModesItemRequestBuilder
        """
        if modes is None:
            raise TypeError("modes cannot be null.")
        from .item.with_modes_item_request_builder import WithModesItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["modes"] = modes
        return WithModesItemRequestBuilder(self.request_adapter, url_tpl_params)
    

