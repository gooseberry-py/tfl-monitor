from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ...models.tfl.api.presentation.entities.place import Place
    from .at.at_request_builder import AtRequestBuilder
    from .overlay.overlay_request_builder import OverlayRequestBuilder

class ItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /Place/{-id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/Place/{%2Did}{?includeChildren*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[ItemRequestBuilderGetQueryParameters]] = None) -> Optional[list[Place]]:
        """
        Gets the place with the given id.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[Place]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.tfl.api.presentation.entities.place import Place

        return await self.request_adapter.send_collection_async(request_info, Place, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[ItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets the place with the given id.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> ItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def at(self) -> AtRequestBuilder:
        """
        The At property
        """
        from .at.at_request_builder import AtRequestBuilder

        return AtRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def overlay(self) -> OverlayRequestBuilder:
        """
        The overlay property
        """
        from .overlay.overlay_request_builder import OverlayRequestBuilder

        return OverlayRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ItemRequestBuilderGetQueryParameters():
        """
        Gets the place with the given id.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "include_children":
                return "includeChildren"
            return original_name
        
        # Defaults to false. If true child places e.g. individual charging stations at a charge point while be included, otherwise just the URLs of any child places will be returned
        include_children: Optional[bool] = None

    
    @dataclass
    class ItemRequestBuilderGetRequestConfiguration(RequestConfiguration[ItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

