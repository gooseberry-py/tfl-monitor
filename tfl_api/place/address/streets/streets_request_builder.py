from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_postcode_item_request_builder import WithPostcodeItemRequestBuilder

class StreetsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /Place/Address/Streets
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new StreetsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/Place/Address/Streets", path_parameters)
    
    def by_postcode(self,postcode: str) -> WithPostcodeItemRequestBuilder:
        """
        Gets an item from the tfl_api.Place.Address.Streets.item collection
        param postcode: Unique identifier of the item
        Returns: WithPostcodeItemRequestBuilder
        """
        if postcode is None:
            raise TypeError("postcode cannot be null.")
        from .item.with_postcode_item_request_builder import WithPostcodeItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["Postcode"] = postcode
        return WithPostcodeItemRequestBuilder(self.request_adapter, url_tpl_params)
    

