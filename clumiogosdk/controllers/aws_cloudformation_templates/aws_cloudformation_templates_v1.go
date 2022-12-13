// Copyright (c) 2021 Clumio All Rights Reserved

// Package awscloudformationtemplates contains methods related to AwsCloudformationTemplates
package awscloudformationtemplates

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// AwsCloudformationTemplatesV1 represents a custom type struct
type AwsCloudformationTemplatesV1 struct {
    config config.Config
}

// ReadAwsConnectionTemplates Returns the AWS CloudFormation templates available to install to connect
//  to Clumio. The provided URL will be pasted into the Amazon S3 URL field when
//  creating the CloudFormation stack.
func (a *AwsCloudformationTemplatesV1) ReadAwsConnectionTemplates()(
    *models.ReadAWSTemplatesResponse, *apiutils.APIError) {

    queryBuilder := a.config.BaseUrl + "/connections/aws/cloudformation-templates"

    
    header := "application/api.clumio.aws-cloudformation-templates=v1+json"
    var result *models.ReadAWSTemplatesResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: a.config,
        RequestUrl: queryBuilder,
        AcceptHeader: header,
        Result: &result,
        RequestType: common.Get,
    })

    return result, apiErr
}


// CreateAwsConnectionTemplate Returns the AWS CloudFormation template URL corresponding to a given
//  configuration of asset types.
func (a *AwsCloudformationTemplatesV1) CreateAwsConnectionTemplate(
    body *models.CreateAwsConnectionTemplateV1Request)(
    *models.CreateAWSTemplateResponse, *apiutils.APIError) {

    queryBuilder := a.config.BaseUrl + "/connections/aws/cloudformation-templates"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.aws-cloudformation-templates=v1+json"
    var result *models.CreateAWSTemplateResponse

    apiErr := common.InvokeAPI(&common.InvokeAPIRequest{
        Config: a.config,
        RequestUrl: queryBuilder,
        AcceptHeader: header,
        Body: payload,
        Result: &result,
        RequestType: common.Post,
    })

    return result, apiErr
}
