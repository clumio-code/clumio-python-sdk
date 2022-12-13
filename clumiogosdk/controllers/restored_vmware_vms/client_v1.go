// Copyright (c) 2021 Clumio All Rights Reserved

package restoredvmwarevms

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// RestoredVmwareVmsV1Client represents a custom type interface
type RestoredVmwareVmsV1Client interface {
    // RestoreVmwareVm Restores the specified source VM backup to the specified target destination. The source VM must be one that was backed up by Clumio.
    RestoreVmwareVm(
        body models.RestoreVmwareVmV1Request)(
        *models.RestoreVMwareVMResponse,  *apiutils.APIError)
    
}

// NewRestoredVmwareVmsV1 returns RestoredVmwareVmsV1Client
func NewRestoredVmwareVmsV1(config config.Config) RestoredVmwareVmsV1Client {
    client := new(RestoredVmwareVmsV1)
    client.config = config
    return client
}
