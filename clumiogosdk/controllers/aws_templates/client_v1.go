// Copyright (c) 2021 Clumio All Rights Reserved

package awstemplates

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// AwsTemplatesV1Client represents a custom type interface
type AwsTemplatesV1Client interface {
    // ReadConnectionTemplates Returns the AWS CloudFormation and Terraform templates available to install to connect
    //  to Clumio.
    ReadConnectionTemplates()(
        *models.ReadAWSTemplatesV2Response,  *apiutils.APIError)
    
    // CreateConnectionTemplate Returns the URLs for AWS CloudFormation and terraform templates  corresponding
    //  to a given configuration of asset types.
    CreateConnectionTemplate(
        body *models.CreateConnectionTemplateV1Request)(
        *models.CreateAWSTemplateV2Response,  *apiutils.APIError)
    
}

// NewAwsTemplatesV1 returns AwsTemplatesV1Client
func NewAwsTemplatesV1(config config.Config) AwsTemplatesV1Client {
    client := new(AwsTemplatesV1)
    client.config = config
    return client
}
