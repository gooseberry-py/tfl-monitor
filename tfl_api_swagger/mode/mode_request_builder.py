from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .active_service_types.active_service_types_request_builder import ActiveServiceTypesRequestBuilder
    from .item.with_mode_item_request_builder import WithModeItemRequestBuilder

class ModeRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /Mode
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ModeRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/Mode", path_parameters)
    
    def by_mode(self,mode: str) -> WithModeItemRequestBuilder:
        """
        Gets an item from the tfl_api.Mode.item collection
        param mode: A mode name e.g. tube, dlr
        Returns: WithModeItemRequestBuilder
        """
        if mode is None:
            raise TypeError("mode cannot be null.")
        from .item.with_mode_item_request_builder import WithModeItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["mode"] = mode
        return WithModeItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def active_service_types(self) -> ActiveServiceTypesRequestBuilder:
        """
        The ActiveServiceTypes property
        """
        from .active_service_types.active_service_types_request_builder import ActiveServiceTypesRequestBuilder

        return ActiveServiceTypesRequestBuilder(self.request_adapter, self.path_parameters)
    

