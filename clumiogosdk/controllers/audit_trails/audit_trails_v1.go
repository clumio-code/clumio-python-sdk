// Copyright (c) 2021 Clumio All Rights Reserved

// Package audittrails contains methods related to AuditTrails
package audittrails

import (
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// AuditTrailsV1 represents a custom type struct
type AuditTrailsV1 struct {
    config config.Config
}

// ListAuditTrails Returns a list of audit trails.
func (a *AuditTrailsV1) ListAuditTrails(
    limit *int64, 
    start *string, 
    filter *string)(
    *models.ListAuditTrailsResponse, *apiutils.APIError) {

    queryBuilder := a.config.BaseUrl + "/audit-trails"

    
    header := "application/api.clumio.audit-trails=v1+json"
    var result *models.ListAuditTrailsResponse
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
