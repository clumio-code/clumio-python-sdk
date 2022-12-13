// Copyright (c) 2021 Clumio All Rights Reserved

package reportdownloads

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// ReportDownloadsV1Client represents a custom type interface
type ReportDownloadsV1Client interface {
    // ListReportDownloads Returns a list of unexpired, generated reports.
    ListReportDownloads(
        limit *int64, 
        start *string, 
        filter *string)(
        *models.ListReportDownloadsResponse,  *apiutils.APIError)
    
    // CreateReportDownload Generates a report of a specified type given certain general conditions such as time range and other type-specific filters.
    CreateReportDownload(
        body models.CreateReportDownloadV1Request)(
        *models.CreateReportDownloadResponse,  *apiutils.APIError)
    
}

// NewReportDownloadsV1 returns ReportDownloadsV1Client
func NewReportDownloadsV1(config config.Config) ReportDownloadsV1Client {
    client := new(ReportDownloadsV1)
    client.config = config
    return client
}
