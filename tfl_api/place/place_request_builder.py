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
    from ..models.tfl.api.presentation.entities.stop_point import StopPoint
    from .address.address_request_builder import AddressRequestBuilder
    from .item.item_request_builder import ItemRequestBuilder
    from .meta.meta_request_builder import MetaRequestBuilder
    from .search.search_request_builder import SearchRequestBuilder
    from .type.type_request_builder import TypeRequestBuilder

class PlaceRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /Place
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PlaceRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/Place{?activeOnly*,categories*,includeChildren*,numberOfPlacesToReturn*,placeGeo%2Elat*,placeGeo%2Elon*,placeGeo%2EneLat*,placeGeo%2EneLon*,placeGeo%2EswLat*,placeGeo%2EswLon*,radius*,type*}", path_parameters)
    
    def by_id(self,id: str) -> ItemRequestBuilder:
        """
        Gets an item from the tfl_api.Place.item collection
        param id: The id of the place, you can use the /Place/Types/{types} endpoint to get a list of places for a given type including their ids
        Returns: ItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.item_request_builder import ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["%2Did"] = id
        return ItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[PlaceRequestBuilderGetQueryParameters]] = None) -> Optional[list[StopPoint]]:
        """
        Gets the places that lie within a geographic region. The geographic region of interest can either be specified            by using a lat/lon geo-point and a radius in metres to return places within the locus defined by the lat/lon of            its centre or alternatively, by the use of a bounding box defined by the lat/lon of its north-west and south-east corners.            Optionally filters on type and can strip properties for a smaller payload.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[StopPoint]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.tfl.api.presentation.entities.stop_point import StopPoint

        return await self.request_adapter.send_collection_async(request_info, StopPoint, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PlaceRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets the places that lie within a geographic region. The geographic region of interest can either be specified            by using a lat/lon geo-point and a radius in metres to return places within the locus defined by the lat/lon of            its centre or alternatively, by the use of a bounding box defined by the lat/lon of its north-west and south-east corners.            Optionally filters on type and can strip properties for a smaller payload.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> PlaceRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PlaceRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PlaceRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def address(self) -> AddressRequestBuilder:
        """
        The Address property
        """
        from .address.address_request_builder import AddressRequestBuilder

        return AddressRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def meta(self) -> MetaRequestBuilder:
        """
        The Meta property
        """
        from .meta.meta_request_builder import MetaRequestBuilder

        return MetaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def search(self) -> SearchRequestBuilder:
        """
        The Search property
        """
        from .search.search_request_builder import SearchRequestBuilder

        return SearchRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def type(self) -> TypeRequestBuilder:
        """
        The Type property
        """
        from .type.type_request_builder import TypeRequestBuilder

        return TypeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PlaceRequestBuilderGetQueryParameters():
        """
        Gets the places that lie within a geographic region. The geographic region of interest can either be specified            by using a lat/lon geo-point and a radius in metres to return places within the locus defined by the lat/lon of            its centre or alternatively, by the use of a bounding box defined by the lat/lon of its north-west and south-east corners.            Optionally filters on type and can strip properties for a smaller payload.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "active_only":
                return "activeOnly"
            if original_name == "include_children":
                return "includeChildren"
            if original_name == "number_of_places_to_return":
                return "numberOfPlacesToReturn"
            if original_name == "place_geo_lat":
                return "placeGeo%2Elat"
            if original_name == "place_geo_lon":
                return "placeGeo%2Elon"
            if original_name == "place_geo_ne_lat":
                return "placeGeo%2EneLat"
            if original_name == "place_geo_ne_lon":
                return "placeGeo%2EneLon"
            if original_name == "place_geo_sw_lat":
                return "placeGeo%2EswLat"
            if original_name == "place_geo_sw_lon":
                return "placeGeo%2EswLon"
            if original_name == "categories":
                return "categories"
            if original_name == "radius":
                return "radius"
            if original_name == "type":
                return "type"
            return original_name
        
        # An optional parameter to limit the results to active records only (Currently only the 'VariableMessageSign' place type is supported)
        active_only: Optional[bool] = None

        # An optional list of comma separated property categories to return in the Place's property bag. If null or empty, all categories of property are returned. Pass the keyword "none" to return no properties (a valid list of categories can be obtained from the /Place/Meta/categories endpoint)
        categories: Optional[list[str]] = None

        # Defaults to false. If true child places e.g. individual charging stations at a charge point while be included, otherwise just the URLs of any child places will be returned
        include_children: Optional[bool] = None

        # If specified, limits the number of returned places equal to the given value
        number_of_places_to_return: Optional[int] = None

        place_geo_lat: Optional[float] = None

        place_geo_lon: Optional[float] = None

        place_geo_ne_lat: Optional[float] = None

        place_geo_ne_lon: Optional[float] = None

        place_geo_sw_lat: Optional[float] = None

        place_geo_sw_lon: Optional[float] = None

        # The radius of the bounding circle in metres when only lat/lon are specified.
        radius: Optional[float] = None

        # Place types to filter on, or null to return all types
        type: Optional[list[str]] = None

    
    @dataclass
    class PlaceRequestBuilderGetRequestConfiguration(RequestConfiguration[PlaceRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

