// Copyright (c) 2021 Clumio All Rights Reserved

package policyassignments

import (
     "github.com/clumio-code/clumio-go-sdk/api_utils"
     "github.com/clumio-code/clumio-go-sdk/config"
     "github.com/clumio-code/clumio-go-sdk/models"
)

// PolicyAssignmentsV1Client represents a custom type interface
type PolicyAssignmentsV1Client interface {
    // SetPolicyAssignments Assign (or unassign) policies on up to 100 entities. This endpoint returns a task
    //  ID and queues a task in the background to execute the request. Use the task ID to
    //  monitor task completion.
    SetPolicyAssignments(
        body *models.SetPolicyAssignmentsV1Request)(
        *models.SetAssignmentsResponse,  *apiutils.APIError)
    
}

// NewPolicyAssignmentsV1 returns PolicyAssignmentsV1Client
func NewPolicyAssignmentsV1(config config.Config) PolicyAssignmentsV1Client {
    client := new(PolicyAssignmentsV1)
    client.config = config
    return client
}
