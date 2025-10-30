from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .disruption_categories.disruption_categories_request_builder import DisruptionCategoriesRequestBuilder
    from .modes.modes_request_builder import ModesRequestBuilder
    from .service_types.service_types_request_builder import ServiceTypesRequestBuilder
    from .severity.severity_request_builder import SeverityRequestBuilder

class MetaRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /Line/Meta
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MetaRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/Line/Meta", path_parameters)
    
    @property
    def disruption_categories(self) -> DisruptionCategoriesRequestBuilder:
        """
        The DisruptionCategories property
        """
        from .disruption_categories.disruption_categories_request_builder import DisruptionCategoriesRequestBuilder

        return DisruptionCategoriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def modes(self) -> ModesRequestBuilder:
        """
        The Modes property
        """
        from .modes.modes_request_builder import ModesRequestBuilder

        return ModesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def service_types(self) -> ServiceTypesRequestBuilder:
        """
        The ServiceTypes property
        """
        from .service_types.service_types_request_builder import ServiceTypesRequestBuilder

        return ServiceTypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def severity(self) -> SeverityRequestBuilder:
        """
        The Severity property
        """
        from .severity.severity_request_builder import SeverityRequestBuilder

        return SeverityRequestBuilder(self.request_adapter, self.path_parameters)
    

