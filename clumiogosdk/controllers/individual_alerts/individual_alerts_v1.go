// Copyright (c) 2021 Clumio All Rights Reserved

// Package individualalerts contains methods related to IndividualAlerts
package individualalerts

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// IndividualAlertsV1 represents a custom type struct
type IndividualAlertsV1 struct {
    config config.Config
}

// ListIndividualAlerts Returns a list of individual alerts.
//  
//  Each alert is associated with a cause, which represents the issue that generated the alert,
//  and each cause belongs to a general alert alert type. Some alert types may be associated with multiple causes.
//  
//  The following table lists the Clumio alert types:
//  
//  
//  +--------------------------+---------------------------------------------------+
//  |        Alert Type        |                    Description                    |
//  +==========================+===================================================+
//  | policy_violated          | An entity's scheduled backup failed.              |
//  +--------------------------+---------------------------------------------------+
//  | restore_failed           | An entity restore failed.                         |
//  +--------------------------+---------------------------------------------------+
//  | file_restore_failed      | A file restore failed.                            |
//  +--------------------------+---------------------------------------------------+
//  | tag_conflict             | An EBS volume has multiple associated tags        |
//  |                          | with different protection policies applied at the |
//  |                          | tag level.                                        |
//  +--------------------------+---------------------------------------------------+
//  | aws_account_disconnected | The connection                                    |
//  |                          | between Clumio Cloud Connector and the user's AWS |
//  |                          | account failed.                                   |
//  +--------------------------+---------------------------------------------------+
//  | enc_key_inaccessible     | An issue is blocking encryption key access.       |
//  +--------------------------+---------------------------------------------------+
//  
func (i *IndividualAlertsV1) ListIndividualAlerts(
    limit *int64, 
    start *string, 
    sort *string, 
    filter *string, 
    embed *string)(
    *models.ListAlertsResponse, *apiutils.APIError) {

    queryBuilder := i.config.BaseUrl + "/alerts/individual"

    
    header := "application/api.clumio.individual-alerts=v1+json"
    var result *models.ListAlertsResponse
    defaultInt64 := int64(0)
    defaultString := "" 
    
    if limit == nil {
        limit = &defaultInt64
    }
    if start == nil {
        start = &defaultString
    }
    if sort == nil {
        sort = &defaultString
    }
    if filter == nil {
        filter = &defaultString
    }
    if embed == nil {
        embed = &defaultString
    }
    
    queryParams := map[string]string{
        "limit": fmt.Sprintf("%v", *limit),
        "start": *start,
        "sort": *sort,
        "filter": *filter,
        "embed": *embed,
    }

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: i.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// ReadIndividualAlert Returns a representation of the specified individual alert.
func (i *IndividualAlertsV1) ReadIndividualAlert(
    individualAlertId string, 
    embed *string)(
    *models.ReadAlertResponse, *apiutils.APIError) {

    pathURL := "/alerts/individual/{individual_alert_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "individual_alert_id": individualAlertId,
    }
    queryBuilder := i.config.BaseUrl + pathURL

    
    header := "application/api.clumio.individual-alerts=v1+json"
    var result *models.ReadAlertResponse
    defaultString := "" 
    
    if embed == nil {
        embed = &defaultString
    }
    
    queryParams := map[string]string{
        "embed": *embed,
    }

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: i.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        PathParams: pathParams,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// UpdateIndividualAlert Manages an existing individual alert. Managing an individual alert includes clearing the alert and adding notes to the specified alert.
func (i *IndividualAlertsV1) UpdateIndividualAlert(
    individualAlertId string, 
    embed *string, 
    body *models.UpdateIndividualAlertV1Request)(
    *models.UpdateAlertResponse, *apiutils.APIError) {

    pathURL := "/alerts/individual/{individual_alert_id}"
    //process optional template parameters
    pathParams := map[string]string{
        "individual_alert_id": individualAlertId,
    }
    queryBuilder := i.config.BaseUrl + pathURL

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.individual-alerts=v1+json"
    var result *models.UpdateAlertResponse
    defaultString := "" 
    
    if embed == nil {
        embed = &defaultString
    }
    
    queryParams := map[string]string{
        "embed": *embed,
    }

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: i.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        PathParams: pathParams,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Patch,
    })

    return result, apiErr
}
