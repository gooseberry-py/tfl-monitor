from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_types_item_request_builder import WithTypesItemRequestBuilder

class TypeRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /Place/Type
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TypeRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/Place/Type", path_parameters)
    
    def by_types(self,types: str) -> WithTypesItemRequestBuilder:
        """
        Gets an item from the tfl_api.Place.Type.item collection
        param types: A comma-separated list of the types to return. Max. approx 12 types.            A valid list of place types can be obtained from the /Place/Meta/placeTypes endpoint.
        Returns: WithTypesItemRequestBuilder
        """
        if types is None:
            raise TypeError("types cannot be null.")
        from .item.with_types_item_request_builder import WithTypesItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["types"] = types
        return WithTypesItemRequestBuilder(self.request_adapter, url_tpl_params)
    

