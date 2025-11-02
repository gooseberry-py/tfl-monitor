from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .search_match import SearchMatch

@dataclass
class SearchResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The from property
    from_: Optional[int] = None
    # The matches property
    matches: Optional[list[SearchMatch]] = None
    # The maxScore property
    max_score: Optional[float] = None
    # The page property
    page: Optional[int] = None
    # The pageSize property
    page_size: Optional[int] = None
    # The provider property
    provider: Optional[str] = None
    # The query property
    query: Optional[str] = None
    # The total property
    total: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SearchResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SearchResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SearchResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .search_match import SearchMatch

        from .search_match import SearchMatch

        fields: dict[str, Callable[[Any], None]] = {
            "from": lambda n : setattr(self, 'from_', n.get_int_value()),
            "matches": lambda n : setattr(self, 'matches', n.get_collection_of_object_values(SearchMatch)),
            "maxScore": lambda n : setattr(self, 'max_score', n.get_float_value()),
            "page": lambda n : setattr(self, 'page', n.get_int_value()),
            "pageSize": lambda n : setattr(self, 'page_size', n.get_int_value()),
            "provider": lambda n : setattr(self, 'provider', n.get_str_value()),
            "query": lambda n : setattr(self, 'query', n.get_str_value()),
            "total": lambda n : setattr(self, 'total', n.get_int_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_int_value("from", self.from_)
        writer.write_collection_of_object_values("matches", self.matches)
        writer.write_float_value("maxScore", self.max_score)
        writer.write_int_value("page", self.page)
        writer.write_int_value("pageSize", self.page_size)
        writer.write_str_value("provider", self.provider)
        writer.write_str_value("query", self.query)
        writer.write_int_value("total", self.total)
        writer.write_additional_data_value(self.additional_data)
    

