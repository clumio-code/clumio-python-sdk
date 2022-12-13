// Copyright (c) 2021 Clumio All Rights Reserved

package managementgroups

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// ManagementGroupsV1Client represents a custom type interface
type ManagementGroupsV1Client interface {
    // ListManagementGroups Returns a list of management groups.
    ListManagementGroups(
        limit *int64, 
        start *string)(
        *models.ListManagementGroupsResponse,  *apiutils.APIError)
    
    // ReadManagementGroup Returns a representation of the specified management group. Management groups are used to
    //  manage the SQL hosts and cloud connectors deployed in vCenter servers.
    //  
    //  Returns a representation of the specified management-groups.
    ReadManagementGroup(
        groupId string)(
        *models.ReadManagementGroupResponse,  *apiutils.APIError)
    
    // UpdateManagementGroup Update the specified management group.
    UpdateManagementGroup(
        groupId string, 
        body *models.UpdateManagementGroupV1Request)(
        *models.UpdateManagementGroupResponse,  *apiutils.APIError)
    
}

// NewManagementGroupsV1 returns ManagementGroupsV1Client
func NewManagementGroupsV1(config config.Config) ManagementGroupsV1Client {
    client := new(ManagementGroupsV1)
    client.config = config
    return client
}
