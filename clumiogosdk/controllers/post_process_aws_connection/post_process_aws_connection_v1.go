// Copyright (c) 2021 Clumio All Rights Reserved

// Package postprocessawsconnection contains methods related to PostProcessAwsConnection
package postprocessawsconnection

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// PostProcessAwsConnectionV1 represents a custom type struct
type PostProcessAwsConnectionV1 struct {
    config config.Config
}

// PostProcessAwsConnection Performs post-processing after AWS Connection Create, Update or Delete. This API should only be invoked by the Clumio Terraform provider and should not be invoked manually.
func (p *PostProcessAwsConnectionV1) PostProcessAwsConnection(
    body *models.PostProcessAwsConnectionV1Request)(
    interface{}, *apiutils.APIError) {

    queryBuilder := p.config.BaseUrl + "/connections/aws/post-process"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.post-process-aws-connection=v1+json"
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
