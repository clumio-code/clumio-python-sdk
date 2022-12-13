// Copyright (c) 2021 Clumio All Rights Reserved

// Package restoredawsec2instances contains methods related to RestoredAwsEc2Instances
package restoredawsec2instances

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// RestoredAwsEc2InstancesV1 represents a custom type struct
type RestoredAwsEc2InstancesV1 struct {
    config config.Config
}

// RestoreAwsEc2Instance Restores the specified EC2 instance backup to the specified target destination.
func (r *RestoredAwsEc2InstancesV1) RestoreAwsEc2Instance(
    embed *string, 
    body models.RestoreAwsEc2InstanceV1Request)(
    *models.RestoreEC2Response, *apiutils.APIError) {

    queryBuilder := r.config.BaseUrl + "/restores/aws/ec2-instances"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.restored-aws-ec2-instances=v1+json"
    var result *models.RestoreEC2Response
    defaultString := "" 
    
    if embed == nil {
        embed = &defaultString
    }
    
    queryParams := map[string]string{
        "embed": *embed,
    }

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: r.config,
        RequestUrl: queryBuilder,
        QueryParams: queryParams,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Post,
    })

    return result, apiErr
}
