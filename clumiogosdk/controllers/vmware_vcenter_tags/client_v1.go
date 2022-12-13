// Copyright (c) 2021 Clumio All Rights Reserved

package vmwarevcentertags

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// VmwareVcenterTagsV1Client represents a custom type interface
type VmwareVcenterTagsV1Client interface {
    // ListVmwareVcenterTags Returns a list of tags in the specified vCenter server.
    ListVmwareVcenterTags(
        vcenterId string, 
        limit *int64, 
        start *string, 
        filter *string, 
        embed *string)(
        *models.ListTagsResponse,  *apiutils.APIError)
    
    // ReadVmwareVcenterTag Returns a representation of the specified tag.
    ReadVmwareVcenterTag(
        vcenterId string, 
        tagId string, 
        embed *string)(
        *models.ReadTagResponse,  *apiutils.APIError)
    
}

// NewVmwareVcenterTagsV1 returns VmwareVcenterTagsV1Client
func NewVmwareVcenterTagsV1(config config.Config) VmwareVcenterTagsV1Client {
    client := new(VmwareVcenterTagsV1)
    client.config = config
    return client
}
