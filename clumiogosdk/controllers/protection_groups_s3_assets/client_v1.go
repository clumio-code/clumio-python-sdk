// Copyright (c) 2021 Clumio All Rights Reserved

package protectiongroupss3assets

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// ProtectionGroupsS3AssetsV1Client represents a custom type interface
type ProtectionGroupsS3AssetsV1Client interface {
    // ListProtectionGroupS3Assets Returns a list of protection group S3 assets.
    ListProtectionGroupS3Assets(
        limit *int64, 
        start *string, 
        filter *string)(
        *models.ListProtectionGroupS3AssetsResponse,  *apiutils.APIError)
    
    // ReadProtectionGroupS3Asset Returns a representation of the specified protection group S3 asset.
    ReadProtectionGroupS3Asset(
        protectionGroupS3AssetId string)(
        *models.ReadProtectionGroupS3AssetResponse,  *apiutils.APIError)
    
}

// NewProtectionGroupsS3AssetsV1 returns ProtectionGroupsS3AssetsV1Client
func NewProtectionGroupsS3AssetsV1(config config.Config) ProtectionGroupsS3AssetsV1Client {
    client := new(ProtectionGroupsS3AssetsV1)
    client.config = config
    return client
}
