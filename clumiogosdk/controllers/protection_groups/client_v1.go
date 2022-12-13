// Copyright (c) 2021 Clumio All Rights Reserved

package protectiongroups

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// ProtectionGroupsV1Client represents a custom type interface
type ProtectionGroupsV1Client interface {
    // ListProtectionGroups Returns a list of protection groups.
    ListProtectionGroups(
        limit *int64, 
        start *string, 
        filter *string)(
        *models.ListProtectionGroupsResponse,  *apiutils.APIError)
    
    // ReadProtectionGroup Returns a representation of the specified protection group.
    ReadProtectionGroup(
        groupId string)(
        *models.ReadProtectionGroupResponse,  *apiutils.APIError)
    
    // CreateProtectionGroup Creates a new protection group by specifying object filters. Appearance in
    //  datasources/protection-groups read/listing is asynchronous and may take a few
    //  seconds to minutes at most. As a result, the protection group won't be protectable
    //  via /policies/assignments until it appears in the /datasources/protection-groups
    //  endpoint. Additionally, to create a protection group in the context of another Organizational
    //  Unit, refer to the Getting Started
    //  documentation.
    CreateProtectionGroup(
        body models.CreateProtectionGroupV1Request)(
        *models.CreateProtectionGroupResponse,  *apiutils.APIError)
    
    // UpdateProtectionGroup Updates a protection group by modifying object filters. Appearance in
    //  datasources/protection-groups read/listing is asynchronous and may take a few
    //  seconds to minutes at most. Must be in the same OU context as the creator of this
    //  protection group.
    UpdateProtectionGroup(
        groupId string, 
        body *models.UpdateProtectionGroupV1Request)(
        *models.UpdateProtectionGroupResponse,  *apiutils.APIError)
    
    // DeleteProtectionGroup Marks a protection group as deleted by taking the protection group ID. Appearance
    //  in /datasources/protection-groups read/listing is asynchronous and may take a few
    //  seconds to minutes at most. Must be in the same OU context as the creator of this
    //  protection group.
    DeleteProtectionGroup(
        groupId string)(
        interface{},  *apiutils.APIError)
    
    // AddBucketProtectionGroup Adds a bucket to protection group and creates a child protection group S3 asset.
    //  Appearance in /datasources/protection-groups/s3-assets read/listing is asynchronous
    //  and may take a few seconds to minutes at most. Must be in the same OU context as
    //  the creator of this protection group. Bucket ID in body can be found in
    //  datasources/aws/s3.
    AddBucketProtectionGroup(
        groupId string, 
        body models.AddBucketProtectionGroupV1Request)(
        *models.AddBucketToProtectionGroupResponse,  *apiutils.APIError)
    
    // DeleteBucketProtectionGroup Deletes a bucket from a protection group and the child protection group S3 asset.
    //  Appearance in /datasources/protection-groups/s3-assets read/listing is asynchronous
    //  and may take a few seconds to minutes at most. Must be in the same OU context as
    //  the creator of this protection group. Bucket ID in path can be found in
    //  datasources/aws/s3.
    DeleteBucketProtectionGroup(
        groupId string, 
        bucketId string)(
        *models.DeleteBucketFromProtectionGroupResponse,  *apiutils.APIError)
    
}

// NewProtectionGroupsV1 returns ProtectionGroupsV1Client
func NewProtectionGroupsV1(config config.Config) ProtectionGroupsV1Client {
    client := new(ProtectionGroupsV1)
    client.config = config
    return client
}
