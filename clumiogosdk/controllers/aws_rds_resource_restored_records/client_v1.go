// Copyright (c) 2021 Clumio All Rights Reserved

package awsrdsresourcerestoredrecords

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// AwsRdsResourceRestoredRecordsV1Client represents a custom type interface
type AwsRdsResourceRestoredRecordsV1Client interface {
    // ListRdsRestoredRecords Returns a list of RDS database restored-records.
    ListRdsRestoredRecords(
        limit *int64, 
        start *string, 
        filter *string)(
        *models.ListRestoredRecordsResponse,  *apiutils.APIError)
    
    // RestoreRdsRecord Start a database backup query with the query statement provided in user input. If the query preview flag is set in the input then the result will be returned in the response otherwise the query will run in background and a task id will be returned.
    RestoreRdsRecord(
        embed *string, 
        body *models.RestoreRdsRecordV1Request)(
        *models.RestoreRecordPreviewResponse,  *apiutils.APIError)
    
}

// NewAwsRdsResourceRestoredRecordsV1 returns AwsRdsResourceRestoredRecordsV1Client
func NewAwsRdsResourceRestoredRecordsV1(config config.Config) AwsRdsResourceRestoredRecordsV1Client {
    client := new(AwsRdsResourceRestoredRecordsV1)
    client.config = config
    return client
}
