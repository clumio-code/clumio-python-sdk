// Copyright (c) 2021 Clumio All Rights Reserved

package individualalerts

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// IndividualAlertsV1Client represents a custom type interface
type IndividualAlertsV1Client interface {
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
    ListIndividualAlerts(
        limit *int64, 
        start *string, 
        sort *string, 
        filter *string, 
        embed *string)(
        *models.ListAlertsResponse,  *apiutils.APIError)
    
    // ReadIndividualAlert Returns a representation of the specified individual alert.
    ReadIndividualAlert(
        individualAlertId string, 
        embed *string)(
        *models.ReadAlertResponse,  *apiutils.APIError)
    
    // UpdateIndividualAlert Manages an existing individual alert. Managing an individual alert includes clearing the alert and adding notes to the specified alert.
    UpdateIndividualAlert(
        individualAlertId string, 
        embed *string, 
        body *models.UpdateIndividualAlertV1Request)(
        *models.UpdateAlertResponse,  *apiutils.APIError)
    
}

// NewIndividualAlertsV1 returns IndividualAlertsV1Client
func NewIndividualAlertsV1(config config.Config) IndividualAlertsV1Client {
    client := new(IndividualAlertsV1)
    client.config = config
    return client
}
