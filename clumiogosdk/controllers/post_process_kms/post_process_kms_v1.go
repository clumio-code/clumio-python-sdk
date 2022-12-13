// Copyright (c) 2021 Clumio All Rights Reserved

// Package postprocesskms contains methods related to PostProcessKms
package postprocesskms

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// PostProcessKmsV1 represents a custom type struct
type PostProcessKmsV1 struct {
    config config.Config
}

// PostProcessKms This API runs automatically and performs post-processing after a KMS template Create, Update, or Delete operation. It must be invoked by the Clumio Terraform provider and must not be invoked manually.
func (p *PostProcessKmsV1) PostProcessKms(
    body *models.PostProcessKmsV1Request)(
    interface{}, *apiutils.APIError) {

    queryBuilder := p.config.BaseUrl + "/wallets/_post-process"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.post-process-kms=v1+json"
    var result interface{}

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: p.config,
        RequestUrl: queryBuilder,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Post,
    })

    return result, apiErr
}
