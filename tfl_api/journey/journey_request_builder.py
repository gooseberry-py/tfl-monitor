from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .journey_results.journey_results_request_builder import JourneyResultsRequestBuilder
    from .meta.meta_request_builder import MetaRequestBuilder

class JourneyRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /Journey
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new JourneyRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/Journey", path_parameters)
    
    @property
    def journey_results(self) -> JourneyResultsRequestBuilder:
        """
        The JourneyResults property
        """
        from .journey_results.journey_results_request_builder import JourneyResultsRequestBuilder

        return JourneyResultsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def meta(self) -> MetaRequestBuilder:
        """
        The Meta property
        """
        from .meta.meta_request_builder import MetaRequestBuilder

        return MetaRequestBuilder(self.request_adapter, self.path_parameters)
    

