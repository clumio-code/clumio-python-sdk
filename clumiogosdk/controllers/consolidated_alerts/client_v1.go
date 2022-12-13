// Copyright (c) 2021 Clumio All Rights Reserved

package consolidatedalerts

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// ConsolidatedAlertsV1Client represents a custom type interface
type ConsolidatedAlertsV1Client interface {
    // ListConsolidatedAlerts Returns a list of consolidated alerts.
    ListConsolidatedAlerts(
        limit *int64, 
        start *string, 
        filter *string)(
        *models.ListConsolidatedAlertsResponse,  *apiutils.APIError)
    
    // ReadConsolidatedAlert Returns a representation of the specified consolidated alert.
    ReadConsolidatedAlert(
        id string)(
        *models.ReadConsolidatedAlertResponse,  *apiutils.APIError)
    
    // UpdateConsolidatedAlert Manages the specified consolidated alert. Managing a consolidated alert includes clearing the alert and adding notes to the specified consolidated alert.
    UpdateConsolidatedAlert(
        id string, 
        body *models.UpdateConsolidatedAlertV1Request)(
        *models.UpdateConsolidatedAlertResponse,  *apiutils.APIError)
    
}

// NewConsolidatedAlertsV1 returns ConsolidatedAlertsV1Client
func NewConsolidatedAlertsV1(config config.Config) ConsolidatedAlertsV1Client {
    client := new(ConsolidatedAlertsV1)
    client.config = config
    return client
}
