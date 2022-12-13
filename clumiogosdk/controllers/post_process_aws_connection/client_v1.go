// Copyright (c) 2021 Clumio All Rights Reserved

package postprocessawsconnection

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// PostProcessAwsConnectionV1Client represents a custom type interface
type PostProcessAwsConnectionV1Client interface {
    // PostProcessAwsConnection Performs post-processing after AWS Connection Create, Update or Delete. This API should only be invoked by the Clumio Terraform provider and should not be invoked manually.
    PostProcessAwsConnection(
        body *models.PostProcessAwsConnectionV1Request)(
        interface{},  *apiutils.APIError)
    
}

// NewPostProcessAwsConnectionV1 returns PostProcessAwsConnectionV1Client
func NewPostProcessAwsConnectionV1(config config.Config) PostProcessAwsConnectionV1Client {
    client := new(PostProcessAwsConnectionV1)
    client.config = config
    return client
}
