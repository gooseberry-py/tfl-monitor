from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .categories.categories_request_builder import CategoriesRequestBuilder
    from .severities.severities_request_builder import SeveritiesRequestBuilder

class MetaRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /Road/Meta
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MetaRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/Road/Meta", path_parameters)
    
    @property
    def categories(self) -> CategoriesRequestBuilder:
        """
        The Categories property
        """
        from .categories.categories_request_builder import CategoriesRequestBuilder

        return CategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def severities(self) -> SeveritiesRequestBuilder:
        """
        The Severities property
        """
        from .severities.severities_request_builder import SeveritiesRequestBuilder

        return SeveritiesRequestBuilder(self.request_adapter, self.path_parameters)
    

