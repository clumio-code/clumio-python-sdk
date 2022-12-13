// Copyright (c) 2021 Clumio All Rights Reserved

// Package policyassignments contains methods related to PolicyAssignments
package policyassignments

import (
    "encoding/json"
    "fmt"

    "github.com/clumio-code/clumio-go-sdk/api_utils"
    "github.com/clumio-code/clumio-go-sdk/common"
    "github.com/clumio-code/clumio-go-sdk/config"
    "github.com/clumio-code/clumio-go-sdk/models"
)

// PolicyAssignmentsV1 represents a custom type struct
type PolicyAssignmentsV1 struct {
    config config.Config
}

// SetPolicyAssignments Assign (or unassign) policies on up to 100 entities. This endpoint returns a task
//  ID and queues a task in the background to execute the request. Use the task ID to
//  monitor task completion.
func (p *PolicyAssignmentsV1) SetPolicyAssignments(
    body *models.SetPolicyAssignmentsV1Request)(
    *models.SetAssignmentsResponse, *apiutils.APIError) {

    queryBuilder := p.config.BaseUrl + "/policies/assignments"

    bytes, err := json.Marshal(body)
    if err != nil {
        return nil, &apiutils.APIError{
            ResponseCode: 500,
            Reason:       fmt.Sprintf("Failed to Marshal Request Body %v", body),
            Response:     []byte(fmt.Sprintf("%v", err)),
        }
    }
    payload := string(bytes)
    header := "application/api.clumio.policy-assignments=v1+json"
    var result *models.SetAssignmentsResponse

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
