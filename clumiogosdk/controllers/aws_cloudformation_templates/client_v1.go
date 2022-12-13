// Copyright (c) 2021 Clumio All Rights Reserved

package awscloudformationtemplates

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// AwsCloudformationTemplatesV1Client represents a custom type interface
type AwsCloudformationTemplatesV1Client interface {
    // ReadAwsConnectionTemplates Returns the AWS CloudFormation templates available to install to connect
    //  to Clumio. The provided URL will be pasted into the Amazon S3 URL field when
    //  creating the CloudFormation stack.
    ReadAwsConnectionTemplates()(
        *models.ReadAWSTemplatesResponse,  *apiutils.APIError)
    
    // CreateAwsConnectionTemplate Returns the AWS CloudFormation template URL corresponding to a given
    //  configuration of asset types.
    CreateAwsConnectionTemplate(
        body *models.CreateAwsConnectionTemplateV1Request)(
        *models.CreateAWSTemplateResponse,  *apiutils.APIError)
    
}

// NewAwsCloudformationTemplatesV1 returns AwsCloudformationTemplatesV1Client
func NewAwsCloudformationTemplatesV1(config config.Config) AwsCloudformationTemplatesV1Client {
    client := new(AwsCloudformationTemplatesV1)
    client.config = config
    return client
}
