// Copyright (c) 2021 Clumio All Rights Reserved

package awsenvironments

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// AwsEnvironmentsV1Client represents a custom type interface
type AwsEnvironmentsV1Client interface {
    // ListAwsEnvironments Returns a list of AWS environments.
    ListAwsEnvironments(
        limit *int64, 
        start *string, 
        filter *string, 
        embed *string)(
        *models.ListAWSEnvironmentsResponse,  *apiutils.APIError)
    
    // ReadAwsEnvironment Returns a representation of the specified AWS environment.
    ReadAwsEnvironment(
        environmentId string, 
        embed *string)(
        *models.ReadAWSEnvironmentResponse,  *apiutils.APIError)
    
}

// NewAwsEnvironmentsV1 returns AwsEnvironmentsV1Client
func NewAwsEnvironmentsV1(config config.Config) AwsEnvironmentsV1Client {
    client := new(AwsEnvironmentsV1)
    client.config = config
    return client
}
