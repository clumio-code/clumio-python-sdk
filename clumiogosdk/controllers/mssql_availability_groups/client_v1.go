// Copyright (c) 2021 Clumio All Rights Reserved

package mssqlavailabilitygroups

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// MssqlAvailabilityGroupsV1Client represents a custom type interface
type MssqlAvailabilityGroupsV1Client interface {
    // ListMssqlAvailabilityGroups Returns a list of Availability Groups.
    ListMssqlAvailabilityGroups(
        limit *int64, 
        start *string, 
        filter *string)(
        *models.ListMssqlAGsResponse,  *apiutils.APIError)
    
    // ReadMssqlAvailabilityGroup Returns a representation of the specified availability group.
    ReadMssqlAvailabilityGroup(
        availabilityGroupId string)(
        *models.ReadMssqlAGResponse,  *apiutils.APIError)
    
}

// NewMssqlAvailabilityGroupsV1 returns MssqlAvailabilityGroupsV1Client
func NewMssqlAvailabilityGroupsV1(config config.Config) MssqlAvailabilityGroupsV1Client {
    client := new(MssqlAvailabilityGroupsV1)
    client.config = config
    return client
}
