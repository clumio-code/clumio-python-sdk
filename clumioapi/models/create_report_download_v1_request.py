#
# Copyright 2023. Clumio, Inc.
#
from typing import Any, Dict, Mapping, Optional, Sequence, Type, TypeVar

from clumioapi.exceptions import clumio_exception

T = TypeVar('T', bound='CreateReportDownloadV1Request')

TypeValues = [
    'activity',
    'compliance',
    'audit',
    'consumption',
]


class CreateReportDownloadV1Request:
    """Implementation of the 'CreateReportDownloadV1Request' model.

    Attributes:
        file_name:
            The name of the report. Field cannot be empty.
        filter:

            +-------------------+------------------+-------------------+-------------------+
            |       Field       | Filter Condition |    Report Type    |    Description    |
            +===================+==================+===================+===================+
            | backup_timestamp  | $gte, $lt, $eq   | Compliance        | Backup timestamp  |
            |                   |                  |                   | denotes the time  |
            |                   |                  |                   | filter for        |
            |                   |                  |                   | Compliance        |
            |                   |                  |                   | reports.          |
            |                   |                  |                   | $gte and $lt      |
            |                   |                  |                   | accept RFC-3339   |
            |                   |                  |                   | timestamps and    |
            |                   |                  |                   | $eq accepts a     |
            |                   |                  |                   | unix timestamp    |
            |                   |                  |                   | denoting the      |
            |                   |                  |                   | offset from the   |
            |                   |                  |                   | current time. $eq |
            |                   |                  |                   | takes precedence  |
            |                   |                  |                   | over both         |
            |                   |                  |                   | $gte and $lt so   |
            |                   |                  |                   | if $eq is used,   |
            |                   |                  |                   | the backend will  |
            |                   |                  |                   | use the relative  |
            |                   |                  |                   | time              |
            |                   |                  |                   | filter instead of |
            |                   |                  |                   | absolute time     |
            |                   |                  |                   | filters. For      |
            |                   |                  |                   | example,          |
            |                   |                  |                   |                   |
            |                   |                  |                   | "filter":"{"backu |
            |                   |                  |                   | p_timestamp":{"$e |
            |                   |                  |                   | q":86400}}"       |
            |                   |                  |                   |                   |
            |                   |                  |                   |                   |
            +-------------------+------------------+-------------------+-------------------+
            | activity_start_ti | $gte, $lt, $eq   | Activity          | Activity start    |
            | mestamp           |                  |                   | timestamp denotes |
            |                   |                  |                   | the time filter   |
            |                   |                  |                   | for Activity      |
            |                   |                  |                   | reports.          |
            |                   |                  |                   | $gte and $lt      |
            |                   |                  |                   | accept RFC-3339   |
            |                   |                  |                   | timestamps and    |
            |                   |                  |                   | $eq accepts a     |
            |                   |                  |                   | unix timestamp    |
            |                   |                  |                   | denoting the      |
            |                   |                  |                   | offset from the   |
            |                   |                  |                   | current time. $eq |
            |                   |                  |                   | takes precedence  |
            |                   |                  |                   | over both         |
            |                   |                  |                   | $gte and $lt so   |
            |                   |                  |                   | if $eq is used,   |
            |                   |                  |                   | the backend will  |
            |                   |                  |                   | use the relative  |
            |                   |                  |                   | time filter       |
            |                   |                  |                   | instead of        |
            |                   |                  |                   | absolute time     |
            |                   |                  |                   | filters.For       |
            |                   |                  |                   | example,          |
            |                   |                  |                   |                   |
            |                   |                  |                   | "filter":"{"activ |
            |                   |                  |                   | ity_start_timesta |
            |                   |                  |                   | mp":{"$eq":86400} |
            |                   |                  |                   | }"                |
            |                   |                  |                   |                   |
            |                   |                  |                   |                   |
            +-------------------+------------------+-------------------+-------------------+
            | timestamp         | $gte, $lte, $eq  | Consumption       | timestamp denotes |
            |                   |                  |                   | the time filter   |
            |                   |                  |                   | for Consumption   |
            |                   |                  |                   | reports.          |
            |                   |                  |                   | $gte and $lte     |
            |                   |                  |                   | accept RFC-3339   |
            |                   |                  |                   | timestamps and    |
            |                   |                  |                   | $eq accepts a     |
            |                   |                  |                   | duration in       |
            |                   |                  |                   | seconds           |
            |                   |                  |                   | denoting the      |
            |                   |                  |                   | offset from the   |
            |                   |                  |                   | current time. $eq |
            |                   |                  |                   | takes precedence  |
            |                   |                  |                   | over both         |
            |                   |                  |                   | $gte and $lte so  |
            |                   |                  |                   | if $eq is used,   |
            |                   |                  |                   | the backend will  |
            |                   |                  |                   | use the relative  |
            |                   |                  |                   | time filter       |
            |                   |                  |                   | instead of        |
            |                   |                  |                   | absolute time     |
            |                   |                  |                   | filters.          |
            |                   |                  |                   |                   |
            |                   |                  |                   | "filter": "{\"tim |
            |                   |                  |                   | estamp\":{\"$gte\\ |
            |                   |                  |                   | ":\"2022-07-      |
            |                   |                  |                   | 27T14:35:33.735Z\\ |
            |                   |                  |                   | ",\"$lte\":\"2022 |
            |                   |                  |                   | -08-              |
            |                   |                  |                   | 03T14:35:33.735Z\\ |
            |                   |                  |                   | "}}"              |
            |                   |                  |                   |                   |
            |                   |                  |                   |                   |
            +-------------------+------------------+-------------------+-------------------+
            | organizational_un | $in              | Consumption       | Organizational    |
            | it_id             |                  |                   | Unit ID (OU ID)   |
            |                   |                  |                   | filters the       |
            |                   |                  |                   | consumption data  |
            |                   |                  |                   | generated for the |
            |                   |                  |                   | report to the     |
            |                   |                  |                   | given OU IDs and  |
            |                   |                  |                   | its children.     |
            |                   |                  |                   |                   |
            |                   |                  |                   | "filter": "{\"org |
            |                   |                  |                   | anizational_unit_ |
            |                   |                  |                   | id\":{\"$in\":[\" |
            |                   |                  |                   | 00000000-0000-    |
            |                   |                  |                   | 0000-0000-        |
            |                   |                  |                   | 000000000000\"]}} |
            |                   |                  |                   | "                 |
            |                   |                  |                   |                   |
            |                   |                  |                   |                   |
            +-------------------+------------------+-------------------+-------------------+
            | entity_type       | $in              | Consumption       |                   |
            |                   |                  |                   | Entity type       |
            |                   |                  |                   | filters the       |
            |                   |                  |                   | consumption data  |
            |                   |                  |                   | generated for the |
            |                   |                  |                   | report to the     |
            |                   |                  |                   | given entity      |
            |                   |                  |                   | types.            |
            |                   |                  |                   | If filter is      |
            |                   |                  |                   | empty, it shows   |
            |                   |                  |                   | consumption       |
            |                   |                  |                   | report of the all |
            |                   |                  |                   | entity types.     |
            |                   |                  |                   |                   |
            |                   |                  |                   | filter={"entity_t |
            |                   |                  |                   | ype":{"$in":["Loc |
            |                   |                  |                   | alProtectionGroup |
            |                   |                  |                   | , DynamoDB"]}}    |
            |                   |                  |                   |                   |
            |                   |                  |                   |                   |
            +-------------------+------------------+-------------------+-------------------+
            | task              | $in              | Activity          |  Possible values  |
            |                   |                  |                   | for task include  |
            |                   |                  |                   | backup and        |
            |                   |                  |                   | restore.          |
            |                   |                  |                   | For example,      |
            |                   |                  |                   |                   |
            |                   |                  |                   | "filter":"{"task" |
            |                   |                  |                   | :{"$in":["ebs_inc |
            |                   |                  |                   | remental_backup"] |
            |                   |                  |                   | }}"               |
            |                   |                  |                   |                   |
            |                   |                  |                   |                   |
            +-------------------+------------------+-------------------+-------------------+
            | status            | $in              | Activity,         |  Filter on        |
            |                   |                  | Compliance        | compliance status |
            |                   |                  |                   | of entity.        |
            |                   |                  |                   | Possible values   |
            |                   |                  |                   | for compliance    |
            |                   |                  |                   | status            |
            |                   |                  |                   | include compliant |
            |                   |                  |                   | and non_compliant |
            |                   |                  |                   | For example,      |
            |                   |                  |                   |                   |
            |                   |                  |                   | "filter": "{"stat |
            |                   |                  |                   | us":{"$in":["non_ |
            |                   |                  |                   | compliant"]}}"    |
            |                   |                  |                   |                   |
            |                   |                  |                   |                   |
            +-------------------+------------------+-------------------+-------------------+
            | primary_entity.id | $in              | Any               | The system-       |
            |                   |                  |                   | generated IDs of  |
            |                   |                  |                   | the primary       |
            |                   |                  |                   | entities affected |
            |                   |                  |                   | by the activity.  |
            |                   |                  |                   | For example,      |
            |                   |                  |                   |                   |
            |                   |                  |                   | filter={"primary_ |
            |                   |                  |                   | entity.id":{"$in" |
            |                   |                  |                   | :["9c2934fc-ff4d- |
            |                   |                  |                   | 11e9-8e11-        |
            |                   |                  |                   | 76706df7fe01"]}}  |
            |                   |                  |                   |                   |
            |                   |                  |                   |                   |
            +-------------------+------------------+-------------------+-------------------+
            | primary_entity.ty | $eq              | Any               | The type of       |
            | pe                |                  |                   | primary entities  |
            |                   |                  |                   | affected by the   |
            |                   |                  |                   | activity.         |
            |                   |                  |                   | Examples of       |
            |                   |                  |                   | primary entity    |
            |                   |                  |                   | types include     |
            |                   |                  |                   | "aws_ebs_volume", |
            |                   |                  |                   | "vmware_vm",      |
            |                   |                  |                   | "microsoft365_mai |
            |                   |                  |                   | lbox". For        |
            |                   |                  |                   | example,          |
            |                   |                  |                   |                   |
            |                   |                  |                   | filter={"primary_ |
            |                   |                  |                   | entity.type":{"$i |
            |                   |                  |                   | n":["aws_ebs_volu |
            |                   |                  |                   | me"]}}            |
            |                   |                  |                   |                   |
            |                   |                  |                   |                   |
            +-------------------+------------------+-------------------+-------------------+
            | primary_entity.va | $in              | Any               | The value or name |
            | lue               |                  |                   | associated with   |
            |                   |                  |                   | the primary       |
            |                   |                  |                   | entities affected |
            |                   |                  |                   | by                |
            |                   |                  |                   | the compliance    |
            |                   |                  |                   | event. For        |
            |                   |                  |                   | example, the      |
            |                   |                  |                   | primary entity    |
            |                   |                  |                   | value associated  |
            |                   |                  |                   | with              |
            |                   |                  |                   | primary entity    |
            |                   |                  |                   | type              |
            |                   |                  |                   | "aws_ebs_volume"  |
            |                   |                  |                   | is "vol-          |
            |                   |                  |                   | 0a5f2e52d6decd664 |
            |                   |                  |                   | " representing    |
            |                   |                  |                   | the name of the   |
            |                   |                  |                   | EBS volume. The   |
            |                   |                  |                   | filter supports   |
            |                   |                  |                   | substring search  |
            |                   |                  |                   | for all           |
            |                   |                  |                   | elements in the   |
            |                   |                  |                   | array For         |
            |                   |                  |                   | example,          |
            |                   |                  |                   |                   |
            |                   |                  |                   | filter={"primary_ |
            |                   |                  |                   | entity.value":{"$ |
            |                   |                  |                   | in":["vol-0a"]}}  |
            |                   |                  |                   |                   |
            |                   |                  |                   |                   |
            +-------------------+------------------+-------------------+-------------------+
            | parent_entity.typ | $in              | Any               |  The types of the |
            | e                 |                  |                   | parent entities   |
            |                   |                  |                   | which are         |
            |                   |                  |                   | associated        |
            |                   |                  |                   | with the primary  |
            |                   |                  |                   | entity affected   |
            |                   |                  |                   | by the activity.  |
            |                   |                  |                   | Examples of the   |
            |                   |                  |                   | parent entity     |
            |                   |                  |                   | types include     |
            |                   |                  |                   | "vmware_vcenter", |
            |                   |                  |                   | "aws_environment" |
            |                   |                  |                   | , "microsoft365_d |
            |                   |                  |                   | omain". For       |
            |                   |                  |                   | example,          |
            |                   |                  |                   |                   |
            |                   |                  |                   | filter={"parent_e |
            |                   |                  |                   | ntity.type":{"$in |
            |                   |                  |                   | ":["aws_environme |
            |                   |                  |                   | nt"]}}            |
            |                   |                  |                   |                   |
            |                   |                  |                   |                   |
            +-------------------+------------------+-------------------+-------------------+
            | parent_entity.id  | $in              | Any               |                   |
            |                   |                  |                   | The value or name |
            |                   |                  |                   | associated with   |
            |                   |                  |                   | the parent        |
            |                   |                  |                   | entities affected |
            |                   |                  |                   | by                |
            |                   |                  |                   | the compliance    |
            |                   |                  |                   | event. For        |
            |                   |                  |                   | example, the      |
            |                   |                  |                   | parent entity     |
            |                   |                  |                   | value associated  |
            |                   |                  |                   | with              |
            |                   |                  |                   | primary entity    |
            |                   |                  |                   | type              |
            |                   |                  |                   | "aws_ebs_volume"  |
            |                   |                  |                   | is                |
            |                   |                  |                   | "891106093485/us- |
            |                   |                  |                   | west-2"           |
            |                   |                  |                   | representing      |
            |                   |                  |                   | the name of the   |
            |                   |                  |                   | AWS Account       |
            |                   |                  |                   | Region. For       |
            |                   |                  |                   | example,          |
            |                   |                  |                   |                   |
            |                   |                  |                   | filter={"parent_e |
            |                   |                  |                   | ntity.id":{"$in": |
            |                   |                  |                   | ["9c2934fc-ff4d-  |
            |                   |                  |                   | 11e9-8e11-        |
            |                   |                  |                   | 76706df7fe01"]}}  |
            |                   |                  |                   |                   |
            |                   |                  |                   |                   |
            +-------------------+------------------+-------------------+-------------------+

            For more information about filtering, refer to the
            Filtering section of this guide.
        p_type:
            The report type. Examples of report types include, "activity",
            "compliance", "audit", and "consumption".
    """

    # Create a mapping from Model property names to API property names
    _names = {'file_name': 'file_name', 'filter': 'filter', 'p_type': 'type'}

    def __init__(self, file_name: str = None, filter: str = None, p_type: str = None) -> None:
        """Constructor for the CreateReportDownloadV1Request class."""

        # Initialize members of the class
        self.file_name: str = file_name
        self.filter: str = filter

        if p_type not in TypeValues:
            raise clumio_exception.ClumioException(
                f'Invalid value for p_type: { p_type }. Valid values are { TypeValues }.',
                None,
            )
        self.p_type: str = p_type

    @classmethod
    def from_dictionary(cls: Type, dictionary: Mapping[str, Any]) -> Optional[T]:
        """Creates an instance of this model from a dictionary

        Args:
            dictionary: A dictionary representation of the object as obtained
                from the deserialization of the server's response. The keys
                MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.
        """
        if not dictionary:
            return None

        # Extract variables from the dictionary
        file_name = dictionary.get('file_name')
        filter = dictionary.get('filter')
        p_type = dictionary.get('type')
        # Return an object of this model
        return cls(file_name, filter, p_type)
