// Copyright (c) 2021 Clumio All Rights Reserved

// Package consolidatedalerts contains methods related to ConsolidatedAlerts
package consolidatedalerts

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// ConsolidatedAlertsV1 represents a custom type struct
type ConsolidatedAlertsV1 struct {
    config config.Config
}

// ListConsolidatedAlerts Returns a list of consolidated alerts.
func (c *ConsolidatedAlertsV1) ListConsolidatedAlerts(
    limit *int64, 
    start *string, 
    filter *string)(
    *models.ListConsolidatedAlertsResponse, *apiutils.APIError) {

    queryBuilder := c.config.BaseUrl + "/alerts/consolidated"

    
    header := "application/api.clumio.consolidated-alerts=v1+json"
    var result *models.ListConsolidatedAlertsResponse
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
        Config: c.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// ReadConsolidatedAlert Returns a representation of the specified consolidated alert.
func (c *ConsolidatedAlertsV1) ReadConsolidatedAlert(
    id string)(
    *models.ReadConsolidatedAlertResponse, *apiutils.APIError) {

    pathURL := "/alerts/consolidated/{id}"
    //process optional template parameters
    pathParams := map[string]string{
        "id": id,
    }
    queryBuilder := c.config.BaseUrl + pathURL

    
    header := "application/api.clumio.consolidated-alerts=v1+json"
    var result *models.ReadConsolidatedAlertResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: c.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// UpdateConsolidatedAlert Manages the specified consolidated alert. Managing a consolidated alert includes clearing the alert and adding notes to the specified consolidated alert.
func (c *ConsolidatedAlertsV1) UpdateConsolidatedAlert(
    id string, 
    body *models.UpdateConsolidatedAlertV1Request)(
    *models.UpdateConsolidatedAlertResponse, *apiutils.APIError) {

    pathURL := "/alerts/consolidated/{id}"
    //process optional template parameters
    pathParams := map[string]string{
        "id": id,
    }
    queryBuilder := c.config.BaseUrl + pathURL

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.consolidated-alerts=v1+json"
    var result *models.UpdateConsolidatedAlertResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: c.config,
        RequestUrl: queryBuilder,
        PathParams: pathParams,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Patch,
    })

    return result, apiErr
}
