from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.api_client_builder import enable_backing_store_for_serialization_writer_factory, register_default_deserializer, register_default_serializer
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.serialization import ParseNodeFactoryRegistry, SerializationWriterFactoryRegistry
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .asterisk.request_builder import RequestBuilder
    from .item.ids_item_request_builder import IdsItemRequestBuilder
    from .meta.meta_request_builder import MetaRequestBuilder
    from .mode.mode_request_builder import ModeRequestBuilder
    from .route.route_request_builder import RouteRequestBuilder
    from .search.search_request_builder import SearchRequestBuilder
    from .status.status_request_builder import StatusRequestBuilder

class Tfl_api_line(BaseRequestBuilder):
    """
    The main entry point of the SDK, exposes the configuration and the fluent API.
    """
    def __init__(self,request_adapter: RequestAdapter) -> None:
        """
        Instantiates a new Tfl_api_line and sets the default values.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        if request_adapter is None:
            raise TypeError("request_adapter cannot be null.")
        super().__init__(request_adapter, "{+baseurl}", None)
        if not self.request_adapter.base_url:
            self.request_adapter.base_url = "https://api.tfl.gov.uk/Line"
        self.path_parameters["base_url"] = self.request_adapter.base_url
    
    def by_ids_id(self,ids_id: str) -> IdsItemRequestBuilder:
        """
        Gets an item from the tfl_api_line.item collection
        param ids_id: A comma-separated list of line ids e.g. victoria,circle,N133. Max. approx. 20 ids.
        Returns: IdsItemRequestBuilder
        """
        if ids_id is None:
            raise TypeError("ids_id cannot be null.")
        from .item.ids_item_request_builder import IdsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["ids%2Did"] = ids_id
        return IdsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def asterisk(self) -> RequestBuilder:
        """
        The Asterisk property
        """
        from .asterisk.request_builder import RequestBuilder

        return RequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def meta(self) -> MetaRequestBuilder:
        """
        The Meta property
        """
        from .meta.meta_request_builder import MetaRequestBuilder

        return MetaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mode(self) -> ModeRequestBuilder:
        """
        The Mode property
        """
        from .mode.mode_request_builder import ModeRequestBuilder

        return ModeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def route(self) -> RouteRequestBuilder:
        """
        The Route property
        """
        from .route.route_request_builder import RouteRequestBuilder

        return RouteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def search(self) -> SearchRequestBuilder:
        """
        The Search property
        """
        from .search.search_request_builder import SearchRequestBuilder

        return SearchRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def status(self) -> StatusRequestBuilder:
        """
        The Status property
        """
        from .status.status_request_builder import StatusRequestBuilder

        return StatusRequestBuilder(self.request_adapter, self.path_parameters)
    

