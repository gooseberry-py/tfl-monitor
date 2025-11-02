from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .bike_points.bike_points_request_builder import BikePointsRequestBuilder
    from .car_park.car_park_request_builder import CarParkRequestBuilder
    from .charge_connector.charge_connector_request_builder import ChargeConnectorRequestBuilder

class OccupancyRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /Occupancy
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new OccupancyRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/Occupancy", path_parameters)
    
    @property
    def bike_points(self) -> BikePointsRequestBuilder:
        """
        The BikePoints property
        """
        from .bike_points.bike_points_request_builder import BikePointsRequestBuilder

        return BikePointsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def car_park(self) -> CarParkRequestBuilder:
        """
        The CarPark property
        """
        from .car_park.car_park_request_builder import CarParkRequestBuilder

        return CarParkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def charge_connector(self) -> ChargeConnectorRequestBuilder:
        """
        The ChargeConnector property
        """
        from .charge_connector.charge_connector_request_builder import ChargeConnectorRequestBuilder

        return ChargeConnectorRequestBuilder(self.request_adapter, self.path_parameters)
    

