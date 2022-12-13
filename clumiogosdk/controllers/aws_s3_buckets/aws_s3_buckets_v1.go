// Copyright (c) 2021 Clumio All Rights Reserved

// Package awss3buckets contains methods related to AwsS3Buckets
package awss3buckets

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// AwsS3BucketsV1 represents a custom type struct
type AwsS3BucketsV1 struct {
    config config.Config
}

// ListAwsS3Buckets Returns a list of S3 buckets.
func (a *AwsS3BucketsV1) ListAwsS3Buckets(
    limit *int64, 
    start *string, 
    filter *string)(
    *models.ListBucketsResponse, *apiutils.APIError) {

    queryBuilder := a.config.BaseUrl + "/datasources/aws/s3-buckets"

    
    header := "application/api.clumio.aws-s3-buckets=v1+json"
    var result *models.ListBucketsResponse
    defaultInt64 := int64(0)
    defaultString := "" 
    
    if limit == nil {
        limit = &defaultInt64
    }
    if start == nil {
        start = &defaultString
    }
    if filter == nil {
        filter = &defaultString
    }
    
    queryParams := map[string]string{
        "limit": fmt.Sprintf("%v", *limit),
        "start": *start,
        "filter": *filter,
    }

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: a.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// ReadAwsS3Bucket Returns a representation of the specified S3 bucket.
func (a *AwsS3BucketsV1) ReadAwsS3Bucket(
    bucketId string)(
    *models.ReadBucketResponse, *apiutils.APIError) {

    pathURL := "/datasources/aws/s3-buckets/{bucket_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "bucket_id": bucketId,
    }
    queryBuilder := a.config.BaseUrl + pathURL

    
    header := "application/api.clumio.aws-s3-buckets=v1+json"
    var result *models.ReadBucketResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: a.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// SetBucketProperties Idempotent call to set properties on an S3 bucket to enable flows like S3
//  continuous backup.
func (a *AwsS3BucketsV1) SetBucketProperties(
    bucketId string, 
    body *models.SetBucketPropertiesV1Request)(
    *models.SetBucketPropertiesResponse, *apiutils.APIError) {

    pathURL := "/datasources/aws/s3-buckets/{bucket_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "bucket_id": bucketId,
    }
    queryBuilder := a.config.BaseUrl + pathURL

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.aws-s3-buckets=v1+json"
    var result *models.SetBucketPropertiesResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: a.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Patch,
    })

    return result, apiErr
}
