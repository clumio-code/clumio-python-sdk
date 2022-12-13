// Copyright (c) 2021 Clumio All Rights Reserved

package audittrails

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// AuditTrailsV1Client represents a custom type interface
type AuditTrailsV1Client interface {
    // ListAuditTrails Returns a list of audit trails.
    ListAuditTrails(
        limit *int64, 
        start *string, 
        filter *string)(
        *models.ListAuditTrailsResponse,  *apiutils.APIError)
    
}

// NewAuditTrailsV1 returns AuditTrailsV1Client
func NewAuditTrailsV1(config config.Config) AuditTrailsV1Client {
    client := new(AuditTrailsV1)
    client.config = config
    return client
}
