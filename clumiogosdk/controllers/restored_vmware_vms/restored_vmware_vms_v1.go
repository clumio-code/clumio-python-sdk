// Copyright (c) 2021 Clumio All Rights Reserved

// Package restoredvmwarevms contains methods related to RestoredVmwareVms
package restoredvmwarevms

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// RestoredVmwareVmsV1 represents a custom type struct
type RestoredVmwareVmsV1 struct {
    config config.Config
}

// RestoreVmwareVm Restores the specified source VM backup to the specified target destination. The source VM must be one that was backed up by Clumio.
func (r *RestoredVmwareVmsV1) RestoreVmwareVm(
    body models.RestoreVmwareVmV1Request)(
    *models.RestoreVMwareVMResponse, *apiutils.APIError) {

    queryBuilder := r.config.BaseUrl + "/restores/vmware/vms"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.restored-vmware-vms=v1+json"
    var result *models.RestoreVMwareVMResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: r.config,
        RequestUrl: queryBuilder,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Post,
    })

    return result, apiErr
}
