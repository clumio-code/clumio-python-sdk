// Copyright (c) 2021 Clumio All Rights Reserved

package awsenvironmenttags

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// AwsEnvironmentTagsV1Client represents a custom type interface
type AwsEnvironmentTagsV1Client interface {
    // ListAwsEnvironmentTags Returns a list of AWS tags in the specified environment.
    ListAwsEnvironmentTags(
        environmentId string, 
        currentCount *int64, 
        limit *int64, 
        totalCount *int64, 
        totalPagesCount *int64, 
        start *string, 
        filter *string, 
        embed *string)(
        *models.ListAwsTagsResponse,  *apiutils.APIError)
    
    // ReadAwsEnvironmentTag Returns a representation of the specified AWS tag in the specified environment.
    ReadAwsEnvironmentTag(
        environmentId string, 
        tagId string, 
        embed *string)(
        *models.ReadAwsTagResponse,  *apiutils.APIError)
    
    // ReadAwsEnvironmentTagEbsVolumesComplianceStats Returns the specified AWS tag's EBS compliance statistics.
    ReadAwsEnvironmentTagEbsVolumesComplianceStats(
        environmentId string, 
        tagId string)(
        *models.ReadEbsTagComplianceStatsResponse,  *apiutils.APIError)
    
}

// NewAwsEnvironmentTagsV1 returns AwsEnvironmentTagsV1Client
func NewAwsEnvironmentTagsV1(config config.Config) AwsEnvironmentTagsV1Client {
    client := new(AwsEnvironmentTagsV1)
    client.config = config
    return client
}
