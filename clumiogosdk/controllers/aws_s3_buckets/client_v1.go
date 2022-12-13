// Copyright (c) 2021 Clumio All Rights Reserved

package awss3buckets

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// AwsS3BucketsV1Client represents a custom type interface
type AwsS3BucketsV1Client interface {
    // ListAwsS3Buckets Returns a list of S3 buckets.
    ListAwsS3Buckets(
        limit *int64, 
        start *string, 
        filter *string)(
        *models.ListBucketsResponse,  *apiutils.APIError)
    
    // ReadAwsS3Bucket Returns a representation of the specified S3 bucket.
    ReadAwsS3Bucket(
        bucketId string)(
        *models.ReadBucketResponse,  *apiutils.APIError)
    
    // SetBucketProperties Idempotent call to set properties on an S3 bucket to enable flows like S3
    //  continuous backup.
    SetBucketProperties(
        bucketId string, 
        body *models.SetBucketPropertiesV1Request)(
        *models.SetBucketPropertiesResponse,  *apiutils.APIError)
    
}

// NewAwsS3BucketsV1 returns AwsS3BucketsV1Client
func NewAwsS3BucketsV1(config config.Config) AwsS3BucketsV1Client {
    client := new(AwsS3BucketsV1)
    client.config = config
    return client
}
